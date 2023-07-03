from django import forms

# Reordering Form and View
# hello im using forms to store the data


class PositionForm(forms.Form):
    position = forms.CharField()
