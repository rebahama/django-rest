from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    ## displays owner with the source
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Warning image is to big Image must be under 2 mbits'
            )

        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Warning image is to wide Image must be under 4096 pixels'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Warning image is to high Image must be under 4096 pixels'
            )
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = '__all__'
    