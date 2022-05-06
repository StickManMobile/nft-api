FROM python:3.10

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=nftapi.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]