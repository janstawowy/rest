# Generated by Django 2.1.2 on 2018-10-23 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movielist', '0003_populate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtimes.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movielist.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='movies',
            field=models.ManyToManyField(null=True, through='showtimes.Screening', to='movielist.Movie'),
        ),
    ]
