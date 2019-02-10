# Generated by Django 2.1.5 on 2019-02-10 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBookApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('genericcollection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AddressBookApp.GenericCollection')),
            ],
            bases=('AddressBookApp.genericcollection',),
        ),
        migrations.AddField(
            model_name='addressbook',
            name='member_of_library',
            field=models.ManyToManyField(to='AddressBookApp.Library'),
        ),
    ]