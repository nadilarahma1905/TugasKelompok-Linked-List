import time
import tracemalloc
import io
import gc
import matplotlib.pyplot as plt
from contextlib import redirect_stdout
from data_siswa import DataSiswa

ukuran_data = [100, 1000, 10000, 100000]

waktu_tambah = []
waktu_hapus = []
memori_tambah = []
memori_hapus = []

for jumlah in ukuran_data:
    data = DataSiswa()

    tracemalloc.start()

    # Mengukur waktu penambahan
    mulai = time.perf_counter()

    with redirect_stdout(io.StringIO()):
        for i in range(jumlah):
            data.tambah_siswa(f"Siswa {i}", "Satu-A")

    waktu_tambah.append(time.perf_counter() - mulai)

    # Mengukur memori setelah penambahan
    memori_tambah.append(tracemalloc.get_traced_memory()[0] / 1024)

    # Menentukan 2 data di posisi tengah (misal untuk 100 data -> Siswa 49 dan Siswa 50)
    tengah = jumlah // 2
    target_hapus = [f"Siswa {tengah - 1}", f"Siswa {tengah}"]

    # Mengukur waktu penghapusan 2 data tengah
    mulai = time.perf_counter()

    with redirect_stdout(io.StringIO()):
        for nama_target in target_hapus:
            data.hapus_siswa(nama_target)

    waktu_hapus.append(time.perf_counter() - mulai)

    # Mengukur memori setelah penghapusan
    gc.collect()
    memori_hapus.append(tracemalloc.get_traced_memory()[0] / 1024)

    tracemalloc.stop()

# Menampilkan hasil pengukuran
print("\n========== HASIL PROFILING ==========")
print(f"{'Jumlah Data':<15}{'Tambah (s)':<15}{'Hapus (s)':<15}{'Memori Tambah (KB)':<20}{'Memori Hapus (KB)'}")

for i in range(len(ukuran_data)):
    print(
        f"{ukuran_data[i]:<15}"
        f"{waktu_tambah[i]:<15.4f}"
        f"{waktu_hapus[i]:<15.4f}"
        f"{memori_tambah[i]:<20.2f}"
        f"{memori_hapus[i]:.2f}"
    )

# ==========================================
# GRAFIK 1: WAKTU EKSEKUSI
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    ukuran_data,
    waktu_tambah,
    marker="o",
    label="Penambahan"
)

plt.plot(
    ukuran_data,
    waktu_hapus,
    marker="o",
    label="Penghapusan (2 Data Tengah)"
)

plt.title("Waktu Eksekusi Singly Linked List")
plt.xlabel("Jumlah Data Siswa")
plt.ylabel("Waktu (detik)")

# Skala logaritmik pada sumbu X dan Y
plt.xscale("log")
plt.yscale("log")

plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("grafik_waktu.png", dpi=300)
plt.show()


# ==========================================
# GRAFIK 2: PENGGUNAAN MEMORI
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    ukuran_data,
    memori_tambah,
    marker="o",
    linestyle="-",
    label="Setelah Penambahan"
)

plt.plot(
    ukuran_data,
    memori_hapus,
    marker="x",
    linestyle="--",
    label="Setelah Penghapusan (2 Data Tengah)"
)

plt.title("Penggunaan Memori Singly Linked List")
plt.xlabel("Jumlah Data Siswa")
plt.ylabel("Memori (KB)")

# Skala logaritmik pada sumbu X
plt.xscale("log")

plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("grafik_memori.png", dpi=300)
plt.show()
