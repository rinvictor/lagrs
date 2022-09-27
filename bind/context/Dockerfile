FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN useradd -ms /bin/bash vrincon
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
