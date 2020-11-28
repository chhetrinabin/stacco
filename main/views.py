from django.shortcuts import render


def moderator(request):
    context = {}
    return render(request, 'main/moderator.html', context)


def student(request):
    context = {}
    return render(request, 'main/student.html', context)


def landlord(request):
    context = {}
    return render(request, 'main/landlord.html', context)