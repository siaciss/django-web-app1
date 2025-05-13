from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.http import Http404
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
            
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form':form})

def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # Mettre à jour le groupe existant dans la BD
            form.save()
            return redirect('band-detail', band.id)
    
    else:
        # On pré-remplir le formulaire avec un groupe existant
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'band':band.name, 'form':form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        # Supprimer le groupe de la BD
        band.delete()
        return redirect('band-list')
    
    return render(request,'listings/band_delete.html', {'band':band})

def about(request):
    #return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')
    return render(request, 'listings/about.html')

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject = f'Message from {form.cleaned_data["name"] or "anomyme"} via Merchex Contact Us form',
                message = form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz']
            )
            return redirect("email-send")
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

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

def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            anno = form.save()
            return redirect('listing-detail', anno.id)
    
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form':form})

def listing_update(request, anno_id):
    listing = Listing.objects.get(id=anno_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing.save()
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'title':listing.title, 'form':form})    

def listing_delete(request, anno_id):
    listing = Listing.objects.get(id=anno_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('annonces-list')
    return render(request, 'listings/listing_delete.html', {'title':listing.title})

def email_send(request):
    return render(request, 'listings/email_send.html')
