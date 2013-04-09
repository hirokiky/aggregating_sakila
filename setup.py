import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
hosts = '192.168.56.1'

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_layout',
    'colander',
    'zope.sqlalchemy',
    'waitress',
    'webhelpers',
    ]

setup(name='sakila',
      version='0.0',
      description='sakila',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='sakila',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sakila:main
      [console_scripts]
      initialize_sakila_db = sakila.scripts.initializedb:main
      """,
      )
