import keyboard

output = open("log.txt", 'w')

def start():
    r = keyboard.record(until='`')
    r = str(r)
    r = r.replace(',', '')
    r = r.replace("KeyboardEvent(", '')
    r = r.replace("down)", '')
    r = r.replace("up)", '')
    output.write(r)
if __name__ == "__main__":
    start()
