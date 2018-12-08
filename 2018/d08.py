#!/usr/bin/env python

from utils import utils


MIN_NODE_SIZE = 2


def get_node(data, idx):
    child_nodes_amount = data[idx]
    metadata_entries = data[idx + 1]
    skip_for_meta = 0
    meta_sum = 0
    child_idx = idx + MIN_NODE_SIZE

    for _ in range(child_nodes_amount):
        skip, meta_sum_child = get_node(data, child_idx)
        meta_sum += meta_sum_child
        child_idx += skip
        skip_for_meta += skip

    for i in range(metadata_entries):
        meta_sum += data[idx + MIN_NODE_SIZE + skip_for_meta + i]

    length = MIN_NODE_SIZE + skip_for_meta + metadata_entries
    return length, meta_sum


def get_node_2(data, idx):
    child_nodes_amount = data[idx]
    metadata_entries = data[idx + 1]
    skip_for_meta = 0
    meta_sum = 0
    meta_sums_child = []
    child_idx = idx + MIN_NODE_SIZE

    for _ in range(child_nodes_amount):
        skip, meta_sum_child = get_node_2(data, child_idx)
        meta_sums_child.append(meta_sum_child)
        child_idx += skip
        skip_for_meta += skip

    meta_data_range = idx + MIN_NODE_SIZE + skip_for_meta
    if not child_nodes_amount:
        meta_sum = sum(data[meta_data_range : meta_data_range + metadata_entries])
    else:
        refs = data[meta_data_range : meta_data_range + metadata_entries]
        for ref in refs:
            if not ref or ref > len(meta_sums_child):
                continue
            meta_sum += meta_sums_child[ref - 1]

    length = MIN_NODE_SIZE + skip_for_meta + metadata_entries
    return length, meta_sum


def main():
    data = utils.get_input(8)

    # Test inputs
    # Should give 138 for a) and 66 for b)
    # data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

    # Should give 23 for a) and 10 for b)
    # data = "3 3 1 1 1 1 0 1 5 1 1 0 0 1 1 0 0 1 1 13 1"

    data = [int(x) for x in data.split()]

    length, meta_sum = get_node(data, 0)
    print(f"Part 1: {meta_sum}")

    length, meta_sum = get_node_2(data, 0)
    print(f"Part 2: {meta_sum}")


if __name__ == "__main__":
    main()
