from django.shortcuts import render, redirect
from index.controller import encenderBUZZER, encenderFOCO, encenderMOTAGUA, encenderCAMARA , apagarTODO, encenderTODO, encenderLED

# Create your views here.
def index_view (request):
    if request.POST:
        id = request.POST['id']

        if int(id) == 1:
            encenderLED()
        elif int(id) == 2:
            encenderBUZZER()
        elif int(id) == 3:
            encenderMOTAGUA()
        elif int(id) == 4:
            encenderCAMARA()
        elif int(id) == 5:
            apagarTODO()
        elif int(id) == 6:
            encenderTODO()
        elif int(id) == 7:
            encenderFOCO()
        
        print("ID: ", id)
    return render(request, 'index.html')