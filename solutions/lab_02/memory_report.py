import sys
import gc
import tracemalloc


# Эта функция создаёт нужный объект по его названию.
def build(kind):
    if kind == "empty_list":
        return []
    elif kind == "list_10":
        return list(range(10))
    elif kind == "tuple_10":
        return tuple(range(10))
    elif kind == "string_10":
        return "abcdefghij"
    elif kind == "int":
        return 123456789
    elif kind == "none":
        return None
    elif kind == "big_list":
        return list(range(100000))
    elif kind == "big_range":
        return range(100000)


def measure(name, n, kind):
    gc.collect()
    tracemalloc.start()
    obj = build(kind)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    size = sys.getsizeof(obj)
    result = {
        "name": name,
        "n": n,
        "size": size,
        "current": current,
        "peak": peak,
    }
    return result

scenarios = [
    ("пустой список", 0, "empty_list"),
    ("список 10 int", 10, "list_10"),
    ("кортеж 10 int", 10, "tuple_10"),
    ("строка 10 символов", 10, "string_10"),
    ("целое число", 1, "int"),
    ("None", 1, "none"),
    ("list(range(100_000))", 100000, "big_list"),
    ("range(100_000)", 100000, "big_range"),
]


# Шаг 1. Собираем результаты. Пока ничего не печатаем.
results = []
for name, n, kind in scenarios:
    result = measure(name, n, kind)
    results.append(result)


# Шаг 2. Теперь печатаем готовые результаты.
print("Отчёт по памяти")
print("-" * 70)

for r in results:
    current_kb = r["current"] / 1024
    peak_kb = r["peak"] / 1024

    print("Сценарий:", r["name"])
    print("  элементов:", r["n"])
    print("  размер объекта:", r["size"], "байт")
    print("  текущая память:", round(current_kb, 1), "KB")
    print("  пиковая память:", round(peak_kb, 1), "KB")
    print("-" * 70)


# Шаг 3. Отношение пиков list/range.
peak_list = None
peak_range = None

for r in results:
    if r["name"] == "list(range(100_000))":
        peak_list = r["peak"]
    if r["name"] == "range(100_000)":
        peak_range = r["peak"]
ratio = peak_list / peak_range
print("Отношение пиков list/range:", round(ratio, 1))