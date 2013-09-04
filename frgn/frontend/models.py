# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, RadioSelect
from django.contrib import admin
from django.core.mail import mail_managers

STUDY_MODE = {
    'school mode': u'хочу заниматься на крусах',
    'repetitor mode': u'хочу, чтобы преподаватель приезжал ко мне домой'
}
STUDY_MODE_CHOISES = [(item, STUDY_MODE[item]) for item in STUDY_MODE]

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Имя:')
    phone = models.CharField(max_length=100, verbose_name=u'Контактый телефон:')
    email = models.EmailField(verbose_name=u'Mail:')
    age = models.IntegerField(verbose_name=u'Возраст')
    mode = models.CharField(
        max_length=256,
        choices=STUDY_MODE_CHOISES,
        verbose_name=u'Вид обучения',
        default='school mode',
    )
    level = models.CharField(
        max_length=256,
        choices=(
            ('Beginner', 'Beginner'),
            ('Elementary', 'Elementary'),
            ('Pre-Intermediate', 'Pre-Intermediate'),
            ('Intermediate', 'Intermediate'),
            ('Upper-Intermediate', 'Upper-Intermediate'),
            ('Advanced', 'Advanced'),
        ),
        default='Beginner',
        verbose_name=u'Предполагаемый уровень'
    )

    def save(self):
        super(Student, self).save()
        mail_managers(
            u'Кто-то хочет учится',
            u"Имя: {0} \n"
            u"Телефон:{1}; Email {2} \n"
            u"уровень: {3} \n"
            u"Возраст {4}\n"
            u"Режим обучения {5}".format(
                self.name, self.email, self.phone, self.level,
                self.age, STUDY_MODE[self.mode]
            ),
            fail_silently=True
        )

class Contact(models.Model):
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


# -- формы --
class ContactForm(ModelForm):
    class Meta:
        model = Contact

class StudentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['mode'].widget.attrs.update({'style' : 'display:none;'})

    class Meta:
        model = Student
        widgets = {
            'mode': RadioSelect
        }

# --- админка ----
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'email', 'text'

class StudentAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'email', 'age', 'level', 'mode'

admin.site.register(Contact, ContactAdmin)
admin.site.register(Student, StudentAdmin)