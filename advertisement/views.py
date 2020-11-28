# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import AdsForm

# def list_ads(request):
#     return HttpResponse("Ads list")


# def add_ads(request):
#     if request.method == 'POST':
#         form = AdvertisementForm(request.POST)
#         if form.is_valid():
#             cd =  form.cleaned_data

#     else:
#         form = AdvertisementForm()
#     return render(request, 'advertisement/add_ads.html',
#     {'form': form}
#     )


# def edit_ads(request):
#     # if request.method == 'POST'
#     pass


from django.shortcuts import get_object_or_404, redirect, render
from .forms import AdsForm, AdsDeleteForm
from .models import Advertisement


def ads_list(request):
    pass


def ads_view(request, pk=None):
    pass
    # ads = get_object_or_404(Advertisement, pk=pk)


def ads_create(request):
    if request.method == 'POST':
        form = AdsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ads_create')
    else:
        form = AdsForm()
    return render(request,
                  'advertisement/ads_create.html',
                  {
                      'form': form
                  })


def ads_edit(request, pk=None):
    ads = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdsForm(request.POST,
                        instance=ads)
        if form.is_valid():
            form.save()
            return redirect('ads_create')
    else:
        form = AdsForm(instance=ads)

    return render(request,
                  'advertisement/ads_edit.html',
                  {
                      'form': form,
                      'ads': ads
                  })


def ads_delete(request, pk=None):
    ads = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdsDeleteForm(request.POST,
                              instance=ads)
        if form.is_valid():
            ads.delete()
            return redirect('ads_create')
    else:
        form = AdsDeleteForm(instance=ads)

    return render(request, 'advertisement/ads_delete.html',
                  {
                      'form': form,
                      'ads': ads,
                  })
