
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from blog.models import Blog

from blog.api.serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self,serializer): #when we post data in api. logged in user will be saved as user
        serializer.save(author=self.request.user)