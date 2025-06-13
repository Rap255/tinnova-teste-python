FROM python:3.9
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
COPY entrypoint.sh /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]