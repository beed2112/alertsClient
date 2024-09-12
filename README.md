# alertsClient


remote listener

Pick your way to run me

straight up python or in a Container

clone me

cd mqttAircraftClientRemote

straight up python python mqttAircraftClientRemote.py <MQTT_SERVER> <MQTT_TOPIC> <MQTT_PORT> [MQTT_ID] [MQTT_PASS]

run me inside a container 

docker build -t alerts-client .


docker run -it alerts-client 143.198.50.168 1883 $MQTT_CLOUD_ID $MQTT_CLOUD_PASS


