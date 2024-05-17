from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField


from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
  


class OrderForm(forms.ModelForm):
    product = ModelChoiceField(queryset=Product.objects.exclude(name__isnull=True))

    class Meta:
        model = Order
        fields = ['product', 'status', 'note', 'branch']  
    # class Meta:
    #     model=Order
    #     fields= '__all__'
    #     exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']