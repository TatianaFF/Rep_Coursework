from __future__ import unicode_literals

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.views.generic import FormView
from django.views.generic.base import View
from django.urls import reverse_lazy, reverse

from .forms import PlaceForm

from .models import Place, Favorite, Category, Deal
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def detail(request, place_id):
    try:
        pl = Place.objects.get(id=place_id)
    except:
        raise Http404('Место не найдено...')

    comments_list = pl.comment_set.order_by()

    return render(request, 'detail.html', {'pl': pl, 'comments_list': comments_list})

def add_comment(request, place_id):
    try:
         pl = Place.objects.get(id=place_id)
    except:
         raise Http404('Место не найдено...')

    pl.comment_set.create(author_comment=request.user,
                            text_comment=request.POST['text_comment'],
                            place_comment=pl.id)

    return HttpResponseRedirect(reverse('detail', args=(pl.id,)))

def add_favorite(request, place_id):
    pl = Place.objects.get(id=place_id)
    if request.method == 'POST':
        fav = Favorite()
        fav.user_favorite = request.user
        fav.place_favorite = pl
        fav.save()

    return HttpResponseRedirect(reverse('detail', args=(pl.id,)))

def add_deal(request, place_id):
    pl = Place.objects.get(id=place_id)
    if request.method == 'POST':
        deal = Deal()
        deal.name_deal = request.POST['name_deal']
        deal.count_ticket = request.POST['count_ticket']
        deal.privileges_deal = request.POST['privileges_deal']
        deal.place_deal = pl
        deal.user_deal = request.user
        deal.save()

    return HttpResponseRedirect(reverse('detail', args=(pl.id,)))

def account(request):
    deal = Deal.objects.all()
    user_deal = []
    favorites = Favorite.objects.all()
    user_favorites = []
    for f in favorites:
        if f.user_favorite == request.user:
            user_favorites.append(f)
    for d in deal:
        if d.user_deal == request.user:
             user_deal.append(d)
    return render(request, "account.html", {'user_favorites': user_favorites, 'user_deal': user_deal})

def about_us(request):
    return render(request, "about_us.html")

def mainFunc(request):
    place = Place.objects.all()
    category = Category.objects.all()
    return render(request, "main.html", {'place': place, 'category': category})

class CreatePlace(generic.CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'place.html'
    success_url = reverse_lazy('account')

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")