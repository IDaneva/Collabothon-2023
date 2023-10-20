# Generated by Django 4.2.6 on 2023-10-20 17:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Family', 'Family')], max_length=20)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('personal_number', models.CharField(default='0000000000', max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('affected_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.account')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customer')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='holder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to='base.customer'),
        ),
    ]
