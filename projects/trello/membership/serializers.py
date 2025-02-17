from rest_framework import serializers
from .models import MemberModel
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = [ 'username' , 'first_name' , 'last_name' , 'password' , 'confirm_password' , 'email']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        try:
            if password and confirm_password and password != confirm_password:
                raise serializers.ValidationError("Passwords do not match")
            if len(password) < 8:
                raise serializers.ValidationError("Password should be at least 8 characters long")     
            validate_password(password)
            
            return attrs
        except serializers.ValidationError as e:
            raise e
            
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)


    def create(self, validated_data):
        print(type(validated_data))
        member = MemberModel.objects.create(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password=make_password(validated_data['password'])
        )
        member.save()
        return member       




class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = ['id','username' , 'first_name' , 'last_name' , 'email' ]


       