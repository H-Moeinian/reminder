# Generated by Django 3.2.5 on 2021-07-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('priority', models.CharField(choices=[('1', 'not important'), ('2', 'important'), ('3', 'very important'), ('4', 'necessary')], default='2', max_length=1)),
                ('set_to_time', models.DateTimeField()),
                ('category', models.ManyToManyField(related_name='tasks', to='todo.Category')),
            ],
        ),
    ]
