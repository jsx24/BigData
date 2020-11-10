# -*- coding: utf-8 -*-

# Scrapy settings for bookcrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# from bookcrawler.configs.db_configs import redis_config, dynamodb_config
from configs.db_configs import redis_config, dynamodb_config

BOT_NAME = 'bookcrawler'

SPIDER_MODULES = ['bookcrawler.spiders']
NEWSPIDER_MODULE = 'bookcrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookcrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bookcrawler.middlewares.BookcrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'bookcrawler.middlewares.RotateUserAgentMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   'bookcrawler.pipelines.DynamoDbPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# 启用scrapy-redis自带的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 启用调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否在关闭spider的时候保存记录，保存（TRUE）,不保存（False）
SCHEDULER_PERSIST = True
# 使用优先级调度请求队列 （默认使用）
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
# REDIS_URL = None #一般可不带
# 指定master的redis地址端口，有密码的加上密码

REDIS_HOST = redis_config()['host']
REDIS_PORT = redis_config()['port']

REDIS_PARAMS = {
    'password': redis_config()['password']
}

# scrapy-dynamodb 配置
AWS_ACCESS_KEY_ID = dynamodb_config['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = dynamodb_config['AWS_SECRET_ACCESS_KEY']
DYNAMODB_PIPELINE_REGION_NAME = dynamodb_config['DYNAMODB_PIPELINE_REGION_NAME']
DYNAMODB_PIPELINE_TABLE_NAME = dynamodb_config['DYNAMODB_PIPELINE_TABLE_NAME']
DYNAMODB_ENDPOINT_URL = dynamodb_config['DYNAMODB_ENDPOINT_URL']