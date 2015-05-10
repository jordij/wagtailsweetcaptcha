from wagtail.wagtailforms.models import AbstractEmailForm, AbstractForm

from .forms import SweetCaptchaFormBuilder


class SweetCaptchaEmailForm(AbstractEmailForm):
    """A SweetCaptchaForm Page. Pages implementing a captcha form with email notification should inhert from it"""

    is_abstract = True  # Don't display me in "Add"

    def __init__(self, *args, **kwargs):
        super(SweetCaptchaEmailForm, self).__init__(*args, **kwargs)
        self.form_builder = SweetCaptchaFormBuilder

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
