from kafka import KafkaConsumer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--topic')
parser.add_argument('--bootstrap-server', default='localhost:9092')
args = parser.parse_args()

consumer = KafkaConsumer(
    args.topic,
    bootstrap_servers=args.bootstrap_server,
    auto_offset_reset='earliest',
    group_id='jenkins-test-group'
)

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
    break
