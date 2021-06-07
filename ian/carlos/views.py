from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

"""

def results(request, question_id):
    list_of_student = Student.objects.all
    context = {'latest_question_list': list_of_student}
    return render(request, 'carlos/index.html', context)
"""


class studentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
