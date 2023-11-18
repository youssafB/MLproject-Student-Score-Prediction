# ## this file countains code that is related to  training my model 

import os
import sys
from dataclasses import dataclass

#from catboost import CatBoostRegressor
#from xgboost import XGBRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models




# Step 1: Choose Models by storing them in a dictionary 

models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
# Step 2: Create Parameter Grids with the same keyes of the  models dictionary 



param_grids={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
}




@dataclass
class ModelTrainerConfig :
    trained_model_file_path= os.path.join('artifacts', "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer (self ,train_arr , test_arr ):
        try:
              # split train and test data to X and y 
             logging.info("splitting train and test input data")
             X_train , y_train  =    train_arr[ :,:-1], train_arr[:,-1]
             X_test ,  y_test    =    test_arr[ :,:-1], test_arr[ :,-1]

            # use evaluate_mode to  chose the best mdoel, best score and report 
             best_score, best_model, report= evaluate_models( X_train ,y_train,models, param_grids )
             logging.info("best model is chosen ")

             # save the best mdoel 
             save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        
             # predit and evalute on test data 
             predicted=best_model.predict(X_test)
             r2_square = r2_score(y_test, predicted)
             logging.info("model evaluation on test data completed  ")
             return r2_square , best_score, best_model , report
             
        
        except Exception as e: 
            raise CustomException(e,sys)

        
    