FROM python:3
COPY . /usr/lib/app/
WORKDIR /usr/lib/app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app.py"]