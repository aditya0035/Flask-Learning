from django import forms

class UserForm(forms.Form):
    firstName=forms.CharField(max_length=200)
    lastName=forms.CharField(max_length=200)
    hdnFirstName=forms.CharField(widget=forms.HiddenInput(),required=False)

    def clean_firstName(self):
        fName=self.cleaned_data
        print(fName)
    def clean(self):
        hdnName=self.cleaned_data["hdnFirstName"]
        print(hdnName)
        if hdnName!='':
          raise forms.ValidationError("Hidden Field Should be null")
        
       