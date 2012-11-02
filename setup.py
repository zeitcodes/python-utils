import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

setup(
    name = 'python-utilikilt',
    version = __import__('python_utils').get_version().replace(' ', '-'),
    url = 'https://bitbucket.org/nextscreenlabs/python-utils',
    author = 'Jason Christa',
    author_email = 'jason@zeitcode.com',
    description = 'A collection of general python utility functions.',
    long_description = get_readme(),
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    install_requires = read_file('requirements.txt'),
    classifiers = [
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
