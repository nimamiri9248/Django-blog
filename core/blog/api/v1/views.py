from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import PostSerializer
from ...models import Post , Category
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView , ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins , viewsets

# Example for Function Based View
"""
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):  
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)    
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""


'''class PostList(APIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostSerializer
    def get(self,request):
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostSerializer
    def get(self,request,pk):
        post=get_object_or_404(Post,id=pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    def put(self,request,pk):
        post=Post.objects.get(id=pk)
        serializer=PostSerializer(instance=post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        post=Post.objects.get(id=pk)
        post.delete()
        return Response("Deleted") '''
    

'''class PostList(ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    # def get(self,request):
    #     serializer=self.serializer_class(self.get_queryset(),many=True)
    #     return Response(serializer.data)
    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    # def get(self,request,pk):
    #     post=get_object_or_404(Post,id=pk)
    #     serializer=self.serializer_class(post)
    #     return Response(serializer.data)
    # def put(self,request,pk):
    #     post=Post.objects.get(id=pk)
    #     serializer=self.serializer_class(instance=post,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def delete(self,request,pk):
    #     post=Post.objects.get(id=pk)
    #     post.delete()
    #     return Response("Deleted") '''

class PostViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    
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
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CategorySerializer
    queryset=Category.objects.all()