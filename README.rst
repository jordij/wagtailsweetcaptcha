**IMPORTANT MALWARE ISSUE: [https://blog.sucuri.net/2015/06/sweetcaptcha-service-used-to-distribute-adware.html](https://blog.sucuri.net/2015/06/sweetcaptcha-service-used-to-distribute-adware.html)** 

Wagtail SweetCaptcha
================
**Wagtail forms SweetCaptcha form field/widget integration app.**

wagtailsweetcaptcha provides a an easy wayto integrate the `django-sweetcaptcha <https://pypi.python.org/pypi/sweetcaptcha/>`_ field when using the Wagtail formbuilder.


Installation
------------

#. Install or add ``wagtailsweetcaptcha`` to your Python path.

#. Add ``wagtailsweetcaptcha`` to your ``INSTALLED_APPS`` setting.

#. Config django-sweetcaptcha as explained in `here <https://github.com/jordij/django-sweetcaptcha>`_.


Usage
-----

Field
~~~~~
The quickest way to add a sweetcaptcha field to a Wagtail Form Page is to inherit from the two options provided, ``SweetCaptchaForm`` or ``SweetCaptchaEmailForm``. The first options inherits from ``AbstractForm`` while the seconds does it from ``AbstractEmailForm``. Either way your page is going to display a sweetcaptcha field at the end of the form.

Example

.. code-block:: python

    from wagtail.wagtailforms.models import AbstractFormField
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
    from wagtail.wagtailcore.fields import RichTextField

    from modelcluster.fields import ParentalKey
    from wagtailsweetcaptcha.models import SweetCaptchaEmailForm


    class SubmitFormField(AbstractFormField):
        page = ParentalKey('SubmitFormPage', related_name='form_fields')


    class SubmitFormPage(SweetCaptchaEmailForm):
        body = RichTextField(blank=True, help_text='Edit the content you want to see before the form.')
        thank_you_text = RichTextField(blank=True, help_text='Set the message users will see after submitting the form.')

        class Meta:
            verbose_name = "Form submission page"
            description = "Page with the form to submit"


    SubmitFormPage.content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel(SubmitFormPage, 'form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], "Email notification")
    ]


The sweetcaptcha field can't be added from the admin UI but will appear in your frontend.
