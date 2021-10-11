from infos.models import User
class UsersServiceImple(object):
    def getAllUsers(self):
        users = User.objects.all()
        return users

    def getUserByUserId(self, user_id):
        user = User.objects.filter(userID=user_id)
        return user