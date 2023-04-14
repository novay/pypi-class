from setuptools import setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name="pypi_class",
    version="0.0.1",
    description="Contoh Library Python dengan Class.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/novay/pypi-class",
    author="Novianto Rahmadi",
    author_email="novay@btekno.id",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["pypi_class"]
)