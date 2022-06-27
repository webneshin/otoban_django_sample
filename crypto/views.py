import json
import requests
from django.utils.translation import ugettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from crypto.serializer import Coin_Price_Serializer, Input_Test_Serializer, Outpot_Test_Serializer


class Coin_Price_View(APIView):
    serializer_class = Coin_Price_Serializer
    permission_classes = [permissions.IsAuthenticated]

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


class Test_Swagger(APIView):
    """
    Tozihat
    """
    serializer_class = Input_Test_Serializer

    # @extend_schema(description='Your description!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    def post(self, request):
        serializer_inpout = Input_Test_Serializer(data=request.data)
        if serializer_inpout.is_valid():
            if serializer_inpout.data['age'] > 40:
                ss = 'pir'
            else:
                ss = 'javan'
            s = Outpot_Test_Serializer(data={
                "full_name": f"{serializer_inpout.data['first_name']} {serializer_inpout.data['last_name']}",
                "age_status": ss
            }, many=True)
            if s.is_valid():
                return Response(s.data, status=status.HTTP_200_OK)
            else:
                raise ValidationError("Problem")


class Test_Swagger_Detail(APIView):

    def post(self, request, detail_id):
        return Response({"detail": detail_id}, status=status.HTTP_200_OK)
