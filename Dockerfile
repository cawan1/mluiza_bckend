FROM kstromeiraos/django-rest-framework 

MAINTAINER Cawan Porto <cawanporto@gmail.com>

RUN apk add --update && \
    pip install django-filter && \
    rm -rf /var/cache/apk/*

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
