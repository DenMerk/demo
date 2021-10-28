ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_ids = set()


for idss in ids.values():
    unique_ids.update(idss)
print(list(unique_ids))
