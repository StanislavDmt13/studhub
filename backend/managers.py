from backend.account.models import User


class BaseManager:

    def __init__(self, user: User, context: dict, *args, **kwargs):
        self.user = user
        self.context = context

        self.args = args
        self.kwargs = kwargs
