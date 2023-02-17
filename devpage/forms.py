from django import forms
from captcha.fields import CaptchaField


class contactForm(forms.Form):
    captcha = CaptchaField()
