import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error as mae
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

features = pd.read_csv('data_transform/all.csv')

data = features.fillna(100000000)

remove_column = ['IsTest', 'IsTrain', 'IsValidation', 'Date', 'Point', 'CityName'
				 , 'MeanForThroughDay', 'MeanForMonthDayByPoints'
                 , 'MeanForThroughDayByPoints', 'MeanForThroughWeekByPoints'
                 , 'MeanForYearDayByPoints', u'Prev2Day', u'Prev3Day'
                 , u'Next2Day', u'Next3Day', 'NextExisting21Value'
                 , 'PrevExisting21Value', 'NextExisting14Value'
                 , 'PrevExisting14Value', 'NextExisting3Value'
                 , 'PrevExisting3Value'
                 , 'BranchNumber', 'MeanForMonth', 'Next1Day', 'Prev7Day'
                 ]

#remove_column = ['IsTest', 'IsTrain', 'IsValidation', 'Date', 'Point', 'CityName'
#				, u'MeanForThroughWeekByPoints', u'MeanForYearDay', u'MeanForYearDayByPoints'
#                ]


dataTrain = data[data.IsTrain == 1]
dataTrain = dataTrain[dataTrain.columns.difference(remove_column)]

X_train = dataTrain[dataTrain.columns.difference(['Count'])]
y_train = dataTrain[['Count']]

dataValidation =  data[data.IsValidation == 1]
dataValidation = dataValidation[dataValidation.columns.difference(remove_column)]

X_test = dataValidation[dataValidation.columns.difference(['Count'])]
y_test = dataValidation[['Count']]

dataResult =  data[data.IsTest == 1]
dataResult = dataResult[dataResult.columns.difference(remove_column)]

X_res = dataResult[dataResult.columns.difference(['Count'])]


dtrain = xgb.DMatrix( X_train, label=y_train)
dtest = xgb.DMatrix( X_test, label=y_test)
dres = xgb.DMatrix( X_res )
evallist  = [(dtest,'eval'), (dtrain,'train')]

param = {'max_depth': 6,
 		'silent': 1,
 		'eta': 0.01,
 		'eval_metric': 'mae'
 }

num_round = 10000

bst = xgb.train( param, dtrain, num_round, evallist, verbose_eval=10 )


result = bst.predict(dres)
