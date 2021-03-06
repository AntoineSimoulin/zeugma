# -*- coding:utf-8 -*-
"""
Created on the 01/26/2018
@author: Nicolas Thiebaut
@email: nicolas@visage.jobs
"""
from zeugma.texttransformers import RareWordsTagger, ItemSelector, TextStats


class TestTextTransformers(object):
    """ Test text transformers """

    def test_rare_words_tagger(self, sample_corpus):
        """ Test rare words tagging on a basic corpus """
        rare_tagger = RareWordsTagger(min_count=2)
        tag = rare_tagger.oov_tag
        out = rare_tagger.fit_transform(sample_corpus)
        assert len(out) == len(sample_corpus)
        assert out[0] == tag + ' a ' + tag + ' ' + tag + ' text'

    def test_item_selector(self):
        test_case = {'a': 1, 'b': 2}
        item_selector = ItemSelector('a')
        out = item_selector.fit_transform(test_case)
        assert out == test_case['a']

    def test_text_stats(self, sample_corpus):
        text_stats = TextStats()
        out = text_stats.fit_transform(sample_corpus)
        assert out[0]['length'] == len(sample_corpus[0])
        assert out[0]['num_sentences'] == 0
