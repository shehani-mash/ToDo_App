#use an official python runtime as the base image
FROM python:3.9-slim

#set the working directory inside the container
WORKDIR /app

#copy the requirements file into the container
COPY requirements.txt .

#install the python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the application code into the container 
COPY . .

#Expose port 5000 fro the FLask app
EXPOSE 5000

#set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

#run the flask application
CMD [ "flask", "run", "--host=0.0.0.0" ]
