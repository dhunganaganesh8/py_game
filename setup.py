try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Ganesh Dhungana',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dhunganaganesh8@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['bin/math.py'],
    'name': 'projectname'
}

setup(**config)
