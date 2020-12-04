# FinalProject-Group4
Divorce

Our data comes from UCI: https://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set

For our project we decided to make a supervised machine learning model that could make a prediction on the input values of a survey. This prediction would tell the survey taker if their relationship is doomed for divorce or not.


We started by looking at data from a survey taken in Turkey that was designed by Gottman couples therapy. The good thing about this data set is that it already had numerical inputs of zero through four. Therefore as a group we had very little data cleaning to do. The survey was designed to formulate whether a person would get divorced, or not, based on their answers of how much they agree with a series of 54 statements. The survey was taken by individuals that were either already divorced, and answering on behalf of their failed marriage, or people that were still in loving committed marriages.


Using the information of whether the subject taking the survey was either married or divorced, we were able to train our divorce predictor by using a logistic regression supervised machine learning model by way of scikit-learn on the data provided. Once we had our model we attached it to the survey in the Divorce Predictor webpage so that anyone who visits our site can learn the fate of their relationship.



Things to consider:
The Survey was translated from Turkish to English, therefore we had to change some of the language in order to make it more easily readable. Everytime they used the word discussion we changed the word to argument as we thought it fit better in the context of the statement. Additionally, the word spouse is used in place of wife to be more inclusive to all genders and relationship types. (wife is also used irregularly in the translated survey)


Also the survey is a very small sample size of about 170 subjects so any conclusions can be taken with a grain of salt. (Even with the small sample size the results seem to be in line with the world average of Divorce rates of around 50%)
