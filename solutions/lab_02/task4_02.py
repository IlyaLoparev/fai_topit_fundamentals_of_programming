import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Пороги поколений:", gc.get_threshold())
print("Текущие счётчики поколений:", gc.get_count())
print("Статистика поколений:", gc.get_stats())

id_first = id(first)
id_second = id(second)
print(id_first, id_second)

del first
del second

collected = gc.collect()
print("gc.collect() вернул:", collected)

print("==== Временное отключение автоматического сборщика ====")
gc.disable()

for i in range(5):
    a = []
    b = []
    a.append(b)
    b.append(a)

del a, b

print("Перед ручной сборкой, gc.get_count():", gc.get_count())
collected_manual = gc.collect()
print("Ручная сборка вернула:", collected_manual)

gc.enable()

print("==== Практическая задача: граф ====")
before = gc.collect()
print("Сборка до создания графа:", before)

node1 = {"name": "A", "links": []}
node2 = {"name": "B", "links": []}
node3 = {"name": "C", "links": []}
node4 = {"name": "D", "links": []}

node1["links"].append(node2)
node2["links"].append(node3)
node3["links"].append(node1)

print("Связи графа:")
print("node1 -> node2:", node1["links"][0] is node2)
print("node2 -> node3:", node2["links"][0] is node3)
print("node3 -> node1:", node3["links"][0] is node1)
print("node4 независим:", node4)

del node1, node2, node3

after = gc.collect()
print("Сборка после удаления циклических узлов:", after)
print("Независимый узел node4 всё ещё доступен:", node4)
print("Сравнение собранных объектов: до =", before, ", после =", after)

