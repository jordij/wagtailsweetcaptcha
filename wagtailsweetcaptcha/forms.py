from wagtail.wagtailforms.forms import FormBuilder

from sweetcaptcha.fields import SweetCaptchaField


class SweetCaptchaFormBuilder(FormBuilder):
    def __init__(self, fields):
        super(SweetCaptchaFormBuilder, self).__init__(fields)
        # Add sweetcaptcha to FIELD_TYPES declaration
        self.FIELD_TYPES.update({'sweetcaptcha': self.create_sweetcaptcha_field})

    def create_sweetcaptcha_field(self, field, options):
        return SweetCaptchaField(**options)

    @property
    def formfields(self):
        # Add sweetcaptcha to formfields property
        fields = super(SweetCaptchaFormBuilder, self).formfields
        fields['sweetcaptcha'] = SweetCaptchaField(label='')

        return fields
