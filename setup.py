import os

from setuptools import setup, Extension

ext = Extension('pack_command', sources=['pack_command.c'])

setup(
    name='pack command',
    version='0.18',
    url='',
    license='MIT',
    author='Simon Zimmermann',
    author_email='simon@insmo.com',
    description='Implements a faster Redis pack_command',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    ext_modules=[ext],
)
