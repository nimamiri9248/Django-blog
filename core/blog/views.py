from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def list(self,request):
    #     queryset=self.get_queryset()
    #     serializer=self.serializer_class(queryset,many=True)
    #     return Response(serializer.data)

    # def create(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def retrieve(self,request,pk=None):
    #     post=get_object_or_404(Post,id=pk)
    #     serializer=self.serializer_class(post)
    #     return Response(serializer.data)

    # def update(self,request,pk=None):
    #     post=Post.objects.get(id=pk)
    #     serializer=self.serializer_class(instance=post,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def destroy(self,request,pk=None):
    #     post=Post.objects.get(id=pk)
    #     post.delete()
    #     return Response("Deleted")

    # def partial_update(self,request,pk=None):
    #     post=Post.objects.get(id=pk)
    #     serializer=self.serializer_class(instance=post,data=request.data,partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
