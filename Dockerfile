FROM python:3.8.2-alpine3.11

# Update
# Add repository for numpy alpine package


RUN pip install requests \
datetime \
mysql-connector-python 


RUN mkdir /script
ADD src/* /script/
RUN chmod +x /script

ADD bash/* /etc/periodic/hourly/hourly
RUN chmod +x /etc/periodic/hourly/hourly
# schedule
COPY cron-root /var/spool/cron/crontabs/root
RUN chmod +x /var/spool/cron/crontabs/root

CMD ["/usr/sbin/crond", "-f"]
