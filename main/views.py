from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495634',
        'name': 'Favian Muhammad Rasyad Reswara',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)