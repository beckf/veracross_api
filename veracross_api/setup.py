from distutils.core import setup
setup(
    name = 'veracross_api',
    packages = ['veracross_api'],
    version = '0.1',
    license='MIT',
    description = 'Simple library for interacting with the Veracross API',
    author = 'Forrest Beck',
    author_email = 'forrest.beck@da.org',
    url = 'https://github.com/beckf',
    download_url = 'https://github.com/beckf/veracross_api/archive/v.01.tar.gz',
    keywords = ['Veracross', 'API'],
    install_requires=[
        'requests'
    ],
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