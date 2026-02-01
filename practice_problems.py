"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    """
    Data Structure Choice: Set
    Justification: A set is ideal because it stores only unique values and provides O(1) average time complexity
    for insert and lookup operations. We iterate through the list and check if a value is already in the set.
    """
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
"""

class TaskQueue:
    """
    Data Structure Choice: Queue (collections.deque)
    Justification: A queue is appropriate because tasks must be processed in FIFO order. Using deque allows
    O(1) time complexity for adding to the end and removing from the front.
    """
    def __init__(self):
        from collections import deque
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if not self.queue:
            return None
        return self.queue.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.
"""

class UniqueTracker:
    """
    Data Structure Choice: Set
    Justification: A set automatically handles uniqueness and allows O(1) average time complexity for insertion and size retrieval.
    This makes it efficient for tracking distinct values in a stream.
    """
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)
