import paho.mqtt.client as mqtt
import time
import os

# The callback for when the client receives a CONNACK response from the server.
"""You can use this to transmit images between devices"""
class Subscriber:
	def __init__(self, host = '192.168.0.179', topic = 'camera'):
		self.hostname = host
		self.channel = topic
		self.save_path = './image/'
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
			print("<-------Received Image"+str(self.num)+"------->")
			self.num +=1
			name = 'fname' + str(self.num)
			with open(os.path(self.save_path + name+'.jpg', 'wb') as fd:
				fd.write(msg.payload)
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message
		client.connect(self.hostname, 1883, 60)
		client.loop_forever()
try:
	receiver = Subscriber()
	msg = receiver.receive()
except KeyboardInterrupt:
	print("Receive ended")
