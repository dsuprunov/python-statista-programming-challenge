FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#COPY . /app
COPY main.py /app/

#RUN coverage run -m pytest
#RUN coverage report

CMD ["python", "main.py"]