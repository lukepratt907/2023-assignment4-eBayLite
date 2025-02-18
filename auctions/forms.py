from django import forms
from .models import Auction


class AuctionForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Give it a title'
        }
        )
    )
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Tell more about the product',
            'rows': '3'
        }
        )
    )
    price = forms.DecimalField(
        label='Price',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting Bid',
            'min': '0.01',
            'max': '999999999.99',
            'step': '0.01'
        }
        )
    )
    category = forms.ChoiceField(
        label='Category',
        required=False,
        choices=Auction.CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category'
        }
        )
    )
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        initial='',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Image URL (optional)',
        }
        )
    )

class CommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Comment Here'
        })
    )