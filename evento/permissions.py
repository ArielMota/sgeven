from rest_framework import permissions

class EventoOrganizadorPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(organizador=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return obj.organizador == request.user