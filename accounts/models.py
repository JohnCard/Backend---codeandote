from helpers.models import TrackingModel
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """
    # Username
    username_validator = UnicodeUsernameValidator()
    
    objects = UserManager()

    username = models.CharField(
        verbose_name="Nombre de usuario",
        max_length=150,
        unique=False,
        blank=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    # First name
    first_name = models.CharField(
        verbose_name="Nombre", max_length=150, blank=True)

    # Last name
    last_name = models.CharField(
        verbose_name="Apellidos", max_length=150, blank=True)

    # Email
    email = models.EmailField(
        verbose_name="Correo electrónico", blank=False, unique=True)

    # Is staff
    is_staff = models.BooleanField(
        verbose_name="Es miembro",
        default=False,
        help_text="Designates whether the user can log into this admin site",
    )

    # Is active
    is_active = models.BooleanField(
        verbose_name="Activo",
        default=True,
        help_text="Designates whether this user should be treated as active., Unselect this instead of deleting accounts.",
    )

    # Last login
    last_login = models.DateTimeField(
        verbose_name="Último acceso", default=timezone.now)

    # Date joined (created)
    date_joined = models.DateTimeField(
        verbose_name="Creado", default=timezone.now)

    # Email verified
    email_verified = models.BooleanField(
        verbose_name="Correo electrónico verificado",
        default=False,
        help_text="Designates whether this user's email is verified.",
    )

    # Balance
    balance = models.DecimalField(
        verbose_name='Saldo',
        max_digits=10,
        decimal_places=2,
        default=75000,
    )

    # image profile
    image = models.ImageField(
        verbose_name='Foto de perfil',
        null=True,
        blank=True,
        upload_to='',
        default='https://cdn-icons-png.freepik.com/512/9398/9398920.png'
    )

    # description
    description = models.TextField(
        verbose_name='Brief description',
        blank=True,
        null=True,
        help_text='Type a brief description about your profession'
    )

    # Fields configuration.
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    # @property
    # def token(self):
    #     token = jwt.encode({
    #         'email': self.email,
    #         'password': self.password,
    #         'exp': datetime.utcnow() + timedelta(hours=24)},
    #         settings.SECRET_KEY,
    #         algorithm='HS256')
    #     return token

    def __str__(self):
        return self.username