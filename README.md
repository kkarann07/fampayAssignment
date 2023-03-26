# YouTube Videos Search App

## Getting Started

### Prerequisites

- Redis # apt install redis-server
- Docker

### Endpoints

- #### GET /api/videos/ 
  - To list all the stored video data in a paginated response sorted in descending order of published datetime
- #### GET /api/videos/search/?q=money
  - To search the stored videos using their title or description

### How To Setup the Environment
- Clone fampayAssignment github repo and move to fampay_youtube_api project
- Download the Prerequisites depending on OS
- #### For running locally
  - Create a virtual environment using ```python -m venv <venv-name>```
  - Activate the virtual environment using ```source <venv-name>/bin/activate```
  - Download requirements using ```pip install -r requirements.txt```
  - Start Redis Server using ```redis-server```
  - Start Celery application using ```celery -A fampay_youtube_api worker -l INFO -E ```
  - Start Celery Beat using ```celery -A fampay_youtube_api beat -l INFO ```
  - Start Django server using ```python manage.py runserver```

- #### Using Docker
  - Build Docker Image using ```docker build -t fampay_youtube_api .```
  - Run Docker image using ```docker run -p 8000:8000 fampay_youtube_api```
  - On successfull start, following logs will be there in terminal
 ```
  Django version 4.1.7, using settings 'fampay_youtube_api.settings'
  Starting development server at http://0.0.0.0:8000/
  Quit the server with CONTROL-C.
  ```