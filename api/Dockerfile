FROM alpine:3.10

#añado python3 y pip al alpine
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

#defino directorio de trabajo
WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "src/app.py"]
