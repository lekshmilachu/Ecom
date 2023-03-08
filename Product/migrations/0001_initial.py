# Generated by Django 4.1.5 on 2023-01-16 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('Product_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=255)),
                ('Product_Brand', models.CharField(max_length=255)),
                ('Product_Description', models.CharField(max_length=1000)),
                ('Product_Price', models.IntegerField()),
                ('Product_Image', models.ImageField(upload_to='product_image')),
                ('Merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
