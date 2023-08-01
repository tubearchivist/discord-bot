FROM python:3.11.3-slim-bullseye
ENV PYTHONUNBUFFERED 1
ENV PATH=/root/.local/bin:$PATH

# install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --user -r requirements.txt

COPY app /app
WORKDIR app

CMD ["python", "bot.py"]
