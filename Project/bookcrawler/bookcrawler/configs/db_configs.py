import socket

# 线上环境
REDIS_PARAMS_PROD = {
    'host': '',
    'port': 6379,
    'password': ''
}

REDIS_PARAMS_DEV = {

            'host':'localhost',
            'port': 6379,
            'password':''
    }

# 线上环境配置是否开启
# 根据获取到的hostname 判断
if socket.gethostname() in ['jiasheng-MBP.local', 'bogon']:
    PROD_ENV = False
else:
    PROD_ENV = True

# PROD_ENV = False


def redis_config():
    """
    判断使用线上还是测试环境
    :return:
    """
    if PROD_ENV:
        redis_configs = REDIS_PARAMS_PROD

    else:
        redis_configs = REDIS_PARAMS_DEV

    return redis_configs



dynamodb_config = {
                "AWS_ACCESS_KEY_ID": "",  # '<aws access key id>'
                "AWS_SECRET_ACCESS_KEY": "",  # '<aws secret access key>'
                "DYNAMODB_PIPELINE_REGION_NAME": "",  # 'us-east-1'
                "DYNAMODB_PIPELINE_TABLE_NAME": "",  # 'my_table'
                "DYNAMODB_ENDPOINT_URL": "",  # '<dynamodb endpoint url>' # optional  (e.g.: http://localhost:8000)
             }