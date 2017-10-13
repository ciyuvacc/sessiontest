#coding:utf8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from mysite import models,forms

def index(request,pid=None,del_pass=None):
    if 'username' in request.COOKIES and 'usercolor' in request.COOKIES:
        username = request.COOKIES['username']
        usercolor = request.COOKIES['usercolor']
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
     
    html = template.render(request_context)

    return HttpResponse(html)


def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()

    html = template.render(locals())

    return HttpResponse(html)



def posting(request):
    template = get_template('posting.html')
    moods = models.Mood.objects.all()
    message = '如果要张贴信息,那么没一个字段都要填...'



    request_context = RequestContext(request)
    request_context.push(locals())

    html = template.render(request_context)

    return HttpResponse(html)



def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感谢您的来信.'
      
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school  = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']


        else:
            message = '请检查您的输入信息是否正确!'
    else:
        form = forms.ContactForm()
    template = get_template('contact.html')

    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)



def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "你的信息已存储,要等管理员启用后才能看到."
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如果要张贴信息,那么没一个字段都要填...'
    else:
        post_form = forms.PostForm()
        message = '如果要张贴信息,那么没一个字段都要填...'

    template = get_template('post2db.html')

    request_context = RequestContext(request)
    request_context.push(locals())

    html = template.render(request_context)

    return HttpResponse(html)

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['user_name']          
            usercolor = request.POST['user_color']
            message = '登陆成功'
        else:
            message = "请检查字段输入内容"
    else:
        login_form = forms.LoginForm()
    template = get_template('login.html')

    request_context = RequestContext(request)
    request_context.push(locals())    

    html = template.render(request_context)
    response = HttpResponse(html)


    try:
        if username: response.set_cookie('username',username)
        if usercolor: response.set_cookie('usercolor',usercolor)
    except:
        pass
    return response
    
def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response
     

