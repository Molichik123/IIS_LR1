Программа находится в ./edu/edu.ipynb. Основные результаты:

Немого о данных: Эти данные были извлечены из базы данных Бюро переписи населения США за 1994 год Ронни Кохави и Барри Беккером (Data Mining and Visualization, Silicon Graphics). Задача прогнозирования состоит в том, чтобы определить, зарабатывает ли человек более 50 тысяч долларов в год. Данные содержат такие признаки: Возраст, рабочий класс, финальный вес записи (количесвто людей в данной категории), образование, нумерация образования по степени, гражданский статус, занятость, семейный статус, раса, пол, капитальный доход, капитальные потери, часы работы в неделю, страна, доход в год. (Ссылка на сайт с выборкой: https://www.kaggle.com/datasets/uciml/adult-census-income)

В ходе исследования были проведены действия:
1) Загрузка и знакомство с данными: у нас в выборке 9 характеристик типа "object" и 6 характеристик типа "int64"
   Переведем "object" в "category". Анализ числовых признаков:

   возраст варьируется от 17 до 90 лет. Средний возраст 38-39 лет,

   образование - от дошкольное до степени доктора. Среднее образование - колледж

   доход - от 0 до ~100 000. Средний доход - 1077

   потери - от 0 до 4 356. Средние потери - 87

   часы в неделю - от 1 до 99. Среднее количество часов в неделю - 40 часов
3) Очистка данных
   Очистка данных не проводилась, так как данные изначально были отобраны с использованием следующих условий:

   Возраст - больше 16 лет

   Вес записи - больше 1 человека

   Уровень прибыли (Income) - больше 100

   Часов работы в неделю - больше 0 часов
4) В ходе анализа были выявлены следующие закономерности:

   Большее число граждан с прибылью меньше 50к от 20 до 35 лет
   Если оценивать тех, кто имеет прибыль больше 50к, то большинство это люди примерно 36-45 лет. (см график ./edu/plot1.png)

   Большую часть выборки составляют люди со степенью бакалавра, студенты колледжа, и люди с высшим обрзованием. При этом люди со степенью бакалавра в большинстве      имеют доход выше 50к, чем остальные категории. (см график ./edu/plot2.png)

   Также большим уровнем дохода обладают женатые люди. А одинокие люди в большинстве своем не имеют большого дохода. (см график ./edu/plot3.png)

   По тепловой карте видно, что лучшая корреляция есть между образованием и капитальным доходом и образованием и капитальными потерями. Также уровень образования 
   связан с тем, сколько часов в неделю тратит сотрудник на работе. У возраста с этими характеристика корреляция будет слабее. (см график ./edu/plot4.png)

   При изучении линейного графика виден сильный рост среднего дохода и средних потерь среди старшего поколения (от 75 и выше). У остальных поколений нет сильных       всплесков в среднем доходе и потерях. Видна тенденция, что с возрастом меняется и доход граждан. (см график ./edu/plot6.png)

   График Bokeh показывает распределение капитального дохода относительно образования. На графике можно уточнить дополнительные характеристики, такие как пол       
   возраст и раса. С помощью графика можно сделать предположение, что больший доход у белых мужчин с высшим образованием. Но нельзя это утверждать, так как скорее 
   всего в выборке большее число объектов имеет белую расу и мужской пол по сравнеию с другими признаками. (см график ./edu/bokeh.html)
5) Обработанная выборка сохранена в файл ./data/clean_data.pkl
   





