#!/usr/bin/env python2.7
import os
import unittest

from webp import mode

class TestCase(unittest.TestCase):
    
    def test_translate(self):
        test_word = "water"
        home_language = "en"
        target_language = "es"
        trans_word = mode.translate(home_language,target_language,test_word)
        assert trans_word == "agua"

