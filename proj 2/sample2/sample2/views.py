
from django.shortcuts import render



def home(request):
    context = {
        'friends':[
            "Jose", "Rose","jass","goss","Boss","Boom","Doom"
        ]
    }
    return render(request, "index.html",context)