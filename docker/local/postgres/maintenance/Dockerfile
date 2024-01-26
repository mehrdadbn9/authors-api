FROM postgres:14.1

COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance
# wanna make some file not all local/bin to  be executable so do below commands

RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
   && rmdir /usr/local/bin/maintenance