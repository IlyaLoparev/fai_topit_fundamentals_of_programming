import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

def prnt(data):
    print("  data =", data)
    print("  id(data) =", id(data))
    print("  id(data[0]) =", id(data[0]))
    print("  id(data[0][1]) =", id(data[0][1]))
print("==== Default ====")
prnt(original)
prnt(alias)
prnt(shallow)
prnt(deep)
print("==== original.append(['Databases', 5]) ====")
original.append(["Databases", 5])
prnt(original)
prnt(alias)
prnt(shallow)
prnt(deep)
print("==== original[0][1] = 3 ====")
original[0][1] = 3
prnt(original)
prnt(alias)
prnt(shallow)
prnt(deep)


wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("==== Wrong matrix ====")
print(wrong_matrix)
print("==== Correct matrix ====")
print(correct_matrix)
