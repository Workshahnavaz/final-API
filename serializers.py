from rest_framework import serializers
from.models import *

class perantstudentserializers(serializers.ModelSerializer):
    class Meta:
        model = parentstudent
        fields = "__all__"

    def validate(self,data):
        if data ['age'] < 18:
            raise serializers.ValidationError({"error" : "wrong"})
        return data
    
    def validate(self, data):
        if data ['name'] :
            for i in data ['name']:
                i.isdigit()
                raise serializers.ValidationError({"show" : "invalid"})
        return 
    
    # def validate(self,data):
    #     for char in data['name']:
    #         if not data ['name'].isalpha():
    #                 raise serializers.ValidationError({"error"})
    #     return data
            
    def validate(self,data):
        if data ['mail']:
            for i in data ['mail']:
                    i.endwith("@gamil.com")
                    raise serializers.ValidationError({"mail should end with @gamil.com"})
        return data
    
    # def validate(self,data):
    #     if "@gmail.com" not in data ['email']:
    #         raise serializers.ValidationError({"mail should end with @gamil.com"})
    #     return data
    
class childstudentserializers(serializers.ModelSerializer):
    class Meta:
        model = childstudent
        fields = "__all__"