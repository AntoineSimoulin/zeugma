#!/usr/bin/env python

from setuptools import setup
import sys

setup(name='zeugma',
      packages=['zeugma'],
      version='0.42',
      license='MIT',
      description="Unified framework for word embeddings (Word2Vec, GloVe, FastText, ...) compatible with scikit-learn Pipeline",
      long_description=open('README.rst' ,'r').read(),
      long_description_content_type='text/x-rst',
      author='Nicolas Thiebaut',
      author_email='nkthiebaut@gmail.com',
      url='https://github.com/nkthiebaut',
      download_url='https://github.com/nkthiebaut/zeugma/archive/0.42.tar.gz',
      keywords=['embeddings'],
      classifiers=[],
      setup_requires=[
          'pytest-runner',
          'numpy>=1.13.3',
          'Cython>=0.27.3',
      ],
      install_requires=[
          'numpy>=1.13.3',
          'Cython>=0.27.3',
          'pandas>=0.20.3',
          'gensim>=3.5.0',
          'scikit_learn>=0.19.1',
          'tensorflow>=1.5.0',
          'keras>=2.1.3',
      ],
      tests_require=['pytest>=3.3.2'],
      )
