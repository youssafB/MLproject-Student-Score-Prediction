from flask import Flask , request , render_template , redirect , url_for
import numpy as np 
import pandas as np
from sklearn.preprocessing import StandardScaler
from src.logger import logging

from src.pipeline.predict_pipeline import CustomData,PredictPipeline


app= Flask(__name__)

# create a route for a home page 
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predictdata' , methods=[ 'GET' , 'POST'])
def predict_datapoint():

    if request.method == 'GET':
     return render_template("home.html")
    
    else:
        # we call CustomData to map data ana transofrm it to a datfrmae 
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        # transform input data to a dataframe:
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        # call the predictpipline and make predictions 
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        # make predcitions 
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        # render the html and give also the predicted value as varible to tha html 
        return render_template('home.html',results=results[0])
   

if __name__=="__main__":
    app.run()   



# this code for my creted form 
#@app.route('/submit', methods=['POST'])
#def submit():
#    result_message = None

#    if request.method == 'POST':
#      user_input = request.form['userInput']
#      selected_location = request.form.get('location')

 #     result_message = f"User entered: {user_input}, Selected Location: {selected_location}"
    
 #   return render_template('form.html', result_message=result_message)

        


