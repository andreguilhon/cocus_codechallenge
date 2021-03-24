FROM python:3.7-buster
ENV DB_NAME=postgres
ENV DB_PORT=5432
ENV DB_HOST=db
ENV DB_PASSWORD=postgres
ENV DB_USER=postgres

RUN apt-get update && apt-get install python3-dev libpq-dev postgresql postgresql-contrib nginx -y --no-install-recommends
COPY nginx/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/filereader

COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY filereader /opt/app/filereader/

WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]