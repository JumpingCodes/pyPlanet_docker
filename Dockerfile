FROM debian

WORKDIR /usr/src/

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN useradd --create-home appuser
RUN apt install -y python3-pygame
USER appuser 

COPY main.py .

CMD [ "python3", "main.py" ]


