import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation


# define class 
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts/data_injection' , 'train.csv')
    test_data_path = os.path.join('artifacts/data_injection' , 'test.csv')
    raw_data_path = os.path.join('artifacts/data_injection' , 'data.csv')

class DataInjection:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() 

    def data_ingestion_insisate(self):
        try:
            # Notebook\Data\cleandata.csv
            data = pd.read_csv(os.path.join("Notebook/Data" , "cleandata.csv"))

            # create directory for artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok=True)
            # save 
            data.to_csv(self.ingestion_config.raw_data_path, index = False)
            # split data 
            logging.info("Split Data into Train test and test Data")
            train_set , test_set = train_test_split(data , test_size=0.20 , random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path , index = False , header = True)
            test_set.to_csv(self.ingestion_config.test_data_path , index = False , header = True)

            logging.info("Data Injection is Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info("Error in Data INjection Stage")
            raise CustomException(e , sys)
        

if __name__ == '__main__':
    obj = DataInjection()
    train_data_path ,test_data_path = obj.data_ingestion_insisate()

    data_tranformation = DataTransformation()
    train_arr , test_arr , _ = data_tranformation.insitiate_data_transformation(train_data_path, test_data_path)

          



#src\components\dataInjection.py
