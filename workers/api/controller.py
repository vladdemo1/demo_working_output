"""
This module for some logic about search and other
"""
from random import choice

from typing import List
from .models import Worker
from .support import POSITIONS_SHORT


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
    
    @staticmethod
    def get_random_worker_by_position(position: str) -> Worker:
        """
        Get random worker by position
        """
        workers_by_position = Worker.objects.filter(position=position)

        return choice(workers_by_position) 



class Positions:
    """
    Support class for get info from positions
    """

    @staticmethod
    def get_positions_slugs() -> tuple:
        """
        Get short names positions for slug
        """
        return (key for key in POSITIONS_SHORT.keys())
    
    @staticmethod
    def get_position_by_slug(slug: str) -> str:
        """
        Get normal name position by slug
        """
        return POSITIONS_SHORT[slug] if slug in POSITIONS_SHORT.keys() else False
    
    @staticmethod
    def get_positions_dict() -> dict:
        """
        Get positions dict
        """
        return POSITIONS_SHORT
