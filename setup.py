from setuptools import setup, find_packages

setup(
    name='pycryptchecker',
    version='1.0.0',
    description='Trx and Bsc Wrapper',
    author='Ayocrypt',
    author_email='akinloluojo1@gmail.com',
    url='https://github.com/ayobami1/TRX-and-BSC-Balance-Checker.git',
    packages=find_packages(),
    install_requires=[
        'requests',
        'base58',
        'web3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
