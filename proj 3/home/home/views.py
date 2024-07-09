from django.shortcuts import render



def home(request):
    movies = {
        
        "The Shawshank Redemption": "1994-09-22",
        "The Godfather": "1972-03-24",
        "The Dark Knight": "2008-07-18",
        "Pulp Fiction": "1994-10-14",
        "Forrest Gump": "1994-07-06",
        "Inception": "2010-07-16",
        "Fight Club": "1999-10-15",
        "The Matrix": "1999-03-31",
        "The Lord of the Rings: The Fellowship of the Ring": "2001-12-19",
        "Interstellar": "2014-11-07"
    }

    return render(request, "index.html",{"context":movies})