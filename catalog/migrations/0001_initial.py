# Generated by Django 3.1.7 on 2021-02-19 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(db_index=True, max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('image_one', models.ImageField(upload_to='images/')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_three', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_four', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_five', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[120, 120], upload_to='')),
                ('img_category', models.CharField(choices=[('thumbnail', 'thumbnail'), ('other', 'other')], default='other', max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.product')),
            ],
            options={
                'db_table': 'product_images',
                'ordering': ['-created_at'],
            },
        ),
    ]
