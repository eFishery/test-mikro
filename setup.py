from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='test_mikro',
      version='0.1',
      description='Python libs for test-mikro eFishery',
      keywords='at mikro test',
      url='https://github.com/eFishery/test-mikro',
      author='ans4175',
      author_email='ans4175@efishery.com',
      license='MIT',
      packages=['test_mikro'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
    )