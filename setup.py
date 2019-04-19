from setuptools import setup

setup(
    name='repath',
    version='0.2.0',
    author='Nikolaos Coutsos',
    author_email='ncoutsos@gmail.com',
    description='Generate regular expressions form ExpressJS path patterns',
    long_description=(
        'A port of the pathToRegexp node module to Python.'
        'Parses express-style paths to PCRE regular expression patterns, taking'
        'advantage of named capture groups.'
    ),
    packages=[],
    py_modules=['repath'],
    keywords='url path pattern regex express route',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
