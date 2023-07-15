# from rest_framework import generics
# from django.forms import model_to_dict
# from rest_framework.decorators import action
#
# from .models import Product
# # from .serialize import
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
# from .serialize import ProductSerializer
#
#
# # class ProductViewSet(viewsets.ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #
# #     @action(methods=['get'], detail=False)
# #     def cader(self, request):
# #         cat = Product.objects.all()
# #         return Response({'car': cat})
#
#
# # TODO: Удобно и понятно использовать если надо делать ограничение доступа
# class ProductApiList(generics.ListAPIView):  # TODO: реализует get and post request
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class ProductApiUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# # CRUD - для примера
# class ProductApiDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# # TODO: Вот что делают классы выше)))
# # class ProductApi(APIView):
# #     def get(self, request):
# #         p = Product.objects.all()
# #         return Response({'products': ProductSerializer(p, many=True).data})
# #
# #     def post(self, request):
# #         serialize = ProductSerializer(data=request.data)
# #         serialize.is_valid(raise_exception=True)
# #         serialize.save()
# #
# #         return Response({'post': serialize.data})
# #
# #     def put(self, request, *args, **kwargs):
# #         pk = kwargs.get("pk", None)
# #         if not pk:
# #             return Response({"error": "Method PUT not allowed"})
# #
# #         try:
# #             instance = Product.objects.get(pk=pk)
# #         except:
# #             return Response({"error": "Object does not exists"})
# #
# #         serializer = ProductSerializer(data=request.data, instance=instance)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response({"post": serializer.data})
# #
# #     def delete(self, request, *args, **kwargs):
# #         pk = kwargs.get("pk", None)
# #         if not pk:
# #             return Response({"error": "Method DELETE not allowed"})
# #
# #         # Здесь код для удаления записи с переданным pk
# #
# #         return Response({"post": "delete post " + str(pk)})
