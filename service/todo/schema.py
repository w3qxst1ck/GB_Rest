import graphene
from graphene_django import DjangoObjectType

from todo.models import Project, User, ToDo


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    todo_by_id = graphene.Field(TodoType, id=graphene.Int(required=True))
    todo_by_project_title = graphene.List(TodoType, title=graphene.String(required=False))

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_todo_by_id(root, info, id):
        try:
            return ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return None

    def resolve_todo_by_project_title(root, info, title=None):
        todos = ToDo.objects.all()
        if title:
            todos.filter(project__title=title)
        return todos


schema = graphene.Schema(query=Query)

