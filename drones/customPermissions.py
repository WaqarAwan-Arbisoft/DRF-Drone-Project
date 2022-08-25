from rest_framework import permissions

class isCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Checking if the method is safe(GET,OPTIONS,HEAD). If it is safe, then return true because user can view the object
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            #If method is not safe, only the owner of the user can make changes to the object
            return obj.owner==request.user