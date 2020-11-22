from django.db.models import Avg

from backend.account.models import User, UserRate
from backend.managers import BaseManager


class UserRateManager(BaseManager):

    def __init__(self, user: User, *args, **kwargs):
        super(UserRateManager, self).__init__(user, *args, **kwargs)
        self.evaluated_id = kwargs.get('pk', self.user.id)

    def calculate_rate(self):
        return UserRate.objects.filter(evaluated=self.evaluated_id).aggregate(rate=Avg('score'))

    def response(self):
        return self.calculate_rate()


class UserRatesManager(BaseManager):

    def __init__(self, user: User, context: dict, *args, **kwargs):
        super(UserRatesManager, self).__init__(user, context, *args, **kwargs)
        # self.evaluated_ids = evaluated_ids

    def calculate_rate(self):
        return UserRate.objects.values('evaluated').annotate(rate=Avg('score'))
            # filter(evaluated__in=self.evaluated_ids).\

    def response(self):
        return self.calculate_rate()
