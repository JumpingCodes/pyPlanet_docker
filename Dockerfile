FROM debian

WORKDIR /usr/src/

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN useradd --create-home appuser
RUN apt install -y python3-pygame
RUN apt install -y python3-pygbag

USER appuser 

COPY pyPlanet/ .

EXPOSE 8000

CMD [ "pygbag", "pyPlanet" ]


