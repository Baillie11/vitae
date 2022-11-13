# Generated by Django 4.1 on 2022-08-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_alter_user_address_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='category',
            field=models.CharField(choices=[('Accounting', 'Accounting'), ('Administration', 'Administration'), ('Advert/Media/Entert', 'Advert/Media/Entert'), ('Banking and Financial Services', 'Banking and Financial Services'), ('Call Centre / Customer Service', 'Call Centre / Customer Service'), ('Community & Sport', 'Community & Sport'), ('Construction', 'Construction'), ('Consulting & Corporate Strategy', 'Consulting & Corporate Strategy'), ('Education & Training', 'Education & Training'), ('Engineering', 'Engineering'), ('Government/Defence', 'Government/Defence'), ('Healthcare & Medical', 'Healthcare & Medical'), ('Hospitality & Tourism', 'Hospitality & Tourism'), ('HR & Recruitment', 'HR & Recruitment'), ('Insurance & Superannuation', 'Insurance & Superannuation'), ('I.T', 'I.T'), ('Legal', 'Legal'), ('Manufacturing/Operations', 'Manufacturing/Operations'), ('Mining, Oil & Gas', 'Mining, Oil & Gas'), ('Primary Industry', 'Primary Industry'), ('Real Estate and Property', 'Real Estate and Property'), ('Retail/Consumer Prods.', 'Retail/Consumer Prods.'), ('Sales & Marketing', 'Sales & Marketing'), ('Science and Technology', 'Science and Technology'), ('Self-Employment', 'Self-Employment'), ('Trades & Services', 'Trades & Services'), ('Transport/Logistics', 'Transport/Logistics'), ('Other', 'Other')], default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('Victoria', 'Victoria'), ('New South Wales', 'New South Wales'), ('Queensland', 'Queensland'), ('South Australia', 'South Australia'), ('Western Australia', 'Western Australia'), ('Tasmania', 'Tasmania'), ('Northern Territory', 'Northern Territory'), ('Australian Capital Territory', 'Australian Capital Territory')], default='Other', max_length=100),
        ),
    ]