from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View,CreateView,FormView,ListView,DetailView,UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login


from myapp.forms import SignUpForm,SignInForm,BooksForm
from myapp.models import BookStore

class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name="register.html"
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request,"Account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to create account")
        return super().form_invalid(form)
    
class SignInView(FormView):
    model=User
    form_class=SignInForm
    template_name="login.html"
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            print('hello')
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("book-list")
            messages.error(request,"login failed")
        return render(request,self.template_name,{"form":form})

class BookListView(ListView):
    model=BookStore
    template_name="book-list.html"
    context_object_name="books"

class AddBooksView(CreateView):
    model=BookStore
    template_name="book-add.html"
    form_class=BooksForm
    success_url=reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Book Added")
        return super().form_valid(form)
    
class BookDetailView(DetailView):
    model=BookStore
    context_object_name="book"
    template_name="book-detail.html"

class BookEditView(UpdateView):
    model=BookStore
    form_class=BooksForm
    template_name="book-edit.html"
    success_url=reverse_lazy('book-list')

class BookDeleteView(View):
    model=BookStore
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        BookStore.objects.get(id=id).delete()
        return redirect('book-list')
    
class IndexView(TemplateView):
    template_name="index.html"




