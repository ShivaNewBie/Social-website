from djoser.serializers import UserSerializer
from djoser.serializers import UserCreateSerializer


from user.models import CustomUser

class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

