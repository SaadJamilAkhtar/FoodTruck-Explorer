from django import forms


class UploadCSVForm(forms.Form):
    """Truck data upload form"""
    csv_file = forms.FileField(
        label='Choose a CSV file',
        help_text='File must be a CSV file.',
        widget=forms.ClearableFileInput(attrs={
            'accept': '.csv',
            'class': 'form-control'
        }),
    )
