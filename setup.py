from setuptools import setup

setup(
    name='django-loki-logger',
    version='0.0.1',
    packages=['django_loki_logger'],
    url='https://github.com/FIRST-ELD/django-loki-logger',
    license='MIT',
    author='Dozorov',
    author_email='ivan@firsteld.com',
    description='Logging handler with loki for django',
    keywords=['python', 'loki', 'grafana', 'logging', 'metrics'],
    install_requires=[
        'requests',
        'pytz',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Environment :: Web Environment",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 3 - Alpha '
    ],
)
