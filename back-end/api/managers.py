from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("O email deve ser fornecido!")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs) 
        user.set_password(password) 
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    
    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser tem que ter is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser tem que ter is_superuser=True.')

        return self._create_user(email, password, **kwargs)