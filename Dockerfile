FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app/project
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["apt-get", "install", "libmysqlclient-dev"]
COPY . ./
EXPOSE 8000
