from nose.tools import *
from carpet_fishing import carpet_fishing

def test_fish():
    fishing = Fish()
    assert_equal(fishing.catch(), "trout")
