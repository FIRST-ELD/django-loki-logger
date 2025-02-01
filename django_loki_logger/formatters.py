# loki_formatter.py
import logging
import sys
import socket
import requests
from typing import Optional, Dict, Any
from django.conf import settings

class LokiLoggerFormatter(logging.Formatter):
    """
    Enhanced Django formatter with Loki-specific formatting
    Includes log level handling and Django context
    """
    def __init__(self, 
                 fmt: Optional[str] = None, 
                 datefmt: Optional[str] = None, 
                 style: str = '%',
                 source: str = 'django',
                 fqdn: bool = False,
                 label_map: Optional[Dict[str, str]] = None):
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        self.source = source
        self.host = socket.getfqdn() if fqdn else socket.gethostname()
        self.label_map = label_map or {}
        self.default_labels = {
            'source': self.source,
            'host': self.host,
            'framework': 'django',
            'level': 'info'
        }

    def _get_labels(self, record: logging.LogRecord) -> Dict[str, str]:
        """Generate labels with proper level handling"""
        labels = {
            'job': record.name,
            'level': record.levelname.lower(),
            'logger': record.name
        }
        
        # Add Django-specific context if available
        if hasattr(record, 'request'):
            labels['request_id'] = getattr(record.request, 'id', '')
            
        return {self.label_map.get(k, k): v for k, v in {**self.default_labels, **labels}.items()}

    def format(self, record: logging.LogRecord) -> Dict[str, Any]:
        """Format log record for Loki"""
        log_line = super().format(record)
        return {
            "streams": [
                {
                    "stream": self._get_labels(record),
                    "values": [
                        [str(int(record.created * 1e9)), log_line]
                    ]
                }
            ]
        }