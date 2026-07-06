from django.shortcuts import render, redirect, get_object_or_404
from .models import Parking
from .forms import ParkingForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParkingSerializer
# Temporary change for Git practice

def index(request):
    parking = Parking.objects.all()
    return render(request, 'parking/index.html', {'parking': parking})


def add(request):
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParkingForm()

    return render(request, 'parking/form.html', {'form': form})


def edit(request, id):
    data = get_object_or_404(Parking, id=id)

    if request.method == 'POST':
        form = ParkingForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParkingForm(instance=data)

    return render(request, 'parking/form.html', {'form': form})


def delete(request, id):
    data = get_object_or_404(Parking, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect('/')

    return render(request, 'parking/delete.html', {'data': data})
@api_view(['GET', 'POST'])
def parking_list(request):

    if request.method == 'GET':
        parking = Parking.objects.all()
        serializer = ParkingSerializer(parking, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParkingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def parking_detail(request, id):

    try:
        parking = Parking.objects.get(id=id)
    except Parking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ParkingSerializer(parking, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)