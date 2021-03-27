from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, "input.html")

def calc(request):
    x = request.GET['x']
    n = request.GET['n']
    sum = 0
    for i in range(1, n + 1):
        val = x ** (-i)
        sum = sum + val

    return render(request, "result.html", {"result": sum})

