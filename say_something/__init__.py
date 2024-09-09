import os

def show_text(text, speaker='mouse'):
    command = f'echo "{text}" | boxes -d {speaker}'
    os.system(command)
