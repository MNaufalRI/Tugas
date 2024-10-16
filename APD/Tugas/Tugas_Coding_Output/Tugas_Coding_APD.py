# Membuat tabel hasil perkalian
tabel = []
for i in range(1, 5):
    baris = []
    for j in range(1, 6):
        baris.append(i * j)
    tabel.append(baris)

# Menampilkan di terminal menggunakan print
print("*", " ".join(map(str, range(1, 6))))

for i in range(1, len(tabel) + 1):
    print(i, " ".join(map(str,tabel[i-1])))