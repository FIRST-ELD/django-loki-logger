# Django-Loki-Logger

[![PyPI version](https://img.shields.io/pypi/v/django-loki-logger.svg)](https://pypi.org/project/django-loki-logger/)
[![Python version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/pypi/l/django-loki-logger.svg)](https://opensource.org/licenses/MIT)

Django logging handler and formatter with grafana/loki
https://grafana.com/loki

Using pip:

```shell
pip install django-loki-logger
```

# Django-loki-logger Usage

`LokiLoggerHttpHandler` is a custom logging handler which sends Loki-messages using `http` or `https`.

Modify your `settings.py` to integrate `django-loki-logger` with Django's logging:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'loki': {
            '()': django_loki_logger.LokiLoggerFormatter,
            'fmt': '%(levelname)s %(message)s [%(module)s]',
            'source': 'my-django-app',
            'fqdn': True,
            'label_map': {'level': 'severity'}
        }
    },
    'handlers': {
        'loki': {
            '()': django_loki_logger.LokiLoggerHttpHandler,
            'host': 'loki.example.com',
            'port': 3100,
            'timeout': 1.0,
            'source': 'my-django-app'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['loki'],
            'level': 'INFO',
            'propagate': True,
        },
        'myapp': {
            'handlers': ['loki'],
            'level': 'DEBUG',
        }
    }
}
```

