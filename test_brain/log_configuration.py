import logging
import os

from rosys import helpers

project = 'test_brain'



def configure():
    config = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '%(asctime)s.%(msecs)03d [%(levelname)s] %(relative_path)s:%(lineno)d: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'filters': {
            'package_path_filter': {
                '()': helpers.PackagePathFilter,
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'filters': ['package_path_filter'],
                'formatter': 'default',
                'level': 'INFO',
                'stream': 'ext://sys.stdout'
            },
            'debugfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filters': ['package_path_filter'],
                'filename': os.path.expanduser('~/.rosys/debug.log'),
                'maxBytes': 1024 * 1000 * 10,  # each file max 10 mb
                'backupCount': 10  # max 100 mb of logs
            },
            'communicationfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filters': ['package_path_filter'],
                'filename': os.path.expanduser('~/.rosys/communication.log'),
                'maxBytes': 1024 * 1000 * 10,  # each file max 10 mb
                'backupCount': 50  # max 500 mb of logs
            }
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['console'],
                'level': 'WARN',
                'propagate': False,
            },
             'nicegui': {
        'handlers': ['debugfile'],
        'level': 'ERROR',
                'propagate': False,
            },
            'rosys.communication': {
                'handlers': ['communicationfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'asyncio': {
                'handlers': ['debugfile'],
                'level': 'WARNING',
                'propagate': False,
            },
            'rosys': {
                'handlers': ['console', 'debugfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            project: {
                'handlers': ['console', 'debugfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }

    logging.config.dictConfig(config)
    return logging.getLogger(project)
