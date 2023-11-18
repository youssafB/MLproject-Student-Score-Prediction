# this is for any fonctionalty written in  a common way 

import pickle
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
import sys
import pandas as pd

from sklearn.metrics import make_scorer, r2_score

#function 1 :  this fucntion is responsible for  svaing  any object to a file using pickle:
def save_object(obj, file_path):
    """
    Save an object to a file using pickle.

    Parameters:
    - obj: The object to be saved.
    - file_path (str): The path to the file where the object will be saved.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)
    print(f"Object saved to {file_path}")


# fucntion 2 :

def evaluate_models(X_train ,y_train, models ,param_grids):
    
        try:
             scores = []
             best_score = 0
             best_model = None

             for model_name , model   in models.items() :
                 # create the grid and fit it  
                 grid_search  = GridSearchCV(model,  param_grids[model_name]  , scoring='r2', cv=3 )
                 grid_search.fit(X_train, y_train)
        
                 # . Retrieve the Best scores and  Parameters for each  model then store them in a list
                 scores.append({
            
                    'model': model, 'best_score': grid_search.best_score_,
                   'best_params': grid_search.best_params_
                  })
                 
                 # select and store the best model and best score 
                 if grid_search.best_score_ > best_score:
                     best_score = grid_search.best_score_
                     best_model = grid_search.best_estimator_

             report = pd.DataFrame(scores) 
        
             return  best_score , best_model , report

             
        except Exception as e :
            raise CustomException(e, sys)
 
      
    


