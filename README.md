# google-cloud-logging-handler
Allows logging directly into Google Cloud.

## Motivation
When you don't want to log to text files and have a sidecar to ship your logs to Google Cloud, you can use this to send the logs directly to Google Cloud.

This is similar to what the [Logback plugin](https://github.com/googleapis/google-cloud-java/tree/master/google-cloud-clients/google-cloud-contrib/google-cloud-logging-logback) is intended for.

## Usage
You can use it just like any other logging.Handler.

For example
```python
import logging
from logging import config

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'text': {
            'format': '%(message)s',
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
        }
    },
    'loggers': {
        'text': {
            'level': 'INFO',
            'handlers': ['cloud_text', 'stdout']
        }
    }
}

config.dictConfig(LOG_CONFIG)
text_logger = logging.getLogger('text')
text_logger.info("Text 1")
```
