import json
import requests
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from crypto.serializer import Coin_Price_Serializer


class Coin_Price_View(APIView):
    serializer_class = Coin_Price_Serializer

    def post(self, request):
        try:
            main = 'USDT'
            serializer = Coin_Price_Serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'error': 'please insert "coin"'
                }, status=status.HTTP_400_BAD_REQUEST)

            key = f'https://api.binance.com/api/v3/ticker/price?symbol={serializer.data["coin"]}{main}'

            data = requests.get(key)
            data_json = data.json()

            return Response(data_json, status=data.status_code)
        except:
            return Response({'error': 'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
