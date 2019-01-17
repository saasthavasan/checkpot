#Taking ubuntu as base
FROM ubuntu

#Specifying port
EXPOSE 3306

#Installing dependencies
RUN apt-get update -qq && apt-get install -y build-essential libev-dev git

#Cloning Mysql-honeypotd
RUN git clone https://github.com/sjinks/mysql-honeypotd
RUN cd mysql-honeypotd && make

#Creating pid file it will contain the process id of mysql-honeypotd
RUN touch mysql-honeypotd/mysql-honeypotd.pid

RUN chmod +x mysql-honeypotd/mysql-honeypotd

#Running mysql-honeypotd. -f option is to specify not to daemonize
CMD ./mysql-honeypotd/mysql-honeypotd -b 0.0.0.0 -p 3306 -P mysql-honeypotd.pid -f
