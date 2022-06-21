from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "delivery_date": {"required": True},
            "price_usd": {"required": True},
            "price_rub": {"read_only": True},
        }


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "url",
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password",
#         ]
#         extra_kwargs = {"password": {"write_only": True}}
#
#
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = [
#             "id",
#             "url",
#             "title",
#             "text",
#             "created",
#             "edited",
#             "author",
#             "likes_count",
#             "unlikes_count",
#         ]
#
#
# class PostForAuthorSerializer(serializers.ModelSerializer):
#     likes = UserInfoSerializer(many=True)
#     unlikes = UserInfoSerializer(many=True)
#
#     class Meta:
#         model = Post
#         fields = [
#             "id",
#             "url",
#             "title",
#             "text",
#             "created",
#             "edited",
#             "author",
#             "likes_count",
#             "unlikes_count",
#             "likes",
#             "unlikes",
#         ]
#
#
# class PostCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = [
#             "id",
#             "url",
#             "title",
#             "text",
#         ]
#
#     def create(self, validated_data):
#         user = self.context["request"].user
#         post = Post.objects.create(**validated_data, author=user)
#         return post
