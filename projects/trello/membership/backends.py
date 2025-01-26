from django.contrib.auth.backends import BaseBackend
from .models import MemberModel
from django.contrib.auth.hashers import check_password
from django.utils.timezone import now

class MemberAuthBackend(BaseBackend):
    def authenticate(self, request, username = ..., password = ..., **kwargs):
        try:
            member = MemberModel.objects.get(username= username)
            if check_password(password , member.password):
                member.last_login = now()
                member.save()
                return member
        except MemberModel.DoesNotExist:
            return None
        
    def get_user(self, member_id):
        try:
            return MemberModel.objects.get(pk=member_id)
        except MemberModel.DoesNotExist:
            return None