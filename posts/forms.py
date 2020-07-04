from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title','overview', 'content','thumbnail',
                 'categories','featured')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type Your message Here'
    }),label="")
    class Meta():
        model = Comment
        fields= ('content',)