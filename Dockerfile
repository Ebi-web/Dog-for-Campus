FROM node:15.12.0-alpine3.10 as node 

FROM php:8.0.2-apache

ENV APACHE_DOCROOT /var/www/html/ \
# timezone environment
  TZ=UTC \
  # locale
  LANG=en_US.UTF-8 \
  LANGUAGE=en_US:en \
  LC_ALL=en_US.UTF-8 \
  # composer environment
  COMPOSER_ALLOW_SUPERUSER=1 \
  COMPOSER_HOME=/composer 

WORKDIR /var/www/html/

COPY --from=composer:2.0.11 /usr/bin/composer /usr/bin/composer 
COPY ./public-html/ /var/www/html/ 
COPY --from=node /usr/local/bin/node /usr/local/bin/
COPY --from=node /usr/local/lib/node_modules/ /usr/local/lib/node_modules/
COPY myhtaccess  /usr/local/apache2/ 

RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
    ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm && \
    ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npx 

# WORKDIR /var/www/html/
# RUN composer install \
#   && npm install