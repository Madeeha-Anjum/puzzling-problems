FROM python:3.10

WORKDIR  /usr/src/app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./src/main.py" ]

# instead of cmd use
CMD ["tail", "-f", "/dev/null"]