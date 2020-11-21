from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet

from backend.views import BaseAPIView


class BaseGenericViewSet(GenericViewSet, BaseAPIView):
    serializer_classes = {}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class BaseModelViewSet(ModelViewSet, BaseAPIView):
    pass


class BaseReadOnlyModelViewSet(ReadOnlyModelViewSet, BaseAPIView):
    pass


class BaseManagerViewSet(BaseGenericViewSet, BaseAPIView):
    manager_class = None
    manager_classes = {}

    def get_manager_class(self):
        assert self.manager_class, "Set manager class"
        return self.manager_classes.get(self.action, self.manager_class)

    def get_manager(self, *args, **kwargs):
        kwargs.setdefault("context", self.get_serializer_context())
        manager = self.get_manager_class()
        manager(user=self.user, *args, **kwargs)
        return manager
