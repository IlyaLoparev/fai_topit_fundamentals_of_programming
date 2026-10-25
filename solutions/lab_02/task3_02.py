import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print("==== Практическая задача ====")
registry = weakref.WeakValueDictionary()

r1 = Record()
r2 = Record()
temp = Record()

registry["one"] = r1
registry["two"] = r2
registry["three"] = temp

print("Сразу после регистрации:", sorted(registry.keys()))

del temp
print("После удаления temp:", sorted(registry.keys()))

del r2
print("После удаления r2:", sorted(registry.keys()))

print("r1 всё ещё доступен:", r1)
print("registry.get('two') после удаления r2:", registry.get("two"))