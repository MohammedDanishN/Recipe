from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import *

# Create your views here.


def student(request):

    student_obj = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        student_obj = Student.objects.filter(
            Q(name__icontains=search) |
            Q(dept_name__department__icontains=search) |
            Q(srn__srn__icontains=search)
        )

    paginator = Paginator(student_obj, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {'students': page_obj}
    return render(request, 'student/student.html', context)


def marks(request, id):
    student_obj = SubjectMarks.objects.filter(student__srn__srn=id)
    total = student_obj.aggregate(total=Sum('marks'))
    # rank
    context = {'students': student_obj, 'total': total}
    return render(request, 'student/marks.html', context)
