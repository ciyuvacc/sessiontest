#coding:utf8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from mysite import models,forms
from django.contrib import messages
#messages.add_message(request,message.INFO,'heheheheh')
#messages.get_messages(request)


def index(request,pid=None,del_pass=None):
    if 'username' in request.session:
        username = request.session['username']
        useremail = request.session['useremail']

    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)


def userinfo(request):
    if 'username' in request.session:
        username = request.session['username']
    else:
        return HttpResponseRedirect('/login/')

    try:
        userinfo = models.User.objects.get(name=username)
    except:
        pass

    template = get_template('userinfo.html')
    html = template.render(locals())
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
            login_name = request.POST['username'].strip()          
            login_password = request.POST['password']
            print login_name,login_password
            try:
                user = models.User.objects.get(name=login_name)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    messages.add_message(request,messages.SUCCESS,'成功登录了')
                    return  HttpResponseRedirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'密码错误,请检查一次')
                    #message = '密码错误,请检查一次!'
            except:
                 messages.add_message(request,messages.WARNING,'找不到用户')
                # message = '目前无法登陆'
        else:
            messages.add_message(request,messages.INFO,'请检查字段输入内容')
           # message = "请检查字段输入内容"
    else:
        login_form = forms.LoginForm()

    template = get_template('login.html')
    request_context = RequestContext(request)
    request_context.push(locals())    

    html = template.render(request_context)
    response = HttpResponse(html)
    return response
    
def logout(request):
    request.session['username']= ""
    response = HttpResponseRedirect('/')
    return response
     

