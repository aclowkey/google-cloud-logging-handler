import logging
from logging import config

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'text': {
            'format': '%(message)s',
        },
        'json': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler'
        },
        'cloud_text': {
            'class': 'google_cloud_logging_handler.GoogleCloudHandler',
            'log_name': 'server-deep_app',
            'formatter': 'text'
        },
        'cloud_struct': {
            'class': 'google_cloud_logging_handler.GoogleCloudHandler',
            'log_name': 'server-deep_access',
            'formatter': 'json',
            'parse_json': True
        }
    },
    'loggers': {
        'text': {
            'level': 'INFO',
            'handlers': ['cloud_text', 'stdout']
        },
        'json': {
            'level': 'INFO',
            'handlers': ['cloud_struct', 'stdout']
        }
    }
}

config.dictConfig(LOG_CONFIG)
text_logger = logging.getLogger('text')
text_logger.info("Text 1")

json_logger = logging.getLogger('json')
json_logger.info({
    "message": "Text 2",
    "ip": "10.15.12.23",
    "user": "Alex",
})
