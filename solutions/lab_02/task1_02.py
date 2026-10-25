print("==== Эксперимент А ====")
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print("==== Эксперимент B ====")
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

print("==== Дополнение ====")
second = [10, 20, 30]
print(first == second)
print(first is second)
second.append(40)
print(first, second)

print("==== Практическая задача ====")
import copy
conf1 = {
    "name": "Punchline",
    "participants": ["Петя", "Ваня", "Федор"],
    "download": [["syscall", True], ["threads", 6], ["display", True]],
}
conf2 = conf1
conf2["name"] = "Standup"
print(conf1, conf2)

conf3 = copy.deepcopy(conf1)
conf3["participants"].append("Тимур")
print(conf1, conf3)

