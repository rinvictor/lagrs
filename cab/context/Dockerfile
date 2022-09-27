FROM ubuntu:20.04
RUN echo "export TZ=Europe/Madrid" >> /etc/profile
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get upgrade -y && apt-get install net-tools -y && apt-get install libnet-ifconfig-wrapper-perl -y && apt-get install iputils-ping -y && apt-get install ssh -y && apt-get install -y locales && localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8 && apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
# Con sshd, ENV no funciona. Para fijar una variable de entorno:
# RUN echo "export MI_VARIABLE=mivalor" >> /etc/profile
RUN echo "export LANG=es_ES.UTF-8" >> /etc/profile
COPY entrypoint.sh /
COPY delta_hosts /tmp

# Esta instrucción no hace nada, solo indica el puerto TCP de escucha, es sólo un mensaje para quien va a usar el contenedor.
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]



