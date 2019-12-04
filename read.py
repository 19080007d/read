data = []
with open('phone.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        print(line.strip())
print(data)
