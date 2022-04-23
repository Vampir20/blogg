from django.shortcuts import render

# Create your views here.
def reviews_page(request):

    return render(request, "Reviews/reviews.html")