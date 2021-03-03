FROM php:8.0.2-apache
COPY ./myhtaccess  /usr/local/apache2/
COPY --from=composer:2.0.11 /usr/bin/composer /usr/bin/composer
