from django.forms import model_to_dict

from infos.models import User
class UsersServiceImple(object):
    def getAllUsers(self):
        users = list(map(lambda x: model_to_dict(x), User.objects.all()))
        return users

    def addUser(self, request):
        new_user = User(nameLast=request.get('name_last'),
                        nameFirst=request.get('name_first'),
                        email=request.get('email'),
                        userAddress=request.get('address_id')
                        )
        new_user.save()
        return "Success!"

    def updateUser(self, request, user_id):
        user = User.objects.get(userID=user_id)
        user.nameLast = request.get('name_last')
        user.nameFirst = request.get('name_first')
        user.email = request.get('email')
        user.userAddress = request.get('address_id')
        user.save()
        return "Success!"

    def deleteUser(self, user_id):

        User.objects.get(userID=user_id).delete()
        return "Success!"

    def getUserByUserId(self, user_id):
        user = User.objects.filter(userID=user_id)
        user = list(map(lambda x: model_to_dict(x), user))
        return user