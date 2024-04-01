from django.shortcuts import render

def newspage(request):
    massage = "Hello, World!"
    context = {
        "massage": massage
    }
    return render(request, './newspage.html', context)
