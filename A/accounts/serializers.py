from rest_framework import serializers



def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('Admin cannot be in email')



class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    #password2 = serializers.CharField(required=True)