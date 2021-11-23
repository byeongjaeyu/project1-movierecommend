from django.db.models.query import QuerySet
from accounts.models import User
from rest_framework import serializers
from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
<<<<<<< Updated upstream
    

    # comments = serializers.RelatedField(many=True, read_only=True)
=======
    # class CommentSerializer(serializers.ModelSerializer):
    
    #     class Meta:
    #         model = Comment
    #         fields = ('__all__')
    #         read_only_fileds = ('review',)

    comments = serializers.StringRelatedField(many=True, read_only=True)
>>>>>>> Stashed changes

    class Meta:
        model = Review
        fields = ('title','movie_title','content','rank','comments',)
        # read_only_fields = ('comment',)

class ReviewListSerializer(serializers.ModelSerializer):
    
    def getUsername(self, obj):
        return obj.user.username
        
    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        model = Review
        fields = ('id', 'title', 'movie_title', 'created_at', 'user', 'username',)

class CommentSerializer(serializers.ModelSerializer):
    
    def getUsername(self, obj):
        return obj.user.username
        
    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fileds = ('review',)
