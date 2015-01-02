"""
Flask-SegmentIO
---------------

Adds SegmentIO support to your Flask application.
"""
import codecs
import os
import re
from setuptools import setup


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r') as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="flask-segmentio",
    version=find_version("flask_segmentio", "__init__.py"),
    url="http://github.com/iromli/flask-segmentio",
    license="MIT",
    author="Isman Firmansyah",
    author_email="isman.firmansyah@gmail.com",
    description="Adds SegmentIO support to your Flask application",
    long_description=__doc__,
    packages=["flask_segmentio"],
    zip_safe=False,
    install_requires=[
        "analytics-python",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ]
)
