#!/usr/bin/env python

from utils import utils
import networkx as nx


def create_graph(data):
    G = nx.DiGraph()
    for line in data:
        if line:
            line_parts = line.split()
            G.add_edge(line_parts[1], line_parts[7])
    starting_nodes = list((node for node in G if G.in_degree(node) == 0))
    return G, starting_nodes


def find_order(G, starting_nodes):
    order = []
    visited = set()
    to_visit = starting_nodes
    skip = 0

    while len(to_visit) != 0:
        to_visit = sorted(list(set(to_visit)))
        i = skip
        node = to_visit[i]

        if node in visited:
            del to_visit[i]
            skip -= 1
            continue

        elif set(G.predecessors(node)).issubset(visited):
            order.append(node)
            visited.add(node)
            del to_visit[i]
            to_visit.extend(list(G.successors(node)))
            skip = 0

        else:
            skip += 1

    return order


def time_task(c):
    return 60 + ord(c) - ord("A") + 1


def part_two(G):
    # How much time is left for specific worker to do
    task_times = []
    # Tasks (nodes) currently worked on
    tasks = []
    # Complete time to finish: return
    overall_time = 0

    # Iterate while tasks have to be done
    while task_times or G:
        # Available tasks are not done yet (removed) and all pre-tasks are
        # done
        available_tasks = [t for t in G if t not in tasks and G.in_degree(t) == 0]

        # Set task for a free worker
        if available_tasks and len(task_times) < 5:
            task = min(available_tasks)  # min: alphabetically first
            task_times.append(time_task(task))
            tasks.append(task)

        # Calculate next task(s) to be done, remove and free worker(s)
        # Add time to overall time
        else:
            min_time = min(task_times)
            completed = [
                tasks[i] for i, time in enumerate(task_times) if time == min_time
            ]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            overall_time += min_time
            G.remove_nodes_from(completed)
    return overall_time


def main():
    data = utils.get_input(7).split("\n")
    G, starting_node = create_graph(data)
    # Very short and via networkX algorithm only:
    # ''.join(nx.lexicographical_topological_sort(G)))
    order = find_order(G, starting_node)
    order_str = "".join(order)
    print(f"Part 1: {order_str}")

    print(f"Part 2: {part_two(G)}")


if __name__ == "__main__":
    main()
