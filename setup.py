from setuptools import setup

setup(name='scrabble-host',
      version='0.1',
      description='A web service based host for scrabble games',
      url='https://github.com/oldironhorse/scrabble-host',
      download_url= \
          'https://github.com/oldironhorse/scrabble-host/archive/0.1.tar.gz',
      author='Simon Redding',
      author_email='s1m0n.r3dd1ng@gmail.com',
      license='GPL 3.0',
      packages=['scrabble.host'],
      install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
