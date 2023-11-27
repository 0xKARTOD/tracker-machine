from setuptools import setup

APP = ['app.py']
DATA_FILES = ['icon.jpg']

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'LSUIElement': True,
        'CFBundleVersion': "1.0"
    },
    'packages': ['rumps','requests']
}

setup(
    app = APP,
    name = 'Tracker Machine',
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'], install_requires = ['rumps', 'requests']
)