# Recruit Restaurant Visitor Forecasting case study
Based on the kaggle competition: [link](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting)

I was given 3-5 days to work on this case study, then present my findings and solutions. It was my first attempt to tackle kaggle competition project.

The goal is to predict the number of daily visitors for each restaurant in Japan for future dates.

This folder includes Python scripts that I wrote during the given short period of time using jupyter notebook, they are:
- Data Exploration: Data Analysis to get an insight of datasets given by Recruit Holdings who launch this competition.
- Random Forest Prediction v1 & v2: Scripts to predict the number of visitors of each restaurant using Random Forest. 

In the first attempt (v1), I use Random Forest technique from scikit-learn to predict the number of visitors with these features: month, day of week, is holiday, is weekend, genre and area. In terms of data transformation, I'm using Label Encoder method at this stage.

In the second attempt (v2), I added a few more rolling functions as features (min, max, mean, median and count observation of each restaurant by day of week) then train test the model again using Random Forest technique.

## Improvements
Obviously this isn't my final solution. If I was given more time, I would probably explore more and perhaps will include reservation data, weather and competitor into the features. 

I would also attempt to adjust the day of week, in particular weekdays public holiday by substituting the day before public holiday as friday, the last day of public holiday as sunday etc. 

The least important features should also be excluded to avoid overfitting.

I would also try out a few models, and compare it with the RF model:
- ARIMA: the most basic model for time series prediction
- LGBM: much more complex than ARIMA and RF, but it's consider by kagglers as the best model to tackle this project.

## Python Libraries
- numpy
- pandas
- seaborn
- matplotlib
- datetime
- scikit-learn



