from six import text_type

from sweetcaptcha.fields import SweetCaptchaField

from wagtail.wagtailadmin import tasks
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractForm

from .forms import SweetCaptchaFormBuilder


class SweetCaptchaEmailForm(AbstractEmailForm):
    """A SweetCaptchaForm Page. Pages implementing a captcha form with email notification should inhert from it"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(SweetCaptchaEmailForm, self).__init__(*args, **kwargs)
        self.form_builder = SweetCaptchaFormBuilder

    def process_form_submission(self, form):
        super(AbstractEmailForm, self).process_form_submission(form)

        if self.to_address:
            content = ''
            for x in form.fields.items():
                if not isinstance(x[1], SweetCaptchaField):  # exclude SweetCaptchaField from notification
                    content += '\n'.join([x[1].label + ': ' + text_type(form.data.get(x[0]))])
            tasks.send_email_task.delay(self.subject, content, [self.to_address], self.from_address,)

    class Meta:
        abstract = True


class SweetCaptchaForm(AbstractForm):
    """A SweetCaptchaForm Page. Pages implementing a captcha form should inhert from it"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(SweetCaptchaForm, self).__init__(*args, **kwargs)
        self.form_builder = SweetCaptchaFormBuilder

    class Meta:
        abstract = True
