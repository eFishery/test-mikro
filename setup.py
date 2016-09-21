from distutils.core import setup

setup(
    name = 'attest',
    version = '0.1.0',
    description = README.md,
    author = 'eFishery',
    author_email = 'ans4175@efishery.com',
    url = 'https://github.com/eFishery/test-mikro', 
    py_modules=['assert_serial'],
    install_requires=[
        'serial','pySerial'
    ],
    entry_points='''
        [console_scripts]
        attest=assert_serial:main
    ''',
)