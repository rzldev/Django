from cgitb import lookup
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django_app.models import Article
from django_app.serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

'''
Function Based API
'''
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def article_list_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_view(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
Class Based API
'''
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
Generics Views API
'''
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class AuthenticationAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get(self, request, id=None):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ArticleViewSet(viewsets.ViewSet):
    lookup_field = 'id'

    def get_object(self, id):
        queryset = Article.objects.all()
        return get_object_or_404(queryset, id=id)

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, id=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ArticleGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin, mixins.UpdateModelMixin):
    lookup_field = 'id'
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()