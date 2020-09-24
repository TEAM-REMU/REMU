from django.shortcuts import render, redirect

# Create your views here.


def result(request):
    search = request.GET.get("search", "")
    print(search)
    return render(request, 'result.html')
