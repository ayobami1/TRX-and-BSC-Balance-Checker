from setuptools import setup, find_packages

setup(
    name='pycryptchecker',
    version='1.0.0',
    description='Trx and Bsc Wrapper',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/your-package-name',
    packages=find_packages(),
    install_requires=[
        'requests',
        'base58',
        # Add other dependencies here
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
