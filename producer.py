from kafka import KafkaProducer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--topic')
parser.add_argument('--message')
parser.add_argument('--bootstrap-server', default='localhost:9092')
args = parser.parse_args()

producer = KafkaProducer(bootstrap_servers=args.bootstrap_server)
producer.send(args.topic, args.message.encode('utf-8'))
producer.flush()
