## Микро АПИ сервис для генерации красивых QR кодов 🤩

### Как запустить:
1. Скопируйте `.env.dist` в `.env` и заполните необходимые данные. 
2. **Docker:**  
   1. Вы можете сразу запустить проект с Docker, а если у вас его нет, то [скачайте и установите](https://docs.docker.com/get-docker/).  
   2. Запустите проект командой:  
       ```shell
       docker compose up
       ```
3. **Без Docker:**  
   1. Создайте [виртуальное окружение (venv)](https://docs.python.org/3/library/venv.html).  
   2. Установите зависимости из `requirements.txt`: 
      ```shell
      pip install -r requirements.txt --pre
      ```
    3. Запустите проект командой:
       ```shell
       python bot.py
       ```