# encoding: utf-8
from setuptools import setup, find_packages
from eureka import __version__ as version
import sys

if sys.version_info >= (3,2):
    install_requires = ['dnspython3','requests']
else:
    install_requires = ['dnspython','requests']

setup(
    name = 'python-eureka',
    version = version,
    description = 'A python interface for Netflix Eureka',
    author = u'Kristian Øllegaard',
    author_email = 'kristian@oellegaard.com',
    zip_safe=False,
    include_package_data = True,
    packages = find_packages(exclude=[]),
    install_requires= install_requires,
    use_2to3=True
)