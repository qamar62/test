from django import forms
      
from .models import Blog, Category

choices = Category.objects.all().values_list('name','name')


choice_list = []
for item in choices:
    choice_list.append(item)


class BlogFrom(forms.ModelForm):
    class Meta:
        model =  Blog
        fields = ('title', 'title_tag', 'author', 'category', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),

        }
