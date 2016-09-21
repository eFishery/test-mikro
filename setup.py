from distutils.core import setup

setup(
    name = 'atduinotest',
    packages = ['atduinotest'], # this must be the same as the name above
    version = 'v0.2.5',
    description = 'atduinotest from eFishery',
    author = 'eFishery',
    author_email = 'ans4175@efishery.com',
    url = 'https://github.com/eFishery/test-mikro',
    download_url = 'https://github.com/eFishery/test-mikro/tarball/v0.2',
    keywords = ['testing', 'arduino', 'efishery'], # arbitrary keywords
    py_modules=['atduinotest'],
    install_requires=[
        'pySerial'
    ],
    entry_points='''
        [console_scripts]
        atduinotest=atduinotest:cli
    ''',
)