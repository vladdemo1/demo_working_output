"""
This module for some logic about search and other
"""
from typing import List
from .models import Worker
from .support import POSITIONS_TUPLE


class Search:
    """
    This class can help search worker by pattern in current names or else
    """

    @staticmethod
    def get_first_worker_by_position(position: str) -> Worker:
        """
        Get first worker by keyword position via search
        """
        return Worker.objects.get(position=position)

    @staticmethod
    def get_subordinates_by_worker(worker: Worker) -> List[Worker]:
        """
        Get all workers-subordinates in current worker
        """
        return Worker.objects.filter(boss=worker)
