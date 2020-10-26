from .avatar import Avatar
from .models import Profil

# def avatar(request):
#     print(Avatar(request))
#     return {'a':Avatar(request)}

def avatar(request):

    return {'a':Profil.objects.filter(user__username=request.user).values('photo')}