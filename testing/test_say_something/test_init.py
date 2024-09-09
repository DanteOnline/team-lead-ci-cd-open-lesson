"""
Test Init
"""
#import os

from say_something import show_text


def test_show_text():
    """
    Test show text
    :return:
    """
    show_text('test text')
    assert True


# def test_say():
#     """
#     Test say
#     :return:
#     """
#     say('some text')
#     assert 'tmp.audio' in os.listdir()
