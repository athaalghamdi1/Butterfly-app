# main_app/views.py

from django.shortcuts import render, redirect
from .models import butterfly, Toy, Photo
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import models
from django.urls import reverse
from .forms import FeedingForm, PhotoForm
from django.contrib.auth.views import LoginView

# def home(request):
#     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def butterflies_index(request):
    butterflies = butterfly.objects.filter(user=request.user)
    return render(request, 'butterflies/index.html', {'butterflies': butterflies})

def butterflies_detail(request, butterflies_id):
    butterflies = butterfly.objects.get(id=butterflies_id)
    toys = Toy.objects.all() 
    toys_butterfly_doesnt_have = Toy.objects.exclude(id__in = butterflies.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    photo_form = PhotoForm()
    return render(request, 'butterflies/detail.html', {
        'butterflies': butterflies,
        'feeding_form': feeding_form,
        'photo_form': photo_form,
        'toys': toys,
        'toys_butterfly_doesnt_have': toys_butterfly_doesnt_have
    })   
def add_feeding(request, butterflies_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.butterflies_id = butterflies_id
        new_feeding.save()
    return redirect('butterflies-detail', butterflies_id=butterflies_id)      
        
    

class butterflyList(ListView):
    model = butterfly
    template_name = 'main_app/butterfly_list.html'
    
class butterflyCreate(CreateView):
    model = butterfly
    fields = ['name', 'species', 'description', 'wingspan']
    success_url = '/butterflies/'
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
    
class butterfliesUpdate(UpdateView):
    model = butterfly
    fields = ['species', 'description', 'wingspan']
    toys = Toy.objects.all()

class butterfliesDelete(DeleteView):
    model = butterfly
    success_url = '/butterflies/'
    
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    def get_success_url(self):
        return reverse('toy-detail', kwargs={'pk': self.object.pk})

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
    
    def get_success_url(self):
       return reverse('toy-detail', kwargs={'pk': self.object.pk})

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def associate_toy(request, butterfly_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    butterfly.objects.get(id=butterfly_id).toys.add(toy_id)
    return redirect('butterflies-detail', {"butterfly_id":butterfly_id, "toy_id": toy_id})

def remove_toy(request, butterflies_id, toy_id):
    butterfly.objects.get(id=butterflies_id).toys.remove(toy_id)
    return redirect('butterflies-detail', {"butterfly_id":butterflies_id, "toy_id": toy_id})


def add_photo(request, butterfly_id):
    form = PhotoForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_photo = form.save(commit=False)
        new_photo.butterfly_id = butterfly_id
        # Remove old photo if it exists
        butterfly_photo = Photo.objects.filter(butterfly_id=butterfly_id)
        if butterfly_photo.first():
            butterfly_photo.first().delete()
        new_photo.save()
    return redirect('butterflies-detail', butterfly_id=butterfly_id)

class Home(LoginView):
    template_name = 'home.html'
    
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('butterflies-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
        
class ButterflyCreate(LoginRequiredMixin, CreateView):
    # CatCreate class code here
    model = butterfly