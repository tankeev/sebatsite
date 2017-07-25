from django import forms
from uploads.core.models import News

class NewsForm(form.class MODELNAMEForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','photo')