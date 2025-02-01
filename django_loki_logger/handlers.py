import logging
import sys

import requests

from django_loki.formatters import LokiFormatter


class LokiLoggerHttpHandler(logging.Handler):
    """Improved Loki HTTP handler with better error handling"""
    def __init__(self, 
                 host: str = 'localhost', 
                 port: int = 3100, 
                 timeout: float = 0.5, 
                 protocol: str = 'http',
                 source: str = 'django',
                 fqdn: bool = False,
                 label_map: Optional[Dict[str, str]] = None):
        super().__init__()
        self._endpoint = f'{protocol}://{host}:{port}/loki/api/v1/push'
        self._timeout = timeout
        self._formatter = DjangoLokiFormatter(
            source=source,
            fqdn=fqdn,
            label_map=label_map
        )

    def setFormatter(self, fmt: logging.Formatter) -> None:
        """Ensure we only use compatible formatters"""
        if not isinstance(fmt, DjangoLokiFormatter):
            raise ValueError("This handler requires a DjangoLokiFormatter")
        self._formatter = fmt

    def emit(self, record: logging.LogRecord) -> None:
        """Send log record to Loki with improved error handling"""
        try:
            payload = self._formatter.format(record)
            response = requests.post(
                self._endpoint,
                json=payload,
                timeout=self._timeout
            )
            
            if response.status_code not in (200, 204):
                self.handleError(record)
        except requests.exceptions.RequestException as e:
            self.handleError(record)
        except Exception as e:
            self.handleError(record)

    def handleError(self, record: logging.LogRecord) -> None:
        """Custom error handling for failed log submissions"""
        sys.stderr.write(f"Failed to send log to Loki: {record.getMessage()}\n")
