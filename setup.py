from setuptools import setup


# read the contents of your README file
from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='google_cloud_logging_handler',
    version='1.2',
    descrition='Logs directly to google cloud',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Alex Chaplianka',
    url="https://github.com/aclowkey",
    author_email='alexettelis@gmail.com',
    download_url='https://github.com/aclowkey/google-cloud-logging-handler/archive/v1.2.tar.gz',
    keywords=['google-cloud','logging'],
    packages=['google_cloud_logging_handler'],
    install_requires=['google-cloud-logging']
)
