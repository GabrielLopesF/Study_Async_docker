FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app/project
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000