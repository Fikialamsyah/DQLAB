# Membuat fungsi
def salam():
    print("Hello, Selamat Pagi")


# Pemangilan fungsi
salam()

# Parameter pada fungsi
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" %luas)

# Pemanggilan fungsi
# 4 dan 6 merupakan parameter yg diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6)


# Fungsi dengan return value
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas

# Pemanggilan fungsi
# 4 dan 6 merupakan parameter yg diinputkan kedalam fungsi luas segitiga
print("Luas segitiga: %d" %luas_segitiga(4, 6))