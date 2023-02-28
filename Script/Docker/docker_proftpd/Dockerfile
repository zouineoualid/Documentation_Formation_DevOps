FROM instantlinux/proftpd

#Création user + création dossier cgi_artefacts_ssl

RUN adduser -h /home/jenkins -D jenkins \
    && mkdir /home/jenkins/cgi-bin \
    && mkdir /home/jenkins/artefacts \
    && mkdir /etc/proftpd/ssl 


COPY jenkins_rsa.pub /etc/proftpd/authorized_keys/jenkins


COPY proftpd.conf /etc/proftpd/
COPY sftp.conf /etc/proftpd/conf.d/

RUN apk add proftpd-mod_sftp
RUN apk add openssh \
    && ssh-keygen -A

CMD ["/usr/local/sbin/proftpd", "-n", "-c", "/usr/local/etc/proftpd.conf" ]
