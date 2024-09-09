"""
Test Init
"""
from say_something import show_text


def test_show_text():
    """
    Test show text
    :return:
    """
    show_text('test text')
    assert True
