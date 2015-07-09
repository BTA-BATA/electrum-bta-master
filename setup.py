#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-bta.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-bta.png'])
    ]


setup(
    name="Electrum-BTA",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'tlslite',
        'dnspython',
    ],
    package_dir={
        'electrum_bta': 'lib',
        'electrum_bta_gui': 'gui',
        'electrum_bta_plugins': 'plugins',
    },
    packages=['electrum_bta','electrum_bta_gui','electrum_bta_gui.qt','electrum_bta_plugins'],
    package_data={
        'electrum_bta': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_bta_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-bta'],
    data_files=data_files,
    description="Lightweight BataCoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="GNU GPLv3",
    url="http://electrum-bta.org",
    long_description="""Lightweight BataCoin Wallet"""
)
