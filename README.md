1. setup

    ```shell
    flutter build web
   
    # install poetry to run a hosting server
    # Please follow the official instruction https://python-poetry.org/docs/
   
    # run a hosting server
    poetry install
    poetry run uvicorn server:app
    ```
    
    This hosting server returns 500 error for `/assets/fonts/MaterialIcons-Regular.otf`, only first 2 times.

2. Open a new guest browser of Google Chrome and access to `http://localhost:8080`. .

4. Reload the web page 2 times or more

    - In the Chrome developer console, we can see that `/assets/fonts/MaterialIcons-Regular.otf` is still 500 error while `curl http://localhost:8000/assets/fonts/MaterialIcons-Regular.otf` returns 200 success response
