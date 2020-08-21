FROM python:3.6

# Create app directory
WORKDIR /app

COPY api.py /app 
COPY application_properties.yaml /app
COPY requirements.txt /app

# Install app dependencies
RUN pip install -r /app/requirements.txt

EXPOSE 5000
ENV FLASK_APP=/app/api.py

CMD ["flask", "run", "--host", "0.0.0.0"]

# CMD [ "python", "api.py" ]
