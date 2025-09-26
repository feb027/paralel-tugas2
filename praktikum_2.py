# Nama Lengkap: Febnawan Fatur Rochman
# NPM         : 237006029
# Kelas       : A

import time
from concurrent.futures import ProcessPoolExecutor
from tabulate import tabulate

ITERATIONS = 10**7 # Ditingkatkan dari 10**6 agar lebih terasa perbedaannya
NUM_TASKS = 8 # Jumlah total pekerjaan, dari range(1, 9)

def heavy(n, iters=ITERATIONS):
    s = 0
    for i in range(iters):
        s += (i * n) % 7
    return s

def run_serial(tasks):
    print("Menjalankan eksekusi serial...")
    start_time = time.perf_counter()
    results = [heavy(n) for n in tasks]
    end_time = time.perf_counter()
    print(f"Hasil (serial): {results}")
    return end_time - start_time

def run_parallel(tasks, num_processes):
    print(f"Menjalankan eksekusi paralel dengan {num_processes} proses...")
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(heavy, tasks))
    end_time = time.perf_counter()
    print(f"Hasil (paralel, {num_processes} proses): {results}")
    return end_time - start_time

def main():
    tasks = range(1, NUM_TASKS + 1)
    
    # 1. Jalankan secara serial sebagai baseline
    serial_time = run_serial(tasks)
    print(f"\nWaktu eksekusi serial: {serial_time:.4f} detik\n")

    process_counts = [2, 4, 8]
    table_data = []
    
    # Menambahkan hasil serial ke tabel (sebagai 1 proses)
    table_data.append([1, f"{serial_time:.4f}", "1.00x", "100.00%"])

    # 2. Jalankan secara paralel dengan jumlah proses yang berbeda
    for p in process_counts:
        parallel_time = run_parallel(tasks, p)
        
        # 3. Hitung Speedup dan Efisiensi
        # Speedup = Waktu Serial / Waktu Paralel
        speedup = serial_time / parallel_time
        
        # Efisiensi = Speedup / Jumlah Proses
        efficiency = (speedup / p) * 100

        print(f"Waktu eksekusi paralel ({p} proses): {parallel_time:.4f} detik")
        print(f"Speedup: {speedup:.2f}x")
        print(f"Efisiensi: {efficiency:.2f}%\n")
        
        table_data.append([p, f"{parallel_time:.4f}", f"{speedup:.2f}x", f"{efficiency:.2f}%"])

    table_headers = ["Proses", "Waktu (s)", "Speedup", "Efisiensi"]
    print("--- Tabel Hasil ---")
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


if __name__ == "__main__":
    main()