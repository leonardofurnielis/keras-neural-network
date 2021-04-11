FROM python:3.8.9-slim-buster

# Flask demo application
WORKDIR /usr/src/home

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

# System packages installation
RUN apt-get update && apt-get install -y nginx supervisor

# Nginx configuration
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf

# Supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Creates a non-root user and adds permission to access the /usr folder
RUN useradd appuser 
RUN chown -R appuser:root /usr/src/home
RUN chown -R appuser:root /var/log/nginx
RUN chown -R appuser:root /var/lib/nginx
RUN chown -R appuser:root /run
RUN chmod -R 777 /run
RUN chmod -R 777 /usr/src/home
RUN chmod -R 777 /var/log/nginx
RUN chmod -R 777 /var/lib/nginx

# RUN chown appuser:root /
# RUN chmod 755 /

USER appuser

EXPOSE 8080

CMD ["/usr/bin/supervisord", "--loglevel=debug"]
