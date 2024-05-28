#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="aibe_coffeebox",
    version="0.0.1",
    description="A GUI app in python to manage the coffee box at work with a Raspberry Pi.",
    author="",
    author_email="",
    url="https://github.com/MischaD/aibe_coffeebox",
    install_requires=["ttkbootstrap", "qrcode"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "aibe_coffeebox = main:main",
        ]
    },
)
