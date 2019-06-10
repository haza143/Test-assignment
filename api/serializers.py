from rest_framework import serializers
from .models import User, Post
from . import services

class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'is_fan',
        )
    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        print(self.context.get('request').user)
        user = self.context.get('request').user
        return services.is_fan(obj, user)


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
