from django.db import models
# Create your models here.
from django.utils.translation import gettext_lazy as _



from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class ResearcherUserManager(BaseUserManager):
    """
    The Manager of the user(Researcher)
    """

    def create_user(self, first_name, last_name, email, password=None, **other_fields):
        """
        Simple user
        """
        if not email:
            raise ValueError(_("the email must be set "))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password=None, **other_fields):
        """
        Superuser(admin)
        """
        # this kind of code is for testing purpose
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff")

        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must be is_active")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser")
        return self.create_user(first_name, last_name, email, password, **other_fields)

# custom user
class Researcher(AbstractBaseUser, PermissionsMixin):
    """
    The user profile of a researcher 
    """
    # attributes
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    email = models.EmailField(_('email adress'), unique=True)
    speciality = models.CharField(max_length=150, blank=True)
    grade = models.CharField(max_length=200, blank=True)
    
    # google scholar info 
    h_index = models.PositiveIntegerField(blank=True, null=True,default=0)
    i10_index = models.PositiveIntegerField(blank=True, null=True,default=0)
    citations = models.PositiveIntegerField(blank=True, null=True,default=0)
    graph_citations = models.JSONField(null=True,blank=True)
    nbr_pubs = models.PositiveIntegerField(blank=True, null=True,default=0)
    graph_pub = models.JSONField(null=True,blank=True)
    
    # extra info  
    image = models.ImageField(blank=True,default='D', upload_to='images')
    linkedin_account = models.URLField(blank=True)
    google_scholar_account = models.URLField(blank=True,unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Relationship between Database tables
    equipe_researchers = models.ForeignKey(
        'Equipe', on_delete=models.SET_NULL, null=True, blank=True)
    
    # interests
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ResearcherUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ordering = ['date_joined']

    # Researche : YAHIA Ilyes
    def get_google_id(self):
        return self.google_scholar_account.partition("user=")[2][:12]
    
    def __str__(self) -> str:
        return " ".join([ self.last_name.upper(), self.first_name.capitalize()])

    def get_username(self) -> str:
        return super().get_username()

class Equipe(models.Model):
    nom = models.CharField(max_length=200)
    site_web=models.URLField(blank=True)
    # Relationship
    division = models.ForeignKey(
        'Division', on_delete=models.CASCADE, null=True)
    chef_equipe = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)
    long_nom = models.CharField(max_length=250,blank=True,null=True)
    
    def __str__(self):
        return self.nom+" "+str(self.id)
    
class Division(models.Model):
    nom = models.CharField(max_length=200, default='')
    site_web=models.URLField(blank=True)
    long_nom = models.CharField(max_length=200,blank=True,null=True)
    # relationshi
    etablisment = models.ForeignKey(
        'Etablisment', on_delete=models.CASCADE, null=True)
    chef_div = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom

class Etablisment(models.Model):
    nom = models.CharField(max_length=200, default='')
    logo = models.ImageField(null=True, blank=True)
    site_web=models.URLField(blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    chef_etablisement = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)
    
    long_nom = models.CharField(max_length=250,blank=True,null=True)
    # directions = models.ForeignKey(
    #     'Directions', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Directions(models.Model):
    nom = models.CharField(max_length=150, )
    chef_direction = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True)
    
class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.state_name
