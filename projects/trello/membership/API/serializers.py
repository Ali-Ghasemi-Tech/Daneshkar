from rest_framework import serializers
from ..models import MemberModel
from django.contrib.auth.password_validation import validate_password



class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = MemberModel
        exclude = ['is_active' , 'last_login']
        widgets ={
            'password': {'write_only': True},
        }

        def validate_username(self , validated_data):
            username = validated_data['username']

            if not username.isalnum() and not '_' in username:
                raise serializers.ValidationError('username should only contain alphabetic characters or underscore!')
            if username[0].isdigit():
                raise serializers.ValidationError('username can not start with a digit')
            return username
    
        
        
        def validate_first_name(self , validated_data):
            first_name = validated_data['first_name']
            
            if not first_name.isalpha():
                raise serializers.ValidationError('first name should only contain alphabetic characters')
            
            return first_name
        
        def validate_last_name(self , validated_data):
            last_name = validated_data['first_name']
            
            if not last_name.isalpha():
                raise serializers.ValidationError('last name should only contain alphabetic characters')
            
            return last_name  

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
            
            

        def create(self, validated_data):
            member = MemberModel.objects.create_user(
                username=validated_data['username'],
                first_name = validated_data['firstnam'],
                last_name = validated_data['lastname'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return member
        

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = ['firstname', 'lastname', 'username']

    def validate_username(self, value):
        if not value.isalnum() and '_' not in value:
            raise serializers.ValidationError("Username should only contain alphabetic characters or underscore!")
        if value[0].isdigit():
            raise serializers.ValidationError("Username cannot start with a digit")
        return value

    def validate_first_name(self, value):
        if not value.isalpha(): 
            raise serializers.ValidationError("First name should only contain alphabetic characters")
        return value

    def validate_last_name(self, value):
        if not value.isalpha(): 
            raise serializers.ValidationError("Last name should only contain alphabetic characters")
        return value 


    def update(self, instance, validated_data):
        """
        Update the MemberModel instance.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
