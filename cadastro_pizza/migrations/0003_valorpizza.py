# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 16:27
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cadastro_pizza', '0002_auto_20160909_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValorPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho_pizza',
                 models.IntegerField(choices=[(1, 'Broto'), (2, 'Grande')], default=2, verbose_name='tamanho pizza')),
                ('quantia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores',
                                            to='cadastro_pizza.Pizza', verbose_name='pizza')),
            ],
            options={
                'db_table': 'valores_pizza',
                'verbose_name_plural': 'Valores',
                'verbose_name': 'Valor',
            },
        ),
    ]
