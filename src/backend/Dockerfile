# Installs python version 3.8.10 from Docker
FROM python:3.8.10

# Makes app directory and sets it as working directory
RUN mkdir -p ./src/app
WORKDIR ./src/app

# Copies requirements.txt to app
# and installs all required python packages
COPY requirements.txt ./src/app
RUN pip install -r requirements.txt

# Configures container to be run as executable
# with follow commands run when starting
ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=5000"]