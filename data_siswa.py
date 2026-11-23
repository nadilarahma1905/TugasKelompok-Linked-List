class NodeSiswa:
    def _init_(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
        self.next = None

class DataSiswa:
    def _init_(self):
        self.head = None

    # CREATE
    def tambah_siswa(self, nama, kelas):
        node_baru = NodeSiswa(nama, kelas)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node_baru

        print("Data siswa berhasil ditambahkan!")

    # READ
    def tampilkan_siswa(self):
        if self.head is None:
            print("Data siswa masih kosong!")
            return

        current = self.head
        nomor = 1

        print("\n======= DATA SISWA =======")
        print(f"{'No':<5} {'Nama':<20} {'Kelas':<10}")
        print("-" * 35)

        while current is not None:
            print(f"{nomor:<5} {current.nama:<20} {current.kelas:<10}")
            current = current.next
            nomor += 1

    def cari_siswa(self, nama):
        current = self.head

        while current is not None:
            if current.nama.lower() == nama.lower():
                return current

            current = current.next

        return None

    # UPDATE
    def ubah_siswa(self, nama, nama_baru, kelas_baru):
        siswa = self.cari_siswa(nama)

        if siswa is None:
            print("Data siswa tidak ditemukan!")
            return

        siswa.nama = nama_baru
        siswa.kelas = kelas_baru

        print("Data siswa berhasil diperbarui!")

    # INSERT DI POSISI TENGAH (0-based)
    def sisipkan_siswa_tengah(self, nama, kelas, posisi):
        if self.head is None or self.head.next is None:
            print("Minimal harus ada 2 data siswa untuk menyisipkan di tengah!")
            return

        if posisi <= 0:
            print("Posisi tengah harus lebih besar dari 0!")
            return

        current = self.head
        indeks = 0

        while current.next is not None and indeks < posisi - 1:
            current = current.next
            indeks += 1

        if current.next is None:
            print("Posisi tidak berada di tengah rangkaian data siswa!")
            return

        node_baru = NodeSiswa(nama, kelas)
        node_baru.next = current.next
        current.next = node_baru
        print(f"Data siswa berhasil disisipkan di tengah (posisi {posisi})!")

    # DELETE
    def hapus_siswa(self, nama):
        if self.head is None:
            print("Data siswa masih kosong!")
            return

        if self.head.nama.lower() == nama.lower():
            node_hapus = self.head
            self.head = node_hapus.next
            node_hapus.next = None

            print("Data siswa berhasil dihapus!")
            return

        current = self.head

        while current.next is not None:
            if current.next.nama.lower() == nama.lower():
                node_hapus = current.next
                current.next = node_hapus.next
                node_hapus.next = None

                print("Data siswa berhasil dihapus!")
                return

            current = current.next

        print("Data siswa tidak ditemukan!")


# PROGRAM UTAMA
if __name__ == "_main_":  # pragma: no cover
    data = DataSiswa()

    while True:
        print("\n====== APLIKASI DATA SISWA ======")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Cari Data Siswa")
        print("4. Ubah Data Siswa")
        print("5. Hapus Data Siswa")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            nama = input("Masukkan Nama  : ")
            kelas = input("Masukkan Kelas : ")
            data.tambah_siswa(nama, kelas)

        elif pilihan == "2":
            data.tampilkan_siswa()

        elif pilihan == "3":
            nama = input("Masukkan nama siswa yang dicari: ")
            siswa = data.cari_siswa(nama)

            if siswa is not None:
                print("Nama  :", siswa.nama)
                print("Kelas :", siswa.kelas)
            else:
                print("Data siswa tidak ditemukan!")

        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru  : ")
            kelas_baru = input("Masukkan kelas baru : ")
            data.ubah_siswa(nama, nama_baru, kelas_baru)

        elif pilihan == "5":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            data.hapus_siswa(nama)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid!")