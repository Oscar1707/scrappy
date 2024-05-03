FROM python:latest
WORKDIR /app
COPY . .
RUN python -m venv venvı
RUN pip install -r requirements.txt
CMD [ "/bin/bash" ]