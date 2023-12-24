from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import random
def homepage(request):
    id_list = models.info_list.objects.values_list('id', flat=True)
    random_id = random.choice(id_list)
    query = models.info_list.objects.filter(id=random_id).all()
    queryset = models.info_list.objects.all()
    return render(request,'homepage.html',{'queryset': queryset, 'query': query})

from django import forms
class infolistModelForm(forms.ModelForm):
    class Meta:
        model = models.info_list
        fields = ['name', 'describe', 'money', 'inventory']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
def homepageadd(request):
    if request.method == 'GET':
        form = infolistModelForm()
        return render(request, 'homepageadd.html', {'form': form})
    form = infolistModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/homepage/')
    return render(request, 'homepageadd.html', {'form': form})
def homepagedelete(request):
    nid = request.GET.get('nid')
    models.info_list.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/homepage/')
def detailsdelete(request):
    nid = request.GET.get('nid')
    models.info_list.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/details/')

def details(request, nid):
    queryset = models.info_list.objects.filter(id=nid).all()
    return render(request,'details.html', {'queryset': queryset})

def boy(request):
    id_list = models.info_list.objects.values_list('id', flat=True)
    random_id = random.choice(id_list)
    query = models.info_list.objects.filter(id=random_id).all()
    set = models.info_list.objects.all()
    queryset = models.info_list.objects.filter(gender=1)
    return render(request, 'boy.html', {'queryset': queryset, 'set': set, 'query': query})
def boydetails(request, nid):
    queryset = models.info_list.objects.filter(gender=1, id=nid)
    return render(request, 'boydetails.html', {'queryset': queryset})

def girl(request):
    id_list = models.info_list.objects.values_list('id', flat=True)
    random_id = random.choice(id_list)
    query = models.info_list.objects.filter(id=random_id).all()
    set = models.info_list.objects.all()
    queryset = models.info_list.objects.filter(gender=2)
    return render(request, 'girl.html', {'queryset': queryset, 'set': set, 'query': query})
def girldetails(request, nid):
    queryset = models.info_list.objects.filter(gender=2, id=nid)
    return render(request, 'girldetails.html', {'queryset': queryset})
def randoms(request):
    id_list = models.info_list.objects.values_list('id', flat=True)
    random_id = random.choice(id_list)
    queryset = models.info_list.objects.filter(id=random_id).all()
    return render(request, 'random.html', {'queryset': queryset})
class loginform(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True, attrs={'class': "form-control"}),
        required=True
    )
#在这里的info是session，可以获得用户的信息
def login(request):
    if request.method == 'GET':
        form = loginform()
        return render(request, 'login.html', {'form': form})
    form = loginform(data=request.POST)
    if form.is_valid():
        admin_object = models.admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect('http://127.0.0.1:8000/homepage/')
    return render(request, 'login.html', {'form': form})

def logout(request):
    request.session.clear()
    return redirect('http://127.0.0.1:8000/login/')
class commentModelForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['text', 'user_id']

def comment(request, nid):
    if request.method == 'GET':
        query = models.comment.objects.filter(user_id=nid).all()
        queryset = models.info_list.objects.filter(id=nid).all()
        return render(request, 'details.html', {'query': query, 'queryset': queryset})
    form = commentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        query = models.comment.objects.filter(user_id=nid).all()
        queryset = models.info_list.objects.filter(id=nid).all()
        return render(request, 'details.html', {'query': query, 'queryset': queryset})
class boycommentModelForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['text', 'user_id']
def boycomment(request, nid):
    if request.method == 'GET':
        query = models.comment.objects.filter(user_id=nid).all()
        queryset = models.info_list.objects.filter(id=nid).all()
        return render(request, 'boydetails.html', {'query': query, 'queryset': queryset})
    form = boycommentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        query = models.comment.objects.filter(user_id=nid).all()
        queryset = models.info_list.objects.filter(id=nid).all()
        return render(request, 'boydetails.html', {'query': query, 'queryset': queryset})
class girlcommentModelForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['text', 'user_id']
def girlcomment(request, nid):
      if request.method == 'GET':
          query = models.comment.objects.filter(user_id=nid).all()
          queryset = models.info_list.objects.filter(id=nid).all()
          return render(request, 'girldetails.html', {'query': query, 'queryset': queryset})
      form = girlcommentModelForm(data=request.POST)
      if form.is_valid():
          form.save()
          query = models.comment.objects.filter(user_id=nid).all()
          queryset = models.info_list.objects.filter(id=nid).all()
          return render(request, 'girldetails.html', {'query': query, 'queryset': queryset})
class randomcommentModelForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['text', 'user_id']
def randomcomment(request, nid):
      if request.method == 'GET':
          id_list = models.info_list.objects.values_list('id', flat=True)
          random_id = random.choice(id_list)
          querys = models.info_list.objects.filter(id=random_id).all()
          query = models.comment.objects.filter(user_id=nid).all()
          queryset = models.info_list.objects.filter(id=nid).all()
          return render(request, 'random.html', {'query': query, 'queryset': queryset, 'querys': querys})
      form = randomcommentModelForm(data=request.POST)
      if form.is_valid():
          form.save()
          id_list = models.info_list.objects.values_list('id', flat=True)
          random_id = random.choice(id_list)
          querys = models.info_list.objects.filter(id=random_id).all()
          query = models.comment.objects.filter(user_id=nid).all()
          queryset = models.info_list.objects.filter(id=nid).all()
          return render(request, 'random.html', {'query': query, 'queryset': queryset, 'querys': querys})
def profile(request):
    if request.method == 'GET':
      return render(request, 'profile.html')

def record(request):
    pass
def commentdelete(request):
    nid = request.GET.get('nid')
    models.comment.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/homepage/')
def boydelete(request):
    nid = request.GET.get('nid')
    models.comment.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/homepage/')
def girldelete(request):
    nid = request.GET.get('nid')
    models.comment.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/homepage/')
def randomdelete(request, nid):
    nid = request.GET.get('nid')
    models.comment.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/homepage/')
def user_history(request):
    url = request.build_absolute_uri()
    title = '页面标题'
    history = request.session.get('history', [])
    history.insert(0, {'title': title, 'url': url})
    history = history[:10]
    request.session['history'] = history
    is_login = request.user.is_authenticated
    context = {'history': history, 'is_login': is_login}
    return render(request, 'user_history.html', context)
class registerform(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=True
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True, attrs={'class': "form-control"}),
        required=True
    )
def register(request):
    if request.method == 'GET':
        form = registerform()
        return render(request, 'register.html', {'form': form})
    form = registerform(data=request.POST)
    if form.is_valid():
        admin_object = models.admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect('http://127.0.0.1:8000/login/')
    return render(request, 'login.html', {'form': form})

def upload_list(request):
    if request.method == 'GET':
      return render(request, 'upload_list.html')
    file_object = request.FILES.get('avatar')
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse('...')