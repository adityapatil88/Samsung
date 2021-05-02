FROM python:3.6
MAINTAINER Aditya Patil "adityadpatil88@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["wsgi.py"]