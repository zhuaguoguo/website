FROM harbor-registry.inner.youdao.com/devops/python:3.7
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

COPY . /www
WORKDIR /www

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
RUN pip install -r requirements.txt

EXPOSE 8880
CMD ["python", "-m", "app.api"]