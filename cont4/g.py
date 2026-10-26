
import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    if n == 0:
        print(0)
        return

    seen = set()
    vals = []
    for i in range(1, n + 1):
        v = int(input_data[i])
        if v not in seen:
            seen.add(v)
            vals.append(v)

    n = len(vals)
    if n == 0:
        print(0)
        return

    left = [-1] * n
    right = [-1] * n
    depths = [0] * n  

    sorted_nodes = [(vals[0], 0)]

    for i in range(1, n):
        val = vals[i]
        idx = bisect_left(sorted_nodes, (val, i))
        
        parent_idx = -1
        
        if idx == 0:
            parent_idx = sorted_nodes[0][1]
        elif idx == len(sorted_nodes):
            parent_idx = sorted_nodes[-1][1]
        else:
            left_cand = sorted_nodes[idx - 1][1]
            right_cand = sorted_nodes[idx][1]
            if depths[left_cand] >= depths[right_cand]:
                parent_idx = left_cand
            else:
                parent_idx = right_cand

        depths[i] = depths[parent_idx] + 1
        if val < vals[parent_idx]:
            left[parent_idx] = i
        else:
            right[parent_idx] = i

        sorted_nodes.insert(idx, (val, i))

    order = []
    st = [0]
    while st:
        curr = st.pop()
        order.append(curr)
        if left[curr] != -1:
            st.append(left[curr])
        if right[curr] != -1:
            st.append(right[curr])

    heights = [0] * n
    max_path = 0

    for i in reversed(order):
        lh = heights[left[i]] if left[i] != -1 else 0
        rh = heights[right[i]] if right[i] != -1 else 0

        path = lh + rh + 1
        if path > max_path:
            max_path = path

        heights[i] = 1 + (lh if lh > rh else rh)

    print(max_path)

if __name__ == '__main__':
    solve()