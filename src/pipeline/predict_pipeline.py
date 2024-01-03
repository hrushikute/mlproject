import os
import sys
import pandas as pd

from src.expection import CustomException
from src.utils import load_object
from src.logger import logging
class Predictpipeline:
    def __init__(self) -> None:
        pass
    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","prepocessor.pkl")
            logging.info("Before loading the model")
            model=load_object(model_path)
            preprocessor=load_object(preprocessor_path)
            logging.info("Done with loading of model and preprocessor.")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys) 
class CustomData: 
    def __init__ (self,
                gender: str,
                race_ethnicity: str,
                parental_level_of_education,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int) -> None:
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        
    def get_data_as_frame(self):
        try:
            custom_data_input_frame_dict={
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_frame_dict)
        except Exception as e:
            raise CustomException(e,sys)