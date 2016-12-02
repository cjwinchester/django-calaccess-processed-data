# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0007_auto_20161202_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form460scheduleb2itemold',
            name='repayment_type',
            field=models.CharField(choices=[('B2F', 'Forgiven'), ('B2R', 'Repay'), ('B2T', 'Third party payment')], help_text='Indicates whether the item is a loan repayment by the campaign filer, a repayment by a third-party or a loan forgiveness by the lender (from LOAN_CD.LOAN_TYPE)', max_length=3, verbose_name='repayment type'),
        ),
        migrations.AlterField(
            model_name='form460scheduleb2itemversionold',
            name='repayment_type',
            field=models.CharField(choices=[('B2F', 'Forgiven'), ('B2R', 'Repay'), ('B2T', 'Third party payment')], help_text='Indicates whether the item is a loan repayment by the campaign filer, a repayment by a third-party or a loan forgiveness by the lender (from LOAN_CD.LOAN_TYPE)', max_length=3, verbose_name='repayment type'),
        ),
    ]
