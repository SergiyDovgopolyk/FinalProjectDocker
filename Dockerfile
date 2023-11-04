# Використовуємо базовий образ Python
FROM python:3.10

# Встановлюємо змінну середовища
ENV APP_HOME /app

# Встановлюємо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Копіюємо файли з вашого проекту в робочу директорію контейнера
COPY src/__main__.py $APP_HOME/
COPY src/AddressBook.py $APP_HOME/
COPY src/Bot.py $APP_HOME/
COPY src/info.py $APP_HOME/
COPY src/auto_save.bin $APP_HOME/
COPY requirements.txt $APP_HOME/

# Встановлюємо залежності всередині контейнера
RUN pip install -r requirements.txt

# Позначаємо порт, який ваш застосунок буде слухати всередині контейнера
EXPOSE 5000

# Запускаємо ваш застосунок всередині контейнера
CMD ["python", "__main__.py"]

