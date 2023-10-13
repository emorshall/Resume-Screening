from django import forms

from .models import Login, ResumeProfile, Skills, CandidateProfile


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['name', 'password']


class ResumeProfileForm(forms.ModelForm):
    class Meta:
        model = ResumeProfile
        fields = ['profile_name', 'profile_keyword', 'active']


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_name', 'active']


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['can_name']
