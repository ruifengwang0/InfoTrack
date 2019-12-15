from django.db import models
from PIL import Image
import uuid
from django.contrib.auth.models import User  #DJANGO DEFAULT USER
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #comment = models.ManyToManyField("Comment",help_text = "Write your comment for the post.")
    location = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    description = models.CharField(max_length=100, default='', help_text = "Describe yourself.")
    phone = models.IntegerField(default=0)
    userid = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text="Unique ID for this particular user.")
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    studentID = models.IntegerField(default = 0, help_text = "Umass studentID.")

    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    grade = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default='FRESHMAN')
    major = models.CharField(max_length = 20, help_text="Please enter your major.",blank=False)

    def __str__(self):
        return self.user.username

# if the current user is created the profile is automatically linked to it
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
    

class Post(models.Model):
    title = models.CharField(max_length = 200, help_text ="Your post title.",blank = True)
    context = models.TextField(help_text ="What is in your mind?",blank = True)
    time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    video = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True) 

    TYPE_OF_POST = (
        ("---","---"),
        ('clubinfo', 'ClubInfo'),
        ('courseinfo', 'CourseInfo'),
        ('lookforride', 'FreeRide'),
        ('tutor', 'TutorInfo'),
        ('rent', 'RentInfo')
    )
    PostType = models.CharField(max_length=50, choices=TYPE_OF_POST, default='---')

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return '%s, %s, %s' % (self.title,self.context,self.time)


# Required for unique comment instances
class Comment(models.Model):
    context = models.TextField(help_text ="Write your comment.",blank = True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    video = models.URLField(blank=True)
    time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True)
    post = models.ForeignKey('Post', null=True)

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return '%s, %s' % (self.context,self.time)
