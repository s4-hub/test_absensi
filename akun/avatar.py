from django.conf import settings
from .models import Profil

# class Avatar(object):
#     def __init__(self, request):
#         self.user = Profil.objects.filter(user__username=request.user).values('photo')
#         avatar = self.user.get(settings.AVATAR_SESSION_ID)

#         if not avatar:
#             avatar = self.user[settings.AVATAR_SESSION_ID] =  {}
#         self.avatar = avatar

class Avatar(object):
    def __init__(self, request):
        self.session = request.session
        avatar = self.session.get(settings.AVATAR_SESSION_ID)

        if not avatar:
            avatar = self.session[settings.AVATAR_SESSION_ID] = {}
        self.avatar = avatar