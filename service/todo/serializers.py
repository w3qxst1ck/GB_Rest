from rest_framework import serializers

from todo.models import Project, ToDo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)
    # users = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('title', 'users', 'repository')


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserModelSerializer()
    user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    # project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = ('id', 'project', 'user', 'text', 'created', 'updated', 'is_active')
