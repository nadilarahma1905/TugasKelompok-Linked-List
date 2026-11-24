class NodeSiswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
        self.next = None


class NodeRiwayat:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackRiwayat:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        node = NodeRiwayat(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        return data


class DataSiswa:
    def __init__(self):
        self.head = None
        self.tail = None
        self.riwayat = StackRiwayat()

    # CREATE
    def tambah_siswa(self, nama, kelas):
        node = NodeSiswa(nama, kelas)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

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

    # SEARCH
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

    # INSERT DI TENGAH
    def sisipkan_siswa_tengah(self, nama, kelas, posisi):
        if self.head is None or self.head.next is None:
            print("Minimal harus ada 2 data siswa untuk menyisipkan di tengah!")
            return

        if posisi <= 0:
            print("Posisi tengah harus lebih besar dari 0!")
            return

        previous = self.head
        indeks = 0

        while previous.next is not None and indeks < posisi - 1:
            previous = previous.next
            indeks += 1

        if previous.next is None:
            print("Posisi tidak berada di tengah rangkaian data siswa!")
            return

        node = NodeSiswa(nama, kelas)
        node.next = previous.next
        previous.next = node

        print(f"Data siswa berhasil disisipkan di tengah (posisi {posisi})!")

    # DELETE
    def hapus_siswa(self, nama):
        current = self.head
        previous = None
        posisi = 0

        while current is not None:
            if current.nama.lower() == nama.lower():
                self.riwayat.push(
                    (current.nama, current.kelas, posisi)
                )

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current is self.tail:
                    self.tail = previous

                if self.head is None:
                    self.tail = None

                current.next = None
                print("Data siswa berhasil dihapus!")
                return

            previous = current
            current = current.next
            posisi += 1

        print("Data siswa tidak ditemukan!")

    # UNDO DELETE
    def undo_hapus(self):
        data = self.riwayat.pop()

        if data is None:
            print("Tidak ada riwayat penghapusan!")
            return

        nama, kelas, posisi = data
        node = NodeSiswa(nama, kelas)

        if self.head is None or posisi == 0:
            node.next = self.head
            self.head = node

            if self.tail is None:
                self.tail = node
        else:
            previous = self.head
            indeks = 0

            while previous.next is not None and indeks < posisi - 1:
                previous = previous.next
                indeks += 1

            node.next = previous.next
            previous.next = node

            if node.next is None:
                self.tail = node

        print("Data siswa yang dihapus berhasil dikembalikan!")


# PROGRAM UTAMA
if __name__ == "__main__": # pragma: no cover
    data = DataSiswa()

    while True:
        print("\n====== APLIKASI DATA SISWA ======")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Cari Data Siswa")
        print("4. Ubah Data Siswa")
        print("5. Hapus Data Siswa")
        print("6. Undo Hapus")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            nama = input("Masukkan Nama  : ")
            kelas = input("Masukkan Kelas (contoh Satu-A): ")
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
            kelas_baru = input("Masukkan kelas baru (contoh Satu-A): ")
            data.ubah_siswa(nama, nama_baru, kelas_baru)

        elif pilihan == "5":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            data.hapus_siswa(nama)

        elif pilihan == "6":
            data.undo_hapus()

        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak ")