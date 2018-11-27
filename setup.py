from setuptools import setup

setup(
    name='Google cloud logging handler',
    version='1.0',
    descrition='Logs directly to google cloud',
    license='MIT',
    author='Alex Chaplianka',
    author_email='alexettelis@gmail.com',
    download_url='https://github.com/aclowkey/google-cloud-logging-handler/archive/1.0.0.tar.gz',
    keywords=['google-cloud','logging'],
    packages=['google_cloud_logging_handler'],
    install_requires=['google-cloud-logging']
)
