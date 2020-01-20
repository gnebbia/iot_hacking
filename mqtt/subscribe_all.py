# This script can be used to connect to all topics, we just have to give it
# the Server IP and the port, which anyway usually is fine, since 1883 is the default
# port of MQTT


import paho.mqtt.client as mqttdef on_connect(client, userdata, flags, rc):
   print "[+] Connection successful"
   client.subscribe('#', qos = 1)        # Subscribe to all topics
   client.subscribe('$SYS/#')            # Broker Status (Mosquitto)def on_message(client, userdata, msg):
   print '[+] Topic: %s - Message: %s' % (msg.topic, msg.payload)client = mqtt.Client(client_id = "MqttClient")
client.on_connect = on_connect
client.on_message = on_message
client.connect('SERVER IP HERE', 1883, 60)
client.loop_forever()
