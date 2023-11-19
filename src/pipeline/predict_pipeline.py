# It encapsulates the entire process of making predictions, 
#from preprocessing the input data to generating the final predictions. 

import sys
import os 
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging


# this class is respponsible of giving the preditions for the input data 
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
           
           # give the paths for the  saved preprocesor and the model 
           model_path=os.path.join("artifacts","model.pkl")
           preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
           
          # loading the preprocessor and the model 
           model         = load_object(file_path=model_path)
           preprocessor  = load_object(file_path=preprocessor_path)
           logging.info(" model and preprocessor loaded")
          # preporcess the input features using the saved processor 
           data_scaled=preprocessor.transform(features)
           
          # predict using the saved model 
           preds=model.predict(data_scaled)
           return preds

        except Exception as e:
            raise CustomException(e , sys)
    

# thsi class is responsible of mapping the input form the html from to the backend 

class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int          
                 
    ):
        
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

     # this fucntion transform the input data to a dataframe 
    def get_data_as_data_frame(self):
        try:
            # first we tranform inputs to a dictinary 
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

