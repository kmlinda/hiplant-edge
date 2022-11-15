#!/usr/bin/env python3
from btlewrap.bluepy import BluepyBackend
import yaml
from datetime import datetime
from miflora.miflora_poller import MiFloraPoller


#
# Connect to Pollers
#
with open('configuration.yaml') as p:
    data = yaml.load(p, Loader=yaml.FullLoader)

#pollers should be automatically found and then selected and defined by user
macs = data['pollers']
pollers = []
for mac in macs:
    pollers.append(MiFloraPoller(mac, BluepyBackend))

#sample polls
print(pollers[2].battery_level())

poll = MiFloraPoller(macs[0], BluepyBackend)
poll.fill_cache()
ready = poll.cache_available()
print(ready)
print(poll.parameter_value("temperature"))

#
# Poll plant data and persist it every 15 minutes
#
TEMPERATURE = "temperature"
MOISTURE = "moisture"
CONDUCTIVITY = "conductivity"
LIGHT = "light"


for poller in pollers: 
    assert isinstance(poller, MiFloraPoller)
    poller.fill_cache()
    print("Battery: " + str(poller.battery_level()))
    print("Temperature: " + str(poller.parameter_value(TEMPERATURE)))
    print("Light: " + str(poller.parameter_value(MOISTURE)))
    print("Humidity: " + str(poller.parameter_value(CONDUCTIVITY)))
    print("Conductivity: " + str(poller.parameter_value(LIGHT)))


#
# Poll hardware data and persist it once per day.
#
# battery level,...

#time = poller._fetch_device_time()[1]
#date = datetime.fromtimestamp(time).strftime("%A, %B %d, %Y %I:%M:%S")
#print(date)

#temp = poller.parameter_value("temperature")
#print(temp)


exit()










#
# Save poll data as is to a file
#

#get poll data
#save to file

#
# Convert poll data to json with plant data
#

#add config file and get plant config data
#

#
# Save poll data to cloud mongoDB/blob?
#

# 












