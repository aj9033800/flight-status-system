from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_notification(message):
    producer.send('flight-status-topic', value=json.dumps(message).encode('utf-8'))
    producer.flush()

if __name__ == "__main__":
    send_notification({'flight': 'AB123', 'status': 'Delayed'})
