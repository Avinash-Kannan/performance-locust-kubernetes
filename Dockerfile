FROM locustio/locust:2.15.1
USER root
RUN apt update && apt install dnsutils telnet curl iputils-ping -y
RUN pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install pipenv locust configparser --upgrade pip
USER locust
COPY tests /home/locust/tests
COPY utils /home/locust/utils