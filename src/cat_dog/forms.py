from django import forms


class PetFilter(forms.Form):
    CHOICES = (("cat", "Cat"), ("dog", "Dog"))
    pet = forms.ChoiceField(choices=CHOICES)
    CHOICES_TYPE = (("png", "png"), ("jpg", "jpg"), ("gif", "gif"))
    type_img = forms.ChoiceField(choices=CHOICES_TYPE)
