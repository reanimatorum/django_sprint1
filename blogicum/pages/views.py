from django.shortcuts import render


app_name = 'pages'


# Create your views here.
def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
