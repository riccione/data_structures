"""
Indexed Binary Priority Queue

Inspired by William Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""
from min_indexed_d_heap import MinIndexedDHeap


class MinIndexedBinaryHeap(MinIndexedDHeap):
    def __init__(self, max_size: int):
        super().__init__(2, max_size)
