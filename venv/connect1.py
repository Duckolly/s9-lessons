import redis

r = redis.StrictRedis(
    host="c-c9qeo5incl3k3k2porbr.rw.mdb.yandexcloud.net",
    port=6380,
    password="Demon7968080",
    ssl=True,
    ssl_ca_certs="/home/<домашняя директория>/.redis/YandexInternalRootCA.crt",
)

r.set("foo", "bar")
print(r.get("foo"))