from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name_category = models.CharField(verbose_name='name_category', db_index=True, max_length=64, default=None)

    def __str__(self):
        return self.name_category


class Place(models.Model):
    name_place = models.CharField(verbose_name='name_place', db_index=True, max_length=64, default=None)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    description_place = models.CharField(verbose_name='description_place', db_index=True, max_length=2048, default=None)
    cost_place = models.FloatField(verbose_name='cost_place', db_index=True, max_length=64, default=None)
    address_place = models.CharField(verbose_name='address_place', db_index=True, max_length=1024, default=None)
    pictures_place = models.ImageField(verbose_name='pictures_place', db_index=True, default=None, upload_to='images/')

    def __str__(self):
        return self.name_place


class Comment(models.Model):
    place_comment = models.ForeignKey(Place, verbose_name='category_comment', on_delete=models.CASCADE, default=None)
    author_comment = models.ForeignKey(User, verbose_name='author_place', on_delete=models.SET_NULL, null=True)
    text_comment = models.CharField(verbose_name='text_comment', max_length=200, default=None)

    def __str__(self):
        return self.text_comment


class Deal(models.Model):
    name_deal = models.CharField(verbose_name='name_deal', max_length=200, default=None)
    place_deal = models.ForeignKey(Place, verbose_name='place_deal', on_delete=models.CASCADE)
    user_deal = models.ForeignKey(User, verbose_name='user_deal', on_delete=models.CASCADE)
    privileges_deal = models.BooleanField(verbose_name='privileges_deal', default=0)
    count_ticket = models.IntegerField(verbose_name='count_ticket', default=1)

    def result(self):
        discount = 0.2
        if self.privileges_deal == 0:
            return self.place_deal.cost_place * self.count_ticket
        else:
            if self.privileges_deal == 1:
                return str(self.place_deal.cost_place * self.count_ticket * (1 - discount))

        def __str__(self):
            return str(self.result())


class Favorite(models.Model):
    place_favorite = models.ForeignKey(Place, verbose_name='place_favorites', on_delete=models.CASCADE)
    user_favorite = models.ForeignKey(User, verbose_name='user_favorite', on_delete=models.CASCADE)

    def __str__(self):
        return self.place_favorite.name_place

