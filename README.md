Создание сервиса предсказаний
----------
Цель:

Создать микросервис предсказаний моделью ML, создать его docker-образ и запустить сервис в контейнере.

Выполнение работы:

Сервис предоставляет возможность получать доступ к предсказаниям модели через HTTP-запросы. Он построен на основе FastAPI и uvicorn, а также может быть запущен в контейнере Docker. 

Для загрузки модели используется скрипт `services/models/get_model.py`. Важно: запускать скрипт следует из директории `services/models`. Чтобы загрузить нужную модель, необходимо указать соответствующее значение Run ID в переменной RUN_NAME в скрипте `get_model.py`. Run ID модели можно найти в MLFlow.

![Image alt](https://github.com/Molichik123/IIS_LR1/raw/lr4/services/model.jpg)

В папке services/mlservice размещен код для взаимодействия с моделью через FastAPI, а также Dockerfile для создания образа сервиса. Чтобы собрать образ с именем estatemodel, выполните команду: docker build . --tag estate_model:0. Для запуска контейнера с портом 8001 используйте команду: docker run -p 8001:8000 -v $(pwd)/../models:/models estate_model:0. 

После старта сервера можно проверить его работоспособность. Для тестирования POST-запросов удобнее всего использовать адрес http://localhost:8001/docs. Чтобы протестировать POST-запрос /api/prediction, нажмите кнопку "try it now" и введите необходимые параметры. В поле employeeid можно указать любое целое число. В качестве тестового тела запроса для поля itemfeatures я использовал следующий JSON:
    
{
"age":35,
"workclass":"Private",
"education.num":10,
"marital.status":"Married-civ-spouse",
"occupation":"Sales",
"relationship":"Husband",
"race":"White",
"sex":"Male",
"capital.gain":5000,
"capital.loss":1000,
"hours.per.week":60
}
    
В итоге на выходе мы получем предсказание, что по входным данным гражданин имеет прибыль > 50000 ("1" = ">50K", "0"= "<50K")

![Image alt](https://github.com/Molichik123/IIS_LR1/raw/lr4/services/Result.jpg)
