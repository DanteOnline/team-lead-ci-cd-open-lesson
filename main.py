from say_something import show_text


while True:
    text = input()
    if text:
        show_text(text)
        #say(text)
    else:
        break
