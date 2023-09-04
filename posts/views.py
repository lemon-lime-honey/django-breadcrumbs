from rest_framework import status, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    renderer_classes = [JSONRenderer]


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def retrieve(self, request, pk):
        post = self.queryset.get(pk=pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=post)
        data = serializer.data
        data['breadcrumbs'] = ['Post', serializer.data['category'], serializer.data['title']]
        return Response(data=data)