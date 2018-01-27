# -*- coding:utf-8 -*-
"""
Created on the 05/01/18
@author: Nicolas Thiebaut
@email: nkthiebaut@gmail.com
"""
import pytest
import numpy as np


@pytest.fixture(scope='module')
def sample_corpus():
    """ Return a sample corpus in a numpy.array """
    corpus = ['Here a first example text',
              'This is a second text with a weird word gwiurgergwggreg',
              'This is a second text with a weird word',
              "Et c'est un troisieme text avec un accent"]
    return np.array(corpus)

