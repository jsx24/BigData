# from bookcrawler.configs.db_configs import redis_config
from   configs.db_configs import redis_config
import redis


REDIS_CONFIG = redis_config()

r = redis.StrictRedis(host=REDIS_CONFIG['host'],
                      port=REDIS_CONFIG['port'],
                      password=REDIS_CONFIG['password'])

r.lpush('book_spider:start_urls', 'https://www.barnesandnoble.com/h/books/browse/')

