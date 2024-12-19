FROM jerryhopper/depbo-tools:latest

FROM python
# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app
COPY requirements.txt /app

RUN rm -f /usr/lib/python3*/EXTERNALLY-MANAGED

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#Set the git credentials

EXPOSE 5000

# Run app.py when the container launches
CMD ["bash", "start.sh"]