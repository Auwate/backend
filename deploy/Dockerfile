FROM debian:bullseye

RUN apt update && apt-get upgrade -y

RUN apt-get install -y git python3-pip libmariadb-dev-compat

WORKDIR /opt

RUN git clone https://github.com/Auwate/backend_repo.git

WORKDIR /opt/backend_repo

RUN pip install -r requirements.txt

EXPOSE 80

RUN chmod +x /docker-startup.sh

CMD [ "/docker-startup.sh" ]

