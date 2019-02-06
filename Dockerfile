FROM kstromeiraos/django-rest-framework 

MAINTAINER Cawan Porto <cawanporto@gmail.com>

RUN apk add --update && \
    apk add tzdata && \
    pip install django-filter && \
    rm -rf /var/cache/apk/*

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" >  /etc/timezone

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
