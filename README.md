# ML production project

## Project Overview

- This project involves predicting students performance using the best R^2 for the model on a flask app. The models are not necessarily important but the goal of the project was to learn how to make a end to end ML pipeline that involves CI/CD on AWS that results in a flask app being built. The following steps outline the process:

1. **Training Data**

- Data ingestion reads and splits the data and data transformation scales the data. Model trainer will run multiple ML algorithms (Random Forest, Decision Tree, Gradient Boosting Regressor, Linear Regression, XGBRegressor, CatBoosting Regressor, AdaBoost Regressor) and find the best R^2. 

3. **Inference**
   
- When the best model in Model trainer is found it will be used to predict the students performance based on the inputs in the flask app. 

4. **Docker**

 - Added Docker to the EC2 instance by doing the steps below:
    - sudo apt-get update -y
    - sudo apt-get upgrade
    - #required
    - curl -fsSL https://get.docker.com -o get-docker.sh
    - sudo sh get-docker.sh
    - sudo usermod -aG docker ubuntu
    - newgrp docker

 - The Docker container was added to an ECR on AWS
  

6. **Compute**

- AWS was used for this project. 

- At first, ElasticBeanstalk (.ebextensions/python.config) was used as a continuous deployment app using Code Pipeline. I wanted to improve this by not only using Docker containers but also having a CI/CD pipeline that starts on Github actions and is pushed to AWS. 

- An EC2 instance was used along with Github Actions. In order to configure the EC2 as a self-hosted runner you need to do the below in Github (settings -> Security and Variables -> Actions):
    - AWS_ACCESS_KEY_ID=
    - AWS_SECRET_ACCESS_KEY=
    - AWS_REGION = us-east-1
    - AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com
    - ECR_REPOSITORY_NAME = simple-app

