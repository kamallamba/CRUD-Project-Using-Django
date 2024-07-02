from django import forms
from.models import StudentsInfo


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentsInfo
        fields=['Name','Roll_NO','Email']
