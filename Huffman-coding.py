
import heapq

class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def print_code(root, code=""):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.ch, ":", code)
        return

    print_code(root.left, code + "0")
    print_code(root.right, code + "1")


# Main program
ch = ['A', 'B', 'C', 'D', 'E', 'F']
freq = [5, 9, 12, 13, 16, 45]

pq = []

# Insert characters into priority queue
for i in range(len(ch)):
    heapq.heappush(pq, Node(ch[i], freq[i]))

# Build Huffman Tree
while len(pq) > 1:
    left = heapq.heappop(pq)
    right = heapq.heappop(pq)

    parent = Node(
        '-',
        left.freq + right.freq,
        left,
        right
    )

    heapq.heappush(pq, parent)

root = heapq.heappop(pq)

print("Huffman Codes:")
print_code(root)
