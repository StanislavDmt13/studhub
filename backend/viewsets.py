from rest_framework.response import Response
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
        manager = self.manager_classes.get(self.action, self.manager_class)
        assert manager, "Set manager class"
        return manager

    def get_manager(self, *args, **kwargs):
        kwargs.setdefault("context", self.get_serializer_context())
        manager = self.get_manager_class()
        return manager(user=self.user, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        manager = self.get_manager(*args, **kwargs)
        return Response(manager.response())

    def retrieve(self, request, *args, **kwargs):
        manager = self.get_manager(*args, **kwargs)
        return Response(manager.response())
