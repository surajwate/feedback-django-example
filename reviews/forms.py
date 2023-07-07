from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="User Name", max_length=25, error_messages={})