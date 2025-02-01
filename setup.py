from setuptools import setup

setup(
    name='django-loki-logger',
    version='0.0.2',
    packages=['django_loki_logger'],
    url='https://github.com/FIRST-ELD/django-loki-logger',
    license='MIT',
    author='Dozorov',
    author_email='ivan@firsteld.com',
    description='Logging handler with Loki for Django',
    keywords=['python', 'loki', 'grafana', 'logging', 'metrics', 'django', 'monitoring'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        # License
        'License :: OSI Approved :: MIT License',

        # Environment
        'Environment :: Web Environment',
        'Framework :: Django',

        # Supported Python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        # Development Status (3 - Alpha, 4 - Beta, 5 - Production/Stable)
        'Development Status :: 4 - Beta',

        # Topics
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: Log Analysis',
    ],
)
