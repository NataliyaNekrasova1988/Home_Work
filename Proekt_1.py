n=int(input())
database = {}
for i in range(n):
    login = input()
    if login in database:
        database[login] += 1
        database[f"{login}{database[login]}"] = 0
        print(f"{login}{database[login]}")
    else:
        database[login] = 0
        print(f'OK')


