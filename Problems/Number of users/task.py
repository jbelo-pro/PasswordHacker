# write your code here
with open('users.json', 'r') as f:
    j = json.load(f)
    print(len(j['users']))
