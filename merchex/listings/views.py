from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    '''return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes préférés sont : </p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
        <p>Mes Annonces</p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
        </ul>
    """)'''
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    #return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings':listings})