FROM python:3.9.2
WORKDIR /var/www/adr
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "adr.py"]