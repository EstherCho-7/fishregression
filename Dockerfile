FROM python:3.11

WORKDIR /code

COPY src/fishregression/main.py /code/

#COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir --upgrade git+https://github.com/EstherCho-7/fishregression.git@0.2.0/cli

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
