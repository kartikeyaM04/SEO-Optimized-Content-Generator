from django import forms

class BlogPromptForm(forms.Form):
    topic = forms.CharField(max_length=100, label="Blog Topic")
    keywords = forms.CharField(
        help_text="Comma-separated keywords",
        widget=forms.TextInput(attrs={"placeholder": "e.g., AI, SEO, automation"})
    )
    tone = forms.ChoiceField(
        choices=[('formal', 'Formal'), ('casual', 'Casual'), ('friendly', 'Friendly')],
        label="Tone of the Blog"
    )
    outline = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 2}),
        help_text="Optionally provide a structure or outline (e.g., intro, bullet points)."
    )
    expected_length = forms.ChoiceField(
        choices=[('short', 'Short (~300 words)'), ('medium', 'Medium (~600 words)'), ('long', 'Long (~1000+ words)')],
        label="Expected Length"
    )
    purpose = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 2}),
        label="Purpose",
        help_text="e.g., To educate beginners, promote a product, improve SEO ranking..."
    )
