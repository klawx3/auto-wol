FROM python:3

#Edit this variables
ENV TIMEOUT=1
ENV HOST=192.168.3.10
ENV MAC=0A-E0-AF-A3-6D-99
ENV BROADCAST=192.168.3.255

#Setup APP
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./main.py" ]

