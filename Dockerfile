FROM alpine:latest

RUN apk --update --upgrade add bash cairo fontconfig ttf-freefont font-noto terminus-font gdk-pixbuf pango-dev py3-cffi py3-pillow py3-pip py3-lxml py3-gunicorn apache2-mod-wsgi
RUN mkdir /myapp
WORKDIR /myapp
COPY . /myapp

RUN pip install weasyprint gunicorn flask
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5001 app:app
