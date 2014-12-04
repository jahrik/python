from nose.tools import *
from ex48 import lexicon

def test_direstions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
