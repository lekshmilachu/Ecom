# Generated by Django 4.1.5 on 2023-01-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='Product_Category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdetails',
            name='Product_Stock',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]