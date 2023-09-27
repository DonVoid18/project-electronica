import pyfirmata2
import pyfirmata
import time
# autodetect
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

def blueOn():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Encendiendo verde")

def redOn():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Encendiendo rojo")

def greenOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)
    print("Encendiendo azul")

def yellowOn():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)
    print("Encendiendo Amarillo")

def allOff():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)
    print("Apagando todas")

# def allOn():
#     board.digital[2].write(1)
#     board.digital[3].write(1)
#     board.digital[4].write(1)
#     board.digital[5].write(1)
#     print("Encendiendo todas")

def encenderBuzzer():
    print("Encendiendo buzzer")
    buzzerPattern(3, 10, 2)

def encenderMotor():
    board.digital[4].write(1)
    print("Encendiendo motor")

def buzzerPattern(pin, recurrence, pattern):
    # Defining patterns by array of time delays
    pattern1 = [0.8, 0.2]
    pattern2 = [0.2, 0.8]
    flag = True

    # Running the loop for given repetition
    for i in range(recurrence):
        if pattern == 1:
            p = pattern1
        elif pattern == 2:
            p = pattern2

        # Follow pattern p to turn the buzzer on/off for time delay
        for delay in p:
            if flag is True:
                # Buzzer is on
                board.digital[pin].write(1)
                flag = False
                time.sleep(delay)

            else:
                # Buzzer is off
                board.digital[pin].write(0)
                flag = True
                time.sleep(delay)

    # Silent buzzer at the end of the pattern repetition
    board.digital[pin].write(0)
    board.exit()


# Execute the 'buzzerPattern' function with custom parameters