from setuptools import setup

setup(
    name='saga-config',
    packages=['sconfig'],
    package_dir={'sconfig': 'lib'},
    version='0.0.1',
    description='A config helper',
    author='Sagacify',
    author_email='dev@sagacify.com',
    url='https://github.com/Sagacify/config-py',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ]
)
