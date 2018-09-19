# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AuthorManager(BaseUserManager):
    """Define a model manager for Author model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save an author with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Author(AbstractUser):
    username = models.CharField(max_length=5, unique=True)
    first_name = models.CharField(max_length=15, default="")
    last_name = models.CharField(max_length=15, default="")
    email = models.EmailField(unique=True)
    bio = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"<Username:{0}> - <Email: {1}>".format(self.username,
                                                       self.email)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthorManager()


class Articles(models.Model):
    """
    User model that holds every article by an author,this model is mapped
    to the Author model by a ManyToOne Relationship
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.TextField()
    relaease_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"<Author:{0}> - <Ariticle: {0}>".format(self.author,
                                                        self.article)
