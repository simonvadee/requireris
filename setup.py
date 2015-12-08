#!/usr/bin/env python3.4

from setuptools import setup, find_packages

def install():
    return setup(name = "requireris",
                 version = "0.1",
                 install_requires=["python-gnupg"]
    )

if __name__ == "__main__":
    install()
