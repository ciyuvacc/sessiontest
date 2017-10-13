#coding:utf8
from django import forms
from django.forms import fields
from mysite import models
from captcha.fields import CaptchaField

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


class LoginForm1(forms.Form):
    COLORS = [
        ['红','红'],
        ['黄','黄'],
        ['绿','绿'],
        ['紫','紫'],
        ['蓝','蓝'],
    ]
    user_name = forms.CharField(label='您的名字',max_length=50,initial='李达')
    user_color = forms.ChoiceField(label='幸运色',choices=COLORS)




class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())






#class PostForm(forms.ModelForm):
#    captcha = CaptchaField()
#    class Meta:
#        model = models.Post
#        fields = ['mood','nickname','message','del_pass']
#    
#
#    def _init_(self,*args,**kwargs):
#        super(PostForm,self),_init_(*args,**kwargs)
#        self.fields['mood'].label = "现在的心情"
#        self.fields['nickname'].label = "您的昵称"
#        self.fields['message'].label = "心情留言"
#        self.fields['del_pass'].label = "设置密码"
#        self.fields['captcha'].label = "确定您不是机器人"
#
