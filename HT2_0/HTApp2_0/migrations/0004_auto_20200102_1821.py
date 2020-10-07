# Generated by Django 3.0.2 on 2020-01-02 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HTApp2_0', '0003_auto_20200102_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='place_comm',
            new_name='place_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text_comm',
        ),
        migrations.RemoveField(
            model_name='place',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='author_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='author_comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_comment',
            field=models.CharField(default=None, max_length=200, verbose_name='text_comment'),
        ),
        migrations.AddField(
            model_name='place',
            name='author_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='author_place'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(db_index=True, default=None, max_length=64, verbose_name='name_category'),
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HTApp2_0.Category', verbose_name='category'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_favorites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HTApp2_0.Place', verbose_name='place_favorites')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_deal', models.CharField(default=None, max_length=200, verbose_name='text_comment')),
                ('place_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HTApp2_0.Place', verbose_name='place_deal')),
                ('user_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_deal')),
            ],
        ),
    ]