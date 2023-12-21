import os
import sys 
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor,)
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.expection import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    train_model_file_path=os.path.join('artifacts','model.pkl')
    
class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config=ModelTrainerConfig()
        
    def initiate_model_training(self,train_arr,test_arr,preprocessor_path):
        try:
            logging.info("Performing train test split.")
            X_train,X_test,y_train,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
                                           )
            
            models= {
                "Random Forest":  RandomForestRegressor(),
                "Decision tree": DecisionTreeRegressor(),
                "Linear Regression": LinearRegression(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "K nearest Neighbor": KNeighborsRegressor(),
                "XBG Regressor": XGBRegressor(),
                "Cat Boost ": CatBoostRegressor(),
                "Ada boost": AdaBoostRegressor(),
                
            }
            
            model_report:dict=evaluate_model(X=X_train,y=y_train,X_test=X_test,y_test=y_test,
                                             models=models)  

            best_model_score = max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            if best_model_score <0.6:
                raise CustomException("No best model found.")
            logging.info(f"Found the best model :{best_model_name}")
        
            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )
            predicted_val = best_model.predict(X_test)
            r2_score_model=r2_score(y_test,predicted_val)
        
            return r2_score_model
        except Exception as e:
            raise CustomException(e,sys)
            