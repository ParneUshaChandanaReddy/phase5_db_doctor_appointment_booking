FROM python:3.8-slim
WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
            && unzip instantclient-basiclite-linuxx64.zip \
            && rm -f instantclient-basiclite-linuxx64.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig

ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python3 app.py





# Installing Oracle instant client

# WORKDIR    /app
# COPY       . .  # Copy my project folder content into /app container directory
# RUN        pip3 install pipenv
# RUN        pipenv install
# EXPOSE     8000
# # For this statement to work you need to add the next two lines into Pipfilefile
# # [scripts]
# # server = "python manage.py runserver 0.0.0.0:8000"
# ENTRYPOINT ["pipenv", "run", "server"]