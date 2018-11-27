from setuptools import setup

setup(
    name='Google cloud logging handler',
    version='1.0',
    descrition='Logs directly to google cloud',
    license='MIT',
    author='Alex Chaplianka',
    author_email='alexettelis@gmail.com',
    keywords=['google-cloud','logging'],
    packages=['google_cloud_logging_handler'],
    install_requires=['google-cloud-logging']
)
