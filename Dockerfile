FROM python:3.7
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
ENV PORT 8080
EXPOSE $PORT
CMD gunicorn -w 2 -b 0.0.0.0:${PORT} app:app
