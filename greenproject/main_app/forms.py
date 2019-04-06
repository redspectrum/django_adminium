from django import forms
import re
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')


#
#
# class ClientCustomerIDForm(forms.Form):
#     ID_PATTERN = re.compile(r"\d{3}-\d{3}-\d{4}")
#
#     # client_customer_id = forms.CharField(label="Сlient customer ID", max_length=50)
#     client_customer_id = forms.CharField(label="Сompte Google Ads", max_length=50)
#
#     def clean_client_customer_id(self):
#         client_customer_id = self.cleaned_data["client_customer_id"]
#
#         if self.ID_PATTERN.match(client_customer_id) is None:
#             # raise forms.ValidationError("Not valid value for client customer id.")
#             raise forms.ValidationError("Valeur non valide pour Сompte Google Ads")
#
#         return client_customer_id.replace("-", "")