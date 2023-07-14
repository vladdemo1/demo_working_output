from django.shortcuts import render

from django.views.generic import View

from .models import Worker
from .controller import Search


class BaseView(View):
    """
    This class contains get for main view page and get context for render fields
    """

    def get(self, request, *args, **kwargs):
        """
        Method 'get' for render main page
        """
        boss = Search.get_first_worker_by_position('Chief Director')
        workers = Search.get_subordinates_by_worker(boss)

        context = {
            'boss': boss,
            'workers': workers,
        }
        return render(request, 'base.html', context)