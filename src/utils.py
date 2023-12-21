import os
import sys
from src.logger import logging
import dill
import numpy as np
import pandas as pd

from src.expection import CustomException

def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_trian,y_train,X_test,y_test,models):
    try:
        pass
    except:
        pass
    