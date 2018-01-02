from setuptools import setup

setup(
    name='executor',
    version='0.1',
    packages=['executor'],
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
        'lxml'
    ],
    entry_points=
    """
    [console_scripts]
    executor=executor.main:cli
    """
)