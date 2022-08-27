from rest_framework import serializers
from comments.models import Comment



class CommentSerializer(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.username')
        is_owner = serializers.SerializerMethodField()
        profile_id = serializers.ReadOnlyField(source='owner.profile.id')
        profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
        


        class Meta:
            model = Comment
            fields = '__all__'

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
