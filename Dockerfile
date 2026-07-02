FROM python:3.13.7

WORKDIR /main

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "view.py"]
