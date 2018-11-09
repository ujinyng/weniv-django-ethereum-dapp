from django.shortcuts import render
from .models import Lecture

def lecture(request):
	lecturelist = Lecture.objects.all()
	return render(request, 'lecture/lecture.html', {'lecturelist':lecturelist})

def lecturedetails(request, pk):
	lecturelist = Lecture.objects.get(pk=pk)
	return render(request, 'lecture/lectureDetail.html', {'lecturelist':lecturelist})