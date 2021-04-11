import paho.mqtt.client as mqtt

#The ip address of the raspberry pi which serve as a broker
def Send(msg, broker_server = '127.0.0.1', topic = 'initial_channel', client_name = 'sensor'):
	MQTT_SERVER = broker_server
	MQTT_PATH = topic
	client = mqtt.Client(client_name)
	client.connect(MQTT_SERVER, 1883, 60)
	client.loop_start()
	client.publish(topic=MQTT_PATH, payload = msg, qos = 1)
	print('one message published')


while True:
	###put the sensor program over here
	###using the Send() function to send message
	msg = input("Enter the message to send")
	Send(msg)