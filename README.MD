### Данные:

train.csv — тренировочная выборка вида: дата,филиал,число_заказов

test.csv — тестовая выборка вида: дата,филиал

### Структура проекта

/data_original/

	train.csv (Date, Point, Count)

	test.csv (Date, Point, Count)

	common.csv (key = ID, Date, Point, Count or NULL) // sort by Date

/data_transform/

	city.csv (key = Point, CityID, BranchNumber, OpenDate, LastDate)

	date.csv (key = ID, Year, Month, YearDay, MonthDay, WeekDay, ThroughMonth, ThroughWeek, ThroughDay)

	target.csv (key = ID, Point, Count, IsTrain, IsTest)

	intrenal_features.csv (key = ID, MeanForThroughMonth, MeanForMonth, MeanForThroughWeek, MeanForWeek, MeanForWeekDay,  MeanForWeekDayByYear)


### Анализ
Требуется предсказать значения после определенного периода. Оказалось, что 6 городов нет в тренировочной выборке.

### Добавленные признаки:
1) год

2) месяц в году

3) день в месяце

4) день в неделе

5) сквозная нумерация (дней, недель, месяцов)

6) признак город и признак филиала

7) среднее за конкретный день в году по всем филиалам-по конкретному филиалу, среднее за неделю ...

### Решение

Обучение градиентного бустинга над признаками представленными выше