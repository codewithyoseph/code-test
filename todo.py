toDos = "Your Words To Count"
counters = {}

for todo in toDos:
    if todo.lower() in counters:
        counters[todo.lower()] += 1
    else:
        counters[todo.lower()] = 1

print(counters)