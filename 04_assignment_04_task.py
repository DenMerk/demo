stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99,
         'email': 42, 'ok': 98}

max_amount = 0
for key in stats.keys():
    if max_amount < stats[key]:
        max_amount = stats[key]
        ads_channel = key
print(ads_channel)
    
