#coding:utf8
from django import forms
from django.forms import fields
from mysite import models


class ContactForm(forms.Form):
    CITY = [
        ['TP','Taipei'],
        ['TY','Taoyuang'],
        ['TC','Taichung'],
        ['TN','Tainan'],
        ['KS','Kaohsiung'],
        ['NA','Others'],
    ]
    user_name = forms.CharField(label='您的名字',max_length=50,initial='李达')
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_school = forms.BooleanField(label='是否在学',required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='您的意见',widget=forms.Textarea)









class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())




class DateInput(forms.DateInput):
    input_type = 'date'


class DiaryForm(forms.ModelForm):

    class Meta:
        model = models.Diary
        fields = ['budget','weight','note','ddate']
        widgets = { 
            'ddate': DateInput(), 
        }
    def _init_(self,*args,**kwargs):
        super(DiaryForm,self),_init_(*args,**kwargs)
        self.fields['budget'].label = "今日花费"
        self.fields['weight'].label = "今日体重"
        self.fields['note'].label = "心情留言"
        self.fields['ddate'].label = "日期"

