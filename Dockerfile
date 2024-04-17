# Use an official Ubuntu base image
FROM python:alpine3.19

# Set the working directory in the container
WORKDIR /.

# Install Python and pip
# RUN apt update && \
#     apt install -y python3-pip

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Make port 3000 available to the world outside this container
# EXPOSE 3000

# Define environment variable to run the app using uvicorn
# ENV UVICORN_HOST=0.0.0.0
# ENV UVICORN_PORT=3000

# Run main.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]