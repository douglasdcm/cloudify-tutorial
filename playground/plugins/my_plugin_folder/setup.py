from setuptools import setup

setup(
    name='my_plugin_pack',
    version='1.0',
    author='Cloudify',
    packages=['.'],
    install_requires=['cloudify-common>=5.0.0'],
)