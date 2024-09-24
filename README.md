# ML production project

## Project Overview
This project involves predicting students performance using the best R^2 for the model on a flask app. The models are not necessarily important but the goal of the project was to learn how to make a end to end ML pipeline that involves CI/CD on AWS that results in a flask app being built. The following steps outline the process:

1. **Training Data**
Data ingestion reads and splits the data and data transformation scales the data. Model trainer will run multiple ML algorithms (Random Forest, Decision Tree, Gradient Boosting Regressor, Linear Regression, XGBRegressor, CatBoosting Regressor, AdaBoost Regressor) and find the best R^2. 
2. **Inference**
When the best model in Model trainer is found it will be used to predict the students performance based on the inputs in the flask app. 
3. **Docker**
4. **Compute**
AWS was used for this project. 

At first, ElasticBeanstalk (.ebextensions/python.config) was used as a continuous deployment app using Code Pipeline. I wanted to improve this by not only using Docker containers but also having a CI/CD pipeline that starts on Github actions and is pushed to AWS. 
5. **Monitoring**
