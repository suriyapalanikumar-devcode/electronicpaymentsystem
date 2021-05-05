# Generated by Django 3.1.7 on 2021-04-17 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txnRefNo', models.PositiveBigIntegerField()),
                ('txnType', models.CharField(choices=[('DR', 'Debit'), ('CR', 'Credit'), ('CH', 'Check'), ('FE', 'Fees'), ('RF', 'Refund')], default='DR', max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('txnDesc', models.CharField(max_length=255)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account')),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
