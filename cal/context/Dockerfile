FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade && apt-get install -y bsdmainutils
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
