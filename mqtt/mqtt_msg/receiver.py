import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
class Receiver:
	def __init__(self, host = '192.168.0.192', topic = 'initial_channel'):
		self.hostname = host
		self.channel = topic
		self.msg = None

	def receive(self):
		def on_connect(client, userdata, flags, rc):
			client.subscribe(self.channel)
			print("Connected with result code "+str(rc))

			# Subscribing in on_connect() means that if we lose the connection and
			# reconnect then subscriptions will be renewed.

		# The callback for when a PUBLISH message is received from the server.
		def on_message(client, obj, msg):
			print("<-------Received One Message------->")
			print(msg.topic+" "+str(msg.payload))
			self.msg = msg.payload
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message
		client.connect(self.hostname, 1883, 60)
		client.loop_forever()
		return self.msg

receiver = Receiver()
msg = receiver.receive()
