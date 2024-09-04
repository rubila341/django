from django.http import HttpResponse

def hello_view(request):
    your_name = "rubila341"  #
    return HttpResponse(f"Hello, {your_name}")
