from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
         'items': items,
    })
    # return HttpResponse('<p>In index view</p>')

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoeNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html')
    # return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))

