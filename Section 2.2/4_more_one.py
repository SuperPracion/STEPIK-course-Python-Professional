num_mass = [int(i) for i in input().split()]
out_set = sorted(set(filter(lambda x: num_mass.count(x) > 1, num_mass)))

# for num in range(len(num_mass)):
#     if num in num_mass[num + 1:]:
#         out_set.add(num)

print(*out_set)
