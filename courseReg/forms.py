from django import forms
from core.models import Course, College, Dept, Major
from courseReg.models import CourseToMajor


class CourseToMajorSelectForm(forms.Form):
    college_choices = [
        ('', 'Select'),
    ]
    dept_choices = [
        ('', 'Select'),
    ]
    major_choices = [
        ('', 'Select'),
    ]

    colleges = College.objects.all()
    depts = Dept.objects.all()
    majors = Major.objects.all()

    for coll in colleges:
        college_choices.append((coll.id, coll.name))
    for dept in depts:
        dept_choices.append((dept.id, dept.name))
    for major in majors:
        major_choices.append((major.id, major.name))

    college = forms.ChoiceField(choices=college_choices)
    department = forms.ChoiceField(choices=dept_choices)
    major = forms.ChoiceField(choices=major_choices)
