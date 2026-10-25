import sys
import gc
import tracemalloc

print("пустой список: ", sys.getsizeof([]))
print("список из 10 целых чисел: ", sys.getsizeof(list(range(10))))
print("кортеж из 10 целых чисел: ", sys.getsizeof(tuple(range(10))))
print("строка из 10 символов: ", sys.getsizeof("abcdefghij"))
print("целое число: ", sys.getsizeof(123456789))
print("None", sys.getsizeof(None))

print("==== Рост списка ====")
arr = []
last_size = sys.getsizeof(arr)
print(f"len={len(arr)}, size={last_size}")

for i in range(100):
    arr.append(i)
    size = sys.getsizeof(arr)
    if size != last_size:
        print(f"len={len(arr)}, size={size}, change={size-last_size}")
        last_size = size

print("==== Tracemalloc ====")
tracemalloc.start()
numbers1 = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("list(range(100_000)):")
print(f"текущий объём: {current / 1024:.1f} KB")
print(f"пиковый объём: {peak    / 1024:.1f} KB")
tracemalloc.start()
numbers2 = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("range(100_000):")
print(f"текущий объём: {current / 1024:.1f} KB")
print(f"пиковый объём: {peak    / 1024:.1f} KB")