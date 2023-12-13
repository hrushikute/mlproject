import os 
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.expection import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preporcessor.pkl')
    
class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformer_obj(self):
        '''
        This fuction is responsible for data transformation.
        '''
        try:
            numerical_features= ['reading_score', 'writing_score']
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Done with numerical data encoding.")
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder",OneHotEncoder())
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Done with categorical variable transformation.")
            # Applying the coloumntransformer on the pipeline
            logging.info(f"Categorical colummns : {categorical_features}")
            logging.info(f"Numerical colummns : {numerical_features}")
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",numerical_pipeline,numerical_features),
                    ("cat_pipeline",categorical_pipeline,categorical_features)
                ]
            )
            return preprocessor
                               
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Done with reading training and testing data.")
            logging.info("Obtaining the preporcesing object")
            
            preprocessing_obj = self.get_data_transformer_obj()
            target_coloumn="math_score"
            numerical_features= ['reading_score', 'writing_score']
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            input_feature_train_df=train_df.drop(columns=target_coloumn,axis=1)
        except Exception as e:
            raise CustomException(e,sys)