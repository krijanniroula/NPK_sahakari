# Generated by Django 2.2.6 on 2019-11-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanaccount',
            name='amount_received',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
        migrations.AlterField(
            model_name='loanpayment',
            name='paid',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
        migrations.AlterField(
            model_name='loanpaymenthistory',
            name='interest',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
        migrations.AlterField(
            model_name='loanpaymenthistory',
            name='paid',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
        migrations.AlterField(
            model_name='loanpaymenthistory',
            name='principle',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
        migrations.AlterField(
            model_name='loanpaymenthistory',
            name='remaining',
            field=models.DecimalField(decimal_places=15, max_digits=30),
        ),
    ]
