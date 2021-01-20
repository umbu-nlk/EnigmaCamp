tahun = int(input("Masukkan tahun yang ingin di cek "))

if tahun%4 == 0:
    if tahun%100 == 0:
        if tahun%400 == 0:
            print("Tahun ini Tahun Kabisat.")
        else:
            print("Tahun ini bukan Tahun Kabisat.")
    else:
        print("Tahun ini Tahun Kabisat.")
else:
    print("Tahun ini bukan Tahun Kabisat.")