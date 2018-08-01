from django import forms
from courses.models import MarksDistribution


class MarksDistributionForm(forms.ModelForm):
    class Meta:
        model = MarksDistribution
        fields = '__all__'

    def clean(self):
        total_sum = 0
        for field in self.fields:
            total_sum += self.cleaned_data.get(field, 0)
        if total_sum != 100:
            raise forms.ValidationError('All the fields doesn\'t add up to 100%')
        else:
            return self.cleaned_data
