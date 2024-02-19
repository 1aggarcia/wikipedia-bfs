from typing import Callable, TypeVar, Generic

T = Generic[TypeVar("T")]
LOOP_LIMIT = 100


def breadth_first_search(start: T, target: T, children_fn: Callable[[T], list[T]]):
    """
    Find and return the shortest route from the `start` to the `target` nodes,
    where `children_fn` is a function to get a list of children nodes
    for any node of type T
    """

    # List of nodes in each layer of the BFS tree
    layers = [[start]]

    # Table that maps nodes to their origin node,
    # like a simplified adjaceny list
    # Used to backtrack the route from the end to the start
    origin_table: dict[T, T] = { start: None }

    found = False
    i = 0

    # search through every layer possible
    while not found and i < LOOP_LIMIT:
        print(f"Searching depth {i}...")
        print(f"- nodes parsed: {len(origin_table)}")
        children = []

        for node in layers[i]:
            # get all children nodes, filter out those we've already searched
            all_children = children_fn(node)
            children += [c for c in all_children if c not in origin_table]

            for child in children:
                # record the parent node of this child
                origin_table[child] = node

                if child == target:
                    found = True
                    print(f"Found: '{target}' in '{node}'")
                    break

            if found:
                break

        layers.append(children)
        i += 1

    if not found:
        raise OverflowError("Loop limit exceeded")

    # backtrack the origin table to find the shortest route
    route = [target]
    step_node = target

    while step_node != start:
        origin = origin_table[step_node]
        route.insert(0, origin)

        step_node = origin

    return route
