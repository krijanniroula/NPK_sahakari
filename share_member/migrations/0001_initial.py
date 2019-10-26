# Generated by Django 2.2.6 on 2019-10-26 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import share_member.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provision', models.CharField(default='Provision 1', max_length=100)),
                ('district', models.CharField(default='Jhapa', max_length=50)),
                ('municipality', models.CharField(default='Gauradaha', max_length=50)),
                ('ward', models.IntegerField(default=1)),
                ('village', models.CharField(default='Gurung Chowk', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShareMember',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('age', models.IntegerField()),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('grand_father_name', models.CharField(max_length=255)),
                ('id', models.IntegerField(default=share_member.models.ids, editable=False, unique=True)),
                ('share_no', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('alternative_person', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('isActive', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share_member.Address')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'share_member',
            },
        ),
    ]
