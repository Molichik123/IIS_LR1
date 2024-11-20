Описание проделанной работы
---
Провести ряд экспериментов по настройке модели, логируя все результаты в MLFlow. Научиться пользоваться инструментами autofeat, mlxtend, MLFlow

Запуск
---
Используем команду sh ./mlflow/start_mlflow.sh

Она запускает mlflow server --backend-store-uri sqlite:///mlruns.db

После запуска MLFlow будет доступен по адресу: http://localhost:5000

Результаты исследования
---
По результатам исследований были получены следующие метрики качества:

MAE - средняя абсолютная ошибка между предсказанными и реальными значениями
![Илюстрация MAE](https://github.com/Molichik123/IIS_LR1/raw/LR3/research/MAE.jpg)

MAPE - метрика, обозначающая среднюю абсолютную ошибку в процентах.
![Илюстрация MAPE](https://github.com/Molichik123/IIS_LR1/raw/LR3/research/MAPE.jpg)

MSE - среднеквадратичная ошибка
![Илюстрация MSE](https://github.com/Molichik123/IIS_LR1/raw/LR3/research/MSE.jpg)

