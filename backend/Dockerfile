FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /root/bin
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /root/bin
ENV PATH="/root/bin:${PATH}"

EXPOSE 8000

CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn main.wsgi:application --bind 0.0.0.0:8080"]
