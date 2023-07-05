from. models import Follow
from django.core.exceptions import ObjectDoesNotExist


# check if request user has followed the user or not
def check_followed (request_id, check_id):
    try:
        Follow.objects.get(be_followed = check_id, to_follow = request_id)
    except ObjectDoesNotExist:
        return False
    else:
        return True
    
