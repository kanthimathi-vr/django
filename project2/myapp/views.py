from django.shortcuts import render

# Create your views here.


def card(request):
    context = {
        'name': 'Kanthimathi V R',
        'role': 'Full-Stack Web Developer',
        'email': 'mathi.v.r.1990@gmail.com',
        'github': 'https://github.com/Kanthimathi-vr',
        'profile_image': 'myapp/img/profile.jpg',
    }
    return render(request, 'myapp/card.html', context)
