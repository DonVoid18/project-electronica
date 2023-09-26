import pyfirmata2

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

def encenderBucer():
    print("Encendiendo bucer")
    board.digital[3].write(1)
def encenderMotor():
    board.digital[4].write(1)
    print("Encendiendo motor")
