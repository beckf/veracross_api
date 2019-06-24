from distutils.core import setup
import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='veracross_api',
    packages=['veracross_api'],
    version='0.5',
    description='Simple library for interacting with the Veracross API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Forrest Beck',
    author_email='forrest.beck@da.org',
    url='https://github.com/beckf/veracross_api',
    download_url='https://github.com/beckf/veracross_api/archive/v.02.tar.gz',
    keywords=['Veracross', 'API'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)