import paho.mqtt.client as mqtt
import random


##publisher part
def Publish(msg, broker_sever, topic, client_name):
    MQTT_Server = broker_sever
    MQTT_PATH = topic
    client = mqtt.Client(client_name)
    client.connect(MQTT_Server, 1883, 60)
    client.loop_start()
    client.publish(topic=MQTT_PATH, payload = msg, qos = 1)

##generate random message to publish
def msg_generator():
    msg_topic_set = ["distance", "angle", "speed"]
    msg_content = random.randint(10,50)
    msg_header = random.choice(msg_topic_set)
    msg = msg_header + str(msg_content)
    return msg

while True:
    ##by testing the publishing function, randomly generate a type of message
    ##publish the message to the broker
    receive_id = random.randint(1,3)




