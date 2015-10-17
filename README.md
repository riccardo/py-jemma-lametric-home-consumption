# Lametric App

Simple quick'n dirty Python application getting home consumption data from a JEMMA DAL endpoint and posting it to your lametric.
It uses a working instance of [JEMMA](http://jemma.energy-home.org) with attached any metering devices compatible with ZigBee Home Automation / [Energy@home](www.energy-home.it) specifications.

# Quck HowTo

- create a dedicated folder on your Raspberry device running JEMMA.
- ```git clone https://github.com/ismb/py-jemma-dal-rest-client.git```
- ``git clone https://github.com/riccardo/py-jemma-lametric-home-consumption.git``
- ```cp -R py-jemma-dal-rest-client/DALClient ./py-lametric-home-consumption/```
- cd py-lametric-home-consumption
- edit py-lametric-home-consumption.properties to fit your Lametric Notification app and JEMMA endpoint specs

Hook this into your raspberry's cron to get periodic updates.

# Info

Questions: find me on the [JEMMA Project Mailing List](http://ismb.github.io/jemma/devteam.html)


