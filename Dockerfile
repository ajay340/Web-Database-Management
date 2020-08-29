# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-slim-buster
FROM mysql

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD Pipfile .
RUN python -m pip install pipenv
RUN pipenv run makemigrations
RUN pipenv run migrate

WORKDIR /app
ADD . /app

RUN pipenv run serve

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:Web-Database-Management. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]
