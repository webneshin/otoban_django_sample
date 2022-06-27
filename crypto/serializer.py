from rest_framework import serializers



class Coin_Price_Serializer(serializers.Serializer):
    coin = serializers.CharField(help_text='sample: BTC')

class Input_Test_Serializer(serializers.Serializer):
    first_name = serializers.CharField(help_text='Sajjad')
    last_name = serializers.CharField(help_text='Ebrahimi')
    age = serializers.IntegerField(help_text='Number')

class Outpot_Test_Serializer(serializers.Serializer):
    full_name = serializers.CharField()
    age_status = serializers.CharField()
