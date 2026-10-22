atzimes = [8, 9, 6, 10, 7, 5, 8]

skaits = len(atzimes)

videja = sum(atzimes) / skaits

lielaka = max(atzimes)

augstas_atzimes = len([a for a in atzimes if a >= 7])

print(f"Atzīmju skaits:", skaits)
print(f"Vidējā atzīme:", videja)
print(f"Lielākā atzīme:", lielaka)
print(f"Atzīmju skaits, kas ir 7 vai lielākas:",augstas_atzimes)