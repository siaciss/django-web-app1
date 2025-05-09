from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.http import Http404
from listings.forms import ContactUsForm

def band_list(request):
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
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    if not band:
        raise Http404("Ce group est introuvable")
    else:
        return render(request, 'listings/band_detail.html', {'band':band})

def about(request):
    #return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')
    return render(request, 'listings/about.html')

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()  # Ajout d'un nouveau formulaire ici
    return render(request, 'listings/contact.html', {'form': form})  # Passe le formulaire au gabarit

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings':listings})

def listing_detail(request, anno_id):
    annonce = Listing.objects.get(id=anno_id)
    return render(request, "listings/listing_detail.html", {"annonce":annonce})
