## this file countains code that is related to reading the data from a specific resource 
# split the data to  train/split 
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# importation fo user test
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# 1 carte a class for  any input is required ( here is the file path to save  train/tes/raw data )

@dataclass
class DataIngestionConfig :
    # given input : path where train_data  and test_data will be saved 
    train_data_path: str = os.path.join('artifacts' , 'train.csv')
    test_data_path: str = os.path.join('artifacts' , 'test.csv')
    raw_data_path: str = os.path.join('artifacts' , 'data.csv')

class DataIngestion :
    def __init__(self ):
        # variable stores the given inputs 
        self.ingestion_config =  DataIngestionConfig()

    #2  fucntion that will read  split  and store the data   
    def initiate_data_ingestion(self ):

        logging.info("Entered the data ingestion method or componetn ")

        try :
            # 2.1 read data (locally) 
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('reading data as a datafrmae ')

            # extract the folder name  from the path 
            directory = os.path.dirname(self.ingestion_config.train_data_path)
            #then  careate it if does not exisit
            os.makedirs(directory, exist_ok=True)
            # we save first raw data in the given input path 
            df.to_csv(self.ingestion_config.raw_data_path , index=False , header=True)

            #2.2 split the data 
            logging.info('train  , split intiation')
            train_set , test_set = train_test_split(df , test_size=0.2 , random_state=42)

            #2.3 SAVE THE SPLITTED DATA IN the given paths  and return the paths 
            train_set.to_csv(self.ingestion_config.train_data_path , index=False , header=True)
            test_set.to_csv(self.ingestion_config.test_data_path ,   index=False , header=True)
            logging.info("Ingestion of the data is completed ")

            #return the paths as an output 
            return (
                self.ingestion_config.train_data_path ,
                self.ingestion_config.test_data_path ,
            )
   
     
        except Exception as e :
            raise CustomException(e, sys)


if __name__=='__main__':
     data_ingestion=DataIngestion()
     train_data, test_data= data_ingestion.initiate_data_ingestion()

     #preprocessing 
     data_transformation_objct= DataTransformation()
     train_arr , test_arr,  processor = data_transformation_objct.initiate_data_transformation(train_data,test_data)
     
     # modeling 
     model_trainer =  ModelTrainer()
     r2_test , best_score, best_model , report=model_trainer.initiate_model_trainer(train_arr,test_arr)
     logging.info("  step done  ")
     print("R2 on Test Set:", r2_test)

     # if you want to take an idea about the traing process
     print("best score  in traing :", best_score)
     print("best model  in traing :", best_model)
     print("report in trianing  :", report)
