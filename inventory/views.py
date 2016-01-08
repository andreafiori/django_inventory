from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from inventory.models import Item, ItemSerializer

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
    return render(request, 'inventory/item_list.html', {'items': items})

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'inventory/item_detail.html', {
         'item': item,
    })

@api_view(['GET', 'POST'])
def item_collection(request):
    if request.method == 'GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_element(request, pk):        
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)