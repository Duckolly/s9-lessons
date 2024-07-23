import json
import requests
import time
from confluent_kafka import Consumer

class KafkaClient:
    def init(self, host: str, port: int, user: str, password: str, cert_path: str, group: str) -> None:
        self._params = {
            'bootstrap.servers': f'{host}:{port}',
            'security.protocol': 'SASL_SSL',
            'ssl.ca.location': cert_path,
            'sasl.mechanism': 'SCRAM-SHA-512',
            'sasl.username': user,
            'sasl.password': password,
            'group.id': group,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,
            'error_cb': self.error_callback,
            'debug': 'all',
            'client.id': 'someclientkey'
        }
        self._consumer = Consumer(self._params)

    def error_callback(self, err):
        print('Something went wrong: {}'.format(err))

    def consume_message(self, topic: str) -> dict:
        self._consumer.subscribe([topic])
        timeout: float = 3.0
        while True:
            msg = self._consumer.poll(timeout=timeout)
            if msg is None:
                time.sleep(1)
                continue
            if msg.error():
                raise Exception(msg.error())
            val = msg.value().decode()
            return json.loads(val)