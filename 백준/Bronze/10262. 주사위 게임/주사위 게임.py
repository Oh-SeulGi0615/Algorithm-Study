g_a1, g_b1, g_a2, g_b2 = map(int, input().split())
e_a1, e_b1, e_a2, e_b2 = map(int, input().split())

possible_g = list(set([i + j for i in range(g_a1, g_b1+1) for j in range(g_a2, g_b2+1)]))
possible_e = list(set([i + j for i in range(e_a1, e_b1+1) for j in range(e_a2, e_b2+1)]))

result_g = sum(list(map(lambda x: x / len(possible_g), possible_g)))
result_e = sum(list(map(lambda x: x / len(possible_e), possible_e)))

if result_g == result_e:
  print('Tie')
elif result_g > result_e:
  print('Gunnar')
else:
  print('Emma')