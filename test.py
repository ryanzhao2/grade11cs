def target(age, rest_heart, intensity):
    max_heart = 220 - age
    reserve = max_heart - rest_heart
    target_heartrate = intensity * reserve + rest_heart
    return target_heartrate


target = target(35, 65, 1)
print(target)