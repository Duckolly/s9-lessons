import json
from typing import Dict
import redis


class RedisClient:
    def __init__(self, host: str, port: int, password: str, cert_path: str) -> None:
        self._client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=cert_path
        )
              
    def set(self, k:str, v: Dict):
        self._client.set(k, json.dumps(v))
              
    def get(self, k:str) -> Dict:
        result = self._client.get(k)
        if not result:
            return {}
        return json.loads(result.decode("utf-8"))
    

class RedisClient:
    def __init__(self, host: str, port: int, password: str, cert_path: str) -> None:
        self._client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=cert_path
        )
              
    def set(self, k:str, v: Dict):
        self._client.set(k, json.dumps(v))
              
    def get(self, k:str) -> Dict:
        result = self._client.get(k)
        if not result:
            return {}
        return json.loads(result.decode("utf-8"))

redis_client = RedisClient(host='c-c9qeo5incl3k3k2porbr.rw.mdb.yandexcloud.net', port=6432, password='Demon7968080', cert_path='path_to_cert')


