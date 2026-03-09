"""
Management command: python manage.py seed_snippets

Populates the database with sample Python DSA categories and code snippets.
Safe to run multiple times – existing entries (matched by title) are skipped.
"""

from django.core.management.base import BaseCommand

from typing_practice.models import Category, CodeSnippet

# ---------------------------------------------------------------------------
# Seed data
# ---------------------------------------------------------------------------

SNIPPETS = [
    # ── Sorting ────────────────────────────────────────────────────────────
    {
        "category": "Sorting",
        "title": "Bubble Sort",
        "difficulty": "Easy",
        "code": """\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted:", bubble_sort(data))
""",
    },
    {
        "category": "Sorting",
        "title": "Merge Sort",
        "difficulty": "Medium",
        "code": """\
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted:", merge_sort(data))
""",
    },
    {
        "category": "Sorting",
        "title": "Quick Sort",
        "difficulty": "Medium",
        "code": """\
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", quick_sort(data))
""",
    },
    # ── Searching ──────────────────────────────────────────────────────────
    {
        "category": "Searching",
        "title": "Binary Search",
        "difficulty": "Easy",
        "code": """\
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    nums = [2, 3, 4, 10, 40]
    target = 10
    idx = binary_search(nums, target)
    print(f"Element {target} found at index {idx}" if idx != -1 else "Not found")
""",
    },
    {
        "category": "Searching",
        "title": "Linear Search",
        "difficulty": "Easy",
        "code": """\
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    nums = [5, 3, 8, 1, 9, 2]
    target = 8
    result = linear_search(nums, target)
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in list")
""",
    },
    # ── Dynamic Programming ────────────────────────────────────────────────
    {
        "category": "Dynamic Programming",
        "title": "Fibonacci (Memoization)",
        "difficulty": "Easy",
        "code": """\
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "0/1 Knapsack",
        "difficulty": "Hard",
        "code": """\
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(dp[i][w], include)

    return dp[n][capacity]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print("Max value:", knapsack(weights, values, capacity))
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "Longest Common Subsequence",
        "difficulty": "Medium",
        "code": """\
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    a = "ABCBDAB"
    b = "BDCABA"
    print(f"LCS length of '{a}' and '{b}':", lcs(a, b))
""",
    },
    # ── Trees ──────────────────────────────────────────────────────────────
    {
        "category": "Trees",
        "title": "Binary Search Tree – Insert & Search",
        "difficulty": "Medium",
        "code": """\
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(val)
    node = bst.search(4)
    print("Found:", node.value if node else "Not found")
""",
    },
    # ── Graphs ─────────────────────────────────────────────────────────────
    {
        "category": "Graphs",
        "title": "BFS Traversal",
        "difficulty": "Medium",
        "code": """\
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }
    print("BFS order:", bfs(graph, 0))
""",
    },
    {
        "category": "Graphs",
        "title": "DFS Traversal",
        "difficulty": "Medium",
        "code": """\
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }
    print("DFS order:", dfs(graph, 0))
""",
    },
    # ── Arrays ─────────────────────────────────────────────────────────────
    {
        "category": "Arrays",
        "title": "Two Sum",
        "difficulty": "Easy",
        "code": """\
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Indices:", two_sum(nums, target))
""",
    },
    {
        "category": "Arrays",
        "title": "Maximum Subarray (Kadane's Algorithm)",
        "difficulty": "Medium",
        "code": """\
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end + 1]


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    value, subarray = max_subarray(nums)
    print(f"Max sum: {value}, Subarray: {subarray}")
""",
    },
    # ── Linked Lists ───────────────────────────────────────────────────────
    {
        "category": "Linked Lists",
        "title": "Reverse a Linked List",
        "difficulty": "Easy",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_list(head)
    print("Reversed:", list_to_array(reversed_head))
""",
    },
    # ── Stacks & Queues ────────────────────────────────────────────────────
    {
        "category": "Stacks & Queues",
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "code": """\
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for t in tests:
        print(f"is_valid('{t}') = {is_valid(t)}")
""",
    },
    # ── Recursion ──────────────────────────────────────────────────────────
    {
        "category": "Recursion",
        "title": "Tower of Hanoi",
        "difficulty": "Medium",
        "code": """\
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    n = 3
    print(f"Solving Tower of Hanoi with {n} disks:")
    hanoi(n, "A", "C", "B")
""",
    },

    # ── DSA Patterns ───────────────────────────────────────────────────────

    # ── Sliding Window ────────────────────────────────────────────────────
    {
        "category": "Sliding Window",
        "title": "Maximum Sum Subarray of Size K",
        "difficulty": "Easy",
        "code": """\
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum += arr[i + k] - arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print("Max sum:", max_sum_subarray(arr, k))
""",
    },
    {
        "category": "Sliding Window",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "code": """\
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    tests = ["abcabcbb", "bbbbb", "pwwkew"]
    for t in tests:
        print(f"'{t}' -> {length_of_longest_substring(t)}")
""",
    },
    {
        "category": "Sliding Window",
        "title": "Minimum Window Substring",
        "difficulty": "Hard",
        "code": """\
from collections import Counter


def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    best = ""
    left = 0

    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            window = s[left:right + 1]
            if not best or len(window) < len(best):
                best = window
            need[s[left]] += 1
            missing += 1
            left += 1

    return best


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))
""",
    },

    # ── Two Pointers ──────────────────────────────────────────────────────
    {
        "category": "Two Pointers",
        "title": "Three Sum",
        "difficulty": "Medium",
        "code": """\
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
""",
    },
    {
        "category": "Two Pointers",
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "code": """\
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        water = width * min(height[left], height[right])
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    print("Max area:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
""",
    },
    {
        "category": "Two Pointers",
        "title": "Trapping Rain Water",
        "difficulty": "Hard",
        "code": """\
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


if __name__ == "__main__":
    print("Water trapped:", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
""",
    },

    # ── Fast & Slow Pointers ──────────────────────────────────────────────
    {
        "category": "Fast & Slow Pointers",
        "title": "Linked List Cycle Detection",
        "difficulty": "Easy",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def make_cycle(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    print("Has cycle:", has_cycle(make_cycle([3, 2, 0, -4], 1)))
    print("Has cycle:", has_cycle(make_cycle([1, 2], -1)))
""",
    },
    {
        "category": "Fast & Slow Pointers",
        "title": "Find Middle of Linked List",
        "difficulty": "Easy",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print("Middle:", find_middle(head).val)

    head = build_list([1, 2, 3, 4, 5, 6])
    print("Middle:", find_middle(head).val)
""",
    },

    # ── Merge Intervals ───────────────────────────────────────────────────
    {
        "category": "Merge Intervals",
        "title": "Merge Overlapping Intervals",
        "difficulty": "Medium",
        "code": """\
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
""",
    },
    {
        "category": "Merge Intervals",
        "title": "Insert Interval",
        "difficulty": "Medium",
        "code": """\
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    print(insert_interval([[1, 3], [6, 9]], [2, 5]))
    print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
""",
    },

    # ── Monotonic Stack ───────────────────────────────────────────────────
    {
        "category": "Monotonic Stack",
        "title": "Next Greater Element",
        "difficulty": "Medium",
        "code": """\
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result


if __name__ == "__main__":
    print(next_greater_element([2, 1, 2, 4, 3]))
    print(next_greater_element([1, 3, 2, 4]))
""",
    },
    {
        "category": "Monotonic Stack",
        "title": "Largest Rectangle in Histogram",
        "difficulty": "Hard",
        "code": """\
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights = heights + [0]

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    return max_area


if __name__ == "__main__":
    print("Max area:", largest_rectangle([2, 1, 5, 6, 2, 3]))
    print("Max area:", largest_rectangle([2, 4]))
""",
    },

    # ── Backtracking ──────────────────────────────────────────────────────
    {
        "category": "Backtracking",
        "title": "Subsets",
        "difficulty": "Medium",
        "code": """\
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
""",
    },
    {
        "category": "Backtracking",
        "title": "Permutations",
        "difficulty": "Medium",
        "code": """\
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i + 1:])
            current.pop()

    backtrack([], nums)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
""",
    },
    {
        "category": "Backtracking",
        "title": "N-Queens",
        "difficulty": "Hard",
        "code": """\
def solve_n_queens(n):
    solutions = []
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row, board):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = "Q"
            backtrack(row + 1, board)
            board[row][col] = "."
            cols.discard(col)
            diag1.discard(row - col)
            diag2.discard(row + col)

    empty_board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, empty_board)
    return solutions


if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print(f"{len(solutions)} solutions for N=4")
    for sol in solutions:
        for row in sol:
            print(row)
        print()
""",
    },

    # ── Binary Search Variants ────────────────────────────────────────────
    {
        "category": "Binary Search Variants",
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "code": """\
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
""",
    },
    {
        "category": "Binary Search Variants",
        "title": "Find First and Last Position",
        "difficulty": "Medium",
        "code": """\
def search_range(nums, target):
    def find_bound(is_first):
        lo, hi, bound = 0, len(nums) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10], 8))
    print(search_range([5, 7, 7, 8, 8, 10], 6))
""",
    },
    {
        "category": "Binary Search Variants",
        "title": "Find Peak Element",
        "difficulty": "Medium",
        "code": """\
def find_peak(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    print("Peak index:", find_peak([1, 2, 3, 1]))
    print("Peak index:", find_peak([1, 2, 1, 3, 5, 6, 4]))
""",
    },

    # ── Top K Elements ────────────────────────────────────────────────────
    {
        "category": "Top K Elements",
        "title": "K Largest Elements (Min-Heap)",
        "difficulty": "Medium",
        "code": """\
import heapq


def k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)


if __name__ == "__main__":
    print(k_largest([3, 1, 5, 12, 2, 11], k=3))
    print(k_largest([5, 4, 8, 2, 7], k=2))
""",
    },
    {
        "category": "Top K Elements",
        "title": "K Most Frequent Elements",
        "difficulty": "Medium",
        "code": """\
import heapq
from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], k=2))
    print(top_k_frequent([1], k=1))
""",
    },

    # ── Prefix Sum ────────────────────────────────────────────────────────
    {
        "category": "Prefix Sum",
        "title": "Subarray Sum Equals K",
        "difficulty": "Medium",
        "code": """\
from collections import defaultdict


def subarray_sum(nums, k):
    count = 0
    prefix = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        prefix += num
        count += freq[prefix - k]
        freq[prefix] += 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))
    print(subarray_sum([1, 2, 3], 3))
""",
    },
    {
        "category": "Prefix Sum",
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "code": """\
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, 3]))
""",
    },

    # ── Trie ──────────────────────────────────────────────────────────────
    {
        "category": "Trie",
        "title": "Implement Trie (Prefix Tree)",
        "difficulty": "Medium",
        "code": """\
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    for word in ["apple", "app", "application"]:
        trie.insert(word)
    print(trie.search("app"))
    print(trie.search("ap"))
    print(trie.starts_with("appl"))
""",
    },

    # ── Union Find ────────────────────────────────────────────────────────
    {
        "category": "Union Find",
        "title": "Union Find (Disjoint Set Union)",
        "difficulty": "Medium",
        "code": """\
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("0-2 connected:", uf.connected(0, 2))
    print("0-3 connected:", uf.connected(0, 3))
""",
    },
    {
        "category": "Union Find",
        "title": "Number of Connected Components",
        "difficulty": "Medium",
        "code": """\
def count_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return 0
        parent[px] = py
        return 1

    return n - sum(union(u, v) for u, v in edges)


if __name__ == "__main__":
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))
    print(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
""",
    },

    # ── Topological Sort ──────────────────────────────────────────────────
    {
        "category": "Topological Sort",
        "title": "Course Schedule (Kahn's Algorithm)",
        "difficulty": "Medium",
        "code": """\
from collections import deque


def can_finish(num_courses, prerequisites):
    in_degree = [0] * num_courses
    graph = [[] for _ in range(num_courses)]

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    completed = 0

    while queue:
        node = queue.popleft()
        completed += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
""",
    },
    {
        "category": "Topological Sort",
        "title": "Topological Order (DFS)",
        "difficulty": "Medium",
        "code": """\
def topo_sort(num_nodes, edges):
    graph = [[] for _ in range(num_nodes)]
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    order = []
    has_cycle = [False]

    def dfs(node):
        if has_cycle[0]:
            return
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                has_cycle[0] = True
                return
            if color[neighbor] == WHITE:
                dfs(neighbor)
        color[node] = BLACK
        order.append(node)

    for i in range(num_nodes):
        if color[i] == WHITE:
            dfs(i)

    if has_cycle[0]:
        return []
    return order[::-1]


if __name__ == "__main__":
    print(topo_sort(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]))
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  PYTHON DATA STRUCTURES – canonical implementations                ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── Arrays ────────────────────────────────────────────────────────────
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Dynamic Array (Python list internals)",
        "difficulty": "Easy",
        "code": """\
# Python's list is a dynamic array.
# Amortised O(1) append; O(n) insert/delete at arbitrary index.

arr = []
for i in range(5):
    arr.append(i)          # O(1) amortised
    print(f"len={len(arr)} cap~={arr.__sizeof__()}")

# Prefix max in O(n)
nums = [3, 1, 4, 1, 5, 9, 2, 6]
prefix_max = []
running = float('-inf')
for n in nums:
    running = max(running, n)
    prefix_max.append(running)

print("Prefix max:", prefix_max)
""",
    },
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Two Sum — Brute O(n²) → Hash O(n)",
        "difficulty": "Easy",
        "code": """\
# ── Brute force O(n²) ────────────────────────────────────────
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ── Optimised O(n) with hash map ─────────────────────────────
def two_sum(nums, target):
    seen = {}                        # value → index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


nums = [2, 7, 11, 15]
print("Brute :", two_sum_brute(nums, 9))
print("Hash  :", two_sum(nums, 9))
# Time: O(n)   Space: O(n)
""",
    },
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "code": """\
# Single-pass O(n) — track min price seen so far
def max_profit(prices):
    min_price = float('inf')
    max_p = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_p:
            max_p = price - min_price
    return max_p


print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
print(max_profit([7, 6, 4, 3, 1]))       # 0
# Time: O(n)   Space: O(1)
""",
    },
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Rotate Array In-Place",
        "difficulty": "Medium",
        "code": """\
# Reverse three times — O(n) time, O(1) space
def rotate(nums, k):
    n = len(nums)
    k %= n

    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)   # [5, 6, 7, 1, 2, 3, 4]
# Time: O(n)   Space: O(1)
""",
    },

    # ── Strings ───────────────────────────────────────────────────────────
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Valid Anagram — Sort vs Hash",
        "difficulty": "Easy",
        "code": """\
from collections import Counter


# Sort approach O(n log n)
def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)


# Hash approach O(n)
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# Manual hash for learning
def is_anagram_manual(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for a, b in zip(s, t):
        count[ord(a) - ord('a')] += 1
        count[ord(b) - ord('a')] -= 1
    return all(c == 0 for c in count)


print(is_anagram("anagram", "nagaram"))   # True
print(is_anagram("rat",     "car"))       # False
# Time: O(n)   Space: O(1) — fixed 26 chars
""",
    },
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "code": """\
from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))      # or tuple(count array)
        groups[key].append(s)
    return list(groups.values())


# O(n) keys using 26-char count tuple (no sort)
def group_anagrams_linear(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Time: O(n * k)  Space: O(n * k)  where k = avg string length
""",
    },
    {
        "category": "Big-O + Arrays + Strings",
        "title": "Encode / Decode Strings",
        "difficulty": "Medium",
        "code": """\
# Length-prefix encoding — handles any characters including delimiters
def encode(strs):
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        result.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return result


original = ["hello", "world", "#test", "12#edge"]
encoded  = encode(original)
decoded  = decode(encoded)
print("Encoded:", encoded)
print("Match  :", original == decoded)
# Time: O(n)   Space: O(n)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  LINKED LISTS + TWO POINTERS                                       ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Linked Lists + Two Pointers",
        "title": "Linked List Node & Utilities",
        "difficulty": "Easy",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

    def __repr__(self):
        vals, node = [], self
        while node:
            vals.append(str(node.val))
            node = node.next
        return " -> ".join(vals)


def build(values):
    dummy = ListNode(0)
    cur   = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    vals, node = [], head
    while node:
        vals.append(node.val)
        node = node.next
    return vals


head = build([1, 2, 3, 4, 5])
print(head)
print(to_list(head))
""",
    },
    {
        "category": "Linked Lists + Two Pointers",
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next


# Iterative — O(n + m) time, O(1) space
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    cur   = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


def build(vals):
    d = ListNode(); c = d
    for v in vals: c.next = ListNode(v); c = c.next
    return d.next

def to_list(h):
    r = []
    while h: r.append(h.val); h = h.next
    return r


a = build([1, 2, 4])
b = build([1, 3, 4])
print(to_list(merge_two_lists(a, b)))   # [1,1,2,3,4,4]
""",
    },
    {
        "category": "Linked Lists + Two Pointers",
        "title": "Remove Nth Node From End",
        "difficulty": "Medium",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next


# Two-pointer one-pass — O(n) time, O(1) space
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n + 1):       # advance fast by n+1
        fast = fast.next

    while fast:                  # move both until fast hits end
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next   # unlink target
    return dummy.next


def build(vals):
    d = ListNode(); c = d
    for v in vals: c.next = ListNode(v); c = c.next
    return d.next

def to_list(h):
    r = []
    while h: r.append(h.val); h = h.next
    return r


print(to_list(remove_nth_from_end(build([1,2,3,4,5]), 2)))  # [1,2,3,5]
# Time: O(n)   Space: O(1)
""",
    },
    {
        "category": "Linked Lists + Two Pointers",
        "title": "Reorder List (L0→Ln→L1→Ln-1…)",
        "difficulty": "Medium",
        "code": """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next


def reorder_list(head):
    # 1. Find middle (slow/fast)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 3. Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next  = second
        second.next = tmp1
        first  = tmp1
        second = tmp2


def build(v):
    d=ListNode();c=d
    for x in v: c.next=ListNode(x);c=c.next
    return d.next

def to_list(h):
    r=[]
    while h: r.append(h.val);h=h.next
    return r


head = build([1, 2, 3, 4, 5])
reorder_list(head)
print(to_list(head))   # [1, 5, 2, 4, 3]
# Time: O(n)   Space: O(1)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  STACKS + QUEUES + SLIDING WINDOW                                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Stacks + Queues + Sliding Window",
        "title": "Stack: Min Stack O(1) getMin",
        "difficulty": "Easy",
        "code": """\
class MinStack:
    \"\"\"Push, pop, top, and getMin all in O(1).\"\"\"

    def __init__(self):
        self.stack     = []   # (val, current_min) pairs
        self.min_stack = []

    def push(self, val):
        cur_min = min(val, self.min_stack[-1]) if self.min_stack else val
        self.stack.append(val)
        self.min_stack.append(cur_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


ms = MinStack()
for v in [5, 3, 7, 2, 8]:
    ms.push(v)
    print(f"push({v})  top={ms.top()}  min={ms.getMin()}")
ms.pop()
print(f"after pop  min={ms.getMin()}")
""",
    },
    {
        "category": "Stacks + Queues + Sliding Window",
        "title": "Queue using Two Stacks",
        "difficulty": "Easy",
        "code": """\
class MyQueue:
    \"\"\"FIFO queue implemented with two LIFO stacks.
    Amortised O(1) push and pop.
    \"\"\"

    def __init__(self):
        self.inbox  = []   # for push
        self.outbox = []   # for pop / peek

    def push(self, x):
        self.inbox.append(x)

    def _transfer(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self):
        self._transfer()
        return self.outbox.pop()

    def peek(self):
        self._transfer()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox


q = MyQueue()
for v in [1, 2, 3]:
    q.push(v)
print(q.peek())   # 1
print(q.pop())    # 1
print(q.pop())    # 2
""",
    },
    {
        "category": "Stacks + Queues + Sliding Window",
        "title": "Daily Temperatures (Monotonic Stack)",
        "difficulty": "Medium",
        "code": """\
# Brute O(n²): nested loop
def daily_temperatures_brute(temps):
    result = [0] * len(temps)
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            if temps[j] > temps[i]:
                result[i] = j - i
                break
    return result


# Optimised O(n): monotonic decreasing stack of indices
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack  = []                    # indices of unresolved days

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print("Brute:", daily_temperatures_brute(temps))
print("Stack:", daily_temperatures(temps))
# Time: O(n)   Space: O(n)
""",
    },
    {
        "category": "Stacks + Queues + Sliding Window",
        "title": "Sliding Window Maximum (Deque)",
        "difficulty": "Hard",
        "code": """\
from collections import deque


# Brute O(n*k)
def max_sliding_window_brute(nums, k):
    return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]


# Monotonic deque O(n)
def max_sliding_window(nums, k):
    result = []
    dq     = deque()           # stores indices; front = max

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Maintain decreasing order
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print("Brute:", max_sliding_window_brute(nums, 3))
print("Deque:", max_sliding_window(nums, 3))
# Time: O(n)   Space: O(k)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  HASH MAPS + SETS                                                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Hash Maps + Sets",
        "title": "Python dict / set Fundamentals",
        "difficulty": "Easy",
        "code": """\
from collections import defaultdict, Counter, OrderedDict

# defaultdict — avoid KeyError on first access
freq = defaultdict(int)
for ch in "abracadabra":
    freq[ch] += 1
print(dict(freq))

# Counter — built-in frequency map
c = Counter("mississippi")
print(c.most_common(3))

# Set operations — O(1) average lookup
seen = set()
nums = [1, 2, 3, 2, 4, 1, 5]
unique_in_order = []
for n in nums:
    if n not in seen:
        seen.add(n)
        unique_in_order.append(n)
print(unique_in_order)

# OrderedDict — LRU-style insertion-order guarantee
od = OrderedDict()
for i in range(3):
    od[i] = i * i
od.move_to_end(0)           # move key 0 to end
print(list(od.items()))
""",
    },
    {
        "category": "Hash Maps + Sets",
        "title": "LRU Cache (OrderedDict)",
        "difficulty": "Medium",
        "code": """\
from collections import OrderedDict


class LRUCache:
    \"\"\"O(1) get and put using OrderedDict.\"\"\"

    def __init__(self, capacity):
        self.cap   = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)        # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict least recently used


lru = LRUCache(2)
lru.put(1, 1); lru.put(2, 2)
print(lru.get(1))    # 1
lru.put(3, 3)        # evicts key 2
print(lru.get(2))    # -1 (evicted)
print(lru.get(3))    # 3
# Time: O(1) for get/put   Space: O(capacity)
""",
    },
    {
        "category": "Hash Maps + Sets",
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "code": """\
# Brute O(n log n): sort then scan
def longest_consecutive_sort(nums):
    if not nums:
        return 0
    nums = sorted(set(nums))
    best = curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            curr += 1
            best = max(best, curr)
        else:
            curr = 1
    return best


# Optimised O(n): set membership check
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:       # start of a sequence
            curr = 1
            while n + curr in num_set:
                curr += 1
            best = max(best, curr)
    return best


nums = [100, 4, 200, 1, 3, 2]
print("Sort :", longest_consecutive_sort(nums))   # 4
print("Set  :", longest_consecutive(nums))         # 4
# Time: O(n)   Space: O(n)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  TREES + BST + BFS/DFS                                             ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Trees + BST + BFS/DFS",
        "title": "Binary Tree Node & Traversals",
        "difficulty": "Easy",
        "code": """\
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def build(vals):
    \"\"\"Level-order build from list (None = missing node).\"\"\"
    if not vals:
        return None
    root = TreeNode(vals[0])
    q    = deque([root])
    i    = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


root = build([4, 2, 6, 1, 3, 5, 7])
print("In   :", inorder(root))    # [1,2,3,4,5,6,7]
print("Pre  :", preorder(root))
print("Post :", postorder(root))
""",
    },
    {
        "category": "Trees + BST + BFS/DFS",
        "title": "Level-Order BFS + Zigzag",
        "difficulty": "Medium",
        "code": """\
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right


def level_order(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result


def zigzag_level_order(root):
    if not root:
        return []
    result, q, left_to_right = [], deque([root]), True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return result


def b(v,l=None,r=None): return TreeNode(v,l,r)
root = b(3, b(9), b(20, b(15), b(7)))
print("BFS    :", level_order(root))
print("Zigzag :", zigzag_level_order(root))
""",
    },
    {
        "category": "Trees + BST + BFS/DFS",
        "title": "Maximum Depth & Diameter of Tree",
        "difficulty": "Easy",
        "code": """\
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def diameter(root):
    \"\"\"Longest path between any two nodes (edges, not nodes).\"\"\"
    best = [0]

    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        best[0] = max(best[0], lh + rh)
        return 1 + max(lh, rh)

    height(root)
    return best[0]


def b(v,l=None,r=None): return TreeNode(v,l,r)
root = b(1, b(2, b(4), b(5)), b(3))
print("Depth   :", max_depth(root))     # 3
print("Diameter:", diameter(root))      # 3
# Time: O(n)   Space: O(h) call-stack
""",
    },
    {
        "category": "Trees + BST + BFS/DFS",
        "title": "Validate BST",
        "difficulty": "Medium",
        "code": """\
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right


# Pass valid range down the recursion — O(n)
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left,  lo, root.val) and
            is_valid_bst(root.right, root.val, hi))


# Iterative inorder must be strictly increasing
def is_valid_bst_iter(root):
    stack, prev = [], float('-inf')
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        if cur.val <= prev:
            return False
        prev = cur.val
        cur  = cur.right
    return True


def b(v,l=None,r=None): return TreeNode(v,l,r)
print(is_valid_bst(b(5, b(3, b(1), b(4)), b(7))))   # False — 4 violates
print(is_valid_bst(b(5, b(3, b(1), b(4, b(3.5), None)), b(7))))  # True
""",
    },
    {
        "category": "Trees + BST + BFS/DFS",
        "title": "Lowest Common Ancestor (LCA)",
        "difficulty": "Medium",
        "code": """\
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right


# General binary tree LCA — O(n)
def lca(root, p, q):
    if not root or root is p or root is q:
        return root
    left  = lca(root.left,  p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root       # p in one subtree, q in the other
    return left or right  # both in same subtree


# BST LCA — O(h) using BST property
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None


def b(v,l=None,r=None): return TreeNode(v,l,r)
n3=b(3); n5=b(5); n1=b(1); n6=b(6); n2=b(2,n7:=b(7),n4:=b(4))
root = b(3, b(5,n6,n2), b(1,b(0),b(8)))
print("LCA:", lca(root, n6, n4).val)    # 5
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  HEAPS + TOP-K + TWO HEAPS                                         ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Heaps + Top-K + Two Heaps",
        "title": "Heap Fundamentals (heapq)",
        "difficulty": "Easy",
        "code": """\
import heapq

# Python only provides min-heap.
# For max-heap, negate values.

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Min-heap
min_heap = nums[:]
heapq.heapify(min_heap)               # O(n)
print("Min:", heapq.heappop(min_heap))  # 1

# Max-heap via negation
max_heap = [-n for n in nums]
heapq.heapify(max_heap)
print("Max:", -heapq.heappop(max_heap)) # 9

# nsmallest / nlargest  O(n log k)
print("3 smallest:", heapq.nsmallest(3, nums))
print("3 largest :", heapq.nlargest(3, nums))

# Push-pop in one op
h = [1, 3, 5]
heapq.heapify(h)
print(heapq.heappushpop(h, 4))   # returns min(4, heap_min)
""",
    },
    {
        "category": "Heaps + Top-K + Two Heaps",
        "title": "Kth Largest Element — Sort vs Heap vs Quickselect",
        "difficulty": "Medium",
        "code": """\
import heapq
import random


# O(n log n) sort
def kth_largest_sort(nums, k):
    return sorted(nums, reverse=True)[k - 1]


# O(n log k) min-heap of size k
def kth_largest_heap(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# O(n) average Quickselect (in-place partition)
def kth_largest_quickselect(nums, k):
    target = len(nums) - k

    def partition(lo, hi):
        pivot = nums[hi]
        p = lo
        for i in range(lo, hi):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[hi] = nums[hi], nums[p]
        return p

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        pi = partition(lo, hi)
        if pi == target: break
        elif pi < target: lo = pi + 1
        else: hi = pi - 1
    return nums[target]


nums = [3, 2, 1, 5, 6, 4]
print(kth_largest_sort(nums[:], 2))            # 5
print(kth_largest_heap(nums[:], 2))            # 5
print(kth_largest_quickselect(nums[:], 2))     # 5
""",
    },
    {
        "category": "Heaps + Top-K + Two Heaps",
        "title": "Find Median from Data Stream (Two Heaps)",
        "difficulty": "Hard",
        "code": """\
import heapq


class MedianFinder:
    \"\"\"
    Two heaps:
      small — max-heap (lower half)  stored as negated values
      large — min-heap (upper half)
    Invariant: len(small) == len(large) or len(small) == len(large)+1
    \"\"\"

    def __init__(self):
        self.small = []   # max-heap  (negated)
        self.large = []   # min-heap

    def add_num(self, num):
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance sizes: small may have at most 1 extra
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


mf = MedianFinder()
for n in [1, 2, 3, 4, 5]:
    mf.add_num(n)
    print(f"add {n}  median = {mf.find_median()}")
# Time: O(log n) per add   Space: O(n)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  GRAPHS + BFS/DFS/TOPO SORT                                        ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Graphs + BFS/DFS/Topo Sort",
        "title": "Graph Representations",
        "difficulty": "Easy",
        "code": """\
# Adjacency list — most common for sparse graphs
graph_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3],
}

# Build from edge list
edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]
adj = {}
for u, v in edges:
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

# Adjacency matrix — O(1) edge lookup, O(V²) space
n = 5
matrix = [[0]*n for _ in range(n)]
for u, v in edges:
    matrix[u][v] = matrix[v][u] = 1

print("Adj list:", adj)
print("Row 0   :", matrix[0])
# Choose list for BFS/DFS, matrix for dense graphs.
""",
    },
    {
        "category": "Graphs + BFS/DFS/Topo Sort",
        "title": "Number of Islands (BFS & DFS)",
        "difficulty": "Medium",
        "code": """\
from collections import deque


# DFS — recursive flood-fill O(m*n)
def num_islands_dfs(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '#'    # mark visited in-place
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


# BFS version
def num_islands_bfs(grid):
    rows, cols, count = len(grid), len(grid[0]), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                q = deque([(r, c)])
                grid[r][c] = '#'
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = cr+dr, cc+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                            grid[nr][nc]='#'
                            q.append((nr,nc))
    return count


g = [['1','1','0'],['0','1','0'],['0','0','1']]
print("Islands:", num_islands_dfs([r[:] for r in g]))   # 2
""",
    },
    {
        "category": "Graphs + BFS/DFS/Topo Sort",
        "title": "Clone Graph",
        "difficulty": "Medium",
        "code": """\
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val       = val
        self.neighbors = neighbors or []


def clone_graph(node):
    if not node:
        return None
    clones = {node: Node(node.val)}
    q      = deque([node])

    while q:
        cur = q.popleft()
        for nb in cur.neighbors:
            if nb not in clones:
                clones[nb] = Node(nb.val)
                q.append(nb)
            clones[cur].neighbors.append(clones[nb])

    return clones[node]


# Build a small graph: 1 -- 2 -- 3 -- 4 -- 1
n1=Node(1); n2=Node(2); n3=Node(3); n4=Node(4)
n1.neighbors=[n2,n4]; n2.neighbors=[n1,n3]
n3.neighbors=[n2,n4]; n4.neighbors=[n3,n1]

c1 = clone_graph(n1)
print("Clone val:", c1.val, "| neighbors:", [n.val for n in c1.neighbors])
# Time: O(V+E)   Space: O(V)
""",
    },
    {
        "category": "Graphs + BFS/DFS/Topo Sort",
        "title": "Pacific Atlantic Water Flow",
        "difficulty": "Medium",
        "code": """\
from collections import deque


def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

    def bfs(starts):
        visited = set(starts)
        q       = deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if (0<=nr<rows and 0<=nc<cols
                        and (nr,nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):
                    visited.add((nr,nc))
                    q.append((nr,nc))
        return visited

    pacific_starts = [(0,c) for c in range(cols)] + \
                     [(r,0) for r in range(rows)]
    atlantic_starts= [(rows-1,c) for c in range(cols)] + \
                     [(r,cols-1) for r in range(rows)]

    return sorted(pacific_starts := bfs(pacific_starts) &
                  bfs(atlantic_starts))


h = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacific_atlantic(h))
# Time: O(m*n)   Space: O(m*n)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  BINARY SEARCH PATTERNS                                            ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Binary Search Patterns",
        "title": "Binary Search Template (3 variants)",
        "difficulty": "Easy",
        "code": """\
# ── Template 1: exact target ─────────────────────────────────
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2    # avoids overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ── Template 2: leftmost insertion point ─────────────────────
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ── Template 3: binary search on answer ─────────────────────
# "Minimum days to make m bouquets of k adjacent flowers"
def min_days(bloom, m, k):
    if m * k > len(bloom): return -1

    def feasible(day):
        bouquets = flowers = 0
        for b in bloom:
            flowers = flowers + 1 if b <= day else 0
            if flowers == k:
                bouquets += 1
                flowers = 0
        return bouquets >= m

    lo, hi = min(bloom), max(bloom)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid
        else: lo = mid + 1
    return lo


print(binary_search([1,2,3,4,5,6], 4))       # 3
print(lower_bound([1,3,3,5,7], 3))            # 1
print(min_days([1,10,3,10,2], m=3, k=1))      # 3
""",
    },
    {
        "category": "Binary Search Patterns",
        "title": "Sqrt(x) — Binary Search on Answer",
        "difficulty": "Easy",
        "code": """\
import math


# Newton's method O(log x) — fastest
def my_sqrt_newton(x):
    if x < 2:
        return x
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r


# Binary search O(log x)
def my_sqrt_bs(x):
    if x < 2:
        return x
    lo, hi = 1, x // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi    # floor


for n in [0, 1, 4, 8, 9, 16, 2147395600]:
    assert my_sqrt_bs(n) == int(math.isqrt(n))
    print(f"sqrt({n}) = {my_sqrt_bs(n)}")
""",
    },
    {
        "category": "Binary Search Patterns",
        "title": "Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "code": """\
def find_median_sorted_arrays(nums1, nums2):
    \"\"\"O(log(min(m,n))) binary search on partition point.\"\"\"
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A                  # ensure A is smaller

    total  = len(A) + len(B)
    half   = total // 2
    lo, hi = 0, len(A)

    while True:
        i = (lo + hi) // 2           # partition index in A
        j = half - i                 # partition index in B

        A_left  = A[i-1] if i > 0       else float('-inf')
        A_right = A[i]   if i < len(A)  else float('inf')
        B_left  = B[j-1] if j > 0       else float('-inf')
        B_right = B[j]   if j < len(B)  else float('inf')

        if A_left <= B_right and B_left <= A_right:
            if total % 2:
                return float(min(A_right, B_right))
            return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        elif A_left > B_right:
            hi = i - 1
        else:
            lo = i + 1


print(find_median_sorted_arrays([1,3], [2]))       # 2.0
print(find_median_sorted_arrays([1,2], [3,4]))     # 2.5
# Time: O(log(min(m,n)))   Space: O(1)
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  DYNAMIC PROGRAMMING — brute → memo → tabulation                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Dynamic Programming",
        "title": "Coin Change — Brute → Memo → DP",
        "difficulty": "Medium",
        "code": """\
import sys
from functools import lru_cache


coins  = [1, 5, 11]
amount = 15

# ── Brute recursion O(n^amount) ───────────────────────────────
def coin_change_brute(amount):
    if amount == 0: return 0
    if amount < 0:  return float('inf')
    return 1 + min(coin_change_brute(amount - c) for c in coins)


# ── Top-down memoization O(n*amount) ─────────────────────────
@lru_cache(maxsize=None)
def coin_change_memo(amount):
    if amount == 0: return 0
    if amount < 0:  return float('inf')
    return 1 + min(coin_change_memo(amount - c) for c in coins)


# ── Bottom-up tabulation O(n*amount) — best for interviews ───
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float('inf') else -1


print("Brute :", coin_change_brute(amount))
print("Memo  :", coin_change_memo(amount))
print("DP    :", coin_change_dp(coins, amount))
# All return 3  (11+3*1  or  5+5+5)
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "Longest Increasing Subsequence (LIS)",
        "difficulty": "Medium",
        "code": """\
import bisect


# O(n²) DP
def lis_dp(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# O(n log n) patience sorting with binary search
def lis_fast(nums):
    tails = []          # tails[i] = smallest tail of IS of length i+1
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails):
            tails.append(n)
        else:
            tails[pos] = n
    return len(tails)


seqs = [[10,9,2,5,3,7,101,18], [0,1,0,3,2,3], [7,7,7,7]]
for s in seqs:
    print(f"DP={lis_dp(s)}  Fast={lis_fast(s)}", s)
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "Unique Paths (Grid DP)",
        "difficulty": "Easy",
        "code": """\
import math


# O(m*n) 2D DP
def unique_paths_dp(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]


# O(n) space optimisation
def unique_paths_1d(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c-1]
    return dp[n-1]


# O(1) combinatorics: C(m+n-2, n-1)
def unique_paths_math(m, n):
    return math.comb(m + n - 2, n - 1)


for m, n in [(3,7), (3,2), (1,1)]:
    d = unique_paths_dp(m, n)
    o = unique_paths_1d(m, n)
    c = unique_paths_math(m, n)
    print(f"({m},{n}): DP={d}  1D={o}  Math={c}")
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "Word Break — Memo → BFS",
        "difficulty": "Medium",
        "code": """\
from collections import deque
from functools import lru_cache


# Top-down memoization
def word_break_memo(s, word_dict):
    words = set(word_dict)

    @lru_cache(maxsize=None)
    def dp(i):
        if i == len(s): return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in words and dp(j):
                return True
        return False

    return dp(0)


# BFS — think of each reachable index as a node
def word_break_bfs(s, word_dict):
    words   = set(word_dict)
    visited = set()
    q       = deque([0])

    while q:
        start = q.popleft()
        if start in visited:
            continue
        visited.add(start)
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in words:
                if end == len(s): return True
                q.append(end)
    return False


s    = "leetcode"
d    = ["leet", "code"]
print("Memo:", word_break_memo(s, d))    # True
print("BFS :", word_break_bfs(s, d))     # True
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  BACKTRACKING + REVISIONS                                          ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Backtracking + Revisions",
        "title": "Combination Sum (with & without duplicates)",
        "difficulty": "Medium",
        "code": """\
# Candidates: reuse allowed — Combination Sum I
def combination_sum(candidates, target):
    result = []

    def bt(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            bt(i, path, remaining - c)      # i, not i+1 (reuse allowed)
            path.pop()

    combination_sum(sorted(candidates), target)
    return result


# Candidates may have duplicates — Combination Sum II
def combination_sum_ii(candidates, target):
    result = []
    candidates.sort()

    def bt(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue                    # skip duplicates at same level
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            bt(i + 1, path, remaining - candidates[i])
            path.pop()

    bt(0, [], target)
    return result


print(combination_sum([2,3,6,7], 7))
print(combination_sum_ii([10,1,2,7,6,1,5], 8))
""",
    },
    {
        "category": "Backtracking + Revisions",
        "title": "Word Search in Grid",
        "difficulty": "Medium",
        "code": """\
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[i]:
            return False

        tmp = board[r][c]
        board[r][c] = '#'           # mark visited

        found = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or dfs(r,c-1,i+1))

        board[r][c] = tmp           # restore
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
print(exist([r[:] for r in board], "ABCCED"))   # True
print(exist([r[:] for r in board], "SEE"))       # True
print(exist([r[:] for r in board], "ABCB"))      # False
# Time: O(m*n*4^L)  Space: O(L) call stack
""",
    },
    {
        "category": "Backtracking + Revisions",
        "title": "Palindrome Partitioning",
        "difficulty": "Medium",
        "code": """\
def partition(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def bt(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                bt(end, path)
                path.pop()

    bt(0, [])
    return result


# Optimisation: pre-compute palindrome DP table
def partition_dp(s):
    n = len(s)
    is_pal = [[False]*n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or is_pal[i+1][j-1]):
                is_pal[i][j] = True

    result = []
    def bt(start, path):
        if start == n:
            result.append(path[:])
            return
        for end in range(start, n):
            if is_pal[start][end]:
                path.append(s[start:end+1])
                bt(end + 1, path)
                path.pop()
    bt(0, [])
    return result


print(partition("aab"))
print(partition_dp("aab"))
""",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  INTERVIEW REFERENCE — type these to internalise the patterns      ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    {
        "category": "Interview Reference",
        "title": "Big-O Complexity Cheat Sheet",
        "difficulty": "Easy",
        "code": """\
# ── Time Complexities ────────────────────────────────────────
# O(1)       Hash lookup, array index, stack push/pop
# O(log n)   Binary search, balanced BST ops, heap push/pop
# O(n)       Linear scan, BFS/DFS, sliding window
# O(n log n) Merge sort, heap sort, sorted()
# O(n^2)     Nested loops, bubble/insertion sort
# O(2^n)     Backtracking subsets, Fibonacci naive recursion
# O(n!)      Permutations, brute-force TSP

# ── Space Complexities ───────────────────────────────────────
# O(1)       Two pointers, in-place rotation
# O(n)       Hash map, recursion call stack (unbalanced tree)
# O(log n)   Recursive call stack on balanced tree / binary search
# O(n^2)     2D DP table, adjacency matrix

# ── Python built-in complexities ────────────────────────────
# list.append        O(1) amortised
# list.insert(i,v)   O(n)
# list.pop()         O(1)
# list.pop(0)        O(n)  — use collections.deque instead
# dict get/set       O(1) average, O(n) worst
# set in             O(1) average
# sorted(iterable)   O(n log n) — Timsort
# heapq.heappush     O(log n)

# ── Always state both ────────────────────────────────────────
# Time: O(?)   Space: O(?)
print("Know your complexities cold.")
""",
    },
    {
        "category": "Interview Reference",
        "title": "Interview Problem-Solving Framework",
        "difficulty": "Easy",
        "code": """\
# ═══════════════════════════════════════════════════════════════
# DURING THE INTERVIEW — step-by-step process
# ═══════════════════════════════════════════════════════════════

# 1. LISTEN carefully — every constraint is a hint
#    - Sorted array?  → Binary search
#    - Repeated elements? → Hash map / set
#    - k smallest/largest? → Heap
#    - Contiguous subarray? → Sliding window
#    - Tree / graph? → BFS (shortest) or DFS (path/cycle)

# 2. CLARIFY before coding
#    - What are the input ranges? Can it be empty/null?
#    - What should we return for edge cases?
#    - Is the input mutable?

# 3. THINK OUT LOUD — narrate every decision
#    "I'll start with brute-force to establish correctness,
#     then optimise the bottleneck."

# 4. START SIMPLE — brute force first
#    Correct > Fast. Then find the bottleneck and optimise.

# 5. CODE cleanly — use meaningful variable names

# 6. TEST before claiming done
#    - Happy path
#    - Edge cases (empty, single element, all same)
#    - Large input (mental big-O check)

# 7. STATE complexity at the end
#    "This runs in O(n log n) time and O(n) space."

print("Process beats raw knowledge. Practice the process.")
""",
    },
    {
        "category": "Interview Reference",
        "title": "Pattern Recognition Guide",
        "difficulty": "Easy",
        "code": """\
# ═══════════════════════════════════════════════════════════════
# PATTERN → TECHNIQUE MAP
# ═══════════════════════════════════════════════════════════════

PATTERNS = {
    "Top K elements / K closest":
        "Min-heap size K  — O(n log k)",

    "Contiguous subarray (sum/length)":
        "Sliding window or prefix sum  — O(n)",

    "Pair with target sum":
        "Hash map (complement lookup) or two-pointers on sorted  — O(n)",

    "Sorted array / search":
        "Binary search — O(log n)",

    "Linked list middle / cycle":
        "Fast & slow pointers — O(n) time, O(1) space",

    "Merge K sorted lists":
        "Min-heap of (val, list_index) — O(n log k)",

    "Shortest path (unweighted)":
        "BFS — O(V + E)",

    "Shortest path (weighted, non-negative)":
        "Dijkstra with min-heap — O((V+E) log V)",

    "Topological order / prerequisite check":
        "Kahn BFS (in-degree) or DFS post-order",

    "Optimisation / count / true-false on subproblems":
        "Dynamic programming — define state, transition, base case",

    "Generate all combinations / permutations":
        "Backtracking with pruning",

    "Prefix / suffix queries on array":
        "Prefix sum array — O(1) range query after O(n) build",
}

for pattern, technique in PATTERNS.items():
    print(f"  {pattern}")
    print(f"    → {technique}")
    print()
""",
    },
    {
        "category": "Interview Reference",
        "title": "Recommended Resources",
        "difficulty": "Easy",
        "code": """\
# ═══════════════════════════════════════════════════════════════
# RECOMMENDED RESOURCES
# ═══════════════════════════════════════════════════════════════

RESOURCES = [
    {
        "name":     "NeetCode 150",
        "url":      "https://neetcode.io",
        "best_for": "Curated 150 problems by pattern with video solutions",
    },
    {
        "name":     "LeetCode",
        "url":      "https://leetcode.com",
        "best_for": "Full problem bank, contests, company-specific lists",
    },
    {
        "name":     "HackerRank",
        "url":      "https://hackerrank.com",
        "best_for": "Structured learning tracks and certifications",
    },
    {
        "name":     "AlgoExpert",
        "url":      "https://algoexpert.io",
        "best_for": "High-quality video explanations for 160 problems",
    },
    {
        "name":     "Grokking the Coding Interview",
        "url":      "https://designgurus.io",
        "best_for": "Pattern-based learning — best for beginners",
    },
    {
        "name":     "CLRS (Introduction to Algorithms)",
        "url":      "https://mitpress.mit.edu/9780262046305",
        "best_for": "Deep algorithmic theory and proofs",
    },
    {
        "name":     "Python DSA (InstaCode)",
        "url":      "http://localhost:8000",
        "best_for": "Muscle-memory via typing practice for every pattern",
    },
]

col_w = 35
print(f"{'Resource':<{col_w}} Best For")
print("-" * 80)
for r in RESOURCES:
    print(f"{r['name']:<{col_w}} {r['best_for']}")
""",
    },

    # ── Greedy Algorithms ─────────────────────────────────────────────────
    {
        "category": "Greedy Algorithms",
        "title": "Activity Selection",
        "difficulty": "Medium",
        "code": """\
# Activity Selection — maximise non-overlapping intervals
# Greedy: sort by finish time, always pick the earliest-finishing activity

def activity_selection(activities):
    # activities = [(start, end), ...]
    activities.sort(key=lambda x: x[1])   # sort by end time (greedy choice)
    selected = [activities[0]]
    for start, end in activities[1:]:
        if start >= selected[-1][1]:       # no overlap with last selected
            selected.append((start, end))
    return selected


if __name__ == "__main__":
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
    print("Selected:", activity_selection(acts))
    # → [(1,4), (5,7), (8,11)]  — 3 activities, maximum possible
""",
    },
    {
        "category": "Greedy Algorithms",
        "title": "Coin Change (Greedy vs DP)",
        "difficulty": "Medium",
        "code": """\
# Coin Change — GREEDY works only for canonical coin systems (USD, EUR)
# For arbitrary coins always use DP

# --- Greedy (canonical coins only) ---
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count  += amount // coin
        amount %= coin
    return count if amount == 0 else -1


# --- DP (works for ANY coin system) ---
def coin_change_dp(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change_greedy([25, 10, 5, 1], 41))  # 4 coins (greedy OK)
    print(coin_change_dp([1, 5, 6, 9], 11))        # 2 coins (greedy fails: 9+1+1 vs 6+5)
""",
    },
    {
        "category": "Greedy Algorithms",
        "title": "Dijkstra's Shortest Path",
        "difficulty": "Hard",
        "code": """\
import heapq

# Dijkstra's Algorithm — single-source shortest path on weighted graph
# Greedy: always extend the currently cheapest frontier node
# Requires: non-negative edge weights
# Time: O((V + E) log V)  |  Space: O(V)

def dijkstra(graph, src):
    dist = {node: float("inf") for node in graph}
    dist[src] = 0
    heap = [(0, src)]    # (cumulative_distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue     # stale heap entry — skip
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("D", 3), ("C", 5)],
        "C": [("B", 1), ("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }
    print(dijkstra(graph, "A"))
    # → {'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 8}
""",
    },

    # ── Python Collections ────────────────────────────────────────────────
    {
        "category": "Python Collections",
        "title": "deque — O(1) Both Ends",
        "difficulty": "Easy",
        "code": """\
from collections import deque

# collections.deque — doubly-linked list backed, O(1) at BOTH ends
# Use instead of list when you need O(1) appendleft / popleft

dq = deque([1, 2, 3])

# Both-end operations — all O(1)
dq.append(4)          # right  → deque([1, 2, 3, 4])
dq.appendleft(0)      # left   → deque([0, 1, 2, 3, 4])
dq.pop()              # right  → 4  (deque([0, 1, 2, 3]))
dq.popleft()          # left   → 0  (deque([1, 2, 3]))

# Bounded queue (maxlen auto-evicts oldest)
window = deque(maxlen=3)
for val in [10, 20, 30, 40]:
    window.append(val)
print(window)         # deque([20, 30, 40], maxlen=3)

# BFS template
graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
queue = deque(["A"])
visited = {"A"}
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb)
            queue.append(nb)
print("BFS:", order)  # ['A', 'B', 'C', 'D']
""",
    },
    {
        "category": "Python Collections",
        "title": "defaultdict and Counter",
        "difficulty": "Easy",
        "code": """\
from collections import defaultdict, Counter

# defaultdict — dict that auto-creates missing keys
# Never raises KeyError for missing key — initialises with factory

# Group by first letter
words = ["apple", "ant", "banana", "avocado", "blueberry"]
groups = defaultdict(list)
for w in words:
    groups[w[0]].append(w)
print(dict(groups))
# {'a': ['apple','ant','avocado'], 'b': ['banana','blueberry']}

# Graph adjacency list
edges = [(1, 2), (1, 3), (2, 4)]
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)   # undirected

# Counter — frequency count in O(n)
text = "abracadabra"
c = Counter(text)
print(c)                         # Counter({'a':5,'b':2,'r':2,'c':1,'d':1})
print(c.most_common(2))          # [('a', 5), ('b', 2)]

# Counter arithmetic
c1 = Counter("aabb")
c2 = Counter("abcc")
print(c1 + c2)                   # Counter({'a':3,'b':3,'c':2})
print(c1 & c2)                   # intersection: min counts
""",
    },
    {
        "category": "Python Collections",
        "title": "heapq — Priority Queue Patterns",
        "difficulty": "Medium",
        "code": """\
import heapq

# Python's heapq is a MIN-heap
# For max-heap: negate values

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Build heap in O(n)
heapq.heapify(nums)
print(nums[0])                   # smallest = 1

# Push / pop — O(log n)
heapq.heappush(nums, 0)
print(heapq.heappop(nums))       # 0

# nlargest / nsmallest — O(n log k)
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(heapq.nlargest(3, data))   # [9, 6, 5]
print(heapq.nsmallest(3, data))  # [1, 1, 2]

# Heap with tuples — priority by first element
tasks = [(3, "low"), (1, "high"), (2, "medium")]
heapq.heapify(tasks)
priority, task = heapq.heappop(tasks)
print(task)                      # 'high'

# Top-K pattern
def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count, key=count.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
""",
    },

    # ── Sorting additions ─────────────────────────────────────────────────
    {
        "category": "Sorting",
        "title": "Insertion Sort",
        "difficulty": "Easy",
        "code": """\
# Insertion Sort — build sorted portion one element at a time
# Best: O(n) nearly-sorted  |  Average/Worst: O(n²)  |  Space: O(1)  |  Stable: True
# Excellent for small n or nearly-sorted data (Python's Timsort uses it for small runs)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # element to insert
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1
        arr[j + 1] = key          # insert in correct position
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted:", insertion_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
""",
    },
    {
        "category": "Sorting",
        "title": "Heap Sort",
        "difficulty": "Medium",
        "code": """\
# Heap Sort — build a max-heap, then repeatedly extract max
# Time: O(n log n) always  |  Space: O(1) in-place  |  Stable: No
# Key insight: heapify gives O(n) build, then n pops each O(log n)

def heap_sort(arr):
    n = len(arr)

    # Step 1 — Build max-heap (heapify from last non-leaf upward)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, n, i)

    # Step 2 — Extract max (root) one by one, place at end
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]   # move max to sorted tail
        _sift_down(arr, end, 0)               # restore heap on reduced size

    return arr


def _sift_down(arr, n, i):
    largest = i
    left,  right = 2 * i + 1, 2 * i + 2
    if left  < n and arr[left]  > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _sift_down(arr, n, largest)


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted:", heap_sort(data))  # [3, 9, 10, 27, 38, 43, 82]
""",
    },

    # ── Dynamic Programming additions ─────────────────────────────────────
    {
        "category": "Dynamic Programming",
        "title": "0-1 Knapsack",
        "difficulty": "Hard",
        "code": """\
# 0-1 Knapsack — classic DP
# Given items with weights & values, maximise value within weight W
# Each item can be taken at most once (0-1 choice)
# Time: O(n * W)  |  Space: O(n * W) → optimisable to O(W)

def knapsack(weights, values, W):
    n  = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]              # skip item i
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]  # take item i
                )
    return dp[n][W]


# Space-optimised O(W) — single row, iterate w right-to-left
def knapsack_opt(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):   # right-to-left prevents reuse
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[W]


if __name__ == "__main__":
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    print(knapsack(w, v, 8))      # 10  (items 1+3: weight 6, value 8)
    print(knapsack_opt(w, v, 8))  # 10
""",
    },
    {
        "category": "Dynamic Programming",
        "title": "Longest Common Subsequence (LCS)",
        "difficulty": "Hard",
        "code": """\
# Longest Common Subsequence — classic 2D DP
# Find length (and optionally reconstruct) the longest subsequence common to both strings
# Time: O(m * n)  |  Space: O(m * n) → optimisable to O(min(m,n))

def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    # dp[i][j] = LCS length of s1[:i] and s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lcs_reconstruct(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Backtrack to find actual subsequence
    i, j, result = m, n, []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1; j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(result))


if __name__ == "__main__":
    print(lcs_length("ABCBDAB", "BDCAB"))       # 4
    print(lcs_reconstruct("ABCBDAB", "BDCAB"))  # "BCAB" or "BDAB"
""",
    },

    # ── Django ────────────────────────────────────────────────────────────
    {
        "category": "Django",
        "title": "Django Model Definition",
        "difficulty": "Easy",
        "code": """\
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title   = models.CharField(max_length=200)
    slug    = models.SlugField(max_length=220, unique=True, blank=True)
    body    = models.TextField()
    author  = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )
    status  = models.CharField(max_length=12, choices=STATUS_CHOICES, default="draft")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        indexes  = [models.Index(fields=["-created"])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} [{self.status}]"


# Migrate: python manage.py makemigrations && python manage.py migrate
""",
    },
    {
        "category": "Django",
        "title": "Django Class-Based Views",
        "difficulty": "Easy",
        "code": """\
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().filter(status="published")
        q  = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q)
        return qs


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_url_kwarg = "slug"

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs["slug"], status="published")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
""",
    },
    {
        "category": "Django",
        "title": "Django URL Routing",
        "difficulty": "Easy",
        "code": """\
# mysite/urls.py  (project-level)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/",  admin.site.urls),
    path("blog/",   include("blog.urls", namespace="blog")),
    path("api/v1/", include("api.urls", namespace="api")),
]


# blog/urls.py  (app-level)
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",                    views.PostListView.as_view(),   name="list"),
    path("<slug:slug>/",        views.PostDetailView.as_view(), name="detail"),
    path("new/",                views.PostCreateView.as_view(), name="create"),
    path("<slug:slug>/edit/",   views.PostUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", views.PostDeleteView.as_view(), name="delete"),
]

# In templates:  {% url 'blog:list' %}
# In code:       reverse("blog:detail", kwargs={"slug": post.slug})
""",
    },
    {
        "category": "Django",
        "title": "Django ORM Queries",
        "difficulty": "Medium",
        "code": """\
from django.db.models import Q, Count, Avg, Max, F, Prefetch
from .models import Post, Comment


# Basic lookups
Post.objects.filter(status="published")
Post.objects.exclude(status="draft")
Post.objects.get(slug="my-post")          # raises DoesNotExist / MultipleObjectsReturned

# Field lookups
Post.objects.filter(title__icontains="django")
Post.objects.filter(created__year=2024)
Post.objects.filter(created__gte="2024-01-01")

# Complex Q objects
Post.objects.filter(Q(status="published") | Q(author__username="admin"))

# Annotations & aggregations
Post.objects.annotate(comment_count=Count("comments")).order_by("-comment_count")
Post.objects.aggregate(avg=Avg("views"), max_views=Max("views"))

# F expressions — compare two fields without loading to Python
Post.objects.filter(views__gt=F("likes"))
Post.objects.update(views=F("views") + 1)

# select_related (FK / OneToOne) → single JOIN query
posts = Post.objects.select_related("author").all()

# prefetch_related (ManyToMany / reverse FK) → 2 queries
posts = Post.objects.prefetch_related(
    Prefetch("comments", queryset=Comment.objects.filter(approved=True))
)

# only() / defer() — limit columns fetched
Post.objects.only("title", "slug", "created")
Post.objects.defer("body")

# bulk operations
Post.objects.bulk_create([Post(title=f"Post {i}") for i in range(100)])
Post.objects.filter(status="draft").update(status="published")
Post.objects.filter(created__year=2020).delete()
""",
    },
    {
        "category": "Django",
        "title": "Django Signals & Custom Manager",
        "difficulty": "Medium",
        "code": """\
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


# ── Custom Manager ────────────────────────────────────────────────────────
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

    def by_author(self, user):
        return self.get_queryset().filter(author=user)


class Post(models.Model):
    title   = models.CharField(max_length=200)
    status  = models.CharField(max_length=12, default="draft")
    author  = models.ForeignKey(User, on_delete=models.CASCADE)

    objects   = models.Manager()       # default manager
    published = PublishedManager()     # custom manager


# Usage:
# Post.published.all()
# Post.published.by_author(request.user)


# ── Signals ───────────────────────────────────────────────────────────────
class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


@receiver(pre_delete, sender=Post)
def log_post_deletion(sender, instance, **kwargs):
    print(f"Deleting post: {instance.title} by {instance.author}")
""",
    },

    # ── Design Patterns ───────────────────────────────────────────────────
    {
        "category": "Design Patterns",
        "title": "Singleton Pattern",
        "difficulty": "Medium",
        "code": """\
# Thread-safe Singleton using __new__
import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:          # double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, url: str = ""):
        if self._initialized:
            return
        self.url = url
        self._conn = None
        self._initialized = True

    def connect(self):
        if not self._conn:
            self._conn = f"<connection to {self.url}>"
        return self._conn


# Usage
db1 = DatabaseConnection("postgresql://localhost/mydb")
db2 = DatabaseConnection("postgresql://localhost/other")
print(db1 is db2)         # True  — same instance
print(db1.url)            # postgresql://localhost/mydb
print(db2.connect())      # <connection to postgresql://localhost/mydb>


# Pythonic alternative: module-level instance (simplest singleton)
# config.py
class _Config:
    debug = False
    db_url = "sqlite:///db.sqlite3"

config = _Config()        # import from anywhere → always same object
""",
    },
    {
        "category": "Design Patterns",
        "title": "Factory Method Pattern",
        "difficulty": "Medium",
        "code": """\
from __future__ import annotations
from abc import ABC, abstractmethod


# Product interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        ...


# Concrete products
class EmailNotification(Notification):
    def __init__(self, recipient: str):
        self.recipient = recipient

    def send(self, message: str) -> str:
        return f"Email → {self.recipient}: {message}"


class SMSNotification(Notification):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str) -> str:
        return f"SMS → {self.phone}: {message}"


class PushNotification(Notification):
    def __init__(self, device_id: str):
        self.device_id = device_id

    def send(self, message: str) -> str:
        return f"Push → {self.device_id}: {message}"


# Factory
class NotificationFactory:
    _registry: dict[str, type[Notification]] = {
        "email": EmailNotification,
        "sms":   SMSNotification,
        "push":  PushNotification,
    }

    @classmethod
    def create(cls, kind: str, **kwargs) -> Notification:
        if kind not in cls._registry:
            raise ValueError(f"Unknown notification type: {kind!r}")
        return cls._registry[kind](**kwargs)

    @classmethod
    def register(cls, kind: str, klass: type[Notification]) -> None:
        cls._registry[kind] = klass


# Usage
n1 = NotificationFactory.create("email", recipient="alice@example.com")
n2 = NotificationFactory.create("sms",   phone="+1-555-9999")
print(n1.send("Hello"))   # Email → alice@example.com: Hello
print(n2.send("Hello"))   # SMS → +1-555-9999: Hello
""",
    },
    {
        "category": "Design Patterns",
        "title": "Observer Pattern",
        "difficulty": "Medium",
        "code": """\
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: Any) -> None:
        ...


class Subject:
    def __init__(self):
        self._observers: dict[str, list[Observer]] = {}

    def subscribe(self, event: str, observer: Observer) -> None:
        self._observers.setdefault(event, []).append(observer)

    def unsubscribe(self, event: str, observer: Observer) -> None:
        if event in self._observers:
            self._observers[event].remove(observer)

    def notify(self, event: str, data: Any = None) -> None:
        for obs in self._observers.get(event, []):
            obs.update(event, data)


# Concrete observers
class EmailAlert(Observer):
    def __init__(self, address: str):
        self.address = address

    def update(self, event: str, data: Any) -> None:
        print(f"[EmailAlert {self.address}] {event}: {data}")


class AuditLog(Observer):
    def update(self, event: str, data: Any) -> None:
        print(f"[AuditLog] {event} — {data}")


# Concrete subject
class OrderService(Subject):
    def place_order(self, order_id: str, amount: float):
        print(f"Order {order_id} placed for ${amount:.2f}")
        self.notify("order_placed", {"id": order_id, "amount": amount})

    def ship_order(self, order_id: str):
        print(f"Order {order_id} shipped")
        self.notify("order_shipped", {"id": order_id})


if __name__ == "__main__":
    svc = OrderService()
    svc.subscribe("order_placed",  EmailAlert("ops@example.com"))
    svc.subscribe("order_placed",  AuditLog())
    svc.subscribe("order_shipped", EmailAlert("customer@example.com"))
    svc.place_order("ORD-001", 49.99)
    svc.ship_order("ORD-001")
""",
    },
    {
        "category": "Design Patterns",
        "title": "Decorator & Strategy Patterns",
        "difficulty": "Medium",
        "code": """\
import time
import functools
from abc import ABC, abstractmethod


# ── Decorator Pattern (function-based) ────────────────────────────────────
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == times:
                        raise
                    print(f"Retry {attempt}/{times} after: {exc}")
        return wrapper
    return decorator


@timer
@retry(times=3, exceptions=(ValueError,))
def fetch_data(url: str) -> str:
    return f"data from {url}"


# ── Strategy Pattern ──────────────────────────────────────────────────────
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        ...


class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data[:]
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class PythonSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data)


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def execute(self, data: list) -> list:
        return self._strategy.sort(data)


if __name__ == "__main__":
    sorter = Sorter(BubbleSort())
    print(sorter.execute([5, 3, 1, 4, 2]))   # [1, 2, 3, 4, 5]
    sorter.set_strategy(PythonSort())
    print(sorter.execute([5, 3, 1, 4, 2]))   # [1, 2, 3, 4, 5]
""",
    },

    # ── Git ───────────────────────────────────────────────────────────────
    {
        "category": "Git",
        "title": "Core Git Workflow",
        "difficulty": "Easy",
        "code": """\
# ── Setup (once per machine) ──────────────────────────────────────────────
git config --global user.name  "Alice Smith"
git config --global user.email "alice@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main

# ── Create / clone ────────────────────────────────────────────────────────
git init my-project
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder

# ── Stage & commit ────────────────────────────────────────────────────────
git status
git add file.py
git add .
git add -p                          # interactive hunk staging

git commit -m "feat: add login page"
git commit --amend -m "fix: correct msg"   # amend last commit (local only!)

# ── Inspect ───────────────────────────────────────────────────────────────
git log --oneline --graph --all
git log -p file.py                  # show patch for each commit
git diff                            # unstaged changes
git diff --staged                   # staged vs last commit
git show HEAD~2:src/app.py          # view file at specific commit

# ── Undo ──────────────────────────────────────────────────────────────────
git restore file.py                 # discard unstaged changes
git restore --staged file.py        # unstage (keep working copy)
git revert HEAD                     # new commit that undoes HEAD (safe)
git reset --soft  HEAD~1            # move HEAD back, keep staged
git reset --mixed HEAD~1            # move HEAD back, keep unstaged  (default)
git reset --hard  HEAD~1            # move HEAD back, discard ALL changes

# ── Remote ───────────────────────────────────────────────────────────────
git remote add origin https://github.com/user/repo.git
git push -u origin main
git pull --rebase origin main       # rebase local on top of remote
git fetch --all --prune             # fetch + remove deleted remote branches
""",
    },
    {
        "category": "Git",
        "title": "Branching & Merging Workflow",
        "difficulty": "Easy",
        "code": """\
# ── Branching ─────────────────────────────────────────────────────────────
git branch                          # list local branches
git branch -a                       # list all (local + remote)
git branch feature/login            # create branch
git switch feature/login            # switch to branch (modern)
git switch -c feature/signup        # create + switch
git checkout -b hotfix/bug-123      # older equivalent

# ── Merging ───────────────────────────────────────────────────────────────
git switch main
git merge feature/login                  # fast-forward when possible
git merge --no-ff feature/login          # always create a merge commit
git merge --squash feature/login         # squash all commits into one staged change

# ── Rebasing ──────────────────────────────────────────────────────────────
git switch feature/login
git rebase main                          # replay feature commits on top of main
git rebase -i HEAD~4                     # interactive: squash, reorder, edit

# ── Conflict resolution ───────────────────────────────────────────────────
# After a conflict:
# 1. Edit conflicting files (remove <<<<< ===== >>>>> markers)
git add resolved_file.py
git rebase --continue                   # or: git merge --continue
git rebase --abort                      # bail out completely

# ── Clean up ──────────────────────────────────────────────────────────────
git branch -d feature/login              # delete merged branch
git branch -D feature/wip               # force-delete unmerged branch
git push origin --delete feature/login  # delete remote branch

# ── Stashing ──────────────────────────────────────────────────────────────
git stash push -m "WIP: login redirect"
git stash list
git stash pop                            # apply latest + remove
git stash apply stash@{2}               # apply specific, keep in list
git stash drop stash@{0}
""",
    },
    {
        "category": "Git",
        "title": "Tags, Hooks & Advanced Techniques",
        "difficulty": "Medium",
        "code": """\
# ── Tags ──────────────────────────────────────────────────────────────────
git tag                             # list tags
git tag v1.0.0                      # lightweight tag
git tag -a v1.0.0 -m "Release 1.0.0"  # annotated tag
git tag -a v0.9.9 abc1234 -m "Hotfix"  # tag a past commit
git push origin v1.0.0
git push origin --tags              # push all tags

# ── Cherry-pick ───────────────────────────────────────────────────────────
git cherry-pick abc1234             # apply a single commit to current branch
git cherry-pick abc1234..def5678    # apply a range of commits

# ── Bisect — find the commit that introduced a bug ────────────────────────
git bisect start
git bisect bad                      # current commit has the bug
git bisect good v1.2.0              # this version was fine
# Git checks out midpoint — test, then:
git bisect good                     # or: git bisect bad
# Repeat until Git pinpoints the culprit
git bisect reset                    # return to original HEAD

# ── Worktrees — multiple checkouts of the same repo ──────────────────────
git worktree add ../feature-branch feature/new-ui
git worktree list
git worktree remove ../feature-branch

# ── Hooks (stored in .git/hooks/) ────────────────────────────────────────
# pre-commit hook example (.git/hooks/pre-commit — must be executable)
#!/bin/bash
python -m pytest tests/unit/ -q --tb=short
if [ $? -ne 0 ]; then
  echo "Tests failed. Aborting commit."
  exit 1
fi

# commit-msg hook — enforce conventional commits
#!/bin/bash
msg=$(cat "$1")
if ! echo "$msg" | grep -qP "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"; then
  echo "Commit message must follow Conventional Commits format."
  exit 1
fi
""",
    },

    # ── Linux Essentials ─────────────────────────────────────────────────
    {
        "category": "Linux Essentials",
        "title": "File Management & Text Processing",
        "difficulty": "Easy",
        "code": """\
# ── Navigate & inspect ────────────────────────────────────────────────────
ls -lah                             # long list, hidden, human sizes
tree -L 2                           # directory tree 2 levels deep
file /path/to/file                  # detect file type
stat file.txt                       # inode, size, timestamps
du -sh /var/log/                    # disk usage of directory

# ── Copy / Move / Delete ──────────────────────────────────────────────────
cp -rp src/ dst/                    # recursive, preserve permissions
mv old_name new_name                # move or rename
rm -rf dir/                         # remove recursively
ln -s /target symlink               # symbolic link
ln  /target hardlink                # hard link

# ── Find ──────────────────────────────────────────────────────────────────
find / -name "*.conf" -type f 2>/dev/null
find /home -user alice -mtime -7    # modified in last 7 days
find / -perm /4000 2>/dev/null      # SUID files
find /var/log -size +100M           # files > 100 MB

# ── Text processing ───────────────────────────────────────────────────────
grep -rn "error" /var/log/          # recursive, show line numbers
grep -v "^#" /etc/ssh/sshd_config   # exclude comment lines
sed 's/old/new/g' file.txt          # global replace (stdout)
sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
awk -F: '{print $1, $3}' /etc/passwd          # print fields 1 and 3
awk -F: '$3 >= 1000 {print $1}' /etc/passwd   # UID >= 1000
sort -k3 -t: -n /etc/passwd         # sort by UID (field 3)
cut -d: -f1,3 /etc/passwd           # extract fields 1 and 3

# ── Archives ─────────────────────────────────────────────────────────────
tar -czvf backup.tar.gz /etc/
tar -xzvf backup.tar.gz -C /opt/
tar -tzvf backup.tar.gz             # list contents without extracting

# ── I/O redirection ──────────────────────────────────────────────────────
command > file.txt                  # stdout to file (overwrite)
command >> file.txt                 # stdout to file (append)
command 2>/dev/null                 # discard stderr
command &> all.txt                  # stdout + stderr to file
cmd1 | cmd2 | cmd3                  # pipeline
""",
    },
    {
        "category": "Linux Essentials",
        "title": "User, Group & Permission Management",
        "difficulty": "Easy",
        "code": """\
# ── User management ───────────────────────────────────────────────────────
useradd -m -s /bin/bash alice       # create user with home + bash shell
useradd -r svcaccount               # system account (no login)
usermod -aG wheel alice             # add alice to wheel group
usermod -s /sbin/nologin svc        # assign nologin shell
userdel -r alice                    # delete user + home dir
passwd alice                        # set/change password

# /etc/passwd format: username:x:UID:GID:comment:home:shell
# /etc/shadow stores hashed passwords (readable only by root)
# /etc/group  format: groupname:x:GID:members

# ── Group management ──────────────────────────────────────────────────────
groupadd developers
groupmod -n devs developers         # rename group
gpasswd -a alice devs               # add alice to devs
gpasswd -d alice devs               # remove alice from devs
id alice                            # show UID, GID, supplemental groups

# ── File permissions ──────────────────────────────────────────────────────
chmod 755 script.sh                 # rwxr-xr-x
chmod u+x,g-w,o-r file.txt         # symbolic mode
chmod -R 750 /opt/app/              # recursive

chown alice file.txt
chown alice:devs /opt/app/
chown -R alice:devs /opt/app/       # recursive

# ── Special permissions ───────────────────────────────────────────────────
chmod u+s /usr/bin/program          # SUID — run as file owner
chmod g+s /shared/dir/              # SGID — new files inherit group
chmod +t  /tmp/                     # sticky bit — only owner can delete

# ── ACLs ──────────────────────────────────────────────────────────────────
setfacl -m u:bob:rx /opt/app/       # grant bob read+execute
setfacl -m g:devs:rw /opt/app/
getfacl /opt/app/                   # view ACL entries
setfacl -x u:bob /opt/app/          # remove bob's ACL entry

# ── sudo ──────────────────────────────────────────────────────────────────
visudo                              # safely edit /etc/sudoers
# alice ALL=(ALL) NOPASSWD: /bin/systemctl restart httpd
""",
    },
    {
        "category": "Linux Essentials",
        "title": "systemd & Process Management",
        "difficulty": "Easy",
        "code": """\
# ── systemctl — manage services ───────────────────────────────────────────
systemctl start   httpd
systemctl stop    httpd
systemctl restart httpd
systemctl reload  httpd             # reload config without full restart
systemctl enable  httpd             # start at boot
systemctl disable httpd
systemctl status  httpd             # status + recent journal entries
systemctl is-active  httpd         # exits 0 if active
systemctl is-enabled httpd         # exits 0 if enabled
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service

# ── journalctl — view logs ────────────────────────────────────────────────
journalctl -u httpd                 # logs for httpd
journalctl -u httpd --since "1 hour ago"
journalctl -f                       # follow (like tail -f)
journalctl -p err -n 50             # last 50 error-level messages
journalctl --disk-usage             # how much space logs use
journalctl --vacuum-time=7d         # keep only last 7 days

# ── Process management ────────────────────────────────────────────────────
ps aux                              # all processes (user-oriented)
ps -ef                              # all processes (full format)
pgrep -a nginx                      # find PID(s) of nginx
kill -SIGTERM 1234                  # graceful terminate
kill -SIGKILL 1234                  # force kill
killall nginx                       # kill all nginx processes
top                                 # interactive process viewer
htop                                # improved interactive viewer
nice -n 10 python script.py         # start with lower priority
renice -n 5 -p 1234                 # change priority of running process

# ── Scheduling — cron ────────────────────────────────────────────────────
crontab -e                          # edit current user's crontab
# MIN HOUR DOM MON DOW COMMAND
# 30 2 * * 0   /usr/local/bin/backup.sh   # every Sunday at 02:30
# */5 * * * *  /opt/check.sh              # every 5 minutes
crontab -l                          # list crontab entries
""",
    },

    # ── Ansible ───────────────────────────────────────────────────────────
    {
        "category": "Ansible",
        "title": "Ansible Inventory & Ad-hoc Commands",
        "difficulty": "Easy",
        "code": """\
# ── Static Inventory (INI format) ─────────────────────────────────────────
# inventory/hosts
[webservers]
web1.example.com
web2.example.com ansible_user=ubuntu

[dbservers]
db1.example.com ansible_host=192.168.1.50 ansible_port=2222

[production:children]
webservers
dbservers

[all:vars]
ansible_user=ansible
ansible_python_interpreter=/usr/bin/python3

# ── ansible.cfg (project-local) ───────────────────────────────────────────
[defaults]
inventory        = ./inventory/hosts
remote_user      = ansible
host_key_checking = False
forks            = 10

[privilege_escalation]
become           = True
become_method    = sudo
become_user      = root
become_ask_pass  = False

# ── Ad-hoc commands ───────────────────────────────────────────────────────
ansible all -m ping                                         # connectivity test
ansible webservers -m shell -a "uptime"                     # run shell command
ansible all -m setup -a "filter=ansible_os_family"         # gather facts
ansible webservers -m yum  -a "name=httpd state=present"   # install package
ansible webservers -m service -a "name=httpd state=started enabled=yes"
ansible all -m copy -a "src=app.conf dest=/etc/app/app.conf mode=0644"
ansible all -m file -a "path=/opt/app state=directory mode=0755 owner=apache"
ansible dbservers  -m shell -a "systemctl status postgresql" --become
ansible webservers -m setup --tree /tmp/facts/             # save facts locally
""",
    },
    {
        "category": "Ansible",
        "title": "Ansible Playbook Structure",
        "difficulty": "Medium",
        "code": """\
# site.yml — main playbook
---
- name: Configure web servers
  hosts: webservers
  become: true
  vars:
    http_port: 80
    max_clients: 200
    app_user: apache

  pre_tasks:
    - name: Ensure Python is present
      raw: dnf install -y python3
      changed_when: false

  tasks:
    - name: Install Apache
      ansible.builtin.dnf:
        name: httpd
        state: present

    - name: Deploy virtual host config
      ansible.builtin.template:
        src: vhost.conf.j2
        dest: /etc/httpd/conf.d/myapp.conf
        owner: root
        group: root
        mode: "0644"
      notify: Restart Apache

    - name: Open firewall port
      ansible.posix.firewalld:
        port: "{{ http_port }}/tcp"
        permanent: true
        state: enabled
        immediate: true

    - name: Ensure Apache is started and enabled
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: true

  handlers:
    - name: Restart Apache
      ansible.builtin.service:
        name: httpd
        state: restarted

  post_tasks:
    - name: Verify Apache responds
      ansible.builtin.uri:
        url: "http://{{ ansible_default_ipv4.address }}/"
        status_code: 200
      retries: 5
      delay: 3

# Run: ansible-playbook site.yml -i inventory/hosts
# Dry run: ansible-playbook site.yml --check
# Limit hosts: ansible-playbook site.yml --limit web1.example.com
# Start at task: ansible-playbook site.yml --start-at-task "Deploy virtual host config"
""",
    },
    {
        "category": "Ansible",
        "title": "Ansible Variables, Loops & Vault",
        "difficulty": "Medium",
        "code": """\
# ── Variables & facts ─────────────────────────────────────────────────────
# group_vars/all.yml
app_name: myapp
app_version: "2.1.0"
db_host: "{{ hostvars['db1.example.com']['ansible_default_ipv4']['address'] }}"

# Access facts:  ansible_facts['os_family']  or  ansible_os_family

# ── Loops ─────────────────────────────────────────────────────────────────
- name: Create application users
  ansible.builtin.user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
    state: present
  loop:
    - { name: deploy,  groups: "wheel,docker" }
    - { name: monitor, groups: "docker" }
    - { name: backup,  groups: "wheel" }

- name: Install required packages
  ansible.builtin.dnf:
    name: "{{ item }}"
    state: present
  loop:
    - git
    - htop
    - python3-pip
    - nginx

# ── Conditionals ──────────────────────────────────────────────────────────
- name: Start firewalld only on RHEL
  ansible.builtin.service:
    name: firewalld
    state: started
  when: ansible_os_family == "RedHat"

# ── Templates (Jinja2) ────────────────────────────────────────────────────
# templates/app.conf.j2
server {
    listen {{ http_port | default(80) }};
    server_name {{ ansible_hostname }};
    {% for vhost in virtual_hosts %}
    location {{ vhost.path }} {
        proxy_pass http://{{ vhost.backend }};
    }
    {% endfor %}
}

# ── Ansible Vault ──────────────────────────────────────────────────────────
# Encrypt a file
ansible-vault encrypt vault/secrets.yml
# Decrypt a file
ansible-vault decrypt vault/secrets.yml
# View encrypted file
ansible-vault view vault/secrets.yml
# Edit in-place
ansible-vault edit vault/secrets.yml
# Encrypt a single string
ansible-vault encrypt_string "supersecret" --name db_password
# Run playbook with vault
ansible-playbook site.yml --ask-vault-pass
ansible-playbook site.yml --vault-password-file ~/.vault_pass
""",
    },

    # ── Kubernetes ────────────────────────────────────────────────────────
    {
        "category": "Kubernetes",
        "title": "Pod & Deployment YAML",
        "difficulty": "Medium",
        "code": """\
# pod.yaml — minimal pod spec
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  labels:
    app: my-app
    tier: backend
spec:
  containers:
    - name: app
      image: python:3.12-slim
      command: ["python", "-m", "http.server", "8080"]
      ports:
        - containerPort: 8080
      resources:
        requests:
          cpu: "100m"
          memory: "128Mi"
        limits:
          cpu: "500m"
          memory: "256Mi"
      livenessProbe:
        httpGet:
          path: /healthz
          port: 8080
        initialDelaySeconds: 10
        periodSeconds: 15
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
      env:
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db_host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db_password
---
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: app
          image: myregistry/my-app:v2.1.0
          ports:
            - containerPort: 8080
""",
    },
    {
        "category": "Kubernetes",
        "title": "Services, ConfigMaps & Secrets",
        "difficulty": "Medium",
        "code": """\
# service.yaml — expose pods via ClusterIP / NodePort / LoadBalancer
apiVersion: v1
kind: Service
metadata:
  name: my-app-svc
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP          # options: ClusterIP | NodePort | LoadBalancer
---
# NodePort example
apiVersion: v1
kind: Service
metadata:
  name: my-app-nodeport
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080      # 30000–32767
  type: NodePort
---
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  db_host: "postgres-svc"
  log_level: "INFO"
  app.properties: |
    server.port=8080
    spring.jpa.show-sql=false
---
# secret.yaml (values must be base64-encoded)
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  db_password: c3VwZXJzZWNyZXQ=   # base64: echo -n "supersecret" | base64
  api_key:     YWJjMTIz             # abc123
# Better: use kubectl create secret generic app-secrets \
#   --from-literal=db_password=supersecret --from-literal=api_key=abc123
""",
    },
    {
        "category": "Kubernetes",
        "title": "kubectl Essential Commands",
        "difficulty": "Easy",
        "code": """\
# ── Context & cluster info ────────────────────────────────────────────────
kubectl config get-contexts
kubectl config use-context my-cluster
kubectl cluster-info
kubectl get nodes -o wide

# ── Pods ──────────────────────────────────────────────────────────────────
kubectl get pods                              # current namespace
kubectl get pods -A                           # all namespaces
kubectl get pods -o wide                      # include node, IP
kubectl describe pod my-app                   # full details + events
kubectl logs my-app                           # stdout logs
kubectl logs my-app -c app --tail=50 -f       # follow specific container
kubectl exec -it my-app -- /bin/bash          # interactive shell
kubectl port-forward pod/my-app 8080:8080     # forward to localhost

# ── Deployments ───────────────────────────────────────────────────────────
kubectl get deployments
kubectl apply -f deployment.yaml
kubectl set image deployment/my-app app=myregistry/my-app:v2.2.0
kubectl rollout status  deployment/my-app
kubectl rollout history deployment/my-app
kubectl rollout undo   deployment/my-app              # roll back
kubectl rollout undo   deployment/my-app --to-revision=2
kubectl scale deployment my-app --replicas=5

# ── Namespaces & resources ────────────────────────────────────────────────
kubectl create namespace staging
kubectl get all -n staging
kubectl get events -n default --sort-by=.lastTimestamp

# ── Debugging ─────────────────────────────────────────────────────────────
kubectl get pod my-app -o yaml                # full YAML spec
kubectl top pods                              # CPU/memory (metrics-server required)
kubectl top nodes
kubectl run debug --image=nicolaka/netshoot --rm -it -- bash   # temporary debug pod

# ── etcd backup (CKA exam) ────────────────────────────────────────────────
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
""",
    },

    # ── Cloud Computing ───────────────────────────────────────────────────
    {
        "category": "Cloud Computing",
        "title": "AWS CLI Core Commands",
        "difficulty": "Easy",
        "code": """\
# ── Setup ─────────────────────────────────────────────────────────────────
aws configure                       # sets key, secret, region, output format
aws configure list
aws sts get-caller-identity         # verify who you're authenticated as

# ── EC2 ───────────────────────────────────────────────────────────────────
aws ec2 describe-instances --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name}' --output table
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.micro \
  --key-name my-key \
  --security-group-ids sg-12345 \
  --subnet-id subnet-12345 \
  --count 1
aws ec2 stop-instances  --instance-ids i-1234567890abcdef
aws ec2 start-instances --instance-ids i-1234567890abcdef
aws ec2 terminate-instances --instance-ids i-1234567890abcdef

# ── S3 ────────────────────────────────────────────────────────────────────
aws s3 ls                           # list buckets
aws s3 ls s3://my-bucket/ --recursive
aws s3 cp  local_file.txt s3://my-bucket/path/
aws s3 cp  s3://my-bucket/file.txt  ./
aws s3 sync ./dist/ s3://my-bucket/dist/ --delete
aws s3 mb  s3://my-new-bucket --region us-east-1
aws s3 rb  s3://my-bucket --force   # remove bucket + all objects

# ── IAM ───────────────────────────────────────────────────────────────────
aws iam list-users
aws iam create-user --user-name ci-deploy
aws iam attach-user-policy --user-name ci-deploy \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam create-access-key --user-name ci-deploy

# ── CloudFormation / IaC ──────────────────────────────────────────────────
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name my-stack \
  --capabilities CAPABILITY_IAM
aws cloudformation describe-stacks --stack-name my-stack
aws cloudformation delete-stack --stack-name my-stack
""",
    },
    {
        "category": "Cloud Computing",
        "title": "Cloud Architecture Patterns",
        "difficulty": "Medium",
        "code": """\
# ── The Three Service Models ───────────────────────────────────────────────
# IaaS — you manage: OS, runtime, middleware, apps, data
#   Provider manages: hardware, networking, hypervisor
#   Examples: AWS EC2, Azure VMs, GCP Compute Engine

# PaaS — you manage: application code and data only
#   Provider manages: everything below
#   Examples: AWS Elastic Beanstalk, Azure App Service, GCP App Engine

# SaaS — you manage: nothing (just use the app)
#   Provider manages: everything
#   Examples: Gmail, Salesforce, Microsoft 365

# ── Well-Architected Framework pillars ────────────────────────────────────
# 1. Operational Excellence — automate, make small reversible changes
# 2. Security              — least privilege, encrypt at rest and in transit
# 3. Reliability           — auto-recover, test disaster recovery
# 4. Performance Efficiency— select right resource type, benchmark regularly
# 5. Cost Optimisation     — pay only for what you use, right-size resources
# 6. Sustainability        — reduce energy impact of cloud workloads

# ── Typical 3-tier web architecture ──────────────────────────────────────
# [Client] → [CDN] → [Load Balancer] → [App Servers (Auto-Scaling Group)]
#                                    → [Cache (Redis/ElastiCache)]
#                                    → [Database (RDS Multi-AZ)]
#                                    ↔ [Object Storage (S3)]
#                                    ↔ [Queue (SQS)]

# ── High Availability recipe ─────────────────────────────────────────────
# 1. Multiple Availability Zones (AZs) — survive datacenter failure
# 2. Auto Scaling Groups  — replace failed instances automatically
# 3. Multi-AZ RDS         — standby replica in separate AZ, auto-failover < 60s
# 4. Read Replicas        — offload read traffic from primary
# 5. ElastiCache          — in-memory caching reduces DB load
# 6. Route53 health checks + failover routing

# ── Back-of-envelope estimation ──────────────────────────────────────────
# DAU x avg_requests_per_day / 86_400 = avg_RPS
# Peak RPS ≈ avg_RPS x 3          (rule of thumb)
# Storage_per_day = DAU x avg_write_bytes
# Bandwidth_in  = RPS x avg_request_size
# Bandwidth_out = RPS x avg_response_size
""",
    },

    # ── System Design ─────────────────────────────────────────────────────
    {
        "category": "System Design",
        "title": "LRU Cache Design",
        "difficulty": "Hard",
        "code": """\
from collections import OrderedDict
from threading import Lock


class LRUCache:
    '''
    O(1) get and put using an OrderedDict (doubly-linked list + hash map).
    OrderedDict maintains insertion order; move_to_end() promotes recency.
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()
        self._lock = Lock()

    def get(self, key: int) -> int:
        with self._lock:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)     # mark as most-recently used
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        with self._lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)  # evict least-recently used


# Manual doubly-linked list implementation (interview version)
class Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key  = key
        self.val  = val
        self.prev = None
        self.next = None


class LRUCacheManual:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, Node] = {}
        self.head = Node()          # dummy head (LRU end)
        self.tail = Node()          # dummy tail (MRU end)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_tail(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._insert_tail(node)
        if len(self.map) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]
""",
    },
    {
        "category": "System Design",
        "title": "Consistent Hashing",
        "difficulty": "Hard",
        "code": """\
import hashlib
import bisect


class ConsistentHashRing:
    '''
    Consistent hashing ring with virtual nodes.
    Adding/removing a server only relocates ~K/n keys (K keys, n servers).
    Virtual nodes improve uniformity across the ring.
    '''

    def __init__(self, replicas: int = 150):
        self.replicas = replicas          # virtual nodes per server
        self._ring: dict[int, str] = {}   # hash → server name
        self._sorted_keys: list[int] = [] # sorted list of hash positions

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_server(self, server: str) -> None:
        for i in range(self.replicas):
            h = self._hash(f"{server}#{i}")
            self._ring[h] = server
            bisect.insort(self._sorted_keys, h)

    def remove_server(self, server: str) -> None:
        for i in range(self.replicas):
            h = self._hash(f"{server}#{i}")
            del self._ring[h]
            idx = bisect.bisect_left(self._sorted_keys, h)
            self._sorted_keys.pop(idx)

    def get_server(self, key: str) -> str | None:
        if not self._ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self._sorted_keys, h) % len(self._sorted_keys)
        return self._ring[self._sorted_keys[idx]]


if __name__ == "__main__":
    ring = ConsistentHashRing(replicas=100)
    for srv in ("server-A", "server-B", "server-C"):
        ring.add_server(srv)

    keys = [f"user:{i}" for i in range(20)]
    distribution: dict[str, int] = {}
    for k in keys:
        srv = ring.get_server(k)
        distribution[srv] = distribution.get(srv, 0) + 1
    print("Distribution:", distribution)

    ring.remove_server("server-B")
    moved = sum(1 for k in keys if ring.get_server(k) != "server-B")
    print(f"Keys still on non-B servers after removal: {moved}/{len(keys)}")
""",
    },
    {
        "category": "System Design",
        "title": "Rate Limiter — Token Bucket",
        "difficulty": "Hard",
        "code": """\
import time
from threading import Lock
from collections import defaultdict


class TokenBucket:
    '''
    Token Bucket rate limiter.
    Allows bursting up to `capacity` tokens while enforcing `rate` tokens/sec
    long-term.
    '''

    def __init__(self, rate: float, capacity: float):
        self.rate = rate              # tokens added per second
        self.capacity = capacity      # max tokens (burst ceiling)
        self._tokens = capacity
        self._last_refill = time.monotonic()
        self._lock = Lock()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self.capacity, self._tokens + elapsed * self.rate)
        self._last_refill = now

    def allow(self, tokens: float = 1.0) -> bool:
        with self._lock:
            self._refill()
            if self._tokens >= tokens:
                self._tokens -= tokens
                return True
            return False


class RateLimiter:
    '''Per-user rate limiter backed by token buckets.'''

    def __init__(self, rate: float = 10, capacity: float = 20):
        self._buckets: dict[str, TokenBucket] = defaultdict(
            lambda: TokenBucket(rate, capacity)
        )
        self._lock = Lock()

    def is_allowed(self, user_id: str) -> bool:
        with self._lock:
            bucket = self._buckets[user_id]
        return bucket.allow()


# ── Alternative: Fixed Window Counter ────────────────────────────────────
class FixedWindowCounter:
    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window = window_seconds
        self._counts: dict[tuple, int] = {}
        self._lock = Lock()

    def _window_key(self, user_id: str) -> tuple:
        return (user_id, int(time.time()) // self.window)

    def is_allowed(self, user_id: str) -> bool:
        key = self._window_key(user_id)
        with self._lock:
            self._counts[key] = self._counts.get(key, 0) + 1
            return self._counts[key] <= self.limit


if __name__ == "__main__":
    limiter = RateLimiter(rate=5, capacity=10)
    for i in range(15):
        allowed = limiter.is_allowed("alice")
        print(f"Request {i+1:2d}: {'✓ allowed' if allowed else '✗ blocked'}")
        time.sleep(0.1)
""",
    },

    # ── Python Fundamentals (PCEP) ────────────────────────────────────────
    {
        "category": "Python Fundamentals",
        "title": "Types, Operators & Truthiness",
        "difficulty": "Easy",
        "code": """\
# ── Built-in types ────────────────────────────────────────────────────────
x: int   = 42
y: float = 3.14
z: complex = 2 + 3j
b: bool  = True          # bool is a subclass of int: True == 1, False == 0
s: str   = "hello"
n = None

# Type checking
print(type(x))             # <class 'int'>
print(isinstance(x, int))  # True
print(isinstance(True, int)) # True  — bool is a subclass of int!

# ── Arithmetic ────────────────────────────────────────────────────────────
print(17 // 5)    # 3    floor division (always rounds toward -∞)
print(-17 // 5)   # -4   NOT -3!
print(17 % 5)     # 2    (result has sign of divisor)
print(-17 % 5)    # 3    NOT -2!
print(2 ** 10)    # 1024
print(9 ** 0.5)   # 3.0  square root

# ── Comparison & identity ─────────────────────────────────────────────────
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)     # True   — value equality
print(a is b)     # False  — different objects
print(a is c)     # True   — same object

# ── Falsy values (everything else is truthy) ──────────────────────────────
falsy = [0, 0.0, 0j, "", b"", [], (), {}, set(), None, False]
for val in falsy:
    print(f"{val!r:15} → {bool(val)}")

# ── String formatting ─────────────────────────────────────────────────────
name, score = "Alice", 98.5
print(f"Name: {name!r}, Score: {score:.1f}")    # f-string (fastest)
print("Name: {}, Score: {:.1f}".format(name, score))   # .format()
print("%-10s %5.1f" % (name, score))            # %-style (legacy)

# ── Walrus operator := (Python 3.8+) ─────────────────────────────────────
import re
if m := re.search(r"(\d+)", "abc 42 xyz"):
    print("Found number:", m.group(1))          # 42

data = [1, 5, 9, 3, 7]
if (n := len(data)) > 3:
    print(f"List has {n} elements")             # 5
""",
    },
    {
        "category": "Python Fundamentals",
        "title": "Functions, Scope & Closures",
        "difficulty": "Easy",
        "code": """\
# ── *args and **kwargs ────────────────────────────────────────────────────
def summarise(*args: int, sep: str = ", ", **meta) -> str:
    total = sum(args)
    label = meta.get("label", "total")
    return f"{label}: {sep.join(str(a) for a in args)} = {total}"

print(summarise(1, 2, 3, sep=" + ", label="sum"))  # sum: 1 + 2 + 3 = 6

# ── Positional-only (/) and keyword-only (*) parameters ──────────────────
def strict(pos_only, /, normal, *, kw_only):
    return pos_only + normal + kw_only

strict(1, 2, kw_only=3)   # OK
# strict(pos_only=1, ...)   # TypeError — pos_only cannot be keyword

# ── LEGB scope rule ───────────────────────────────────────────────────────
# Local → Enclosing → Global → Built-in
x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x          # refers to enclosing x
        x = "modified enclosing"
        print(x)
    inner()
    print(x)                # modified enclosing

outer()
print(x)                    # global (unchanged)

# ── Closures ──────────────────────────────────────────────────────────────
def make_counter(start: int = 0):
    count = start
    def increment(step: int = 1) -> int:
        nonlocal count
        count += step
        return count
    return increment

counter = make_counter(10)
print(counter())    # 11
print(counter(5))   # 16
print(counter())    # 17

# ── Lambda ────────────────────────────────────────────────────────────────
square  = lambda x: x * x
add     = lambda a, b: a + b
clamp   = lambda x, lo, hi: max(lo, min(hi, x))

pairs = [(3, "c"), (1, "a"), (2, "b")]
pairs.sort(key=lambda p: p[0])          # sort by first element
print(pairs)                            # [(1, 'a'), (2, 'b'), (3, 'c')]
""",
    },
    {
        "category": "Python Fundamentals",
        "title": "Comprehensions & Built-ins",
        "difficulty": "Easy",
        "code": """\
# ── List / Set / Dict / Generator comprehensions ──────────────────────────
squares    = [x**2 for x in range(10)]
evens      = [x for x in range(20) if x % 2 == 0]
flat       = [n for row in [[1,2],[3,4],[5,6]] for n in row]
unique_sq  = {x**2 for x in [-3,-2,-1,0,1,2,3]}   # set
word_len   = {w: len(w) for w in ["hello", "world", "python"]}  # dict
gen        = (x**2 for x in range(10))             # generator (lazy)

# ── Key built-in functions ────────────────────────────────────────────────
nums = [4, 2, 7, 1, 9, 3]
print(sorted(nums))                      # [1, 2, 3, 4, 7, 9]
print(sorted(nums, reverse=True))        # [9, 7, 4, 3, 2, 1]
print(min(nums), max(nums), sum(nums))   # 1  9  26

words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))           # by length
print(sorted(words, key=str.lower))     # case-insensitive

# map, filter, zip, enumerate
doubled   = list(map(lambda x: x*2, nums))
positives = list(filter(lambda x: x > 3, nums))
pairs     = list(zip(range(5), "abcde"))           # [(0,'a'),(1,'b')...]
indexed   = list(enumerate(words, start=1))        # [(1,'banana')...]

# any / all
print(any(x > 8 for x in nums))     # True  (9 > 8)
print(all(x > 0 for x in nums))     # True  (all positive)

# ── map / zip for matrix transposition ───────────────────────────────────
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [list(row) for row in zip(*matrix)]
# [[1,4,7],[2,5,8],[3,6,9]]

# ── Useful stdlib: itertools ──────────────────────────────────────────────
from itertools import chain, product, combinations, permutations, groupby

print(list(chain([1,2], [3,4], [5])))        # [1,2,3,4,5]
print(list(combinations("ABC", 2)))          # AB AC BC
print(list(permutations("AB", 2)))           # AB BA
print(list(product([0,1], repeat=3)))        # all 3-bit binary strings
""",
    },

    # ── Python OOP (PCAP/PCPP) ────────────────────────────────────────────
    {
        "category": "Python OOP",
        "title": "Classes, Inheritance & Dunder Methods",
        "difficulty": "Medium",
        "code": """\
from __future__ import annotations
from functools import total_ordering


@total_ordering
class Vector:
    '''2D vector with full arithmetic and comparison support.'''

    __slots__ = ("x", "y")     # save memory, disallow arbitrary attributes

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # ── Representation ────────────────────────────────────────────────────
    def __repr__(self) -> str:          # developer-friendly
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:           # user-friendly
        return f"({self.x}, {self.y})"

    # ── Arithmetic ────────────────────────────────────────────────────────
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__    # scalar * vector

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)

    def __abs__(self) -> float:         # magnitude
        return (self.x**2 + self.y**2) ** 0.5

    # ── Comparison (@total_ordering needs __eq__ + one other) ─────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: Vector) -> bool:
        return abs(self) < abs(other)

    def __hash__(self):                 # required when __eq__ is defined
        return hash((self.x, self.y))

    # ── Container protocol ────────────────────────────────────────────────
    def __len__(self) -> int:
        return 2

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, idx: int) -> float:
        return (self.x, self.y)[idx]


v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)        # (4, 6)
print(abs(v1))        # 5.0
print(list(v1))       # [3, 4]
print(v1 > v2)        # True  (magnitude 5 > 2.24)
""",
    },
    {
        "category": "Python OOP",
        "title": "Generators & Decorators",
        "difficulty": "Medium",
        "code": """\
import functools
import time
from typing import Generator, Iterator


# ── Generator functions ───────────────────────────────────────────────────
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n: int, it: Iterator) -> list:
    return [next(it) for _ in range(n)]


fib = fibonacci()
print(take(10, fib))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Generator with send() — coroutine-style ─────────────────────────────────
def running_average() -> Generator[float, float, None]:
    total = count = 0
    while True:
        value = yield total / count if count else 0
        total += value
        count += 1


avg = running_average()
next(avg)              # prime the generator
print(avg.send(10))    # 10.0
print(avg.send(20))    # 15.0
print(avg.send(30))    # 20.0


# ── Parametrised decorator ────────────────────────────────────────────────
def cache(maxsize: int = 128):
    def decorator(func):
        _cache: dict = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args not in _cache:
                if len(_cache) >= maxsize:
                    _cache.pop(next(iter(_cache)))   # evict oldest
                _cache[args] = func(*args)
            return _cache[args]
        wrapper.cache_info = lambda: {"size": len(_cache), "maxsize": maxsize}
        return wrapper
    return decorator


@cache(maxsize=256)
def expensive(n: int) -> int:
    time.sleep(0.001)    # simulate work
    return n * n

print(expensive(10))              # computed
print(expensive(10))              # cached
print(expensive.cache_info())     # {'size': 1, 'maxsize': 256}
""",
    },
    {
        "category": "Python OOP",
        "title": "Metaclasses & Descriptors",
        "difficulty": "Hard",
        "code": """\
from __future__ import annotations


# ── Descriptor — typed attribute ──────────────────────────────────────────
class Typed:
    '''Data descriptor that enforces a type constraint on an attribute.'''

    def __set_name__(self, owner: type, name: str):
        self.public_name  = name
        self.private_name = f"_{name}"

    def __init__(self, expected_type: type):
        self.expected_type = expected_type

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.public_name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(obj, self.private_name, value)


class Person:
    name = Typed(str)
    age  = Typed(int)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age

p = Person("Alice", 30)
print(p.name, p.age)       # Alice 30
try:
    p.age = "thirty"        # TypeError: age must be int, got str
except TypeError as e:
    print(e)


# ── Metaclass — registry pattern ──────────────────────────────────────────
class PluginMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        key = namespace.get("plugin_name")
        if key:
            mcs.registry[key] = cls
        return cls


class BasePlugin(metaclass=PluginMeta):
    def run(self): ...


class JSONPlugin(BasePlugin):
    plugin_name = "json"
    def run(self): return "Processing JSON"


class XMLPlugin(BasePlugin):
    plugin_name = "xml"
    def run(self): return "Processing XML"


print(PluginMeta.registry)
# {'json': <class 'JSONPlugin'>, 'xml': <class 'XMLPlugin'>}
plugin = PluginMeta.registry["json"]()
print(plugin.run())        # Processing JSON
""",
    },

    # ── Strings ──────────────────────────────────────────────────────────
    {
        "category": "Strings",
        "title": "String Fundamentals & Slicing",
        "difficulty": "easy",
        "code": """\
# ── String basics (immutable sequence of Unicode codepoints)
s = "Hello, World!"
print(len(s))           # 13
print(s[0])             # 'H'   — positive index
print(s[-1])            # '!'   — negative index (from tail)
print(s[7:12])          # 'World'  — slice [start:stop]
print(s[:5])            # 'Hello'
print(s[7:])            # 'World!'
print(s[::-1])          # '!dlroW ,olleH'  — reversed
print(s[::2])           # 'Hlo ol!'        — every 2nd char

# ── Immutability — every 'change' creates a new object
s2 = s.replace("World", "Python")
print(s2)               # 'Hello, Python!'
print(s is s2)          # False — different objects

# ── Concatenation: + is O(n²) in a loop; use join()
parts = ["a", "b", "c", "d"]
bad  = ""
for p in parts:
    bad += p            # O(n²) — avoid

good = "".join(parts)   # O(n)  — preferred
print(good)             # 'abcd'

# ── String interning (CPython caches short identifier-like strings)
a = "hello"
b = "hello"
print(a is b)           # True  — same interned object
a = "hello world"
b = "hello world"
print(a is b)           # False — spaces prevent interning
print(a == b)           # True  — value equality always works

# ── Encoding / bytes
raw = "café"
encoded = raw.encode("utf-8")   # b'caf\\xc3\\xa9'
decoded = encoded.decode("utf-8")
print(decoded == raw)            # True
""",
    },
    {
        "category": "Strings",
        "title": "String Methods & Formatting",
        "difficulty": "easy",
        "code": """\
# ── Case transformation
s = "Hello World"
print(s.lower())         # 'hello world'
print(s.upper())         # 'HELLO WORLD'
print(s.title())         # 'Hello World'
print(s.swapcase())      # 'hELLO wORLD'

# ── Search & test
print(s.find("World"))   #  6  (-1 if not found)
print(s.index("World"))  #  6  (raises ValueError if not found)
print(s.count("l"))      #  3
print(s.startswith("He")) # True
print(s.endswith("ld"))   # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True

# ── Strip / split / join
text = "  hello   "
print(text.strip())       # 'hello'
print(text.lstrip())      # 'hello   '
print(text.rstrip())      # '  hello'

csv = "a,b,,c,d"
parts = csv.split(",")            # ['a','b','','c','d']
print("-".join(parts))            # 'a-b--c-d'
print("|".join(filter(None, parts)))  # 'a|b|c|d'  — skip blanks

# ── Replace & formatting
print("aabbcc".replace("b", "X"))  # 'aaXXcc'
print("aabbcc".replace("b", "X", 1))  # 'aaXbcc'  — max 1

name, score = "Alice", 98.5
print(f"Player {name} scored {score:.1f}")   # f-string (3.6+)
print("{} scored {:.1f}".format(name, score))
print("%-8s %5.1f" % (name, score))         # % style

# ── Multiline & raw strings
path  = r"C:\\Users\\ankus\\file.txt"  # raw — backslashes literal
query = (
    "SELECT *"
    " FROM users"
    " WHERE active = 1"
)          # implicit concatenation — no \\n
print(query)

# ── Useful builtins on strings
print(sorted("dcba"))     # ['a', 'b', 'c', 'd']
print(list(reversed("abc")))  # ['c', 'b', 'a']
print(ord('A'), chr(65))  # 65 'A'
""",
    },
    {
        "category": "Strings",
        "title": "String Algorithm Patterns",
        "difficulty": "medium",
        "code": """\
from collections import Counter

# ── 1. Palindrome check — O(n)
def is_palindrome(s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l] != s[r]:
            return False
        l += 1; r -= 1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False

# ── 2. Anagram check — O(n)
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Alternative: sorted(s) == sorted(t)  — O(n log n)
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False

# ── 3. Sliding window — longest substring without repeating chars
def length_of_longest_substring(s: str) -> int:
    seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")

# ── 4. KMP substring search — O(n + m)
def kmp_search(text: str, pattern: str) -> list[int]:
    def build_lps(p):
        lps = [0] * len(p)
        length, i = 0, 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1; lps[i] = length; i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0; i += 1
        return lps

    lps = build_lps(pattern)
    result, j = [], 0
    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            result.append(i - j + 1)
            j = lps[j - 1]
    return result

print(kmp_search("ababcabcababd", "ababd"))  # [7]
print(kmp_search("aaaaaa", "aaa"))          # [0, 1, 2, 3]

# ── 5. Group anagrams — O(n * k log k)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple, list] = {}
    for word in strs:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'],['tan','nat'],['bat']]
""",
    },

    # ── Bitwise Algorithms ─────────────────────────────────────────────
    {
        "category": "Bitwise Algorithms",
        "title": "Bitwise Operators & Fundamentals",
        "difficulty": "easy",
        "code": """\
# ── The 6 bitwise operators
a, b = 0b1010, 0b1100   # 10, 12

print(f"a     = {a:08b}  ({a})")
print(f"b     = {b:08b}  ({b})")
print(f"a & b = {a&b:08b}  ({a&b})")   # AND  → 8   (1000)
print(f"a | b = {a|b:08b}  ({a|b})")   # OR   → 14  (1110)
print(f"a ^ b = {a^b:08b}  ({a^b})")   # XOR  → 6   (0110)
print(f"~a    = {~a:>08b}  ({~a})")    # NOT  → -11 (two's complement)
print(f"a<<1  = {a<<1:08b}  ({a<<1})") # LEFT SHIFT  × 2
print(f"a>>1  = {a>>1:08b}  ({a>>1})") # RIGHT SHIFT ÷ 2

# ── Key XOR properties (memorise these)
# a ^ 0  = a       (identity)
# a ^ a  = 0       (self-inverse)
# a ^ b  = b ^ a   (commutative)
# (a^b)^c = a^(b^c) (associative)

x = 42
print(x ^ 0)   # 42
print(x ^ x)   # 0
print((x ^ 5) ^ 5)  # 42  — XOR is its own inverse

# ── In-place swap with XOR (no temp variable)
p, q = 15, 27
p ^= q; q ^= p; p ^= q
print(p, q)    # 27, 15

# ── Left / right shift = multiply / floor-divide by powers of 2
n = 6
print(n << 1)  # 12   (6 * 2)
print(n << 3)  # 48   (6 * 8)
print(n >> 1)  # 3    (6 // 2)
print(n >> 2)  # 1    (6 // 4)

# ── Two's complement in Python (arbitrary precision — no overflow)
k = 5
print(f" 5 in 8-bit two's complement: {5  & 0xFF:08b}")   # 00000101
print(f"-5 in 8-bit two's complement: {-5 & 0xFF:08b}")   # 11111011
print(f"~5 = {~k}")   # -6  (always -(n+1))

# ── Arithmetic vs logical right shift
print(-8 >> 1)   # -4  (arithmetic — sign bit extended)
print(8  >> 1)   #  4
""",
    },
    {
        "category": "Bitwise Algorithms",
        "title": "Bit Manipulation Tricks",
        "difficulty": "medium",
        "code": """\
# ── Core bit operations (i is 0-indexed from LSB)
def check_bit(n: int, i: int) -> bool:  return bool(n & (1 << i))
def set_bit(n: int, i: int) -> int:     return n | (1 << i)
def clear_bit(n: int, i: int) -> int:   return n & ~(1 << i)
def toggle_bit(n: int, i: int) -> int:  return n ^ (1 << i)
def update_bit(n: int, i: int, v: int) -> int:
    return clear_bit(n, i) | (v << i)

n = 0b10110100   # 180
print(f"n            = {n:08b}  ({n})")
print(f"check  bit 2 = {check_bit(n, 2)}")   # False
print(f"check  bit 4 = {check_bit(n, 4)}")   # True
print(f"set    bit 0 = {set_bit(n, 0):08b}") # 10110101
print(f"clear  bit 4 = {clear_bit(n, 4):08b}")  # 10100100
print(f"toggle bit 7 = {toggle_bit(n, 7):08b}") # 00110100

# ── Isolate / kill the lowest set bit
def lsb(n: int) -> int:       return n & (-n)      # isolate lowest 1-bit
def clear_lsb(n: int) -> int: return n & (n - 1)   # clear lowest 1-bit

print(f"lsb({n:b})       = {lsb(n):08b}")       # 00000100
print(f"clear_lsb({n:b}) = {clear_lsb(n):08b}") # 10110000

# ── Power of two check
def is_power_of_two(n: int) -> bool: return n > 0 and (n & (n - 1)) == 0

for v in [0, 1, 2, 3, 4, 16, 18]:
    print(f"{v:3d} → {is_power_of_two(v)}")

# ── Count set bits (Hamming weight) — Brian Kernighan's algorithm
def count_bits(n: int) -> int:
    count = 0
    while n:
        n &= n - 1   # clear lowest set bit each iteration
        count += 1
    return count

print(count_bits(0b11011011))  # 6
print(bin(255).count("1"))     # 8 (Python built-in)
print(255 .bit_count())        # 8 (Python 3.10+)

# ── Next power of two ≥ n
def next_pow2(n: int) -> int:
    if n <= 1: return 1
    n -= 1
    for shift in [1, 2, 4, 8, 16]:
        n |= n >> shift
    return n + 1

print([next_pow2(k) for k in [1, 3, 5, 8, 9, 17]])
# [1, 4, 8, 8, 16, 32]

# ── Bit mask for n lowest bits
def low_mask(n: int) -> int: return (1 << n) - 1

print(f"low_mask(4) = {low_mask(4):08b}")  # 00001111
print(f"low_mask(7) = {low_mask(7):08b}")  # 01111111
""",
    },
    {
        "category": "Bitwise Algorithms",
        "title": "Bitwise Problem Patterns",
        "difficulty": "medium",
        "code": """\
# ── 1. Find the single non-duplicate (XOR cancels pairs)
def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result

print(single_number([4, 1, 2, 1, 2]))   # 4
print(single_number([2, 2, 1]))          # 1

# ── 2. Find two non-duplicate numbers — O(n) time, O(1) space
def single_number_iii(nums: list[int]) -> list[int]:
    xor_all = 0
    for n in nums: xor_all ^= n       # xor of the two unique numbers
    diff_bit = xor_all & (-xor_all)   # any bit that differs between them
    a = 0
    for n in nums:
        if n & diff_bit:
            a ^= n
    return [a, xor_all ^ a]

print(sorted(single_number_iii([1, 2, 1, 3, 2, 5])))  # [3, 5]

# ── 3. Counting bits 0..n — O(n) DP
def count_bits_dp(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)  # dp[i//2] + last bit
    return dp

print(count_bits_dp(5))  # [0,1,1,2,1,2]

# ── 4. Reverse bits of a 32-bit integer
def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(reverse_bits(0b00000010100101000001111010011100))
# 964176192 = 0b00111001011110000010100101000000

# ── 5. Bitmask DP — travel salesman style (subset enumeration)
# Find min cost Hamiltonian path on small graph using bitmask DP
def tsp_bitmask(dist: list[list[int]]) -> int:
    n = len(dist)
    FULL = (1 << n) - 1
    INF  = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0    # start at city 0, visited = {0}

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF: continue
            if not (mask >> u & 1): continue
            for v in range(n):
                if mask >> v & 1: continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    return min(dp[FULL][v] + dist[v][0] for v in range(1, n))

cost = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print(tsp_bitmask(cost))  # 80

# ── 6. Sieve of Eratosthenes with bitset — memory-efficient
def sieve_bitset(limit: int) -> list[int]:
    is_composite = 0            # each bit = one number
    for i in range(2, int(limit**0.5) + 1):
        if not (is_composite >> i & 1):
            for j in range(i*i, limit + 1, i):
                is_composite |= 1 << j
    return [i for i in range(2, limit + 1) if not (is_composite >> i & 1)]

print(sieve_bitset(30))  # [2,3,5,7,11,13,17,19,23,29]
""",
    },

    # ── Pandas & NumPy ─────────────────────────────────────────────────
    {
        "category": "Pandas & NumPy",
        "title": "NumPy Array Fundamentals",
        "difficulty": "easy",
        "code": """\
import numpy as np

# ── Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
z = np.zeros((3, 4))          # 3x4 of zeros
o = np.ones((2, 3))           # 2x3 of ones
e = np.eye(4)                  # 4x4 identity matrix
r = np.arange(0, 10, 2)       # [0 2 4 6 8]
l = np.linspace(0, 1, 5)      # [0. .25 .5 .75 1.]

print(b.shape)    # (2, 3)
print(b.ndim)     # 2
print(b.dtype)    # float32
print(b.size)     # 6
print(b.nbytes)   # 24

# ── Indexing & slicing (same as Python, but returns views not copies)
m = np.arange(12).reshape(3, 4)
print(m[1, 2])         # 6   — row 1, col 2
print(m[:, 1])         # [1 5 9]  — entire col 1
print(m[0:2, 1:3])     # [[1 2],[5 6]]  — submatrix

# ── Universal functions (ufuncs) — element-wise, vectorised
x = np.array([1.0, 4.0, 9.0, 16.0])
print(np.sqrt(x))      # [1. 2. 3. 4.]
print(np.log2(x))      # [0. 2. 3.17... 4.]
print(x ** 2)          # [1. 16. 81. 256.]

# ── Broadcasting — shape rules: align from right, stretch dim-1
row = np.array([[1, 2, 3]])       # shape (1, 3)
col = np.array([[10], [20], [30]])  # shape (3, 1)
print(row + col)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# ── Aggregations
data = np.random.seed(0); data = np.random.randint(1, 100, (4, 5))
print(data.sum())            # total
print(data.sum(axis=0))      # column sums
print(data.sum(axis=1))      # row sums
print(data.mean(), data.std(), data.min(), data.max())

# ── Boolean masking (no Python loops needed)
scores = np.array([72, 85, 91, 63, 78, 95])
print(scores[scores >= 80])   # [85 91 95]
print(np.where(scores >= 80, "pass", "fail"))

# ── Linear algebra
A = np.array([[2, 1], [5, 3]])
b_vec = np.array([8, 21])
x_sol = np.linalg.solve(A, b_vec)   # solve Ax = b
print(x_sol)                         # [3. 2.]
print(np.allclose(A @ x_sol, b_vec)) # True
""",
    },
    {
        "category": "Pandas & NumPy",
        "title": "Pandas Series & DataFrame",
        "difficulty": "easy",
        "code": """\
import pandas as pd
import numpy as np

# ── Series — 1-D labeled array
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s["b"])           # 20  — label access
print(s[1])             # 20  — positional access (deprecated; use iloc)
print(s.iloc[1])        # 20  — preferred positional
print(s[s > 15])        # b 20, c 30, d 40  — boolean filter

# ── DataFrame — 2-D labeled table
data = {
    "name":   ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "score":  [88, 72, 95, 63, 81],
    "grade":  ["B", "C", "A", "D", "B"],
    "passed": [True, True, True, False, True],
}
df = pd.DataFrame(data)
print(df.shape)           # (5, 4)
print(df.dtypes)
print(df.describe())      # stats for numeric columns

# ── Selection
print(df["name"])                    # one column → Series
print(df[["name", "score"]])         # multiple columns → DataFrame
print(df.loc[0])                     # row by label
print(df.loc[1:3, ["name","score"]]) # label slice
print(df.iloc[0:2, 0:2])            # positional slice

# ── Boolean filtering  
print(df[df["score"] >= 80])
print(df[(df["score"] >= 70) & (df["passed"])])

# ── Adding / modifying columns
df["letter_grade"] = df["score"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 80 else "C" if x >= 70 else "F"
)
df["score_z"] = (df["score"] - df["score"].mean()) / df["score"].std()
print(df[["name", "score", "letter_grade", "score_z"]])

# ── Sorting & ranking
print(df.sort_values("score", ascending=False))
print(df["score"].rank(ascending=False))

# ── Basic aggregations
print(df["score"].mean())     # 79.8
print(df["score"].median())   # 81.0
print(df.groupby("grade")["score"].mean())
""",
    },
    {
        "category": "Pandas & NumPy",
        "title": "Pandas Data Wrangling",
        "difficulty": "medium",
        "code": """\
import pandas as pd
import numpy as np

# ── Missing data
df = pd.DataFrame({
    "A": [1, np.nan, 3, np.nan, 5],
    "B": [10, 20, np.nan, 40, 50],
    "C": ["x", "y", "y", np.nan, "x"],
})
print(df.isnull().sum())           # count NaN per column
df_drop = df.dropna()              # drop rows with any NaN
df_fill = df.fillna({"A": 0, "B": df["B"].mean(), "C": "unknown"})
df["A"] = df["A"].interpolate()    # linear interpolation

# ── GroupBy — split / apply / combine
students = pd.DataFrame({
    "name":  ["Alice","Bob","Carol","Dave","Eve","Frank"],
    "dept":  ["CS","CS","Math","Math","CS","Math"],
    "score": [88, 72, 95, 63, 91, 78],
})
grp = students.groupby("dept")
print(grp["score"].mean())         # mean score per dept
print(grp["score"].agg(["mean","max","min","count"]))
print(grp.apply(lambda g: g.nlargest(1, "score")))  # top student per dept

# ── Merge / join (like SQL)
orders = pd.DataFrame({"order_id":[1,2,3,4], "cust_id":[10,20,10,30],
                        "amount":[100,200,150,50]})
customers = pd.DataFrame({"cust_id":[10,20,40], "name":["Alice","Bob","Carol"]})

inner   = pd.merge(orders, customers, on="cust_id", how="inner")   # 3 rows
left    = pd.merge(orders, customers, on="cust_id", how="left")    # 4 rows
outer   = pd.merge(orders, customers, on="cust_id", how="outer")   # 5 rows
print(left[["order_id","name","amount"]])

# ── Pivot table
sales = pd.DataFrame({
    "region": ["N","N","S","S","N"],
    "product":["A","B","A","B","A"],
    "revenue":[100,200,150,180,120],
})
pivot = sales.pivot_table(values="revenue", index="region",
                           columns="product", aggfunc="sum", fill_value=0)
print(pivot)
# product     A    B
# region
# N         220  200
# S         150  180

# ── Time series
idx = pd.date_range("2024-01-01", periods=10, freq="D")
ts  = pd.Series(np.random.randn(10), index=idx)
print(ts["2024-01-03":"2024-01-07"])           # date slice
print(ts.resample("W").mean())                 # weekly means
print(ts.rolling(3).mean())                    # 3-day rolling average
print(ts.shift(1))                             # lag by 1 period

# ── Pipe for readable chains
result = (
    students
    .query("score >= 70")
    .assign(grade=lambda d: d["score"].apply(lambda x: "A" if x>=90 else "B"))
    .groupby(["dept","grade"])
    .size()
    .reset_index(name="count")
)
print(result)
""",
    },

    # ── Django (extended) ──────────────────────────────────────────────
    {
        "category": "Django",
        "title": "Function-Based Views & Forms",
        "difficulty": "easy",
        "code": """\
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Post
from .forms import PostForm

# ── Basic FBV pattern
def index(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    # raises 404 if missing
    return render(request, 'blog/detail.html', {'post': post})

# ── Create view with form validation
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form})

# ── ModelForm definition
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content', 'category', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters.")
        return title.strip()

# ── Rendering a form in a template (DTL)
# {% for field in form %}
#   <label>{{ field.label }}</label>
#   {{ field }}
#   {% if field.errors %}
#     <ul class="errors">{% for e in field.errors %}<li>{{ e }}</li>{% endfor %}</ul>
#   {% endif %}
# {% endfor %}
# {{ form.non_field_errors }}
""",
    },
    {
        "category": "Django",
        "title": "Django Authentication & Permissions",
        "difficulty": "medium",
        "code": """\
# ── Built-in auth URLs (project urls.py)
from django.contrib.auth import views as auth_views
from django.urls import path

auth_patterns = [
    path('login/',    auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/',   auth_views.LogoutView.as_view(), name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]

# ── Protecting FBVs
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

@permission_required('blog.add_post', raise_exception=True)
def create_post(request): ...

# ── Protecting CBVs
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model               = Post
    fields              = ['title', 'content']
    permission_required = 'blog.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# ── Custom user model (define before first migration)
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.username

# settings.py
# AUTH_USER_MODEL = 'accounts.CustomUser'

# ── Manual login / logout in a view
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
""",
    },
    {
        "category": "Django",
        "title": "Middleware, Caching & Settings",
        "difficulty": "medium",
        "code": """\
# ──────────────────────────────────────────────
# 1. Custom Middleware
# ──────────────────────────────────────────────
import time
from django.utils.deprecation import MiddlewareMixin

class TimingMiddleware:
    '''New-style middleware (callable).'''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        response['X-Request-Duration'] = f'{duration:.3f}s'
        return response

# settings.py MIDDLEWARE list (order matters — outermost first):
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'myapp.middleware.TimingMiddleware',          # ← custom
# ]

# ──────────────────────────────────────────────
# 2. Caching
# ──────────────────────────────────────────────
# settings.py — Redis backend
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

from django.views.decorators.cache import cache_page
from django.core.cache import cache

@cache_page(60 * 15)            # cache entire view for 15 minutes
def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/list.html', {'posts': posts})

# Low-level API
def get_popular_posts():
    key = 'popular_posts'
    posts = cache.get(key)
    if posts is None:
        posts = list(Post.objects.order_by('-views')[:10])
        cache.set(key, posts, timeout=300)    # 5 minutes
    return posts

cache.delete('popular_posts')               # invalidate key
cache.clear()                               # wipe entire cache

# ──────────────────────────────────────────────
# 3. Production settings snippet
# ──────────────────────────────────────────────
import os

SECRET_KEY    = os.environ['DJANGO_SECRET_KEY']        # never hardcode
DEBUG         = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

SECURE_SSL_REDIRECT    = True
CSRF_COOKIE_SECURE     = True
SESSION_COOKIE_SECURE  = True
SECURE_HSTS_SECONDS    = 31536000
X_FRAME_OPTIONS        = 'DENY'
""",
    },
    {
        "category": "Django",
        "title": "Django REST Framework (DRF)",
        "difficulty": "medium",
        "code": """\
# pip install djangorestframework
# INSTALLED_APPS += ['rest_framework']

from rest_framework import serializers, viewsets, permissions, routers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Category

# ── Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    author   = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model  = Post
        fields = ['id', 'title', 'slug', 'author', 'category',
                  'status', 'created_at']
        read_only_fields = ['slug', 'created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short.")
        return value

# ── ViewSet with custom action
class PostViewSet(viewsets.ModelViewSet):
    queryset            = Post.objects.filter(status='published')
    serializer_class    = PostSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def my_posts(self, request):
        qs = self.queryset.filter(author=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

# ── Router (auto-generates URLs)
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

# urls.py
# urlpatterns = [path('api/', include(router.urls))]

# ── Auto-generated endpoints:
# GET    /api/posts/          → list
# POST   /api/posts/          → create
# GET    /api/posts/{pk}/     → retrieve
# PUT    /api/posts/{pk}/     → update
# PATCH  /api/posts/{pk}/     → partial_update
# DELETE /api/posts/{pk}/     → destroy
# GET    /api/posts/my_posts/ → custom action
""",
    },
    {
        "category": "Django",
        "title": "Django Testing",
        "difficulty": "medium",
        "code": """\
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Category

User = get_user_model()

# ── Model test
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='alice', password='pass123'
        )
        self.cat = Category.objects.create(name='Tech', slug='tech')

    def test_str_representation(self):
        post = Post.objects.create(
            title='Hello', slug='hello',
            author=self.user, category=self.cat,
            content='Body', status='published',
        )
        self.assertEqual(str(post), 'Hello')

    def test_default_status_is_draft(self):
        post = Post(title='Draft', author=self.user)
        self.assertEqual(post.status, 'draft')

# ── View test
class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bob', password='pass123')
        self.cat = Category.objects.create(name='News', slug='news')
        self.post = Post.objects.create(
            title='Test Post', slug='test-post',
            author=self.user, category=self.cat,
            content='Content here', status='published',
        )

    def test_index_status_200(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_detail_page(self):
        url = reverse('blog:detail', args=[self.post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_create_requires_login(self):
        url = reverse('blog:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)    # redirect to login

    def test_create_post_authenticated(self):
        self.client.login(username='bob', password='pass123')
        response = self.client.post(reverse('blog:create'), {
            'title': 'New Post', 'content': 'Body', 'category': self.cat.pk
        })
        self.assertEqual(Post.objects.count(), 2)

# Run: python manage.py test blog
# Run with coverage: coverage run manage.py test && coverage report
""",
    },
    {
        "category": "Django",
        "title": "Django Admin Customisation",
        "difficulty": "easy",
        "code": """\
from django.contrib import admin
from .models import Post, Category, Tag

# ── Simple registration
admin.site.register(Category)
admin.site.register(Tag)

# ── Full customisation with @admin.register decorator
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display   = ['title', 'author', 'category', 'status', 'created_at']
    list_filter    = ['status', 'category', 'created_at']
    search_fields  = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}   # auto-fill slug from title
    date_hierarchy = 'created_at'
    ordering       = ['-created_at']
    list_per_page  = 25

    # Fieldsets control the form layout
    fieldsets = [
        ('Content', {'fields': ['title', 'slug', 'author', 'category', 'content']}),
        ('Publishing', {'fields': ['status', 'tags'], 'classes': ['collapse']}),
    ]

    # Inline relations
    from django.contrib.admin import TabularInline
    # class CommentInline(TabularInline):
    #     model = Comment; extra = 0

    # Bulk action
    @admin.action(description='Publish selected posts')
    def publish_posts(modeladmin, request, queryset):
        queryset.update(status='published')

    actions = ['publish_posts']

    # Override queryset to add annotations
    def get_queryset(self, request):
        from django.db.models import Count
        qs = super().get_queryset(request)
        return qs.annotate(comment_count=Count('comments'))

    @admin.display(description='Comments', ordering='comment_count')
    def comment_count(self, obj):
        return obj.comment_count

# Setup: python manage.py createsuperuser → /admin/
""",
    },
    {
        "category": "Django",
        "title": "Django Migrations & ORM Advanced",
        "difficulty": "hard",
        "code": """\
# ──────────────────────────────────────────────
# 1. Migration workflow
# ──────────────────────────────────────────────
# python manage.py makemigrations         # generate 0001_initial.py etc.
# python manage.py migrate                # apply to DB
# python manage.py showmigrations         # status overview
# python manage.py sqlmigrate blog 0001   # inspect SQL
# python manage.py migrate blog 0002      # roll back to 0002
# python manage.py squashmigrations blog 0001 0010  # compact history

# ── Example: data migration
from django.db import migrations

def set_default_status(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(status='').update(status='draft')

class Migration(migrations.Migration):
    dependencies = [('blog', '0003_post_status')]
    operations   = [migrations.RunPython(set_default_status,
                                         reverse_code=migrations.RunPython.noop)]

# ──────────────────────────────────────────────
# 2. Advanced ORM techniques
# ──────────────────────────────────────────────
from django.db.models import (
    Q, F, Count, Avg, Sum, Max, Min,
    Subquery, OuterRef, Exists, Prefetch, Window
)
from django.db.models.functions import Rank, TruncMonth

# Q objects — complex filters
Post.objects.filter(
    Q(status='published') & (Q(author__username='alice') | Q(category__slug='tech'))
)

# F expressions — reference field value in DB without Python roundtrip
Post.objects.filter(updated_at__gt=F('created_at'))
Post.objects.update(views=F('views') + 1)   # atomic increment

# Aggregation + annotation
from .models import Category
Category.objects.annotate(
    post_count=Count('post'),
    avg_views=Avg('post__views'),
).filter(post_count__gte=5).order_by('-post_count')

# Subquery — latest post per author
from django.db.models import OuterRef, Subquery
latest = Post.objects.filter(author=OuterRef('pk')).order_by('-created_at')
User.objects.annotate(latest_post_title=Subquery(latest.values('title')[:1]))

# Prefetch with custom queryset
published = Prefetch('post_set',
                     queryset=Post.objects.filter(status='published'),
                     to_attr='published_posts')
cats = Category.objects.prefetch_related(published)
for cat in cats:
    print(cat.name, len(cat.published_posts))

# Window function — rank posts by views within each category
Post.objects.annotate(
    rank=Window(expression=Rank(), partition_by=[F('category')],
                order_by=F('views').desc())
).filter(rank=1)   # top post per category
""",
    },

    # ── FastAPI ────────────────────────────────────────────────────────
    {
        "category": "FastAPI",
        "title": "FastAPI Basics & Path Operations",
        "difficulty": "easy",
        "code": """\
# pip install fastapi uvicorn[standard]
# Run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Blog API", version="1.0.0")

# ── Pydantic models (data validation + serialisation)
class PostCreate(BaseModel):
    title:   str
    content: str
    published: bool = False

class PostResponse(BaseModel):
    id:        int
    title:     str
    content:   str
    published: bool

    class Config:
        from_attributes = True    # Pydantic v2 (was orm_mode in v1)

# ── In-memory "database" for demo
_db: dict[int, dict] = {}
_next_id = 1

# ── Path operations (order matters — specific routes first)
@app.get("/")
def root():
    return {"message": "Welcome to Blog API"}

@app.get("/posts", response_model=list[PostResponse])
def list_posts():
    return list(_db.values())

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    if post_id not in _db:
        raise HTTPException(status_code=404, detail="Post not found")
    return _db[post_id]

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(payload: PostCreate):
    global _next_id
    post = {"id": _next_id, **payload.model_dump()}
    _db[_next_id] = post
    _next_id += 1
    return post

@app.put("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, payload: PostCreate):
    if post_id not in _db:
        raise HTTPException(status_code=404, detail="Post not found")
    _db[post_id].update(payload.model_dump())
    return _db[post_id]

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    if post_id not in _db:
        raise HTTPException(status_code=404, detail="Post not found")
    del _db[post_id]
""",
    },
    {
        "category": "FastAPI",
        "title": "FastAPI with SQLAlchemy & Alembic",
        "difficulty": "medium",
        "code": """\
# pip install sqlalchemy alembic psycopg2-binary

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.sql import func
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Generator

DATABASE_URL = "postgresql://user:pass@localhost/blogdb"
engine       = create_engine(DATABASE_URL)

class Base(DeclarativeBase): pass

# ── SQLAlchemy ORM model
class DBPost(Base):
    __tablename__ = "posts"
    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String(200), nullable=False)
    content    = Column(String, nullable=False)
    published  = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(engine)   # create tables

# ── Pydantic schemas
class PostSchema(BaseModel):
    title: str; content: str; published: bool = False

class PostOut(PostSchema):
    id: int; created_at: str
    class Config: from_attributes = True

# ── Dependency injection — db session per request
def get_db() -> Generator:
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.get("/posts", response_model=list[PostOut])
def list_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(DBPost).offset(skip).limit(limit).all()

@app.post("/posts", status_code=201, response_model=PostOut)
def create_post(payload: PostSchema, db: Session = Depends(get_db)):
    post = DBPost(**payload.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/posts/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(DBPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not found")
    return post

@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(DBPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(post); db.commit()

# Alembic init:  alembic init alembic
# Create rev:    alembic revision --autogenerate -m "create posts"
# Apply:         alembic upgrade head
""",
    },
    {
        "category": "FastAPI",
        "title": "FastAPI Authentication (JWT)",
        "difficulty": "medium",
        "code": """\
# pip install python-jose[cryptography] passlib[bcrypt]

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

SECRET_KEY = "super-secret-change-in-production"   # use env var in prod
ALGORITHM  = "HS256"
TOKEN_EXPIRE_MINUTES = 30

pwd_ctx    = CryptContext(schemes=["bcrypt"])
oauth2     = OAuth2PasswordBearer(tokenUrl="token")
app        = FastAPI()

# ── Simulated user store
USERS_DB = {
    "alice": {"username": "alice", "hashed_pw": pwd_ctx.hash("secret")},
}

class Token(BaseModel):
    access_token: str; token_type: str

class UserOut(BaseModel):
    username: str

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2)) -> UserOut:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload  = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None: raise credentials_exc
    except JWTError:
        raise credentials_exc
    user = USERS_DB.get(username)
    if user is None: raise credentials_exc
    return UserOut(username=username)

@app.post("/token", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS_DB.get(form.username)
    if not user or not verify_password(form.password, user["hashed_pw"]):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = create_access_token({"sub": user["username"]},
                                 timedelta(minutes=TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=UserOut)
def read_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@app.get("/protected")
def protected_route(user: UserOut = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}! This is protected."}
""",
    },
    {
        "category": "FastAPI",
        "title": "FastAPI Async, Background Tasks & Middleware",
        "difficulty": "medium",
        "code": """\
import asyncio
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import time

app = FastAPI()

# ── CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Custom middleware
@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.time() - start:.3f}s"
    return response

# ── Async endpoint — non-blocking I/O
@app.get("/async-demo")
async def async_demo():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://httpbin.org/get", timeout=5.0)
    return {"status": resp.status_code}

# ── Async DB simulation
async def fetch_from_db(item_id: int) -> dict:
    await asyncio.sleep(0.01)   # simulate DB latency
    return {"id": item_id, "name": f"Item {item_id}"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return await fetch_from_db(item_id)

# ── Background tasks (fire-and-forget after response)
def send_email_notification(email: str, message: str):
    # heavy work runs after response is sent
    print(f"Sending email to {email}: {message}")

@app.post("/subscribe")
async def subscribe(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_notification, email,
                              "Welcome to our newsletter!")
    return {"detail": "Subscribed — confirmation email on its way"}

# ── Global exception handler
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

# ── Lifespan events (replaces deprecated on_event)
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup: connecting to DB / loading models...")
    yield
    print("Shutdown: closing connections...")

app2 = FastAPI(lifespan=lifespan)
""",
    },
    {
        "category": "FastAPI",
        "title": "FastAPI Dependency Injection & Testing",
        "difficulty": "medium",
        "code": """\
from fastapi import FastAPI, Depends, Header, HTTPException, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# ── Simple dependency
def get_settings():
    return {"max_page_size": 100, "default_page_size": 10}

Settings = Annotated[dict, Depends(get_settings)]

@app.get("/items")
def list_items(
    page:    int = Query(1, ge=1),
    size:    int = Query(10, ge=1, le=100),
    cfg:     Settings = Depends(),
):
    limit = min(size, cfg["max_page_size"])
    return {"page": page, "size": limit, "items": []}

# ── Header dependency (e.g. API key)
async def verify_api_key(x_api_key: Annotated[str | None, Header()] = None):
    if x_api_key != "secret-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return x_api_key

@app.get("/admin", dependencies=[Depends(verify_api_key)])
def admin_panel():
    return {"message": "Welcome, admin"}

# ── Nested dependency chain
class DBSession:
    def __init__(self): self.connected = True
    def close(self): self.connected = False

def get_db():
    db = DBSession()
    try: yield db
    finally: db.close()

def get_repo(db: DBSession = Depends(get_db)):
    return {"db": db}

@app.get("/data")
def get_data(repo: dict = Depends(get_repo)):
    return {"using_db": repo["db"].connected}

# ── Testing with TestClient (synchronous, uses requests under the hood)
client = TestClient(app)

def test_list_items():
    resp = client.get("/items?page=1&size=5")
    assert resp.status_code == 200
    assert resp.json()["size"] == 5

def test_admin_no_key():
    resp = client.get("/admin")
    assert resp.status_code == 403

def test_admin_valid_key():
    resp = client.get("/admin", headers={"x-api-key": "secret-key"})
    assert resp.status_code == 200

# Run tests: pytest test_main.py -v
# OpenAPI docs auto-generated at: /docs  (Swagger UI)
#                                 /redoc (ReDoc)
""",
    },
    {
        "category": "FastAPI",
        "title": "FastAPI vs Django — Comparison",
        "difficulty": "easy",
        "code": """\
# ──────────────────────────────────────────────────────────────
# FastAPI vs Django — Side-by-Side Quick Reference
# ──────────────────────────────────────────────────────────────

# FEATURE COMPARISON
# ------------------------------------------------------------------
# Feature            | Django                  | FastAPI
# ------------------------------------------------------------------
# Type               | Full-stack framework    | Async API framework
# ORM                | Built-in Django ORM     | SQLAlchemy / Tortoise
# Admin Panel        | ✅ Built-in             | ❌ (use SQLAdmin/3rd)
# Auth System        | ✅ Built-in             | ❌ (implement/JWT)
# Data validation    | Forms / DRF serializer  | Pydantic (automatic)
# Async support      | Partial (ASGI)          | ✅ Native async/await
# Performance        | Good                    | Excellent (Starlette)
# API docs           | DRF browsable API       | ✅ Auto Swagger/ReDoc
# Learning curve     | Medium                  | Low-Medium
# Best for           | Full web apps           | Microservices/APIs
# ------------------------------------------------------------------

# ── Equivalent hello world
# Django (views.py):
from django.http import JsonResponse
def hello_django(request):
    return JsonResponse({"message": "Hello from Django"})

# FastAPI (main.py):
from fastapi import FastAPI
app_fa = FastAPI()

@app_fa.get("/hello")
def hello_fastapi():
    return {"message": "Hello from FastAPI"}

# ── Equivalent model + validation
# Django:
# class Post(models.Model):
#     title   = models.CharField(max_length=200)
#     content = models.TextField()
#
# FastAPI (Pydantic):
from pydantic import BaseModel, Field

class Post(BaseModel):
    title:   str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=1)

# ── When to choose which
# Use Django when:
#   - Building a full website (HTML + admin + auth)
#   - ORM + migrations out of the box is needed
#   - Team is already familiar with Django
#   - Monolithic app with many features

# Use FastAPI when:
#   - Building REST/GraphQL APIs or microservices
#   - Async I/O performance is critical
#   - Auto-generated API documentation is a priority
#   - Type safety + Pydantic validation throughout
""",
    },

    # ── Docker (DCA) ───────────────────────────────────────────────────
    {
        "category": "Docker",
        "title": "Docker Architecture & Installation",
        "difficulty": "easy",
        "code": """\
# ── Docker architecture overview
# Client → REST API (/var/run/docker.sock) → Dockerd → containerd → container
# All state:  /var/lib/docker
# Config:     /etc/docker/daemon.json

# ── Install Docker Engine (Ubuntu)
# apt-get update && apt-get install -y ca-certificates curl gnupg
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor \
#   -o /etc/apt/keyrings/docker.gpg
# apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin
# systemctl enable --now docker

# Allow non-root user
# usermod -aG docker $USER && newgrp docker

# ── daemon.json — configure the Docker engine
daemon_json_example = '''
{
  "log-driver": "json-file",
  "log-opts": {"max-size": "10m", "max-file": "3"},
  "storage-driver": "overlay2",
  "insecure-registries": [],
  "userns-remap": "default",
  "live-restore": true
}
'''
# File location: /etc/docker/daemon.json
# Reload:  systemctl reload docker   (or restart)

# ── Verify installation
# docker version          — client + server versions
# docker info             — full daemon configuration
# docker system df        — disk usage by images/containers/volumes
# docker system prune -a  — remove all unused resources

# ── Key concepts
# Image  — read-only layered template (stored in registry)
# Container — running instance of an image (writable layer on top)
# Registry   — stores + distributes images (Docker Hub, ECR, GCR, Harbor)
# Dockerfile — recipe to build an image
# Layer cache: order Dockerfile from LEAST-changing → MOST-changing instructions
""",
    },
    {
        "category": "Docker",
        "title": "Docker Image & Container Commands",
        "difficulty": "easy",
        "code": """\
# ════════════════════════════════
# IMAGE COMMANDS
# ════════════════════════════════

# Pull / push
# docker pull nginx:1.25
# docker push myrepo/myapp:1.0

# List & inspect
# docker images                         — list local images
# docker image ls --filter dangling=true
# docker image inspect nginx:1.25
# docker history nginx:1.25             — show layers

# Tag
# docker tag nginx:1.25 myrepo/nginx:custom

# Remove
# docker rmi nginx:1.25
# docker image prune                    — remove dangling images

# Save / load (offline transfer)
# docker save nginx:1.25 | gzip > nginx.tar.gz
# docker load < nginx.tar.gz

# ════════════════════════════════
# CONTAINER COMMANDS
# ════════════════════════════════

# Run in background, name it, map port, mount volume
# docker run -d --name web -p 8080:80 -v mydata:/data nginx

# Run interactively (auto-remove on exit)
# docker run -it --rm -e ENV=dev python:3.12-slim bash

# Run with resource limits
# docker run -d --memory="512m" --cpus="1.5" nginx

# ── Inspect & monitor
# docker ps                     — running containers
# docker ps -a                  — all containers
# docker stats                  — live CPU/MEM/NET/IO
# docker top web                — processes inside container
# docker logs web -f --tail=100
# docker exec -it web /bin/bash

# ── Copy files
# docker cp web:/etc/nginx/nginx.conf ./nginx.conf
# docker cp ./index.html web:/usr/share/nginx/html/

# ── Container details
# docker inspect web
# docker inspect web -f '{{.NetworkSettings.IPAddress}}'
# docker diff web                       — filesystem changes since start

# ── Lifecycle
# docker stop web    — SIGTERM → wait → SIGKILL
# docker kill web    — immediate SIGKILL
# docker rm web
# docker container prune                — remove all stopped containers

# ── Restart policies
# docker run -d --restart=always nginx
# docker run -d --restart=unless-stopped nginx
# docker run -d --restart=on-failure:3 nginx
""",
    },
    {
        "category": "Docker",
        "title": "Dockerfile Best Practices",
        "difficulty": "medium",
        "code": """\
# ── Multi-stage Dockerfile (Python/FastAPI example)

# Stage 1: build
# FROM python:3.12-slim AS builder
# WORKDIR /build
# COPY requirements.txt .
# RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: lean runtime image
# FROM python:3.12-slim
# RUN groupadd -r app && useradd -r -g app app
# WORKDIR /app
# COPY --from=builder /install /usr/local
# COPY --chown=app:app . .
# EXPOSE 8000
# HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
#   CMD curl -f http://localhost:8000/health || exit 1
# USER app
# CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# ── Key Dockerfile instructions
instructions = {
    "FROM":        "Base image — always pin a specific tag, never :latest",
    "RUN":         "Execute command → creates a new layer",
    "COPY":        "Copy files from host (prefer over ADD for local files)",
    "ADD":         "COPY + URL fetch + tar extraction (use sparingly)",
    "ENV":         "Persistent environment variable in the container",
    "ARG":         "Build-time variable (not persisted in final image)",
    "EXPOSE":      "Document which port the app listens on (informational)",
    "VOLUME":      "Declare a mount point (creates anonymous volume)",
    "USER":        "Switch to non-root user",
    "WORKDIR":     "Set working directory (creates if missing)",
    "CMD":         "Default command — overridable at docker run",
    "ENTRYPOINT":  "Fixed executable; CMD becomes its arguments",
    "HEALTHCHECK": "Define a health probe command",
}

# ── Build commands
# docker build -t myapp:1.0 .
# docker build --no-cache -t myapp:1.0 .
# docker build --build-arg VERSION=1.2 -t myapp:1.0 .
# docker buildx build --platform linux/amd64,linux/arm64 -t myapp:1.0 --push .

# ── .dockerignore (always maintain this!)
dockerignore_example = '''
.git
*.md
__pycache__/
*.pyc
.env
.env.*
secrets/
*.key
*.pem
node_modules/
tests/
'''
# Without .dockerignore, COPY . . sends .git + secrets to build context!

# ── Security rules
# 1. Use specific tags: FROM python:3.12.3-slim-bookworm
# 2. Run as non-root: RUN useradd -m -u 1000 app; USER app
# 3. Combine RUN commands to reduce layer count
# 4. Never ENV DB_PASSWORD=secret  (baked into image history!)
# 5. Pin apt packages; clean cache in same RUN layer
""",
    },
    {
        "category": "Docker",
        "title": "Docker Networking",
        "difficulty": "medium",
        "code": """\
# ── Network Drivers
network_drivers = {
    "bridge":  "Default; isolated container LAN on single host",
    "host":    "No isolation; container shares host network stack",
    "overlay": "Multi-host Swarm networking (encrypted tunnel)",
    "macvlan": "Assign real MAC address to container",
    "none":    "No networking whatsoever",
    "ipvlan":  "Layer 2/3 multi-host without MAC per container",
}

# ── CRITICAL: Always use user-defined bridge networks
# The default docker0 bridge does NOT support inter-container DNS.
# User-defined networks get built-in DNS — containers reach each other by name!

# Create custom bridge network
# docker network create my-net
# docker network create --driver bridge \
#   --subnet 172.20.0.0/16 --gateway 172.20.0.1 my-net

# Run containers on same network — DNS works automatically
# docker run -d --network my-net --name db postgres:15
# docker run -d --network my-net --name api myapp
# Inside api container:  curl http://db:5432   ← resolved by name!

# Connect existing container to a network
# docker network connect my-net app2
# docker network disconnect my-net app2

# Overlay network (Swarm multi-host)
# docker network create --driver overlay --attachable prod-net

# ── Network commands
# docker network ls
# docker network inspect bridge
# docker network inspect my-net --format '{{json .Containers}}'
# docker network rm my-net
# docker network prune          — remove unused networks

# ── Port mapping
# -p host_port:container_port
# docker run -p 8080:80 nginx          — map host:8080 → container:80
# docker run -p 127.0.0.1:8080:80 nginx  — bind only to localhost
# docker run -P nginx                  — auto-map all EXPOSE'd ports

# ── Inspect container IP
# docker inspect web -f '{{.NetworkSettings.IPAddress}}'
# docker inspect web -f '{{json .NetworkSettings.Networks}}'
# docker port web                      — show all port mappings
""",
    },
    {
        "category": "Docker",
        "title": "Docker Volumes & Storage",
        "difficulty": "medium",
        "code": """\
# ── Three storage types
storage = {
    "Volume":     "Managed by Docker (/var/lib/docker/volumes); persists; best for DB",
    "Bind Mount": "User-specified host path; persists; best for dev / config injection",
    "tmpfs":      "In-memory only; never persisted; best for secrets/caches",
}

# ── Volume commands
# docker volume create mydata
# docker volume ls
# docker volume inspect mydata
# docker volume rm mydata
# docker volume prune             — remove unused volumes

# ── Mount volume in container (--mount is preferred over -v)
# docker run -d \
#   --mount type=volume,source=mydata,target=/var/lib/postgresql/data \
#   postgres:15

# Shorthand -v syntax (still widely used)
# docker run -d -v mydata:/var/lib/postgresql/data postgres:15

# ── Bind mount (absolute host path required)
# docker run -d \
#   --mount type=bind,source=$(pwd)/config,target=/etc/app,readonly \
#   myapp

# ── tmpfs (memory-only, never written to disk)
# docker run -d \
#   --mount type=tmpfs,target=/run/secrets \
#   myapp

# ── Backup a named volume
# docker run --rm \
#   -v mydata:/volume \
#   -v $(pwd):/backup \
#   alpine tar czf /backup/mydata-backup.tar.gz -C /volume .

# Restore
# docker run --rm \
#   -v mydata:/volume \
#   -v $(pwd):/backup \
#   alpine tar xzf /backup/mydata-backup.tar.gz -C /volume

# ── Copy-on-Write: container writes only affect its own writable layer
# The base image layers are shared read-only across all containers
# Only the diff is stored per container — very efficient!
""",
    },
    {
        "category": "Docker",
        "title": "Docker Compose",
        "difficulty": "medium",
        "code": """\
# ── compose.yaml — multi-container app definition

compose_yaml = '''
services:
  web:
    build: .
    image: myapp:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379/0
    depends_on:
      db:
        condition: service_healthy     # waits for healthcheck to pass
      cache:
        condition: service_started
    volumes:
      - ./src:/app/src                 # bind mount for dev hot-reload
    networks:
      - backend

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  cache:
    image: redis:7-alpine
    networks:
      - backend

volumes:
  pgdata:

networks:
  backend:
    driver: bridge
'''

# ── Compose commands
# docker compose up -d              — start all services detached
# docker compose up -d --build      — rebuild images before start
# docker compose stop               — stop containers (keep them)
# docker compose down               — stop + remove containers
# docker compose down -v            — also remove named volumes
# docker compose ps                 — service status
# docker compose logs -f web        — follow logs for service
# docker compose logs --tail=50
# docker compose exec web bash      — shell into running service
# docker compose run --rm web pytest  — one-off command
# docker compose up -d --scale web=3  — run 3 web replicas
""",
    },
    {
        "category": "Docker",
        "title": "Docker Swarm & Security",
        "difficulty": "hard",
        "code": """\
# ════════════════════════════════
# DOCKER SWARM
# ════════════════════════════════

# Init the swarm (first manager node)
# docker swarm init --advertise-addr 192.168.1.10

# Get join tokens
# docker swarm join-token worker    — print worker join command
# docker swarm join-token manager   — print manager join command

# Join as worker (run on worker node)
# docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Node management
# docker node ls
# docker node update --availability drain node1   — gracefully evacuate
# docker node promote node2                       — promote to manager
# docker node demote node2

# Create a service (Swarm's equivalent of docker run)
# docker service create \
#   --name web --replicas 3 \
#   -p 80:80 \
#   --update-delay 10s --update-parallelism 1 \
#   nginx:1.25

# Rolling update
# docker service update --image nginx:1.26 web
# docker service rollback web               — undo last update

# Scale + inspect
# docker service scale web=5
# docker service ls
# docker service ps web
# docker service logs web --follow

# Deploy a stack (Compose file on Swarm)
# docker stack deploy -c compose.yaml myapp-stack
# docker stack ls && docker stack services myapp-stack
# docker stack rm myapp-stack

# Fault tolerance: always use ODD number of managers
# 3 managers → tolerates 1 failure
# 5 managers → tolerates 2 failures

# ════════════════════════════════
# DOCKER SECURITY
# ════════════════════════════════

# Run as non-root + drop all capabilities
# docker run -u 1000:1000 \
#   --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
#   --read-only \
#   --security-opt no-new-privileges \
#   nginx

# Swarm secrets (encrypted at rest + in transit, mounted as files)
# echo "superSecret" | docker secret create db_pass -
# docker secret create tls_cert ./cert.pem
# docker service create --secret db_pass myapp
# Mounted at: /run/secrets/db_pass  (in-memory tmpfs)
# NEVER store secrets in ENV variables — they appear in docker inspect!

# Image scanning
# docker scout cves myapp:1.0
# trivy image --severity HIGH,CRITICAL myapp:1.0

# Docker Content Trust (sign + verify images)
# export DOCKER_CONTENT_TRUST=1
# docker push myuser/myapp:1.0       — signs the image
# docker pull myuser/myapp:1.0       — verifies signature before pull

# Linux security primitives Docker uses:
security_primitives = {
    "Namespaces":   "Isolate pid, net, mnt, uts, ipc, user",
    "Cgroups":      "CPU, memory, I/O limits",
    "Seccomp":      "Syscall filtering (block ptrace, mount, etc.)",
    "Capabilities": "Fine-grained privilege control (drop ALL, add minimal)",
    "AppArmor":     "Mandatory access control profiles",
}
""",
    },

    # ── Kubernetes extended (CKA) ──────────────────────────────────────
    {
        "category": "Kubernetes",
        "title": "Kubernetes Architecture & Core Objects",
        "difficulty": "easy",
        "code": """\
# ── Kubernetes Architecture
# Control Plane:
#   kube-apiserver    — REST gateway; all clients talk here
#   etcd              — distributed key-value store (cluster state)
#   kube-scheduler    — assigns Pods to Nodes based on resources + taints
#   kube-controller-manager — runs Deployment/ReplicaSet/Node controllers
#   cloud-controller-manager — integrates with cloud provider APIs
#
# Worker Node:
#   kubelet      — node agent; ensures containers match PodSpec
#   kube-proxy   — maintains iptables/IPVS rules for Service VIPs
#   container runtime (containerd, CRI-O)

# ── Core Object Hierarchy
# Cluster → Namespace → Pod → Container
# Pod        — smallest schedulable unit; shares net + PID namespace
# ReplicaSet — ensures N pod replicas always running
# Deployment — manages ReplicaSets; rolling updates + rollbacks
# StatefulSet — ordered, stable-identity pods (databases)
# DaemonSet  — one pod per node (log agents, monitoring)
# Job        — run-to-completion workload
# CronJob    — scheduled Job

# ── Namespace operations
# kubectl get namespaces
# kubectl create namespace staging
# kubectl config set-context --current --namespace=staging

# ── Labels & selectors (the glue between objects)
# Every Service, ReplicaSet uses selectors to find its Pods
labels_example = {
    "app": "web",
    "version": "v2",
    "env": "prod",
    "tier": "frontend",
}

# kubectl get pods -l app=web,env=prod
# kubectl get pods --selector='env in (prod,staging)'

# ── Annotations (non-identifying metadata)
annotations_example = {
    "kubernetes.io/change-cause": "deploy v2.1.0",
    "prometheus.io/scrape": "true",
    "prometheus.io/port": "8080",
}
""",
    },
    {
        "category": "Kubernetes",
        "title": "Kubernetes Networking & Services",
        "difficulty": "medium",
        "code": """\
# ── Kubernetes Networking rules:
# 1. Every Pod gets a unique cluster-wide IP
# 2. Pods on any node can communicate without NAT
# 3. Services provide stable VIPs (virtual IPs) to a set of pods
# 4. CoreDNS resolves: <service>.<namespace>.svc.cluster.local

# ── Service types
service_types = {
    "ClusterIP":    "Internal VIP only (default) — no external access",
    "NodePort":     "Exposes on every node's IP:port (30000-32767)",
    "LoadBalancer": "Cloud LB; provisions external IP",
    "ExternalName": "DNS CNAME alias to external service",
    "Headless":     "ClusterIP: None — returns pod IPs directly (for StatefulSets)",
}

# ClusterIP Service YAML
cluster_ip_yaml = '''
apiVersion: v1
kind: Service
metadata:
  name: web-svc
spec:
  selector:
    app: web          # matches pods with this label
  ports:
    - port: 80        # Service port
      targetPort: 8080  # Container port
  type: ClusterIP
'''

# NodePort Service
node_port_yaml = '''
apiVersion: v1
kind: Service
metadata:
  name: web-nodeport
spec:
  selector:
    app: web
  type: NodePort
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080   # optional; auto-assigned if omitted
'''

# ── Ingress (HTTP routing at Layer 7)
ingress_yaml = '''
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-svc
                port:
                  number: 80
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-svc
                port:
                  number: 80
  tls:
    - hosts: [app.example.com]
      secretName: tls-secret
'''

# ── Network Policies (firewall rules for pods)
# Default: all pod-to-pod + pod-to-external traffic is ALLOWED
# Once a NetworkPolicy selects a pod, ONLY explicitly allowed traffic is permitted
# kubectl get networkpolicies -A
""",
    },
    {
        "category": "Kubernetes",
        "title": "Kubernetes Storage: PV, PVC & StorageClass",
        "difficulty": "medium",
        "code": """\
# ── Storage architecture
# PersistentVolume (PV)       — cluster-scoped storage resource (admin creates)
# PersistentVolumeClaim (PVC) — namespace-scoped request for storage (user creates)
# StorageClass                — defines a provisioner for dynamic PV creation

# ── PersistentVolume YAML
pv_yaml = '''
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce          # RWO: one node R/W  | ROX: many nodes R | RWX: many R/W
  persistentVolumeReclaimPolicy: Retain   # or Delete / Recycle
  storageClassName: standard
  hostPath:
    path: /mnt/data          # dev only; use cloud volumes in prod
'''

# ── PersistentVolumeClaim YAML
pvc_yaml = '''
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard   # empty string = no class; "" = use default
'''

# ── Use PVC in a Pod
pod_with_pvc = '''
apiVersion: v1
kind: Pod
metadata:
  name: db-pod
spec:
  containers:
    - name: postgres
      image: postgres:15
      env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
      volumeMounts:
        - mountPath: /var/lib/postgresql/data
          name: db-storage
  volumes:
    - name: db-storage
      persistentVolumeClaim:
        claimName: db-pvc
'''

# ── StorageClass (dynamic provisioning)
sc_yaml = '''
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
'''

# ── Key commands
# kubectl get pv,pvc -A
# kubectl describe pvc db-pvc
# kubectl delete pvc db-pvc     — triggers reclaimPolicy on bound PV
""",
    },
    {
        "category": "Kubernetes",
        "title": "Kubernetes RBAC & Security",
        "difficulty": "hard",
        "code": """\
# ── RBAC components
# ServiceAccount — identity for a Pod (default SA auto-created per namespace)
# Role           — namespace-scoped set of permissions
# ClusterRole    — cluster-scoped set of permissions (or reusable across namespaces)
# RoleBinding    — binds Role to Subject(s) within a namespace
# ClusterRoleBinding — binds ClusterRole to Subject(s) cluster-wide

# ── ServiceAccount
sa_yaml = '''
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-sa
  namespace: default
automountServiceAccountToken: false   # explicit opt-in is safer
'''

# ── Role (namespace-scoped)
role_yaml = '''
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
  - apiGroups: [""]            # "" = core API group
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "update", "patch"]
'''

# ── RoleBinding
rolebinding_yaml = '''
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
  - kind: ServiceAccount
    name: api-sa
    namespace: default
  - kind: User
    name: alice
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
'''

# ── Security Context (pod-level + container-level)
security_context_yaml = '''
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:1.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
          add: ["NET_BIND_SERVICE"]
      volumeMounts:
        - name: tmp
          mountPath: /tmp
  volumes:
    - name: tmp
      emptyDir: {}
'''

# ── Check permissions
# kubectl auth can-i create pods --as=system:serviceaccount:default:api-sa
# kubectl auth can-i --list --namespace=default
""",
    },
    {
        "category": "Kubernetes",
        "title": "Kubernetes Troubleshooting & CKA Patterns",
        "difficulty": "hard",
        "code": """\
# ════════════════════════════════
# TROUBLESHOOTING WORKFLOW
# ════════════════════════════════

# Pod not starting?
# kubectl get pods -n <ns> -o wide
# kubectl describe pod <pod>        — look for Events section
# kubectl logs <pod>                — stdout/stderr
# kubectl logs <pod> --previous     — crashed container logs
# kubectl logs <pod> -c <container> — multi-container pod

# Pod stuck in Pending?
# → No node has enough resources OR nodeSelector/affinity mismatch OR PVC not bound
# kubectl describe pod <pod> | grep -A5 Events

# Pod in CrashLoopBackOff?
# → App is crashing; check logs --previous; common: bad env var, missing secret/cm

# Node NotReady?
# kubectl describe node <node>      — look for conditions, disk pressure, memory
# kubectl get events -n kube-system --sort-by='.lastTimestamp'

# Service not reachable?
# kubectl get endpoints <svc>       — must show pod IPs; if empty, selector mismatch
# kubectl run test --rm -it --image=busybox -- wget -qO- http://<svc>:<port>

# ════════════════════════════════
# CKA EXAM SPEED PATTERNS
# ════════════════════════════════

# Generate YAML stubs instantly (don't write from scratch!)
# kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
# kubectl create deployment web --image=nginx:1.25 --replicas=3 --dry-run=client -o yaml
# kubectl create service clusterip web-svc --tcp=80:8080 --dry-run=client -o yaml
# kubectl create configmap app-cfg --from-literal=ENV=prod --dry-run=client -o yaml
# kubectl create secret generic db-sec --from-literal=password=s3cr3t --dry-run=client -o yaml

# Apply + verify
# kubectl apply -f manifest.yaml
# kubectl get all -n <namespace>
# kubectl rollout status deployment/web

# Rolling update & rollback
# kubectl set image deployment/web nginx=nginx:1.26
# kubectl rollout history deployment/web
# kubectl rollout undo deployment/web
# kubectl rollout undo deployment/web --to-revision=2

# Scale
# kubectl scale deployment/web --replicas=5
# kubectl autoscale deployment/web --min=2 --max=10 --cpu-percent=70

# Useful one-liners
# kubectl get pods --all-namespaces -o wide
# kubectl get events --sort-by='.lastTimestamp' -A
# kubectl top nodes && kubectl top pods -A
# kubectl exec -it <pod> -- /bin/sh
# kubectl port-forward svc/web-svc 8080:80

# ── Drain + cordon a node (maintenance)
# kubectl cordon node1             — prevent new pod scheduling
# kubectl drain node1 --ignore-daemonsets --delete-emptydir-data
# kubectl uncordon node1           — re-enable scheduling

# ── etcd backup (CKA exam task)
# ETCDCTL_API=3 etcdctl snapshot save /tmp/etcd-backup.db \
#   --endpoints=https://127.0.0.1:2379 \
#   --cacert=/etc/kubernetes/pki/etcd/ca.crt \
#   --cert=/etc/kubernetes/pki/etcd/server.crt \
#   --key=/etc/kubernetes/pki/etcd/server.key
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PYTHON DATA STRUCTURES — deep-dive implementations from QMD guides
    # ══════════════════════════════════════════════════════════════════

    # ── Array Fundamentals ─────────────────────────────────────────────
    {
        "category": "Array Fundamentals",
        "title": "Python List — Indexing & Slicing",
        "difficulty": "easy",
        "code": """\
import array

lst = [1, 2, 3, 4]                      # Python list  (any type)
arr = array.array('i', [1, 2, 3, 4])   # C-typed int array

# ── Positive & negative indexing
a = [10, 20, 30, 40, 50]
print(a[0], a[2], a[4])   # 10 30 50
print(a[-1])               # 50  (last)
print(a[-2])               # 40  (second last)

# ── Slicing  arr[start : stop : step]   stop is exclusive
print(a[1:4])     # [20, 30, 40]
print(a[:3])      # [10, 20, 30]
print(a[2:])      # [30, 40, 50]
print(a[::2])     # [10, 30, 50]   every 2nd element
print(a[::-1])    # [50, 40, 30, 20, 10]  reversed

# ── Slice assignment
a[1:3] = [200, 300]
print(a)          # [10, 200, 300, 40, 50]

# ── Negative-step slice
arr2 = [1, 2, 3, 4, 5]
print(arr2[4:1:-1])   # [5, 4, 3]

# ── O(1) random access
first = a[0]                  # 10
last  = a[-1]                 # 50
mid   = a[len(a) // 2]        # 300

# ── Common one-liners
a.append(60)                  # O(1) amortised
a.insert(0, 5)                # O(n) — shifts all right
val = a.pop()                 # O(1) remove last
val = a.pop(1)                # O(n) remove by index
a.remove(20)                  # O(n) remove first occurrence
del a[2]                      # O(n) delete by index
del a[1:3]                    # O(n) delete slice
a.extend([70, 80])            # O(k) extend with iterable
c = a + [90, 100]             # O(n+m) creates new list
""",
    },
    {
        "category": "Array Fundamentals",
        "title": "Array Search & Binary Search",
        "difficulty": "easy",
        "code": """\
import bisect

arr = [42, 17, 85, 3, 99, 56]

# ── O(n) linear search
def linear_search(arr, target):
    '''Return index of target or -1 if not found.'''
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search(arr, 85))   # 2
print(linear_search(arr, 7))    # -1


# ── O(log n) binary search (requires sorted array)
sorted_arr = [3, 17, 42, 56, 85, 99]
idx = bisect.bisect_left(sorted_arr, 56)
print(idx)                    # 3
print(sorted_arr[idx] == 56)  # True


# ── Manual binary search implementation
def binary_search(arr: list, target: int) -> int:
    '''Iterative binary search — O(log n).'''
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1    # discard left half
        else:
            hi = mid - 1    # discard right half

    return -1               # not found


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(arr, 23))   # 5
print(binary_search(arr, 10))   # -1

# ── bisect for insertion points
data = [1, 3, 5, 7, 9]
bisect.insort(data, 4)     # inserts 4 in sorted order
print(data)                # [1, 3, 4, 5, 7, 9]
""",
    },
    {
        "category": "Array Fundamentals",
        "title": "Sorting & Two-Pointer Techniques",
        "difficulty": "medium",
        "code": """\
arr = [64, 25, 12, 22, 11]

# ── In-place sort — Timsort O(n log n)
arr.sort()
print(arr)              # [11, 12, 22, 25, 64]

arr.sort(reverse=True)
print(arr)              # [64, 25, 22, 12, 11]

# ── sorted() — returns new list
arr2 = [3, 1, 4, 1, 5, 9, 2, 6]
asc  = sorted(arr2)
desc = sorted(arr2, reverse=True)

# ── Custom key
words = ["banana", "fig", "apple", "cherry"]
words.sort(key=len)
print(words)   # ['fig', 'apple', 'banana', 'cherry']

pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=lambda x: x[1])
print(pairs)   # [(3,'a'), (1,'b'), (2,'c')]


# ── Two-pointer: pair that sums to target (sorted array)
def two_sum_sorted(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if   s == target: return (lo, hi)
        elif s < target:  lo += 1
        else:             hi -= 1
    return None

print(two_sum_sorted([1, 3, 5, 7, 9, 11], 12))   # (1, 4)  → 3+9


# ── Reverse array in-place with two pointers
def reverse_inplace(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1; hi -= 1

arr = [1, 2, 3, 4, 5]
reverse_inplace(arr)
print(arr)   # [5, 4, 3, 2, 1]


# ── Remove duplicates from sorted array in-place
def remove_dupes(arr):
    if not arr: return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1   # new length
""",
    },
    {
        "category": "Array Fundamentals",
        "title": "Sliding Window & 2D Arrays",
        "difficulty": "medium",
        "code": """\
# ── Fixed-size window: max sum subarray of size k — O(n)
def max_sum_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # slide
        best = max(best, window_sum)
    return best

print(max_sum_window([2, 1, 5, 1, 3, 2], 3))   # 9  (5+1+3)


# ── Variable window: longest subarray with sum <= target
def longest_window(arr, target):
    lo = win_sum = best = 0
    for hi in range(len(arr)):
        win_sum += arr[hi]
        while win_sum > target:
            win_sum -= arr[lo]
            lo += 1
        best = max(best, hi - lo + 1)
    return best

print(longest_window([1, 2, 3, 4, 5], 9))   # 4


# ── 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])   # 6  (row 1, col 2)

# Initialise safely with list comprehension
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]
# NEVER do [[0]*cols]*rows — all rows share the same list object!

# Row-major traversal
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        print(matrix[r][c], end=" ")
    print()

# Transpose using zip
T = [list(row) for row in zip(*matrix)]
print(T)   # [[1,4,7],[2,5,8],[3,6,9]]
""",
    },
    {
        "category": "Array Fundamentals",
        "title": "Fixed-Size Array ADT Class",
        "difficulty": "hard",
        "code": """\
class Array:
    '''Fixed-capacity typed array ADT backed by a Python list.'''

    def __init__(self, capacity: int, fill=None):
        self._capacity = capacity
        self._data     = [fill] * capacity
        self._size     = 0

    def __len__(self):           return self._size
    def __getitem__(self, i):    return self._data[i]
    def __setitem__(self, i, v): self._data[i] = v
    def is_full(self):           return self._size == self._capacity
    def is_empty(self):          return self._size == 0

    def __repr__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"

    def append(self, val):
        '''Amortised O(1).'''
        if self.is_full(): raise OverflowError("Array is full")
        self._data[self._size] = val
        self._size += 1

    def insert(self, idx: int, val):
        '''O(n) — shift right.'''
        if self.is_full():    raise OverflowError("Array is full")
        if idx > self._size:  raise IndexError("Index out of range")
        for i in range(self._size, idx, -1):
            self._data[i] = self._data[i - 1]
        self._data[idx] = val
        self._size += 1

    def delete(self, idx: int):
        '''O(n) — shift left.'''
        if self.is_empty():   raise IndexError("Array is empty")
        if idx >= self._size: raise IndexError("Index out of range")
        val = self._data[idx]
        for i in range(idx, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val

    def search(self, val) -> int:
        '''O(n) linear search.'''
        for i in range(self._size):
            if self._data[i] == val:
                return i
        return -1


# ── Demo
arr = Array(capacity=8)
for v in [10, 20, 40, 50]: arr.append(v)
arr.insert(2, 30)   # [10, 20, 30, 40, 50]
arr.insert(0, 5)    # [5, 10, 20, 30, 40, 50]
print(arr.delete(0), arr)   # 5  [10, 20, 30, 40, 50]
print(arr.search(30))       # 2
""",
    },

    # ── Linked List Fundamentals ───────────────────────────────────────
    {
        "category": "Linked List Fundamentals",
        "title": "Node, Traversal & Search",
        "difficulty": "easy",
        "code": """\
# ── Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # reference to next node (None = end)

# ── Doubly Linked List Node (add prev pointer)
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# ── Linked List class shell
class LinkedList:
    def __init__(self):
        self.head = None   # entry point to the list

    def is_empty(self) -> bool:
        return self.head is None

    def __repr__(self):
        parts, curr = [], self.head
        while curr:
            parts.append(str(curr.data))
            curr = curr.next
        return " -> ".join(parts) + " -> None"

    # ── O(n) traversal
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    # ── O(n) linear search
    def search(self, target) -> bool:
        curr = self.head
        while curr:
            if curr.data == target:
                return True
            curr = curr.next
        return False


# ── Demo
ll = LinkedList()

# Manually wire nodes
n1 = Node(10); n2 = Node(20); n3 = Node(30)
n1.next = n2; n2.next = n3
ll.head = n1

ll.traverse()              # 10 20 30
print(repr(ll))            # 10 -> 20 -> 30 -> None
print(ll.search(20))       # True
print(ll.search(99))       # False
""",
    },
    {
        "category": "Linked List Fundamentals",
        "title": "Insert at Head, Tail & Position",
        "difficulty": "easy",
        "code": """\
def insert_at_head(self, data):
    '''Prepend a node — O(1).'''
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


def insert_at_tail(self, data):
    '''Append a node — O(n). Use tail pointer for O(1).'''
    new_node = Node(data)
    if self.is_empty():
        self.head = new_node; return
    curr = self.head
    while curr.next:
        curr = curr.next
    curr.next = new_node


def insert_at_position(self, data, pos):
    '''Insert at 0-based index — O(n).'''
    if pos == 0:
        self.insert_at_head(data); return
    new_node = Node(data)
    curr = self.head
    for _ in range(pos - 1):
        if curr is None:
            raise IndexError("Position out of range")
        curr = curr.next
    if curr is None:
        raise IndexError("Position out of range")
    new_node.next = curr.next
    curr.next     = new_node


# ── Optimisation: O(1) tail append with a tail pointer
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_tail(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node; return
        self.tail.next = node   # O(1) — no traversal
        self.tail      = node


# ── Demo
ll = LinkedList()
ll.insert_at_head(30)   # 30 -> None
ll.insert_at_head(20)   # 20 -> 30 -> None
ll.insert_at_head(10)   # 10 -> 20 -> 30 -> None
ll.insert_at_tail(40)   # 10 -> 20 -> 30 -> 40 -> None
ll.insert_at_position(25, 2)   # 10 -> 20 -> 25 -> 30 -> 40 -> None
print(ll)
""",
    },
    {
        "category": "Linked List Fundamentals",
        "title": "Delete by Value & Reverse In-Place",
        "difficulty": "medium",
        "code": """\
def delete_by_value(self, target):
    '''Remove first node where data == target — O(n).'''
    if self.is_empty():
        raise ValueError("List is empty")

    # Case 1: target is the head
    if self.head.data == target:
        self.head = self.head.next
        return

    # Case 2: target is in the middle or tail
    prev, curr = None, self.head
    while curr:
        if curr.data == target:
            prev.next = curr.next   # bypass node
            return
        prev, curr = curr, curr.next

    raise ValueError(f"{target} not found in list")


def reverse(self):
    '''Reverse the list in-place — O(n) time, O(1) space.'''
    prev    = None
    current = self.head

    while current:
        next_node    = current.next   # save next
        current.next = prev           # flip pointer
        prev         = current        # advance prev
        current      = next_node      # advance current

    self.head = prev   # prev is now the new head


# ── Demo
ll = LinkedList()
for v in [10, 20, 30, 40]: ll.insert_at_tail(v)

ll.delete_by_value(20)
print(ll)   # 10 -> 30 -> 40 -> None

ll.delete_by_value(10)
print(ll)   # 30 -> 40 -> None

for v in [1, 2, 3, 4, 5]:
    ll2 = LinkedList()
    [ll2.insert_at_tail(x) for x in [1,2,3,4,5]]
ll2.reverse()
print(ll2)  # 5 -> 4 -> 3 -> 2 -> 1 -> None
""",
    },
    {
        "category": "Linked List Fundamentals",
        "title": "Doubly & Circular Linked Lists",
        "difficulty": "medium",
        "code": """\
# ── Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self): return self.head is None

    def insert_at_tail(self, data):
        node = DNode(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev      = self.tail
            self.tail.next = node
            self.tail      = node

    def delete_tail(self):   # O(1) — impossible in singly LL!
        if self.tail is None: return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> "); curr = curr.next
        print("None")

    def traverse_backward(self):
        curr = self.tail
        while curr:
            print(curr.data, end=" <-> "); curr = curr.prev
        print("None")


dll = DoublyLinkedList()
for v in [10, 20, 30, 40]: dll.insert_at_tail(v)
dll.traverse_forward()    # 10 <-> 20 <-> 30 <-> 40 <-> None
dll.traverse_backward()   # 40 <-> 30 <-> 20 <-> 10 <-> None
dll.delete_tail()
dll.traverse_forward()    # 10 <-> 20 <-> 30 <-> None


# ── Circular Linked List
class CircularLinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node; node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head: curr = curr.next
            curr.next = node; node.next = self.head

    def traverse(self):
        if self.head is None: return
        curr = self.head
        while True:
            print(curr.data, end=" -> "); curr = curr.next
            if curr == self.head: break
        print("(HEAD)")


cll = CircularLinkedList()
for v in [1, 2, 3, 4]: cll.insert(v)
cll.traverse()   # 1 -> 2 -> 3 -> 4 -> (HEAD)
""",
    },
    {
        "category": "Linked List Fundamentals",
        "title": "Classic LL Problems: Cycle, Merge, Remove Nth",
        "difficulty": "hard",
        "code": """\
# ── Floyd's Cycle Detection — O(n) time, O(1) space
def has_cycle(head):
    '''Two-pointer: slow moves 1 step, fast moves 2 steps.
    If they meet, a cycle exists.
    '''
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:   # met inside the cycle
            return True
    return False


# ── Find the middle node — O(n) time, O(1) space
def find_middle(head):
    '''When fast reaches end, slow is at the middle.'''
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # middle node


# ── Merge two sorted linked lists — O(n+m)
def merge_sorted(l1, l2):
    dummy = Node(0)
    curr  = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2   # attach the remaining tail
    return dummy.next


# ── Remove N-th node from end — O(n) one-pass
def remove_nth_from_end(head, n):
    dummy      = Node(0); dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1):    # advance fast by n+1 steps
        fast = fast.next
    while fast:               # move both until fast reaches end
        fast = fast.next; slow = slow.next
    slow.next  = slow.next.next   # unlink the target
    return dummy.next


# ── Python built-in: collections.deque is a doubly linked list!
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)   # O(1) prepend
dq.append(4)       # O(1) append
dq.popleft()       # O(1) remove front
dq.pop()           # O(1) remove rear
""",
    },

    # ── Stack & Queue Fundamentals ───────────────────────────────────
    {
        "category": "Stack & Queue Fundamentals",
        "title": "Stack — List & LinkedStack Implementation",
        "difficulty": "easy",
        "code": """\
class Stack:
    '''Stack backed by a Python list. Top of stack = end of list.'''
    def __init__(self):
        self._data = []

    def is_empty(self) -> bool: return len(self._data) == 0
    def size(self)     -> int:  return len(self._data)
    def peek(self):
        if self.is_empty(): raise IndexError("peek from empty stack")
        return self._data[-1]

    def push(self, item) -> None:
        self._data.append(item)     # O(1) amortised

    def pop(self):
        if self.is_empty(): raise IndexError("pop from empty stack")
        return self._data.pop()     # O(1)

    def __len__(self):  return self.size()
    def __repr__(self): return f"Stack({self._data}  <- top)"


# ── Linked-list backed stack (no resizing overhead)
class _SNode:
    __slots__ = ("data", "next")
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self): return self._size == 0
    def peek(self):
        if self.is_empty(): raise IndexError("peek from empty stack")
        return self._head.data

    def push(self, item) -> None:
        self._head = _SNode(item, self._head)   # prepend O(1)
        self._size += 1

    def pop(self):
        if self.is_empty(): raise IndexError("pop from empty stack")
        val        = self._head.data
        self._head = self._head.next
        self._size -= 1
        return val


# ── Demo
s = Stack()
s.push(10); s.push(20); s.push(30)
print(s)            # Stack([10, 20, 30]  <- top)
print(s.peek())     # 30
print(s.pop())      # 30
print(len(s))       # 2

# Quick cheat sheet
lst = []
lst.append(x := 5)  # push  O(1)
lst.pop()            # pop   O(1)
lst[-1] if lst else None  # peek  O(1)
not lst              # is_empty O(1)
""",
    },
    {
        "category": "Stack & Queue Fundamentals",
        "title": "Stack Applications: Balanced Parens & Postfix",
        "difficulty": "medium",
        "code": """\
# ── Application 1: Balanced brackets
def is_balanced(expr: str) -> bool:
    stack  = Stack()
    OPEN   = set("([{")
    MATCH  = {')': '(', ']': '[', '}': '{'}
    for ch in expr:
        if ch in OPEN:
            stack.push(ch)             # push opening bracket
        elif ch in MATCH:
            if stack.is_empty():
                return False           # closing with nothing open
            if stack.pop() != MATCH[ch]:
                return False           # mismatched pair
    return stack.is_empty()            # unmatched opens remaining?


tests = [
    ("([]{})",  True),
    ("{[()]}",  True),
    ("([)]",    False),
    ("{",       False),
    ("]",       False),
]
for expr, expected in tests:
    result = is_balanced(expr)
    status = "ok" if result == expected else "FAIL"
    print(f"{status}  {expr!r:12s} -> {result}")


# ── Application 2: Evaluate Postfix (RPN) expression
def eval_postfix(tokens: list) -> float:
    '''e.g. ["3","4","+","5","*"] -> 35.0 meaning (3+4)*5'''
    stack = Stack()
    OPS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    for tok in tokens:
        if tok in OPS:
            b = stack.pop()    # second operand (popped first)
            a = stack.pop()    # first  operand
            stack.push(OPS[tok](a, b))
        else:
            stack.push(float(tok))
    return stack.pop()


# "3 4 + 5 *"  ->  (3+4)*5 = 35
print(eval_postfix(["3","4","+","5","*"]))   # 35.0

# "5 1 2 + 4 * + 3 -"  ->  14
print(eval_postfix(["5","1","2","+","4","*","+","3","-"]))  # 14.0
""",
    },
    {
        "category": "Stack & Queue Fundamentals",
        "title": "Queue — deque, LinkedQueue & CircularQueue",
        "difficulty": "easy",
        "code": """\
from collections import deque

# ── Queue backed by deque — all ops O(1)
class Queue:
    def __init__(self):
        self._data = deque()

    def is_empty(self) -> bool: return len(self._data) == 0
    def size(self)     -> int:  return len(self._data)
    def peek(self):
        if self.is_empty(): raise IndexError("peek from empty queue")
        return self._data[0]           # front element

    def enqueue(self, item) -> None:
        self._data.append(item)        # add to rear  O(1)

    def dequeue(self):
        if self.is_empty(): raise IndexError("dequeue from empty queue")
        return self._data.popleft()    # remove front O(1)

    def __len__(self): return self.size()
    def __repr__(self): return f"Queue(front-> {list(self._data)} <-rear)"


# ── Fixed-capacity circular queue (ring buffer)
class CircularQueue:
    def __init__(self, capacity: int):
        self._cap   = capacity + 1    # +1 to tell full vs empty
        self._data  = [None] * self._cap
        self._front = 0
        self._rear  = 0

    def is_empty(self): return self._front == self._rear
    def is_full(self):  return (self._rear + 1) % self._cap == self._front
    def size(self):     return (self._rear - self._front) % self._cap

    def enqueue(self, item) -> None:
        if self.is_full(): raise OverflowError("queue is full")
        self._data[self._rear] = item
        self._rear = (self._rear + 1) % self._cap   # wrap around

    def dequeue(self):
        if self.is_empty(): raise IndexError("empty queue")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        return val


# ── Demo
q = Queue()
q.enqueue(10); q.enqueue(20); q.enqueue(30)
print(q)              # Queue(front-> [10, 20, 30] <-rear)
print(q.peek())       # 10
print(q.dequeue())    # 10  (FIFO)
print(q.dequeue())    # 20

# Quick cheat sheet — never use list.pop(0)!
d = deque()
d.append(x := 1)   # enqueue  O(1)
d.popleft()         # dequeue  O(1)
d[0]                # peek     O(1)
not d               # is_empty O(1)
""",
    },
    {
        "category": "Stack & Queue Fundamentals",
        "title": "Priority Queue & threading.Queue",
        "difficulty": "medium",
        "code": """\
import heapq
from queue import Queue as TQueue, PriorityQueue, LifoQueue
import threading

# ── Min-heap priority queue
class MinPriorityQueue:
    '''Lowest priority number -> dequeued first.'''
    def __init__(self):
        self._heap = []
        self._idx  = 0     # tie-breaker for equal priorities

    def enqueue(self, item, priority: int) -> None:
        heapq.heappush(self._heap, (priority, self._idx, item))
        self._idx += 1

    def dequeue(self):
        if not self._heap: raise IndexError("empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return item, priority

    def peek(self):
        if not self._heap: raise IndexError("empty priority queue")
        return self._heap[0][2], self._heap[0][0]

    def __len__(self):  return len(self._heap)
    def is_empty(self): return len(self._heap) == 0


pq = MinPriorityQueue()
pq.enqueue("low",    3)
pq.enqueue("urgent", 1)
pq.enqueue("medium", 2)
while not pq.is_empty():
    print(pq.dequeue())   # urgent(1), medium(2), low(3)


# ── Standard library thread-safe queues
q  = TQueue(maxsize=5)
q.put(10); q.put(20)
print(q.get())       # 10  (FIFO, blocks if empty)

ls = LifoQueue()
ls.put(1); ls.put(2)
print(ls.get())      # 2   (LIFO / stack)

spq = PriorityQueue()
spq.put((1, "urgent")); spq.put((3, "low"))
print(spq.get())     # (1, 'urgent')


# ── Producer-Consumer pattern
def producer(q):
    for i in range(3): q.put(i)
    q.put(None)             # None as sentinel

def consumer(q):
    while (item := q.get()) is not None:
        print(f"consumed {item}")

shared_q = TQueue()
t1 = threading.Thread(target=producer, args=(shared_q,))
t2 = threading.Thread(target=consumer, args=(shared_q,))
t1.start(); t2.start()
t1.join();  t2.join()
""",
    },
    {
        "category": "Stack & Queue Fundamentals",
        "title": "Advanced: Queue via Stacks & Monotonic Deque",
        "difficulty": "hard",
        "code": """\
# ── Queue implemented with two stacks — amortised O(1)
class QueueViaStacks:
    def __init__(self):
        self._inbox  = Stack()   # enqueue here
        self._outbox = Stack()   # dequeue from here

    def enqueue(self, item) -> None:
        self._inbox.push(item)

    def _transfer(self):
        '''Move everything to outbox (reverses order = FIFO).'''
        if self._outbox.is_empty():
            while not self._inbox.is_empty():
                self._outbox.push(self._inbox.pop())

    def dequeue(self):
        self._transfer()
        if self._outbox.is_empty(): raise IndexError("empty queue")
        return self._outbox.pop()

    def peek(self):
        self._transfer(); return self._outbox.peek()

    def is_empty(self):
        return self._inbox.is_empty() and self._outbox.is_empty()


q = QueueViaStacks()
for v in [10, 20, 30]: q.enqueue(v)
print(q.dequeue())   # 10  (FIFO)
print(q.dequeue())   # 20


# ── Monotonic deque — sliding window maximum O(n)
def sliding_max(nums: list, k: int) -> list:
    '''O(n) — deque stores indices, front = current maximum.'''
    d, result = deque(), []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()       # discard smaller elements from rear
        d.append(i)
        if d[0] == i - k:
            d.popleft()   # discard out-of-window index
        if i >= k - 1:
            result.append(nums[d[0]])   # front = maximum in window
    return result

print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]


# ── Next greater element — monotonic stack O(n)
def next_greater(arr: list) -> list:
    n, result = len(arr), [-1] * len(arr)
    stack = Stack()    # stores indices
    for i in range(n):
        while not stack.is_empty() and arr[stack.peek()] < arr[i]:
            idx         = stack.pop()
            result[idx] = arr[i]   # arr[i] is the next greater
        stack.push(i)
    return result

print(next_greater([4, 5, 2, 10, 8]))   # [5, 10, 10, -1, -1]
""",
    },

    # ── Hash Table Fundamentals ────────────────────────────────────────
    {
        "category": "Hash Table Fundamentals",
        "title": "Hash Functions & Collision Concepts",
        "difficulty": "easy",
        "code": """\
# ── How hashing works
# index = hash(key) % capacity

# ── Example: capacity = 8
examples = {
    "Alice": hash("Alice") % 8,
    "Bob":   hash("Bob")   % 8,
    42:      hash(42)      % 8,
}
print(examples)   # shows bucket indices (some may collide)

# ── Polynomial rolling hash (manual implementation)
def str_hash(key: str, cap: int) -> int:
    '''Simple polynomial rolling hash.'''
    h, p = 0, 31
    for ch in key:
        h = (h * p + ord(ch)) % cap
    return h

print(str_hash("Alice", 8))
print(str_hash("Bob",   8))

# ── Only immutable objects are hashable in Python
d = {}
d[(1, 2)] = "tuple key ok"     # tuple: hashable
# d[[1,2]] = "oops"            # list: TypeError!

# ── Collision strategies
collision_strategies = {
    "Separate Chaining": "Each bucket holds a list of (key, value) pairs",
    "Linear Probing":    "probe (h + i) % cap — suffers primary clustering",
    "Quadratic Probing": "probe (h + i^2) % cap — reduces clustering",
    "Double Hashing":    "probe (h + i*h2(k)) % cap — eliminates clustering",
}

# ── Load factor controls resize
# lambda = n / capacity
# Python dict resizes at lambda ~ 0.67 (keeps operations fast)
# Our HashTable resizes at lambda >= 0.75

# ── Conceptual bucket structure
table = [
    [],                           # bucket 0
    [],                           # bucket 1
    [("Alice", "555-1234"),       # bucket 2
     (42,      "meaning")],       # collision: chained!
    [],
    [("Bob", "555-5678")],        # bucket 4
]
""",
    },
    {
        "category": "Hash Table Fundamentals",
        "title": "HashTable Class — put, get, delete",
        "difficulty": "medium",
        "code": """\
class HashTable:
    '''Hash table with separate chaining.'''
    LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size     = 0
        self._buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key) -> int:
        return hash(key) % self.capacity

    @property
    def load_factor(self) -> float:
        return self.size / self.capacity

    def __len__(self):       return self.size
    def __contains__(self, key): return self.get(key) is not None
    def __repr__(self):
        pairs = [(k, v) for b in self._buckets for k, v in b]
        return "{" + ", ".join(f"{k!r}: {v!r}" for k, v in pairs) + "}"

    def put(self, key, value) -> None:
        '''Insert or update — O(1) average.'''
        idx, bucket = self._hash(key), self._buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value); return   # update
        bucket.append((key, value))
        self.size += 1
        if self.load_factor >= self.LOAD_FACTOR_THRESHOLD:
            self._resize()

    def get(self, key, default=None):
        '''Return value for key, or default — O(1) average.'''
        for k, v in self._buckets[self._hash(key)]:
            if k == key: return v
        return default

    def __getitem__(self, key):
        v = self.get(key, sentinel := object())
        if v is sentinel: raise KeyError(key)
        return v

    def __setitem__(self, key, value): self.put(key, value)

    def delete(self, key) -> bool:
        '''Remove key; return True if found — O(1) average.'''
        idx, bucket = self._hash(key), self._buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i); self.size -= 1; return True
        return False

    def __delitem__(self, key):
        if not self.delete(key): raise KeyError(key)


# ── Demo
ht = HashTable()
ht["name"] = "Alice"
ht["age"]  = 30
ht["city"] = "NYC"

print(ht["name"])          # Alice
print(len(ht))             # 3
del ht["age"]
print("age" in ht)         # False
print(ht)
""",
    },
    {
        "category": "Hash Table Fundamentals",
        "title": "Resize, Open Addressing & Iteration",
        "difficulty": "hard",
        "code": """\
def _resize(self) -> None:
    '''Double capacity and rehash all entries.'''
    old_buckets   = self._buckets
    self.capacity *= 2
    self._buckets  = [[] for _ in range(self.capacity)]
    self.size      = 0              # put() will re-count
    for bucket in old_buckets:
        for key, value in bucket:
            self.put(key, value)    # re-insert with new hash


# ── Iteration (keys, values, items)
def __iter__(self):
    for bucket in self._buckets:
        for key, _ in bucket:
            yield key

def keys(self):   return list(self)
def values(self): return [self.get(k) for k in self]
def items(self):  return [(k, self.get(k)) for k in self]


# ── Open addressing with linear probing + tombstones
class OpenHashTable:
    _DELETED = object()   # tombstone sentinel

    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size     = 0
        self._slots   = [None] * capacity

    def _hash(self, key, i=0) -> int:
        return (hash(key) + i) % self.capacity   # linear probe

    def put(self, key, value) -> None:
        for i in range(self.capacity):
            idx   = self._hash(key, i)
            entry = self._slots[idx]
            if entry is None or entry is self._DELETED:
                self._slots[idx] = (key, value)
                self.size += 1; return
            if entry[0] == key:
                self._slots[idx] = (key, value); return
        raise OverflowError("Hash table is full")

    def get(self, key, default=None):
        for i in range(self.capacity):
            idx   = self._hash(key, i)
            entry = self._slots[idx]
            if entry is None:               return default
            if entry is self._DELETED:      continue
            if entry[0] == key:             return entry[1]
        return default


# ── Verify resize works
ht = HashTable(capacity=4)
for ch in "abcdef":
    ht[ch] = ord(ch)    # triggers resize at lambda=0.75
print(ht.capacity)      # 16  (doubled twice: 4->8->16)
print(ht.load_factor)   # ~0.375  (comfortable)
""",
    },
    {
        "category": "Hash Table Fundamentals",
        "title": "Hash Table Applications",
        "difficulty": "easy",
        "code": """\
from collections import Counter, defaultdict

# ── Two Sum in O(n) — hash table lookup
def two_sum(nums, target):
    seen = {}                      # val -> index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]


# ── Word frequency counter
words = "the quick brown fox jumps over the lazy dog".split()
freq  = Counter(words)
print(freq.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]


# ── Group anagrams — all words with same sorted chars share a key
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]


# ── Grouping with defaultdict
groups = defaultdict(list)
data = [("a", 1), ("b", 2), ("a", 3)]
for k, v in data:
    groups[k].append(v)
print(dict(groups))   # {'a': [1, 3], 'b': [2]}


# ── Memoization with a dict
def fib(n, memo={}):
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print([fib(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
""",
    },

    # ── Graph Fundamentals ─────────────────────────────────────────────
    {
        "category": "Graph Fundamentals",
        "title": "Graph Representations",
        "difficulty": "easy",
        "code": """\
# ── Three ways to store a graph ──────────────────────────────

# 1. Adjacency List  (most common for sparse graphs)
#    Space: O(V + E)   Neighbour lookup: O(deg)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'F'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'B'],
}

# 2. Adjacency Matrix  (dense graphs, O(1) edge query)
#    Space: O(V^2)   edge(u,v)?: O(1)
#       A  B  C  D
mat = [[0, 1, 1, 0],   # A
       [1, 0, 0, 1],   # B
       [1, 0, 0, 1],   # C
       [0, 1, 1, 0]]   # D

# 3. Edge List  (good for Kruskal's MST)
#    Space: O(E)
edges = [('A','B'), ('A','C'), ('B','D'), ('C','D')]

# ── Comparison
#            | Adj List | Adj Matrix | Edge List
# Space      | O(V+E)   | O(V^2)     | O(E)
# edge(u,v)? | O(deg)   | O(1)       | O(E)
# neighbours | O(deg)   | O(V)       | O(E)
# Add edge   | O(1)     | O(1)       | O(1)
# Best for   | Sparse   | Dense      | Kruskal

# Rule: adjacency list is almost always the right choice

# ── defaultdict makes adjacency list construction easy
from collections import defaultdict
g = defaultdict(list)
for u, v in [('A','B'), ('A','C'), ('B','D')]:
    g[u].append(v)
    g[v].append(u)   # undirected: add both directions
print(dict(g))
""",
    },
    {
        "category": "Graph Fundamentals",
        "title": "Graph Class Implementation",
        "difficulty": "medium",
        "code": """\
class Graph:
    '''Adjacency list graph — directed or undirected, weighted or unweighted.'''

    def __init__(self, directed: bool = False):
        self._adj       = {}        # vertex -> [(neighbour, weight), ...]
        self._directed  = directed
        self._edge_count = 0

    # ── Vertex operations
    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = []

    def remove_vertex(self, v):
        if v not in self._adj: return
        for u in self._adj:
            self._adj[u] = [(n, w) for n, w in self._adj[u] if n != v]
        del self._adj[v]

    # ── Edge operations
    def add_edge(self, u, v, weight: float = 1) -> None:
        self.add_vertex(u); self.add_vertex(v)
        self._adj[u].append((v, weight))
        if not self._directed:
            self._adj[v].append((u, weight))
        self._edge_count += 1

    def remove_edge(self, u, v) -> None:
        self._adj[u] = [(n, w) for n, w in self._adj[u] if n != v]
        if not self._directed:
            self._adj[v] = [(n, w) for n, w in self._adj[v] if n != u]
        self._edge_count -= 1

    # ── Queries
    def neighbours(self, v) -> list:
        return [n for n, _ in self._adj.get(v, [])]

    def has_edge(self, u, v) -> bool:
        return any(n == v for n, _ in self._adj.get(u, []))

    def vertices(self) -> list:    return list(self._adj)
    def num_vertices(self) -> int: return len(self._adj)
    def num_edges(self)    -> int: return self._edge_count


# ── Build and query
g = Graph(directed=False)
for u, v in [('A','B'),('A','C'),('B','D'),('C','D'),('D','E'),('E','F'),('B','F')]:
    g.add_edge(u, v)

print(g.num_vertices())     # 6
print(g.num_edges())        # 7
print(g.neighbours('B'))    # ['A', 'D', 'F']
print(g.has_edge('A', 'D')) # False

# ── Convenience: build from adjacency dict
def from_dict(d: dict, directed=False) -> Graph:
    gr = Graph(directed)
    for u, nbrs in d.items():
        for v in nbrs:
            gr.add_edge(u, v)
    return gr
""",
    },
    {
        "category": "Graph Fundamentals",
        "title": "BFS, DFS & Connected Components",
        "difficulty": "medium",
        "code": """\
from collections import deque

# ── BFS — visit all vertices level by level — O(V+E)
def bfs(graph: Graph, start) -> list:
    visited = {start}
    queue   = deque([start])
    order   = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for nbr in graph.neighbours(v):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order


def bfs_distances(graph: Graph, start) -> dict:
    '''Shortest hop-count from start to every reachable vertex.'''
    dist  = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nbr in graph.neighbours(v):
            if nbr not in dist:
                dist[nbr] = dist[v] + 1
                queue.append(nbr)
    return dist


# ── DFS recursive — explores one branch fully before next — O(V+E)
def dfs_rec(graph: Graph, v, visited: set = None) -> list:
    if visited is None: visited = set()
    visited.add(v); result = [v]
    for nbr in graph.neighbours(v):
        if nbr not in visited:
            result += dfs_rec(graph, nbr, visited)
    return result


# ── DFS iterative — avoids Python recursion limit
def dfs_iter(graph: Graph, start) -> list:
    visited, stack, order = set(), [start], []
    while stack:
        v = stack.pop()
        if v in visited: continue
        visited.add(v); order.append(v)
        for nbr in reversed(graph.neighbours(v)):
            if nbr not in visited: stack.append(nbr)
    return order


# ── Connected components — O(V+E)
def connected_components(graph: Graph) -> list[list]:
    visited, components = set(), []
    for v in graph.vertices():
        if v not in visited:
            component, queue = [], deque([v])
            visited.add(v)
            while queue:
                u = queue.popleft(); component.append(u)
                for nbr in graph.neighbours(u):
                    if nbr not in visited:
                        visited.add(nbr); queue.append(nbr)
            components.append(component)
    return components


# BFS vs DFS comparison
# BFS: queue, shortest path (unweighted), O(width) memory
# DFS: stack/recursion, topological sort, O(height) memory
""",
    },
    {
        "category": "Graph Fundamentals",
        "title": "Cycle Detection & Topological Sort",
        "difficulty": "hard",
        "code": """\
from collections import deque

# ── Cycle detection — undirected (DFS with parent tracking)
def has_cycle_undirected(graph: Graph) -> bool:
    visited = set()
    def dfs(v, parent):
        visited.add(v)
        for nbr in graph.neighbours(v):
            if nbr not in visited:
                if dfs(nbr, v): return True
            elif nbr != parent:   # back edge found!
                return True
        return False
    return any(dfs(v, None) for v in graph.vertices() if v not in visited)


# ── Cycle detection — directed (white/grey/black colouring)
def has_cycle_directed(graph: Graph) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph.vertices()}
    def dfs(v):
        color[v] = GREY
        for nbr in graph.neighbours(v):
            if color[nbr] == GREY:  return True    # back edge!
            if color[nbr] == WHITE and dfs(nbr): return True
        color[v] = BLACK
        return False
    return any(dfs(v) for v in graph.vertices() if color[v] == WHITE)


# ── Topological Sort — Kahn's algorithm (BFS / in-degree) O(V+E)
def topo_sort_kahn(graph: Graph) -> list | None:
    '''Returns topological order, or None if cycle exists.'''
    in_deg = {v: 0 for v in graph.vertices()}
    for v in graph.vertices():
        for nbr in graph.neighbours(v):
            in_deg[nbr] += 1

    queue  = deque(v for v, d in in_deg.items() if d == 0)
    result = []
    while queue:
        v = queue.popleft(); result.append(v)
        for nbr in graph.neighbours(v):
            in_deg[nbr] -= 1
            if in_deg[nbr] == 0: queue.append(nbr)

    return result if len(result) == graph.num_vertices() else None


# ── Topological Sort — DFS post-order O(V+E)
def topo_sort_dfs(graph: Graph) -> list:
    visited, stack = set(), []
    def dfs(v):
        visited.add(v)
        for nbr in graph.neighbours(v):
            if nbr not in visited: dfs(nbr)
        stack.append(v)    # push AFTER all children
    for v in graph.vertices():
        if v not in visited: dfs(v)
    return stack[::-1]     # reverse = topological order
""",
    },
    {
        "category": "Graph Fundamentals",
        "title": "Shortest Paths: Dijkstra & Bellman-Ford",
        "difficulty": "hard",
        "code": """\
import heapq

# ── Dijkstra — O((V+E) log V) — non-negative weights only
def dijkstra(graph: Graph, start) -> tuple[dict, dict]:
    '''Returns (dist, prev) for path reconstruction.'''
    dist = {v: float('inf') for v in graph.vertices()}
    prev = {v: None         for v in graph.vertices()}
    dist[start] = 0
    heap = [(0, start)]    # (distance, vertex)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue   # stale entry
        for nbr, w in graph._adj[u]:
            new_d = dist[u] + w
            if new_d < dist[nbr]:
                dist[nbr] = new_d; prev[nbr] = u
                heapq.heappush(heap, (new_d, nbr))
    return dist, prev


def reconstruct(prev: dict, target) -> list:
    path, v = [], target
    while v is not None: path.append(v); v = prev[v]
    return path[::-1]


# ── Bellman-Ford — O(V*E) — handles negative weights
def bellman_ford(graph: Graph, start) -> tuple[dict, bool]:
    '''Returns (dist, has_negative_cycle).'''
    dist = {v: float('inf') for v in graph.vertices()}
    dist[start] = 0; V = graph.num_vertices()

    for _ in range(V - 1):          # relax V-1 times
        updated = False
        for u in graph.vertices():
            for nbr, w in graph._adj[u]:
                if dist[u] + w < dist[nbr]:
                    dist[nbr] = dist[u] + w; updated = True
        if not updated: break        # early exit

    # V-th pass: detect negative cycle
    for u in graph.vertices():
        for nbr, w in graph._adj[u]:
            if dist[u] + w < dist[nbr]:
                return dist, True    # negative cycle!
    return dist, False


# ── Demo — weighted directed graph
wg = Graph(directed=True)
for u, v, w in [('A','B',4),('A','C',2),('B','D',3),('C','B',1),('C','D',5),('D','E',2)]:
    wg.add_edge(u, v, w)

dist, prev = dijkstra(wg, 'A')
print(dist)                       # A:0 B:3 C:2 D:6 E:8
print(reconstruct(prev, 'D'))     # ['A', 'C', 'B', 'D']
""",
    },
    {
        "category": "Graph Fundamentals",
        "title": "Union-Find, MST & Grid BFS",
        "difficulty": "hard",
        "code": """\
# ── Union-Find with rank + path compression — O(alpha(n)) per op
class UnionFind:
    def __init__(self, vertices):
        self.parent     = {v: v for v in vertices}
        self.rank       = {v: 0 for v in vertices}
        self.components = len(vertices)

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # path compress
        return self.parent[v]

    def union(self, u, v) -> bool:
        '''Returns False if already same component (cycle!).'''
        ru, rv = self.find(u), self.find(v)
        if ru == rv: return False
        if self.rank[ru] < self.rank[rv]: ru, rv = rv, ru
        self.parent[rv] = ru
        if self.rank[ru] == self.rank[rv]: self.rank[ru] += 1
        self.components -= 1
        return True

    def connected(self, u, v) -> bool:
        return self.find(u) == self.find(v)


# ── Kruskal's MST — O(E log E)
def kruskal(vertices: list, edges: list) -> tuple:
    '''edges = [(weight, u, v), ...]'''
    edges = sorted(edges); uf = UnionFind(vertices)
    mst, total = [], 0
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w)); total += w
            if len(mst) == len(vertices) - 1: break
    return mst, total


verts    = ['A','B','C','D','E']
wt_edges = [(1,'A','B'),(3,'A','C'),(4,'B','C'),(2,'B','D'),
            (5,'C','D'),(6,'C','E'),(7,'D','E')]
mst, cost = kruskal(verts, wt_edges)
print(mst, cost)   # [('A','B',1),...] 12


# ── BFS on 2D grid — shortest path ignoring walls
def grid_bfs(grid, src, dst) -> int:
    rows, cols = len(grid), len(grid[0])
    DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
    def valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0
    if not valid(*src) or not valid(*dst): return -1
    visited, queue = {src}, deque([(src, 0)])
    while queue:
        (r, c), steps = queue.popleft()
        if (r, c) == dst: return steps
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if valid(nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), steps + 1))
    return -1

grid = [[0,0,1,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,1,1,0,0],[0,0,0,1,0]]
print(grid_bfs(grid, (0,0), (4,4)))   # 8
""",
    },
]


# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------


class Command(BaseCommand):
    help = "Seed the database with sample Python DSA categories and code snippets."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing snippets and categories before seeding.",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            CodeSnippet.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared all existing data."))

        created_categories = 0
        created_snippets = 0
        skipped_snippets = 0

        for entry in SNIPPETS:
            category, cat_created = Category.objects.get_or_create(
                name=entry["category"]
            )
            if cat_created:
                created_categories += 1

            snippet, sn_created = CodeSnippet.objects.get_or_create(
                title=entry["title"],
                category=category,
                defaults={
                    "code_content": entry["code"].strip(),
                    "difficulty": entry["difficulty"],
                },
            )
            if sn_created:
                created_snippets += 1
            else:
                skipped_snippets += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Created {created_categories} categories, "
                f"{created_snippets} snippets. "
                f"Skipped {skipped_snippets} already-existing snippets."
            )
        )
