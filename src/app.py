from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata, KafkaProducer
from datetime import datetime
import os
import sys

TOPIC_NAME = os.environ.get('KAFKA_TOPIC', '')
MESSAGE_KEY = os.environ.get('KAFKA_MESSAGE_KEY', '')
MESSAGE_VALUE = os.environ.get('KAFKA_MESSAGE_VALUE', sys.argv[1])
BOOSTRAP_SERVER = os.environ.get('KAFKA_BOOSTRAP_SERVER', '')

producer = KafkaProducer(bootstrap_servers=BOOSTRAP_SERVER.split(","))

print("producing message... ")
producer.send(TOPIC_NAME, key=MESSAGE_KEY.encode('utf-8'), value=MESSAGE_VALUE.encode('utf-8')).get(timeout=30)
print("produce message success!")