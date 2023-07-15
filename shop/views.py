from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsAdminOrReadOnly
from .serialize import ProductSerializer
from .models import Product, Category


# TODO: Удобно и понятно использовать если надо делать ограничение доступа
class ProductApiList(generics.ListCreateAPIView):  # TODO: реализует get and post request
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAuthenticated,)


class ProductApiUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )  # Указываем конкретно на, что вешаем аутентификацию


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryApiList(generics.ListCreateAPIView):  # TODO: реализует get and post request
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryApiUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


# TODO: Вот что делают классы выше неявно)))
# class ProductApi(APIView):
#     def get(self, request):
#         p = Product.objects.all()
#         return Response({'products': ProductSerializer(p, many=True).data})
#
#     def post(self, request):
#         serialize = ProductSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#
#         return Response({'post': serialize.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Product.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = ProductSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         # Здесь код для удаления записи с переданным pk
#
#         return Response({"post": "delete post " + str(pk)})
