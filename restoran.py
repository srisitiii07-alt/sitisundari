"""
Program Kasir Restoran Sederhana
Berdasarkan alur konsep:
1. Mulai Program (Inisialisasi total = 0)
2. Tampilkan Menu Makanan
3. Proses Pemesanan (Pilih menu & input jumlah)
4. Cek Pilihan 0 (Selesai memilih atau lanjut pesan)
5. Hitung Diskon (> Rp200.000 -> 20%)
6. Tampilkan Struk Pembayaran
"""

def format_rupiah(nominal):
    """Fungsi pembantu untuk memformat angka menjadi format rupiah (cth: Rp25.000)"""
    return f"Rp{nominal:,.0f}".replace(",", ".")

def main():
    # 1. Mulai Program & Inisialisasi
    print("=" * 45)
    print("      SELAMAT DATANG DI KASIR RESTORAN       ")
    print("=" * 45)

    # Daftar menu makanan (id: [Nama, Harga])
    daftar_menu = {
        1: ("Nasi Goreng", 25000),
        2: ("Mie Ayam", 15000),
        3: ("Ayam Geprek", 20000),
        4: ("Sate Ayam", 30000),
        5: ("Bakso", 18000)
    }

    total_belanja = 0
    daftar_pesanan = []

    # Perulangan proses pemesanan (while)
    while True:
        # 2. Tampilkan Menu Makanan
        print("\n--- DAFTAR MENU MAKANAN ---")
        for nomor, item in daftar_menu.items():
            print(f"{nomor}. {item[0]:<15} - {format_rupiah(item[1])}")
        print("0. Selesai Memilih")
        print("-" * 30)

        # 3 & 4. Input Pilihan Menu & Cek Selesai (0)
        try:
            pilihan = int(input("Pilih menu (0-5): "))
        except ValueError:
            print("[!] Masukkan angka yang valid!")
            continue

        # Cek apakah memilih 0 untuk selesai
        if pilihan == 0:
            print("\n>> Memproses pesanan...")
            break
        elif pilihan in daftar_menu:
            try:
                jumlah = int(input(f"Masukkan jumlah {daftar_menu[pilihan][0]}: "))
                if jumlah <= 0:
                    print("[!] Jumlah pesanan minimal 1.")
                    continue
            except ValueError:
                print("[!] Masukkan jumlah berupa angka!")
                continue

            # Hitung subtotal & tambahkan ke total
            nama_makanan, harga = daftar_menu[pilihan]
            subtotal = harga * jumlah
            total_belanja += subtotal
            daftar_pesanan.append((nama_makanan, harga, jumlah, subtotal))

            print(f"-> {jumlah}x {nama_makanan} berhasil ditambahkan! (Subtotal: {format_rupiah(subtotal)})")
        else:
            print("[!] Pilihan menu tidak valid. Silakan pilih 0-5.")
            continue

    # 5. Hitung Diskon
    # Jika total belanja > Rp200.000 maka mendapat diskon 20%, jika tidak diskon 0%
    if total_belanja > 200000:
        persen_diskon = 20
        potongan = total_belanja * 0.20
    else:
        persen_diskon = 0
        potongan = 0

    total_bayar = total_belanja - potongan

    # 6. Tampilkan Struk Pembayaran
    print("\n" + "=" * 45)
    print("             STRUK PEMBAYARAN                ")
    print("=" * 45)

    if daftar_pesanan:
        print("Rincian Pesanan:")
        for nama, harga, jml, sub in daftar_pesanan:
            print(f" - {nama:<13} ({jml}x @ {format_rupiah(harga)}) = {format_rupiah(sub)}")
        print("-" * 45)

    print(f"Total Belanja : {format_rupiah(total_belanja)}")
    print(f"Diskon        : {persen_diskon}%")
    print(f"Potongan      : {format_rupiah(potongan)}")
    print("-" * 45)
    print(f"Total Bayar   : {format_rupiah(total_bayar)}")
    print("=" * 45)
    print("                Terima Kasih                 ")
    print("=" * 45)

if __name__ == "__main__":
    main()