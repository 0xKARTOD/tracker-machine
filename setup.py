from setuptools import setup

APP = ['app.py']
DATA_FILES = ['icon.jpg']
APP_NAME = 'Tracker Machine'


OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'LSUIElement': True,
        'CFBundleVersion': "1.0",
        'CFBundleShortVersionString': "1.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, All Rights Reserved"
    },
    'packages': ['rumps','requests']
}

setup(
    app = APP,
    name = APP_NAME,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'], install_requires = ['rumps', 'requests']
)