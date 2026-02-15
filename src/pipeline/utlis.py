import os
import pickle
import sys
from src.exception import CustomException

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        # create directory safely
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # remove old file if exists (prevents permission issue)
        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
