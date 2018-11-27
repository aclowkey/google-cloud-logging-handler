import json
from logging import StreamHandler
from google.cloud import logging


class GoogleCloudHandler(StreamHandler):
    def __init__(self, **kwargs):
        StreamHandler.__init__(self)
        if 'log_name' not in kwargs.keys():
            raise ValueError("Missing log_name value'")
        log_name = kwargs['log_name']
        if not isinstance(log_name, str):
            raise ValueError("Invalid value: log_name must be of type string")

        self.parse_json = False
        if 'parse_json' in kwargs.keys():
            parse_json = kwargs['parse_json']
            if not isinstance(parse_json, bool):
                raise ValueError("Invalid value: parse_json must be of type bool")
            self.parse_json = parse_json

        self.logger = logging.Client().logger(log_name)

    def emit(self, record):
        text = self.format(record)
        if self.parse_json:
            info = json.loads(text)
            self.logger.log_struct(severity=record.levelname, info=info)
        else:
            self.logger.log_text(severity=record.levelname, text=text)

