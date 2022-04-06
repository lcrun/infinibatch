from setuptools import setup, find_packages

setup(
    name='infinibatch',
    version='0.1.1',
    url='https://github.com/lcrun/infinibatch',
    author='Frank Seide',
    author_email='fseide@microsoft.com',
    description='Infinibatch is a library of checkpointable iterators for randomized data loading of massive data sets in deep neural network training.',
    packages=find_packages()
)
