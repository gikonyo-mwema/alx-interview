#!/usr/bin/python3
""" Lockboxes challenge """


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing locked boxes.
            Each inner list contains keys that can open other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Initialize a list to track visited boxes
    visited[0] = True  # Mark the first box (index 0) as visited
    queue = [0]  # Initialize a queue with the first box

    while queue:
        current_box = queue.pop(0)  # Get the front element from the queue
        for key in boxes[current_box]:
            if 0 <= key < n:  # Check if the key is within valid range

                if not visited[key]:  # If the box is unvisited
                    visited[key] = True  # Mark the box as unvisited
                    queue.append(key)  # Add the key to the queue

    return all(visited)  # Return True if all boxes are visited, else False
