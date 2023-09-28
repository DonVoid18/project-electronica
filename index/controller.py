import pyfirmata2
import time
# autodetect
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

def encenderLED():
    print("Encendiendo LED")
    board.digital[2].write(1)

def encenderBUZZER():
    print("Encendiendo BUZZER")
    # board.digital[3].write(1)
    melodiaBUZZER()

def encenderMOTAGUA():
    # problema
    print("Encendiendo MOT.AGUA")
    board.digital[4].write(1)
    

def encenderCAMARA():
    # problema
    print("Encendiendo CAMARA")
    board.digital[5].write(1)

def encenderFOCO():
    print("Encendiendo FOTO")
    board.digital[6].write(1)

def apagarTODO():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
    board.digital[6].write(0)
    print("Apagando todas")

def encenderTODO():
    board.digital[2].write(1)
    board.digital[3].write(1)
    board.digital[4].write(1)
    board.digital[5].write(1)
    board.digital[6].write(1)
    melodiaBUZZER()
    print("Encendiendo todas")

def melodiaBUZZER():
    print("Reproduciendo música")
    # Define constants for note frequencies and durations
    Do = 523.25
    Re = 587.33
    Mi = 659.26
    Fa = 698.46
    Sol = 783.99
    La = 880.0
    Si = 987.77
    Pausa = 0.0
    duracion = 1000
    negra = 62  # 1000ms
    corchea = 31  # 500ms
    blanca = 125  # 2000ms
    retardo = 100  # 750ms

    # Define buzzer pins
    pinBuzzer1 = 3
    pinBuzzer2 = 3

    # Setup function (not used in this case)
    def play_note(note, duration_ms, buzzer_pin):
        if note == Pausa:
            time.sleep(duration_ms / 1000.0)
            return

        frequency = note
        duration = duration_ms / 1000.0

        period = 1.0 / frequency
        cycles = int(duration / (2 * period))

        for _ in range(cycles):
            board.digital[buzzer_pin].write(1)
            time.sleep(period)
            board.digital[buzzer_pin].write(0)
            time.sleep(period)

    def loop():
        # First measure
        play_note(Sol, negra, pinBuzzer1)
        time.sleep(negra / 1000.0)
        play_note(Re, negra, pinBuzzer2)
        time.sleep(negra / 1000.0)
        play_note(La, negra, pinBuzzer1)
        time.sleep(negra / 1000.0)
        play_note(Fa, negra, pinBuzzer2)
        time.sleep(negra / 1000.0)
        play_note(Do, negra, pinBuzzer1)
        time.sleep(negra / 1000.0)
        play_note(Sol, negra, pinBuzzer2)
        time.sleep(negra / 1000.0)

        # Second measure
        play_note(Do, corchea, pinBuzzer1)
        time.sleep(corchea / 1000.0)
        play_note(Sol, corchea, pinBuzzer2)
        time.sleep(corchea / 1000.0)
        play_note(Sol, negra, pinBuzzer1)
        time.sleep(negra / 1000.0)
        play_note(Re, negra, pinBuzzer2)
        time.sleep(negra / 1000.0)
        play_note(La, negra, pinBuzzer1)
        time.sleep(negra / 1000.0)
        play_note(Fa, negra, pinBuzzer2)
        time.sleep(negra / 1000.0)
        time.sleep(corchea / 1000.0)
        time.sleep(corchea / 1000.0)
    loop()

# def encenderBuzzer():
#     print("Encendiendo buzzer")
#     # Play "Happy Birthday" melody
#     happy_birthday_melody()

# def buzzerPattern(pin, note_duration_ms):
#     board.digital[pin].write(1)
#     time.sleep(note_duration_ms / 1000.0)  # Convert milliseconds to seconds
#     board.digital[pin].write(0)

# def happy_birthday_melody():
#     # Define the notes and their durations for "Happy Birthday"
#     melody = [
#         ("C4", 500), ("C4", 500), ("G4", 500), ("G4", 500),
#         ("A4", 500), ("A4", 500), ("G4", 1000),
#         ("F4", 500), ("F4", 500), ("E4", 500), ("E4", 500),
#         ("D4", 500), ("D4", 500), ("C4", 1000),
#     ]

#     for note, duration in melody:
#         # Play each note with the specified duration
#         play_note(note, duration)

# def play_note(note, duration_ms):
#     # Define the frequencies for each note (you may need to adjust these)
#     notes = {
#         "C4": 261.63,
#         "D4": 293.66,
#         "E4": 329.63,
#         "F4": 349.23,
#         "G4": 392.00,
#         "A4": 440.00,
#         "B4": 493.88,
#         "C5": 523.25,
#         "D5": 587.33,
#         "E5": 659.26,
#         "F5": 698.46,
#         "G5": 783.99,
#     }

#     if note in notes:
#         frequency = notes[note]
#         buzzer_pin = 3  # Change this to the appropriate buzzer pin
#         duration = duration_ms / 1000.0  # Convert milliseconds to seconds

#         # Calculate the period for the note
#         period = 1.0 / frequency

#         # Calculate the number of cycles to generate for the note duration
#         cycles = int(duration / (2 * period))

#         # Play the note by toggling the buzzer pin
#         for _ in range(cycles):
#             buzzerPattern(buzzer_pin, int(period * 1000))
#             time.sleep((period * 1000) / 2000)  # Add a small delay between cycles
#     else:
#         # If the note is not in the notes dictionary, do nothing (rest)
#         time.sleep(duration_ms / 1000.0)
