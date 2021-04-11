import picamera
from time import sleep
import paho.mqtt.publish as publish
import path.mqtt.client as mqtt

"""This is used to transmit images captured from PiCamera"""
#define the broker's address and topic
MQTT_SERVER = "192.168.0.127"
MQTT_PATH = "camera"

#create a client "p1"
client = mqtt.Client("p1")
#connect the client to the broker
client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()
#start the while loop to capture the image
i = 0
camera = picamera.PiCamera()
while True:
	input("Press enter to capture the "+i+" th photo-->")
	#establish a camera object and capture the image
	i+=1
	sleep(0.25)
	image_name = "/home/pi/Desktop/img/image" + str(i) + ".jpg"
	camera.capture(image_name, resize = (960,540))
	#open the saved image and conver the image into byte array
	with open(image_name, "rb") as publish_msg:
		img_str = publish_msg.read()
		byteArray = bytes(img_str)
		#publish the image
		client.publish(topic=MQTT_PATH, payload = byteArray, qos = 0)
		# time.sleep(2)
	camera.close()
