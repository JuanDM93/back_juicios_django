# Generated by Django 3.1 on 2020-08-17 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('tipo', models.CharField(max_length=10)),
                ('asignados', models.TextField()),
                ('abogados', models.ManyToManyField(to='accounts.Abogado')),
            ],
        ),
        migrations.CreateModel(
            name='Juzgado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='JuicioFederal',
            fields=[
                ('juicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.juicio')),
                ('extraFederal', models.TextField()),
            ],
            bases=('services.juicio',),
        ),
        migrations.CreateModel(
            name='JuicioLocal',
            fields=[
                ('juicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.juicio')),
                ('extraLocal', models.TextField()),
            ],
            bases=('services.juicio',),
        ),
        migrations.AddField(
            model_name='juicio',
            name='juzgado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juicios', to='services.juzgado'),
        ),
        migrations.CreateModel(
            name='Acuerdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('contenido', models.TextField()),
                ('juicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acuerdos', to='services.juicio')),
            ],
        ),
    ]
