
# Students Performance in Exams Prediction
This project is designed to predict students' exam performance enabling targeted interventions. It is an end-to-end machine learning project with modular coding , covering  :
- data exploration
- preprocessing
-  model building
-   creation of a Flask web application,
-   and finally, deploying the model.

# Screenshot of UI
![HomepageUI](./Screenshots/HomepageUI.jpg)

## Dataset

The dataset used in this project is obtained from Kaggle and can be found [here](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977). It includes the following features:

- `gender`: Student's gender (male/female)
- `race/ethnicity`: Ethnicity of the student
- `parental level of education`: Parental education level
- `lunch`: Type of lunch the student receives
- `test preparation course`: Whether the student completed a test preparation course
- `math score`: Student's math exam score
- `reading score`: Student's reading exam score
- `writing score`: Student's writing exam score

Target variable:
* `price`: Price of the given Diamond.

Dataset Source Link :



# AWS Deployment Link :

AWS Elastic Beanstalk link : [http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/](http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/)


# Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv file.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested . The best model found was catboost regressor.
    * After this hyperparameter tuning is performed on catboost and knn model.
    * A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.

#### Exploratory Data Analysis Notebook

Link : [EDA Notebook](https://github.com/youssafB/MLproject1/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb)

#### Model Training Approach Notebook

Link : [Model Training Notebook](https://github.com/youssafB/MLproject1/blob/main/notebook/2.%20MODEL%20TRAINING.ipynb)


