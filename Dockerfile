#base image
FROM python:3-onbuild

#set dir for app
WORKDIR /usr/src/app

#copy all files to container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install flask requests

#port number for container
EXPOSE 5000

#run the app
CMD ["python", "./app.py"]