from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого товара")
        return super().dispatch(request, *args, **kwargs)


class OwnerOrModeratorMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        if not (user == obj.owner or user.has_perm("catalog.change_product")):
            raise PermissionDenied("У вас нет прав для этого действия")
        return super().dispatch(request, *args, **kwargs)
