#!/usr/bin/env python

from distutils.core import setup

setup(
    name="mediathekviewweb_cli",
    version="0.1",
    description="CLI utility to query the mediathekviewweb",
    author="Joachim Lusiardi",
    author_email="joachim@lusiardi.de",
    url="https://github.com/jlusiardi/mediathekviewweb_cli",
    install_requires=[
        "websocket-client",
        "requests",
    ],
    scripts=['bin/mediathekviewweb_cli'],
)
