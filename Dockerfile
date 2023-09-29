# base image with python
FROM python:3.9

# Working Directory for the app
WORKDIR app/

# Copy the code from system
COPY app.py .

# Install the required libraries for flask at intermediate level
RUN pip install flask

# Run the application once your container is done
CMD ["python","app.py"]
