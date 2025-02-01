# Django-Loki-Logger
Django logging handler and formatter with grafana/loki

# Install Grafana

# Install Loki

## Installation methods


# Installation

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
            '()': DjangoLokiFormatter,
            'fmt': '%(levelname)s %(message)s [%(module)s]',
            'source': 'my-django-app',
            'fqdn': True,
            'label_map': {'level': 'severity'}
        }
    },
    'handlers': {
        'loki': {
            '()': LokiLoggerHttpHandler,
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

