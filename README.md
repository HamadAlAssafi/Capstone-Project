# Capstone Project

## Fake News Predictor

### Libraries

- Pandas
- Matplotlib
- numpy
- seaborn
- re
- pickle
- sklearn
- nltk


### Files Description

1. templates Folder

- It contains HTML file to make user inputs news title, then output the predicted value (fake, or true) by the model

2.  Data-Fake.zip

- It contains CSV file that have all the fake news dataset

3.  Data-True.zip

- It contains CSV file that have all the True news dataset

4. Notebook Folder

- It contains my work in building the model as (.ipynb) & (.HTML)

5. FakeNewsModel.pkl

- It contains the model itself as (PKL)

6. app.py

- It contains the (Flask) app that runs the model within web app
  **Nowadays we receive a large amount of news from different mediums, and there are many of them (fake or unreal), so I decided in this project to create Machine Learning model that can predicts whether the news is real or fake**

### Summary of the Project

1. The project related to Data Science Nanodegree at Udacity
2. I have used NLP and Machine Learning Pipelines to create model that classifiy whether the news is real or fake based on it is title, the algorthim that I used is (Logistic Regression)
3. I have deployed the model to website using (Flask)
4. I have published blogpost in medium about my findings [Blogpost](https://hamadalassafi.medium.com/fake-news-predictor-25d130592f87)
5. The dataset was exported from Kaggle [Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

6. README FILE

### Installation Steps:

1. Run the following commands in the project's root directory to set up the web app.

- Run the following command in the project's directory to run your web app.
  `python app.py`

- Go to http://0.0.0.0:3001/

### Acknowledgments

- I would like to thank the contributors in Kaggle for providing the data to make us work on it, and also I would like to thank Udacity for this amazing opportunity.
