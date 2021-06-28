from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.http import response
from django.shortcuts import redirect
from .models import UrlDetailes

from django.shortcuts import render, HttpResponse

from .models import UrlDetailes
from .serializers import UrlDetailesSerailizer
from rest_framework.response import Response
from rest_framework import status


def redirect_shortner(request, slug):
    try:
        data = UrlDetailes.objects.get(shorted_url=slug)
        return redirect(data.original_url)
    except UrlDetailes.DoesNotExist:
        return HttpResponse('Url Not Existed')


class UrlViewSet(GenericAPIView):
    """
    It Will Return Long URL to Shorten URL
    """
    permission_classes = [AllowAny]
    serializer_class = UrlDetailesSerailizer

    def post(self, request, format=None):
        serializer_class = UrlDetailesSerailizer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            data = UrlDetailes.objects.get(
                original_url=serializer_class.data['original_url'])
            return Response('http://127.0.0.1:8000/{}'.format(data.shorted_url), status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
