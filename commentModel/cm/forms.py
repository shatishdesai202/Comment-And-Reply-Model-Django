from django import forms
from .models import Comment

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (('content'),)
        widgets={
                   "content":forms.Textarea(attrs={'placeholder':'Name','name':'Name','id':'common_id_for_imputfields','class':'form-control',
                   'rows':3})
                }  
