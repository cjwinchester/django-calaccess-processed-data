# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form460ScheduleHItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_item', models.IntegerField(help_text='Line number of the filing form where the loan is itemized (from LOAN_CD.LINE_ITEM)', verbose_name='line item')),
                ('lender_code', models.CharField(blank=True, choices=[('COM', 'Committee'), ('IND', 'Individual'), ('OTH', 'Other'), ('PTY', 'Political Party'), ('RCP', 'Recipient committee'), ('SCC', 'Small Contributor Committee'), ('???', 'Unknown value')], help_text='Code describing the lender (from LOAN_CD.ENTITY_CD)', max_length=3, verbose_name='lender code')),
                ('lender_committee_id', models.CharField(blank=True, help_text="lender's filer identification number, if it is a committee (from LOAN_CD.CMTE_ID)", max_length=9, verbose_name='lender committee id')),
                ('lender_title', models.CharField(blank=True, help_text='Name title of the lender (from LOAN_CD.LNDR_NAMT)', max_length=10, verbose_name='lender title')),
                ('lender_lastname', models.CharField(blank=True, help_text='Last name of the lender or business name (from LOAN_CD.LNDR_NAML)', max_length=200, verbose_name='lender lastname')),
                ('lender_firstname', models.CharField(blank=True, help_text='First name of the lender (from LOAN_CD.LNDR_NAMF)', max_length=45, verbose_name='lender firstname')),
                ('lender_name_suffix', models.CharField(blank=True, help_text='Name suffix of the lender (from LOAN_CD.LNDR_NAMS)', max_length=10, verbose_name='lender name suffix')),
                ('lender_city', models.CharField(blank=True, help_text='City of the lender (from LOAN_CD.LOAN_CITY)', max_length=30, verbose_name='lender city')),
                ('lender_state', models.CharField(blank=True, help_text='State of the lender (from LOAN_CD.LOAN_ST)', max_length=2, verbose_name='lender state')),
                ('lender_zip', models.CharField(blank=True, help_text='Zip code (usually zip5, sometimes zip9) of the lender (from LOAN_CD.LOAN_ZIP4)', max_length=10, verbose_name='lender zip')),
                ('lender_employer', models.CharField(blank=True, help_text='Employer of the lender (from LOAN_CD.LOAN_EMP)', max_length=200, verbose_name='lender employer')),
                ('lender_occupation', models.CharField(blank=True, help_text='Occupation of the lender (from LOAN_CD.LOAN_OCC)', max_length=60, verbose_name='lender occupation')),
                ('lender_is_self_employed', models.BooleanField(default=False, help_text='Indicates whether or not the lender is self-employed(from LOAN_CD.LOAN_SELF)', verbose_name='lender is self employed')),
                ('treasurer_title', models.CharField(blank=True, help_text="Name title of the lender committee's treasurer (from LOAN_CD.TRES_NAMT)", max_length=10, verbose_name='treasurer title')),
                ('treasurer_lastname', models.CharField(blank=True, help_text="Last name of the lender committee's treasurer (from LOAN_CD.TRES_NAML)", max_length=200, verbose_name='treasurer lastname')),
                ('treasurer_firstname', models.CharField(help_text="First name of the lender committee's treasurer (from LOAN_CD.TRES_NAMF)", max_length=45, verbose_name='treasurer firstname')),
                ('treasurer_name_suffix', models.CharField(blank=True, help_text="Name suffix of the lender committee's treasurer (from LOAN_CD.TRES_NAMS)", max_length=10, verbose_name='treasurer name suffix')),
                ('treasurer_city', models.CharField(blank=True, help_text="City of the lender committee's treasurer (from LOAN_CD.TRES_CITY)", max_length=30, verbose_name='treasurer city')),
                ('treasurer_state', models.CharField(blank=True, help_text="State of the lender committee's treasurer (from LOAN_CD.TRES_ST)", max_length=2, verbose_name='treasurer state')),
                ('treasurer_zip', models.CharField(blank=True, help_text="Zip code (usually zip5, sometimes zip9) of the lender committee's treasurer (from LOAN_CD.TRES_ZIP4)", max_length=10, verbose_name='treasurer zip')),
                ('intermediary_title', models.CharField(blank=True, help_text='Name title of the intermediary (from LOAN_CD.INTR_NAMT)', max_length=10, verbose_name='intermediary title')),
                ('intermediary_lastname', models.CharField(blank=True, help_text='Last name of the intermediary or business name (from LOAN_CD.INTR_NAML)', max_length=200, verbose_name='intermediary lastname')),
                ('intermediary_firstname', models.CharField(help_text='First name of the intermediary (from LOAN_CD.INTR_NAMF)', max_length=45, verbose_name='intermediary firstname')),
                ('intermediary_name_suffix', models.CharField(blank=True, help_text='Name suffix of the intermediary (from LOAN_CD.INTR_NAMS)', max_length=10, verbose_name='intermediary name suffix')),
                ('intermediary_city', models.CharField(blank=True, help_text='City of the intermediary (from LOAN_CD.INTR_CITY)', max_length=30, verbose_name='intermediary city')),
                ('intermediary_state', models.CharField(blank=True, help_text='State of the intermediary (from LOAN_CD.INTR_ST)', max_length=2, verbose_name='intermediary state')),
                ('intermediary_zip', models.CharField(blank=True, help_text='Zip code (usually zip5, sometimes zip9) of the intermediary (from LOAN_CD.INTR_ZIP4)', max_length=10, verbose_name='intermediary zip')),
                ('transaction_id', models.CharField(help_text='Identifies a unique transaction across versions of the a given Form 460 filing (from LOAN_CD.TRAN_ID)', max_length=20, verbose_name='transaction id')),
                ('memo_reference_number', models.CharField(blank=True, help_text="A value assigned by the filer which refers to the item'sfootnote in the TEXT_MEMO_CD table (from LOAN_CD.MEMO_REFNO)", max_length=20, verbose_name='memo reference number')),
                ('begin_period_balance', models.DecimalField(decimal_places=2, help_text='Outstanding balance of the loan at the beginning of theperiod covered by the filing (from LOAN_CD.LOAN_AMT4)', max_digits=14, verbose_name='beginning period balance')),
                ('amount_loaned', models.DecimalField(decimal_places=2, help_text='Amount loaned during the period covered by the filing (from LOAN_CD.LOAN_AMT1)', max_digits=14, verbose_name='amount loaned')),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='Amount paid back during the period covered by the filing (from LOAN_CD.LOAN_AMT5)', max_digits=14, verbose_name='amount paid')),
                ('amount_forgiven', models.DecimalField(decimal_places=2, help_text='Amount forgiven by the campaign filer during the period covered by the filing (from LOAN_CD.LOAN_AMT6)', max_digits=14, verbose_name='amount forgiven')),
                ('end_period_balance', models.DecimalField(decimal_places=2, help_text='Outstanding balance of the loan at the end of the period covered by the filing (from LOAN_CD.LOAN_AMT2)', max_digits=14, verbose_name='end period balance')),
                ('date_due', models.DateField(help_text='Date that the loan is due (from LOAN_CD.LOAN_DATE2)', null=True, verbose_name='date due')),
                ('interest_received', models.DecimalField(decimal_places=2, help_text='Amount of interest paid on the loan during the period covered by the campaign filing (from LOAN_CD.LOAN_AMT7)', max_digits=14, verbose_name='interest paid')),
                ('interest_rate', models.CharField(blank=True, help_text='Interest rate of the loan. This is sometimes expressed as a decimal (e.g., 0.10) and other times as a percent (e.g., 10.0% (from LOAN_CD.LOAN_RATE)', max_length=30, verbose_name='interest rate')),
                ('original_amount', models.DecimalField(decimal_places=2, help_text='Original amount loaned by the lender to the campaign filer (from LOAN_CD.LOAN_AMT8)', max_digits=14, verbose_name='original amount')),
                ('date_incurred', models.DateField(help_text='Date the loan was made or received (from LOAN_CD.LOAN_DATE1)', null=True, verbose_name='')),
                ('cumulative_ytd_contributions', models.DecimalField(decimal_places=2, help_text='Cumulative amount of contributions (loans, monetary and nonmonetary contributions) from the campaign filer to the recipient during the calendar year covered by this statement (from LOAN_CD.LOAN_AMT3)', max_digits=14, verbose_name='cumulative year-to-date contributions')),
                ('filing', models.ForeignKey(help_text='Foreign key referring to the Form 460 on which the loan was reported (from LOAN_CD.FILING_ID)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_h_items', to='calaccess_processed.Form460Filing')),
            ],
        ),
        migrations.CreateModel(
            name='Form460ScheduleHItemVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_item', models.IntegerField(help_text='Line number of the filing form where the loan is itemized (from LOAN_CD.LINE_ITEM)', verbose_name='line item')),
                ('lender_code', models.CharField(blank=True, choices=[('COM', 'Committee'), ('IND', 'Individual'), ('OTH', 'Other'), ('PTY', 'Political Party'), ('RCP', 'Recipient committee'), ('SCC', 'Small Contributor Committee'), ('???', 'Unknown value')], help_text='Code describing the lender (from LOAN_CD.ENTITY_CD)', max_length=3, verbose_name='lender code')),
                ('lender_committee_id', models.CharField(blank=True, help_text="lender's filer identification number, if it is a committee (from LOAN_CD.CMTE_ID)", max_length=9, verbose_name='lender committee id')),
                ('lender_title', models.CharField(blank=True, help_text='Name title of the lender (from LOAN_CD.LNDR_NAMT)', max_length=10, verbose_name='lender title')),
                ('lender_lastname', models.CharField(blank=True, help_text='Last name of the lender or business name (from LOAN_CD.LNDR_NAML)', max_length=200, verbose_name='lender lastname')),
                ('lender_firstname', models.CharField(blank=True, help_text='First name of the lender (from LOAN_CD.LNDR_NAMF)', max_length=45, verbose_name='lender firstname')),
                ('lender_name_suffix', models.CharField(blank=True, help_text='Name suffix of the lender (from LOAN_CD.LNDR_NAMS)', max_length=10, verbose_name='lender name suffix')),
                ('lender_city', models.CharField(blank=True, help_text='City of the lender (from LOAN_CD.LOAN_CITY)', max_length=30, verbose_name='lender city')),
                ('lender_state', models.CharField(blank=True, help_text='State of the lender (from LOAN_CD.LOAN_ST)', max_length=2, verbose_name='lender state')),
                ('lender_zip', models.CharField(blank=True, help_text='Zip code (usually zip5, sometimes zip9) of the lender (from LOAN_CD.LOAN_ZIP4)', max_length=10, verbose_name='lender zip')),
                ('lender_employer', models.CharField(blank=True, help_text='Employer of the lender (from LOAN_CD.LOAN_EMP)', max_length=200, verbose_name='lender employer')),
                ('lender_occupation', models.CharField(blank=True, help_text='Occupation of the lender (from LOAN_CD.LOAN_OCC)', max_length=60, verbose_name='lender occupation')),
                ('lender_is_self_employed', models.BooleanField(default=False, help_text='Indicates whether or not the lender is self-employed(from LOAN_CD.LOAN_SELF)', verbose_name='lender is self employed')),
                ('treasurer_title', models.CharField(blank=True, help_text="Name title of the lender committee's treasurer (from LOAN_CD.TRES_NAMT)", max_length=10, verbose_name='treasurer title')),
                ('treasurer_lastname', models.CharField(blank=True, help_text="Last name of the lender committee's treasurer (from LOAN_CD.TRES_NAML)", max_length=200, verbose_name='treasurer lastname')),
                ('treasurer_firstname', models.CharField(help_text="First name of the lender committee's treasurer (from LOAN_CD.TRES_NAMF)", max_length=45, verbose_name='treasurer firstname')),
                ('treasurer_name_suffix', models.CharField(blank=True, help_text="Name suffix of the lender committee's treasurer (from LOAN_CD.TRES_NAMS)", max_length=10, verbose_name='treasurer name suffix')),
                ('treasurer_city', models.CharField(blank=True, help_text="City of the lender committee's treasurer (from LOAN_CD.TRES_CITY)", max_length=30, verbose_name='treasurer city')),
                ('treasurer_state', models.CharField(blank=True, help_text="State of the lender committee's treasurer (from LOAN_CD.TRES_ST)", max_length=2, verbose_name='treasurer state')),
                ('treasurer_zip', models.CharField(blank=True, help_text="Zip code (usually zip5, sometimes zip9) of the lender committee's treasurer (from LOAN_CD.TRES_ZIP4)", max_length=10, verbose_name='treasurer zip')),
                ('intermediary_title', models.CharField(blank=True, help_text='Name title of the intermediary (from LOAN_CD.INTR_NAMT)', max_length=10, verbose_name='intermediary title')),
                ('intermediary_lastname', models.CharField(blank=True, help_text='Last name of the intermediary or business name (from LOAN_CD.INTR_NAML)', max_length=200, verbose_name='intermediary lastname')),
                ('intermediary_firstname', models.CharField(help_text='First name of the intermediary (from LOAN_CD.INTR_NAMF)', max_length=45, verbose_name='intermediary firstname')),
                ('intermediary_name_suffix', models.CharField(blank=True, help_text='Name suffix of the intermediary (from LOAN_CD.INTR_NAMS)', max_length=10, verbose_name='intermediary name suffix')),
                ('intermediary_city', models.CharField(blank=True, help_text='City of the intermediary (from LOAN_CD.INTR_CITY)', max_length=30, verbose_name='intermediary city')),
                ('intermediary_state', models.CharField(blank=True, help_text='State of the intermediary (from LOAN_CD.INTR_ST)', max_length=2, verbose_name='intermediary state')),
                ('intermediary_zip', models.CharField(blank=True, help_text='Zip code (usually zip5, sometimes zip9) of the intermediary (from LOAN_CD.INTR_ZIP4)', max_length=10, verbose_name='intermediary zip')),
                ('transaction_id', models.CharField(help_text='Identifies a unique transaction across versions of the a given Form 460 filing (from LOAN_CD.TRAN_ID)', max_length=20, verbose_name='transaction id')),
                ('memo_reference_number', models.CharField(blank=True, help_text="A value assigned by the filer which refers to the item'sfootnote in the TEXT_MEMO_CD table (from LOAN_CD.MEMO_REFNO)", max_length=20, verbose_name='memo reference number')),
                ('begin_period_balance', models.DecimalField(decimal_places=2, help_text='Outstanding balance of the loan at the beginning of theperiod covered by the filing (from LOAN_CD.LOAN_AMT4)', max_digits=14, verbose_name='beginning period balance')),
                ('amount_loaned', models.DecimalField(decimal_places=2, help_text='Amount loaned during the period covered by the filing (from LOAN_CD.LOAN_AMT1)', max_digits=14, verbose_name='amount loaned')),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='Amount paid back during the period covered by the filing (from LOAN_CD.LOAN_AMT5)', max_digits=14, verbose_name='amount paid')),
                ('amount_forgiven', models.DecimalField(decimal_places=2, help_text='Amount forgiven by the campaign filer during the period covered by the filing (from LOAN_CD.LOAN_AMT6)', max_digits=14, verbose_name='amount forgiven')),
                ('end_period_balance', models.DecimalField(decimal_places=2, help_text='Outstanding balance of the loan at the end of the period covered by the filing (from LOAN_CD.LOAN_AMT2)', max_digits=14, verbose_name='end period balance')),
                ('date_due', models.DateField(help_text='Date that the loan is due (from LOAN_CD.LOAN_DATE2)', null=True, verbose_name='date due')),
                ('interest_received', models.DecimalField(decimal_places=2, help_text='Amount of interest paid on the loan during the period covered by the campaign filing (from LOAN_CD.LOAN_AMT7)', max_digits=14, verbose_name='interest paid')),
                ('interest_rate', models.CharField(blank=True, help_text='Interest rate of the loan. This is sometimes expressed as a decimal (e.g., 0.10) and other times as a percent (e.g., 10.0% (from LOAN_CD.LOAN_RATE)', max_length=30, verbose_name='interest rate')),
                ('original_amount', models.DecimalField(decimal_places=2, help_text='Original amount loaned by the lender to the campaign filer (from LOAN_CD.LOAN_AMT8)', max_digits=14, verbose_name='original amount')),
                ('date_incurred', models.DateField(help_text='Date the loan was made or received (from LOAN_CD.LOAN_DATE1)', null=True, verbose_name='')),
                ('cumulative_ytd_contributions', models.DecimalField(decimal_places=2, help_text='Cumulative amount of contributions (loans, monetary and nonmonetary contributions) from the campaign filer to the recipient during the calendar year covered by this statement (from LOAN_CD.LOAN_AMT3)', max_digits=14, verbose_name='cumulative year-to-date contributions')),
                ('filing_version', models.ForeignKey(help_text='Foreign key referring to the version of the Form 460 that includes the outstanding loan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_h_items', to='calaccess_processed.Form460FilingVersion')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulehitemversion',
            unique_together=set([('filing_version', 'line_item')]),
        ),
        migrations.AlterIndexTogether(
            name='form460schedulehitemversion',
            index_together=set([('filing_version', 'line_item')]),
        ),
        migrations.AlterUniqueTogether(
            name='form460schedulehitem',
            unique_together=set([('filing', 'line_item')]),
        ),
    ]
