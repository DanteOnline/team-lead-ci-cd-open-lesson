"""
Main module
"""
from say_something import show_text, say


while True:
    text = input()
    if text:
        show_text(text)
        say(text)
    else:
        break
