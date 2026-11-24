import unittest
from data_siswa import DataSiswa, StackRiwayat


class TestDataSiswa(unittest.TestCase):
    def setUp(self):
        self.data = DataSiswa()

    def nama_siswa(self):
        hasil = []
        current = self.data.head

        while current is not None:
            hasil.append(current.nama)
            current = current.next

        return hasil
    
    def test_stack_riwayat(self):
        stack = StackRiwayat()

        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.pop())

        stack.push("Ani")
        stack.push("Budi")

        self.assertEqual(stack.pop(), "Budi")
        self.assertEqual(stack.pop(), "Ani")
        self.assertTrue(stack.is_empty())

    def test_tambah_dan_tampilkan(self):
        self.data.tambah_siswa("Ani", "Satu-A")
        self.data.tambah_siswa("Budi", "Satu-B")

        self.data.tampilkan_siswa()

        self.assertEqual(self.nama_siswa(), ["Ani", "Budi"])
        self.assertEqual(self.data.tail.nama, "Budi")

    def test_tampilkan_kosong(self):
        self.data.tampilkan_siswa()
        self.assertIsNone(self.data.head)

    def test_cari_siswa(self):
        self.data.tambah_siswa("Ani", "Satu-A")

        siswa = self.data.cari_siswa("ANI")

        self.assertEqual(siswa.nama, "Ani")
        self.assertIsNone(self.data.cari_siswa("Budi"))

    def test_ubah_siswa(self):
        self.data.tambah_siswa("Ani", "Satu-A")

        self.data.ubah_siswa("Ani", "Anisa", "Satu-B")
        self.data.ubah_siswa("Budi", "Budi Baru", "Dua-A")

        self.assertEqual(self.data.head.nama, "Anisa")
        self.assertEqual(self.data.head.kelas, "Satu-B")

    def test_sisipkan_di_tengah(self):
        self.data.tambah_siswa("Ani", "Satu-A")
        self.data.tambah_siswa("Budi", "Satu-B")
        self.data.tambah_siswa("Cici", "Dua-A")

        self.data.sisipkan_siswa_tengah("Dina", "Dua-B", 1)

        self.assertEqual(
            self.nama_siswa(),
            ["Ani", "Dina", "Budi", "Cici"]
        )

    def test_sisipan_tidak_valid(self):
        self.data.sisipkan_siswa_tengah("Ani", "Satu-A", 1)

        self.data.tambah_siswa("Ani", "Satu-A")
        self.data.tambah_siswa("Budi", "Satu-B")

        self.data.sisipkan_siswa_tengah("Cici", "Dua-A", 0)
        self.data.sisipkan_siswa_tengah("Cici", "Dua-A", 5)

        self.assertEqual(self.nama_siswa(), ["Ani", "Budi"])

    def test_hapus_siswa(self):
        self.data.tambah_siswa("Ani", "Satu-A")
        self.data.tambah_siswa("Budi", "Satu-B")
        self.data.tambah_siswa("Cici", "Dua-A")

        self.data.hapus_siswa("Budi")
        self.assertEqual(self.nama_siswa(), ["Ani", "Cici"])

        self.data.hapus_siswa("Cici")
        self.assertEqual(self.data.tail.nama, "Ani")

        self.data.hapus_siswa("Ani")
        self.assertIsNone(self.data.head)
        self.assertIsNone(self.data.tail)

        self.data.hapus_siswa("Tidak ada")

    def test_undo_hapus(self):
            self.data.tambah_siswa("Ani", "Satu-A")
            self.data.tambah_siswa("Budi", "Satu-B")
            self.data.tambah_siswa("Cici", "Dua-A")

            self.data.hapus_siswa("Budi")
            self.data.undo_hapus()

            self.assertEqual(
                self.nama_siswa(),
                ["Ani", "Budi", "Cici"]
            )

            self.data.hapus_siswa("Cici")
            self.data.undo_hapus()

            self.assertEqual(self.data.tail.nama, "Cici")

    def test_undo_kosong(self):
         self.data.undo_hapus()
 
if __name__ == "__main__":
    unittest.main()