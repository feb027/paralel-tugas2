# Nama Lengkap: Febnawan Fatur Rochman
# NPM         : 237006029
# Kelas       : A

import threading
import time
import random
from tabulate import tabulate

# --- Spesifikasi Tugas ---
NUM_FILES = 10
MIN_SLEEP = 0.5
MAX_SLEEP = 2.0

def download_file(file_index, duration):
    print(f"Mulai mengunduh file {file_index+1} selama {duration:.2f} detik...")
    time.sleep(duration)
    print(f"Selesai mengunduh file {file_index+1}.")

def run_serial(jobs):
    start_time = time.perf_counter()
    for i, sec in jobs:
        download_file(i, sec)
    end_time = time.perf_counter()
    return end_time - start_time

def run_threads(jobs):
    threads = []
    start_time = time.perf_counter()
    for i, sec in jobs:
        thread = threading.Thread(target=download_file, args=(i, sec))
        threads.append(thread)
        thread.start() 

    for thread in threads:
        thread.join() 
    
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    # 1. Membuat daftar pekerjaan dengan durasi acak
    jobs = [(i, random.uniform(MIN_SLEEP, MAX_SLEEP)) for i in range(NUM_FILES)]
    
    total_durasi_simulasi = sum(sec for _, sec in jobs)
    print(f"Total file: {NUM_FILES}")
    print(f"Total durasi simulasi (jika ideal): ~{total_durasi_simulasi:.2f} detik\n")

    # 2. Menjalankan eksekusi serial
    print("--- Memulai Eksekusi Serial ---")
    serial_time = run_serial(jobs)
    print(f"\nWaktu eksekusi serial: {serial_time:.4f} detik\n")

    # 3. Menjalankan eksekusi threaded
    print("--- Memulai Eksekusi Threaded ---")
    threaded_time = run_threads(jobs)
    print(f"\nWaktu eksekusi threaded: {threaded_time:.4f} detik\n")

    # 4. Menghitung speedup
    # Speedup = Waktu Serial / Waktu Paralel
    try:
        speedup = serial_time / threaded_time
    except ZeroDivisionError:
        speedup = float('inf')

    # 5. Menampilkan hasil dalam tabel
    table_headers = ["Mode", "Jumlah File", "Waktu (s)", "Speedup"]
    table_data = [
        ["Serial", NUM_FILES, f"{serial_time:.4f}", "1.00x"],
        ["Threaded", NUM_FILES, f"{threaded_time:.4f}", f"{speedup:.2f}x"]
    ]

    print("--- Tabel Hasil ---")
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


if __name__ == "__main__":
    main()