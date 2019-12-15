from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from InfoTrack.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile,Comment



##Q:Fix the profileform
##Q:Fix the EditForm
class ProfileForm(forms.Form):
    username = forms.CharField(required = True)
    password1 = forms.CharField(max_length=100,required = True)
    password2 = forms.CharField(max_length=100,required = True)

    first_name = forms.CharField(max_length=200,required = True)
    last_name = forms.CharField(max_length=200,required = True)
    email = forms.EmailField(required = True)
    studentID = forms.IntegerField(required = True)

    birth_date = forms.DateField(required = False)
    phone = forms.IntegerField(required = False)

    location = forms.CharField(max_length=100,required = False)

    grade = forms.CharField(max_length=20,required = False)
    major = forms.CharField(max_length = 20, help_text="Please enter your major.",required = False)

    website = forms.URLField(required = False)
    description = forms.CharField(max_length=100, help_text = "Describe yourself.",required = False)

    class Meta:
        model = UserProfile
        fields = ("username",
        "password1",
        "password2",
        "first_name",
        "last_name",
        "email",
        "password",
        "studentID",
        "birth_date",
        "phone",
        "location",
        "birth_date",
        "grade",
        "major",
        "website",
        "description"
        )

    def save(self, commit=True):
        # user_profile = super(ProfileForm, self).save(commit=False)
        user = User()
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        user.username = self.cleaned_data["username"]

        if commit:
            user.save()
            print(user.id)
            user_profile = UserProfile(user=user)
            user_profile.studentID = self.cleaned_data["studentID"]
            user_profile.location = self.cleaned_data["location"]
            user_profile.birth_date = self.cleaned_data["birth_date"]
            user_profile.phone = self.cleaned_data["phone"]
            user_profile.grade = self.cleaned_data["grade"]
            user_profile.major = self.cleaned_data["major"]
            user_profile.website = self.cleaned_data["website"]
            user_profile.description = self.cleaned_data["description"]
            print(user_profile.userid)
            print(user_profile.user_id)
            # print(UserProfile.objects.get(userid=user_profile.userid))
            user_profile.save()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2"
        )


    def save(self,commit =True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]

        if commit:

            user.save()

        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password"
            )
        

class  PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'context', 'video', 'PostType',"image")

class  CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('context', 'video',"image")