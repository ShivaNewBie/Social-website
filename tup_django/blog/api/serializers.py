from rest_framework import serializers

from blog.models import Blog

from user.serializers import UserCreateSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    author_detail = UserCreateSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('author_detail','title','description','image','created_at','author','slug','name',)
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')