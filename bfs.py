from typing import Callable, TypeVar, Generic

T = Generic[TypeVar("T")]
LOOP_LIMIT = 10


def breadth_first_search(start: T, end: T, children_fn: Callable[[T], list[T]]):
    """
    Find and return the shortest route from the `start` to the `end` nodes,
    where `children_fn` is a function to get a list of children nodes
    for any node of type T
    """

    # List of nodes in each layer of the BFS tree
    layers = [[start]]

    # Table mapping nodes to their origin node,
    # like a simplified adjaceny list
    # Used to backtrack the route from the end to the start
    origin_table: dict[T, T] = { start: None }

    found = False
    i = 0

    # loop over each layer
    while not found and i < LOOP_LIMIT:
        print(f"Searching depth {i}...")
        children = []

        for node in layers[i]:
            # check all children to see if the target is inside
            children += children_fn(node)

            for child in children:
                # add origin node to the table if one hasn't been recorded yet
                if child not in origin_table:
                    origin_table[child] = node

                if child == end:
                    found = True
                    print(f"Found: '{end}' in '{node}'")
                    break

            if found:
                break

        layers.append(children)
        i += 1

    # backtrack the origin table to find the shortest route
    route = [end]
    step_node = end

    while step_node != start:
        origin = origin_table[step_node]
        route.insert(0, origin)

        step_node = origin

    return route
