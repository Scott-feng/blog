from django.forms import ModelForm,Textarea,TextInput
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        #form display
        fields=['name','text']
        widgets={
            'name':TextInput(attrs={'class':'form-control','placeholder':'Type your username here...'}),
            'text':Textarea(attrs={'class':'form-control','placeholder':'Type your comment here...'}),
        }
