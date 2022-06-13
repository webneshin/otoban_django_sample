from rest_framework import serializers



class Coin_Price_Serializer(serializers.Serializer):
    coin = serializers.CharField(help_text='sample: BTC')
