from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import Post
from main.serializers import (
    PostSerializer,
    PostForAuthorSerializer,
    PostCreateUpdateSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created, viewed or edited.
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Administrators get the full list of users, and everyone else gets only themselves"""

        queryset = User.objects.order_by("-date_joined")
        user = self.request.user
        if user.is_staff:
            return queryset.all()
        else:
            return queryset.filter(id=user.id)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["list", "retrieve", "update", "partial_update"]:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == "create":
            permission_classes = [permissions.AllowAny]
        elif self.action == "destroy":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]


class IsOwnerOrStaffOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Object-level permission to allow staff or owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # We allow like and unlike from any authenticated Users
        if request.user.is_authenticated and view.action in ["like", "unlike"]:
            return True

        # Only author and staff can edit posts
        return request.user.is_staff or obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created")
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filterset_fields = ["author"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action in ["retrieve"]:
            user = self.request.user
            pk = self.kwargs.get("pk")
            if user.is_authenticated and (
                user.is_staff or Post.objects.filter(pk=pk, author=user).exists()
            ):
                serializer_class = PostForAuthorSerializer
        elif self.action in ["create", "update", "partial_update"]:
            serializer_class = PostCreateUpdateSerializer

        return serializer_class

    @action(detail=True, methods=["patch"])
    def like(self, request, pk=None):
        user = self.request.user
        post = self.get_object()
        if user.is_authenticated and user != post.author:
            post.likes.add(user)
            post.unlikes.remove(user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def unlike(self, request, pk=None):
        user = self.request.user
        post = self.get_object()
        if user.is_authenticated and user != post.author:
            post.unlikes.add(user)
            post.likes.remove(user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)
