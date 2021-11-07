#Install python 3.6 from dockerhub
FROM python:3.6
#Copy all the contents of the current directory into a new folder called "app"
COPY . /app
#Change directory into "app"
WORKDIR /app
# Install all the requirements provided in the requirements.txt file
RUN pip install -r requirements.txt
#Expose the container ports
EXPOSE 5000
# Next step is equivalent to saying "python app.py" in your terminal
CMD ["python","app.py"]