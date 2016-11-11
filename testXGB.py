import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_absolute_error as mae


features = pd.read_csv('data_transform/all.csv')

data = features.fillna(100000000)

remove_column = ['IsTest', 'IsTrain', 'IsValidation', 'Date', 'Point', 'CityName'
				 , 'MeanForThroughDay', 'MeanForMonthDayByPoints'
                 , 'MeanForThroughDayByPoints', 'MeanForThroughWeekByPoints'
                 , 'MeanForYearDayByPoints', u'Prev2Day', u'Prev3Day'
                 , u'Next2Day', u'Next3Day']

dataTrain = data[data.IsTrain == 1]
dataTrain = dataTrain[dataTrain.columns.difference(remove_column)]

X_train = dataTrain[dataTrain.columns.difference(['Count'])]
y_train = dataTrain[['Count']]

dataValidation =  data[data.IsValidation == 1]
dataValidation = dataValidation[dataValidation.columns.difference(remove_column)]

X_test = dataValidation[dataValidation.columns.difference(['Count'])]
y_test = dataValidation[['Count']]


dtrain = xgb.DMatrix( X_train, label=y_train)
dtest = xgb.DMatrix( X_test, label=y_test)
evallist  = [(dtest,'eval'), (dtrain,'train')]

param = {'max_depth': 7,
 		'silent': 1,
 		'eta': 0.01,
 		'eval_metric': 'mae',
 		'lambda': 20
 }

num_round = 5000
bst = xgb.train( param, dtrain, num_round, evallist )

#predictions = bst.predict(dtest)
#print mae(y_test, predictions)