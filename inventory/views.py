from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from inventory.models import Item

def index(request):
    return render(request, 'inventory/homepage.html')

def items_pagination(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 3) # records per page
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return render(request, 'inventory/list_pagination.html', {"items": items})

def items_list(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {'items': items})

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'inventory/item_detail.html', {
         'item': item,
    })
