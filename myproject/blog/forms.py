# 데이터를 입력할 수 있는 양식
from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        # 모두 다 가져 온 것
