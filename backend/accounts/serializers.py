from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ReadOnlyField

from .models import User


class UserSerializer(ModelSerializer):
    get_full_name = ReadOnlyField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'birthday', 'photo', 'phone', 'get_full_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
