FROM python:3.10-buster

WORKDIR /flask2-seed

RUN apt-get update && \
    apt-get -y install locales wait-for-it && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN pip install --upgrade pip setuptools

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]