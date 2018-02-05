from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _ in range(10):
    time.sleep(1)
    # producer.send('AAPL', b'some_message_bytes')
    producer.send('AAPL', {'foo': 'bar'})
    print('AAPL')

producer.flush()
producer = KafkaProducer(retries=5)