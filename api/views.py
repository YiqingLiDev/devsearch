from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializers
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializers(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializers(projects, many=False)

    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    # user = request.user.profile
    data = request.data
    print(data)

    serializer = ProjectSerializers(project, many=False)
    return Response(serializer,data)
