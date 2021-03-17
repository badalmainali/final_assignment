# Generated by Django 3.1.6 on 2021-03-02 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_person_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]