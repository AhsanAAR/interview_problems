import heapq as hq
# this implements min heap using a simple python list and provides O(lgn) push and pop operations.
my_heap = [0, 0, 2, 4, -4, 5, 10, -1]
print("orginal list", my_heap)
hq.heapify(my_heap)  # O(n)

print("\nheapified list", my_heap)

# O(lgn)
print(f"\nmin element = {hq.heappop(my_heap)}")
print(f"min element = {hq.heappop(my_heap)}")
print(f"min element = {hq.heappop(my_heap)}")

print("\nmodfied heap", my_heap)

hq.heappush(my_heap, 1)

print("\ninserted 1 into heap", my_heap)
