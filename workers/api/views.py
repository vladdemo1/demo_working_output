from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import View, DetailView

from .models import Worker
from .controller import Search, Positions


class BaseView(View):
    """
    This class contains get for main view page and get context for render fields
    """
    def get(self, request, page=1, *args, **kwargs):
        """
        Method 'get' for render main page
        """
        boss = Search.get_first_worker_by_position('Chief Director')
        workers = Search.get_subordinates_by_worker(boss)

        paginator = Paginator(workers, per_page=4)
        workers_object = paginator.get_page(page)

        positions = Positions.get_positions_dict()

        context = {
            'boss': boss,
            'workers': workers_object,
            'positions': positions,
        }
        return render(request, 'base.html', context)


class PositionView(View):
    """
    This view show workers by position with pagination
    """
    def get(self, request, position="Chief Director", page=1, *args, **kwargs):
        """
        Method 'get' for render current page with workers
        """
        current_worker = Search.get_random_worker_by_position(Positions.get_position_by_slug(position))
        workers = Search.get_subordinates_by_worker(current_worker)

        paginator = Paginator(workers, per_page=4)
        workers_object = paginator.get_page(page)

        positions = Positions.get_positions_dict()

        context = {
            'boss': current_worker,
            'workers': workers_object,
            'positions': positions,
        }
        return render(request, 'base.html', context)


class WorkerDetailView(DetailView):
    """
    This view for detain present current worker
    """
    def get(self, request, *args, **kwargs):
        """
        Selected product add to cart
        """
        position, first_name, last_name = kwargs.get('position'), kwargs.get('first_name'), kwargs.get('last_name')
        
        worker = Search.get_worker_info(position=position, first_name=first_name, last_name=last_name)
        positions = Positions.get_positions_dict()

        context = {
            'worker': worker,
            'positions': positions,
        }
        return render(request, 'worker_detail.html', context)


class SearchView(View):
    """
    This class about search
    """

    def post(self, request, *args, **kwargs):
        """
        search py pattern
        """

        form_data = request.POST.dict()

        page = kwargs.get('page') if kwargs.get('page') else 1

        pattern = str(form_data.get('pattern'))
        pattern_for_search = pattern.lower()

        workers = Search.get_workers_by_keyword(keyword=pattern_for_search)

        # paginator = Paginator(workers, per_page=4)
        # workers_object = paginator.get_page(page)

        positions = Positions.get_positions_dict()

        context = {
            'workers': workers,
            'pattern': pattern,
            'positions': positions,
        }
        return render(request, 'search.html', context)
