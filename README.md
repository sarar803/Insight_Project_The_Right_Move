# Insight Project: The Right Move
This is the code for my Insight Data Science project, The Right Move. The goal of my project was to predict the buildings in Manhattan more likely to have noise, heat/hot water, and elevator complaints using data from the year before, so renters could get a sense if an apartment was likely to have problems before moving in.

The file "apartment_violation_create_dataset.ipynb" puts together the different data sources I used and creates features. I used data from NYC Department of Buildings (e.g., building height, age, location), NYC 311 (noise, heat/hot water, and elevator complaints), the U.S. Census (I used a spatial join to assign each building to its census tract and created features inclusing percent of renters in the census tract and population density), and the New York State Liquor Auntory (I made a feature for distance to the nearest bar by creating a distance matrix between all buildings and all bars in Manhattan). 

The file "model_fitting.ipynb" fits a logistic model with L2 regularization for each of the outcomes (noise, heat/hot water, and elevator complaints). I used 2016 complaints and features from 2013-2015 to train the model, and 2017 complaints and features from 2014-2016 to test the model. I evalauted the model on recall and created visualizations incluing ROC curves and confusion matrixes. 

