FROM nginx


#Création dossier certificat
RUN mkdir /etc/nginx/ssl

#Copie certificat
COPY nginx_cert.pem  /etc/nginx/ssl
COPY nginx_key.pem  /etc/nginx/ssl

#copie du fichier default.conf pour activer le TLS

COPY default.conf /etc/nginx/conf.d/default.conf

#Activer cgi
RUN apt update
RUN apt install -y fcgiwrap
RUN mkdir -p /usr/lib/www/cgi-bin
COPY script_python.py /usr/lib/cgi-bin/
RUN chmod +x /usr/lib/cgi-bin/script_python.py
COPY fastcgi_params /etc/nginx/fastcgi_params

#Démarrer FCGIWRAP

CMD script_service.sh