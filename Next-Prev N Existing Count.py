tmp = pd.DataFrame()
tmp[["Count", "IsTest", "IsTrain", "IsValidation"]]= target[["Count", "IsTest", "IsTrain", "IsValidation"]]
tmp["Point"] = date.Point
tmp["Date"] = pd.to_datetime(date.Date)

tmp.head(10)

resultExistingMean = pd.DataFrame()

def GetNextNExistingValue(n):
    result = np.array([np.nan] * tmp.shape[0])
    k = 1
    for i in range(tmp.shape[0]):
        currentDay = tmp.Date[i]
        targetCity = tmp.Point[i]
        tmpForCity = tmp[(tmp.Point == targetCity) &(tmp.IsTrain == 1)] #получение данных только по определенному 
        #городу и из Train части
        valueLessWhenN = (tmpForCity.Date.map(lambda x: (x  - currentDay).days) <= n) \
                        &(tmpForCity.Date.map(lambda x: (x  - currentDay).days) > 0)
        # получение городов, чья разница между первоночальной датой и вычисляемой меньше n и больше 0 (в днях)
        targetCount = tmpForCity.Count[valueLessWhenN] #получение Count переменных для этих городов
        targetCount = targetCount.dropna() #удаление отсутвующих значений для вычисления средних
        meanCount = np.mean(targetCount)
        result[i] = meanCount
        k += 1
        if ( (k % 500) == 1):
            print k / 500,
    return result

def GetPrevNExistingValue(n):
    result = np.array([np.nan] * tmp.shape[0])
    k = 1
    for i in range(tmp.shape[0]):
        currentDay = tmp.Date[i]
        targetCity = tmp.Point[i]
        tmpForCity = tmp[(tmp.Point == targetCity) &(tmp.IsTrain == 1)] #получение данных только по определенному 
        #городу и из Train части
        valueLessWhenN = (tmpForCity.Date.map(lambda x: (x  - currentDay).days) >= n) \
                        &(tmpForCity.Date.map(lambda x: (x  - currentDay).days) < 0)
        # получение городов, чья разница между первоночальной датой и вычисляемой меньше n и больше 0 (в днях)
        targetCount = tmpForCity.Count[valueLessWhenN] #получение Count переменных для этих городов
        targetCount = targetCount.dropna() #удаление отсутвующих значений для вычисления средних
        meanCount = np.mean(targetCount)
        result[i] = meanCount
        k += 1
        if ( (k % 500) == 1):
            print k / 500,
    return result


#resultExistingMean["NextExisting1Value"] = pd.Series(GetNextNExistingValue(1))

#resultExistingMean["NextExisting2Value"] = pd.Series(GetNextNExistingValue(2))

#resultExistingMean["NextExisting3Value"] = pd.Series(GetNextNExistingValue(3))

#resultExistingMean["NextExisting7Value"] = pd.Series(GetNextNExistingValue(7))

#resultExistingMean["NextExisting14Value"] = pd.Series(GetNextNExistingValue(14))

#resultExistingMean["NextExisting21Value"] = pd.Series(GetNextNExistingValue(21))

#resultExistingMean["NextExisting30Value"] = pd.Series(GetNextNExistingValue(30))

#resultExistingMean.to_csv('data_transform/resultExistingMean.csv', index=None)

#resultExistingMean["PrevExisting1Value"] = pd.Series(GetPrevNExistingValue(-1))

#resultExistingMean["PrevExisting2Value"] = pd.Series(GetPrevNExistingValue(-2))

#resultExistingMean["PrevExisting3Value"] = pd.Series(GetPrevNExistingValue(-3))

#resultExistingMean["PrevExisting7Value"] = pd.Series(GetPrevNExistingValue(-7))

#resultExistingMean["PrevExisting14Value"] = pd.Series(GetPrevNExistingValue(-14))

#resultExistingMean["PrevExisting21Value"] = pd.Series(GetPrevNExistingValue(-21))

#resultExistingMean["PrevExisting30Value"] = pd.Series(GetPrevNExistingValue(-30))

#resultExistingMean.to_csv('data_transform/resultExistingMean.csv', index=None)

