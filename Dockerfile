FROM registry.hub.docker.com/library/python:3.8.9

# Flask application
WORKDIR /home/vcap/app

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

# Creates a non-root user and adds permission to access folders
RUN useradd appuser 
RUN chown -R appuser:root /home/vcap/app
RUN chown -R appuser:root /var/log/nginx
RUN chown -R appuser:root /var/lib/nginx
RUN chown -R appuser:root /run

RUN chmod -R 777 /home/vcap/app
RUN chmod -R 777 /var/log/nginx
RUN chmod -R 777 /var/lib/nginx
RUN chmod -R 777 /run

USER appuser

CMD ["/usr/bin/supervisord", "--loglevel=debug"]
