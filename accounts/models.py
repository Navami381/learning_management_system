from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=12,unique=True)
    ROLE_CHOICES=(
        ("trainer","trainer"),
        ("student","student")
    )
    role=models.CharField(max_length=100,choices=ROLE_CHOICES,default="student")


class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linkedin_url = models.URLField(null=True)

    student=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")



class TrainerProfile(models.Model):

    expertise_areas = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    languages=models.CharField(max_length=200,null=True)

    experience_years=models.CharField(max_length=200,null=True)

    githuburl = models.URLField(null=True)

    linkedurl = models.URLField(null=True)

    trainer=models.OneToOneField(User,on_delete=models.CASCADE)



from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,*args,**kwargs):
    if created and instance.role=="student":
        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)


def create_trainer_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role=="trainer":

        TrainerProfile.objects.create(trainer=instance)

post_save.connect(create_trainer_profile,sender=User)


from django.core.mail import send_mail
def send_invitation_mail(sender,instance,created,*args,**kwargs):
    if created and instance.role=="student":

        send_mail(
         "Account creation confirmation",
         "you have succesfully created account in studentprofile .",
        ""
        "navamipm2020@gmail.com",
        ["anjithkallada1500@gmail.com"]
        
            )
post_save.connect(send_invitation_mail,sender=User)


