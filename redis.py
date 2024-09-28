import redis
from reader import get_config

def get_redis():
    return redis.Redis(
        host=get_config("redis.host"),  # Redis server host
        port=get_config("redis.port"),  # Redis server port (default is 6379)
        password=None,                  # If Redis is protected with a password, include it here
        decode_responses=True           # To get the values as strings instead of bytes
    )