# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django.core.mail import mail_managers

class Contact(models.Model): # тема, имя отправителя, мэйл, и само сообщение
    name = models.CharField(max_length=100, verbose_name=u'Имя:')
    email = models.EmailField(verbose_name=u'Mail:')
    phone = models.CharField(max_length=100, verbose_name=u'Контактый телефон:')
    text = models.TextField(verbose_name=u'О себе:')

    def save(self):
        super(Contact, self).save()
        mail_managers(
            u'В базу добавлен новый репетитр.',
            u"Имя: {0} \n"
            u"Телефон:{1}; Email {2} \n"
            u"О себе: {3} \n".format(
                self.name, self.email, self.phone, self.text
            ),
            fail_silently=True
        )


    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __unicode__(self):
        return self.name


class ContactForm(ModelForm):

    class Meta:
        model = Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'email', 'text'


admin.site.register(Contact, ContactAdmin)