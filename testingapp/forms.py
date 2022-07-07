from django import  forms

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            "title",
            "text",
            "image"
        )
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "text": forms.Textarea(attrs={"class":"form-control"}),
            "image": forms.FileInput(attrs={"class":"form-control"}),

        }