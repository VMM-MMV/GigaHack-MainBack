import redis
from reader import get_config
import json

class CustomRedis():
    redis_instance = None
    def __init__(self):
        self.redis_instance = redis.Redis(
            host=get_config("redis.host"),  # Redis server host
            port=get_config("redis.port"),  # Redis server port (default is 6379)
            password=None,                  # If Redis is protected with a password, include it here
            decode_responses=True           # To get the values as strings instead of bytes
        )

    def set_cache(self, id, info):
        curr_history= self.redis_instance.get(id)
        if not curr_history:
            curr_history = '[]'

        curr_history = json.loads(curr_history)
        curr_history.append({"user": info})

        self.redis_instance.set("message", json.dumps(curr_history))