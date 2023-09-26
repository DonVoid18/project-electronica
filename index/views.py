from django.shortcuts import render, redirect
from index.controller import blueOn, greenOn, redOn , yellowOn, allOff, encenderBuzzed, encenderMotor

# Create your views here.
def index_view (request):
    if request.POST:
        id = request.POST['id']
        if int(id) == 1:
            redOn()
        elif int(id) == 2:
            greenOn()
        elif int(id) == 3:
            blueOn()
        elif int(id) == 4:
            yellowOn()
        elif int(id) == 5:
            allOff()
        elif int(id) == 7:
            encenderBuzzed()
        elif int(id) == 8:
            encenderMotor()
        print(id)
    return render(request, 'index.html')