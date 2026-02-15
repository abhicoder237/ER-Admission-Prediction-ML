import os ,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler ,OneHotEncoder
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.pipeline.utlis import save_obj


@dataclass
class DataTransformationConfig:
    preprocess_obj_file_path = os.path.join("artifacts/data_transformation/preprocessor.pkl")


class DataTransformation:
    def  __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_transformation_obj(self):
        try:
            num_cols = [
                'Foreigners',
                'risk_chance',
                'age_group',
                'is_peak_hour',
                'is_weekend',
                'support'
            ]

            cat_cols = [
                'gender',
                'marital_Status',
                'IsGlobal'
            ]

            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore"))
            ])

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, num_cols),
                ("cat_pipeline", cat_pipeline, cat_cols)
            ])

            return preprocessor

        except Exception as e:
             raise CustomException(e ,sys)


    def handle_outliers(self , df , col):
        try:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)


            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)

            iqr =  Q3 - Q1

            upper_limit = Q3 + (1.5 * iqr)
            lower_limit = Q1 - (1.5 * iqr)

            df.loc[(df[col] > upper_limit) , col] = upper_limit
            df.loc[(df[col] < lower_limit) , col] = lower_limit

            return df

        except Exception as e:
            logging.info("Handlers Outliers")
            raise CustomException(e ,sys)


    def insitiate_data_transformation(self ,train_path , test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            # ✅ fix: replace Unknown
            train_data.replace("Unknown", np.nan, inplace=True)
            test_data.replace("Unknown", np.nan, inplace=True)

            num_cols = [
                'Foreigners',
                'risk_chance',
                'age_group',
                'is_peak_hour',
                'is_weekend',
                'support'
            ]

            for col in num_cols:
                self.handle_outliers(df=train_data, col=col)
                logging.info("Train Data Outlier Transform")

            for col in num_cols:
                self.handle_outliers(df=test_data, col=col)
                logging.info("Test Data Outlier Transform")

            preprocess_obj = self.get_transformation_obj()

            target_col = 'ResidentDay_log'
            drop = [target_col]

            input_feature_train_data = train_data.drop(drop , axis =1)
            target_feature_train_data = train_data[drop]

            input_feature_test_data = test_data.drop(drop , axis =1)
            target_feature_test_data = test_data[drop]

            input_train_arr = preprocess_obj.fit_transform(input_feature_train_data)
            test_train_arr = preprocess_obj.transform(input_feature_test_data)

            # ✅ fix: replace np.c__ (broken) with np.hstack
            train_arr = np.hstack((input_train_arr , target_feature_train_data.values))
            test_arr = np.hstack((test_train_arr , target_feature_test_data.values))

            save_obj(
                file_path=self.data_transformation_config.preprocess_obj_file_path ,
                obj = preprocess_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocess_obj_file_path
            )

        except Exception as e:
            raise CustomException(e ,sys)
