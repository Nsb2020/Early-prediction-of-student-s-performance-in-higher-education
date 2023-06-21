<img src="https://github.com/Nsb2020/Early-prediction-of-student-s-performance-in-higher-education/blob/main/Hamoye%20_Logo.png" style="height: 100%; width:100%;">   

## EARLY PREDICTION OF STUDENT’S PERFORMANCE IN HIGHER EDUCATION 
### PROJECT BY: TEAM GITHUB [HDSC spring '23]
## Introduction
Obtaining a university degree is a formidable challenge faced by students worldwide. The process can be overwhelming as students adapt to a more demanding academic environment, deal with separation from family, and encounter other obstacles. These difficulties significantly impact academic performance, often leading to failure and dropout. Various factors, including financial hardships, contribute to high dropout rates, which not only frustrate students on a personal level but also have a detrimental effect on productivity and the community as a whole. To address this urgent issue, tertiary institutions have implemented counseling services, tutoring programs, workshops, and mentoring initiatives, striving to support students and improve their chances of success.
## Aims and Objective
The central aim of this project is to investigate the optimal approach for accurately predicting students' academic performance and identifying their risk of dropout at the earliest stages of their higher education journey. Our objective is to develop a comprehensive system that facilitates the prompt segmentation of students from the beginning of their academic path. By doing so, we aim to establish a proactive framework that effectively addresses potential obstacles and provides timely support to at-risk students. 
 
## Data
The dataset used in this project was compiled by a higher education institution from various disjoint databases. It encompasses information about students enrolled in diverse undergraduate degrees, including agronomy, design, education, nursing, journalism, management, social service, and technologies. The dataset represents students from different nationalities across Europe, America, and Africa. It includes data available at the time of student enrollment, such as academic paths, demographics, and socio-economic factors, as well as the students' academic performance at the end of the first and second semesters. The primary objective of utilizing this dataset is to develop classification models capable of predicting students' dropout rates and academic success. The problem is formulated as a three-category classification task, with a notable imbalance in the distribution of classes. The dataset consists of 4424 instances (rows) and 36 attributes (columns).The link to the dataset can be found [here](https://archive-beta.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

## Model Building
In this project stage, a comprehensive set of 15 models was constructed, with the aim of addressing the imbalances found in the datasets at each stage of the academic journey. The following models were specifically designed and utilized:
1. SMOTE + Random Forest Classifier.
2. SVMSMOTE.
3. SVMSMOTE + Random Forest Classifier.
4. Balanced Random Forest Classifier.
5. Easy Ensemble Classifier.

These models were carefully chosen and implemented to effectively handle the imbalanced nature of the datasets and enhance the accuracy of predictions.


## Model Deployment
The Flask framework was utilized to deploy the model on the Heroku platform, enabling real-time predictions for various life scenarios.
## Skills and Technologies
* Python Libraries (Pandas & Numpy)
* Data Preprocessing 
* Exploratory Data Analysis
* Data Visualization(Seaborn and Matplotlib)
* Features Engineering & Selection
* Machine Learning 
* Google Collobarotory Notebook
* VS Studio Code
* Flask
* Heroku
*  HTML (Hypertext Markup Language) and CSS (Cascading Style Sheet)



<img src="https://github.com/Nsb2020/Early-prediction-of-student-s-performance-in-higher-education/blob/main/Hamoye%20Logo.png" alt="Citigroup" style="width:30%;">
