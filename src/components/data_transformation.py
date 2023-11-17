## this file countains code that is related to preprocessing the data 

import sys
import os 
import numpy as np
import pandas as pd 
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


# similary to datingestion creating any required input fr this data transofrmation  
# the input here is the preporcessor file path

@dataclass
class DataTransformationConfig:
    # d input : path where  the preprocessor object will be saved as pkl file 
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")   


class DataTransformation:
    def __init__(self ):
        self.data_transformation_config = DataTransformationConfig()

    # this fucntion is responsible for creating the preproceesor ( pipline of transofrmations )
    def get_data_transformer_object(self):

        

        try :
            # chosing numerical and categorical features 
            numerical_columns   = ["writing_score", "reading_score"]
            categorical_columns =  [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # create two pipelines each countians the required transofrmations for each  type of features 
            num_pipeline= Pipeline( 
                steps= [
                ('imputer',  SimpleImputer(strategy= "median") ) ,
                ('scaler',   StandardScaler(with_mean=False) )

                ] 
            )
            logging.info("Numerical Encoding completed")

            cat_pipeline= Pipeline( 
                steps= [
                ('imputer',            SimpleImputer(strategy="most_frequent") )  ,
                ('one_hote_encoder',   OneHotEncoder() )
                #('scaler',             StandardScaler())

                ] 
            )
            logging.info("Numerical Transofrmations completed")
            logging.info("Categorical Transofrmations  completed")

            # combine both  piplines in one entity 
            preprocessor =  ColumnTransformer( [
                ("num_pipeline",    num_pipeline , numerical_columns ),
                ("cat_pipeline",    cat_pipeline , categorical_columns )

            ]
            )
            return  preprocessor

        except Exception as e  :
             raise CustomException(e, sys)
        
    
 # this fucntion is responsible to apply the given transoifrmation in my processor into data
    def  initiate_data_transformation(self , train_path , test_path):

        try:
            # reading the train and test data as df 
            train_df= pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            # get the preprocessor object 
            preprocessing_obj = self.get_data_transformer_object()
           
            # exclude target variable form the processing and give its vairable 
            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            # aplly the procesing on your trainig and testing  data 
            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")
            input_feature_train_arr=preprocessing_obj .fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj .transform(input_feature_test_df)
            

            # concatenate  the features and the target  
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df) ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

             # save the proprocessor in the given path (can be used to transofer other new data)
            save_object(


                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
             # retunr the trnaing and testing data as two aarays after transofrmations

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            
            )
        except Exception as e:
            raise CustomException(e,sys)


    
           


        
