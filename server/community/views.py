from django.contrib.auth import get_user_model
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.fields import REGEX_TYPE
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from accounts.models import User
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)

        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete' : f'리뷰가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)