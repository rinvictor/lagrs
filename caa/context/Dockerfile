FROM ubuntu:20.04
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get upgrade -y && apt-get install net-tools -y && apt-get install libnet-ifconfig-wrapper-perl -y && apt-get install iputils-ping -y && apt-get install ssh -y && apt-get install -y locales && localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8
ENV LANG es_ES.UTF-9
COPY entrypoint.sh /
COPY delta_hosts /tmp
ENTRYPOINT ["/entrypoint.sh"]


