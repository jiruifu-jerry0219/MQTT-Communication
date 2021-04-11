import paho.mqtt.client as mqtt
import time

"""This program is used to test the receiver function of MQTT, different from the subscriber.py, this program build the subscriber as a class"""
# The callback for when the client receives a CONNACK response from the server.
class Subscriber:
	def __init__(self, host = '192.168.0.175', topic = 'test_channel', path = '/home/jirui/img_rec/'):
		self.hostname = host
		self.channel = topic
		self.save_path = path
		self.num = 0
		self.msg = None

	def receive(self):
		def on_connect(client, userdata, flags, rc):
			client.subscribe(self.channel)
			print("Connected with result code "+str(rc))

			# Subscribing in on_connect() means that if we lose the connection and
			# reconnect then subscriptions will be renewed.


		# The callback for when a PUBLISH message is received from the server.
		def on_message(client, obj, msg):
			print('message # '+str(self.num)+str(msg.payload))
			self.num +=1


		client = mqtt.Client()

		client.on_connect = on_connect
		client.on_message = on_message
		client.connect(self.hostname, 1883, 60)
		client.loop_forever()

receiver = Subscriber()
msg = receiver.receive()
