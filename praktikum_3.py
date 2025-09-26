# Nama Lengkap: Febnawan Fatur Rochman
# NPM         : 237006029
# Kelas       : A

import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tabulate import tabulate

# Untuk tugas I/O-Bound
NUM_IO_TASKS = 10
MIN_SLEEP = 0.5
MAX_SLEEP = 2.0

# Untuk tugas CPU-Bound
NUM_CPU_TASKS = 8
ITERATIONS = 10**7
NUM_WORKERS = 8



def download_file(duration):
    time.sleep(duration)
    return f"Selesai setelah {duration:.2f} detik."

def heavy(n, iters=ITERATIONS):
    s = 0
    for i in range(iters):
        s += (i * n) % 7
    return s


def run_serial(func, tasks):
    start_time = time.perf_counter()
    for task in tasks:
        func(task)
    end_time = time.perf_counter()
    return end_time - start_time

def run_with_executor(Executor, func, tasks, workers):
    start_time = time.perf_counter()
    with Executor(max_workers=workers) as executor:
        list(executor.map(func, tasks))
    end_time = time.perf_counter()
    return end_time - start_time


def main():
    print("--- Memulai Eksperimen I/O-Bound ---")
    io_tasks = [random.uniform(MIN_SLEEP, MAX_SLEEP) for _ in range(NUM_IO_TASKS)]
    
    io_serial_time = run_serial(download_file, io_tasks)
    io_threads_time = run_with_executor(ThreadPoolExecutor, download_file, io_tasks, NUM_WORKERS)
    io_processes_time = run_with_executor(ProcessPoolExecutor, download_file, io_tasks, NUM_WORKERS)
    
    print(f"Waktu Serial (I/O): {io_serial_time:.4f}s")
    print(f"Waktu Threads (I/O): {io_threads_time:.4f}s")
    print(f"Waktu Processes (I/O): {io_processes_time:.4f}s\n")
    
    io_speedup_threads = io_serial_time / io_threads_time
    io_speedup_processes = io_serial_time / io_processes_time


    print("--- Memulai Eksperimen CPU-Bound ---")
    cpu_tasks = range(1, NUM_CPU_TASKS + 1)
    
    cpu_serial_time = run_serial(heavy, cpu_tasks)
    cpu_threads_time = run_with_executor(ThreadPoolExecutor, heavy, cpu_tasks, NUM_WORKERS)
    cpu_processes_time = run_with_executor(ProcessPoolExecutor, heavy, cpu_tasks, NUM_WORKERS)

    print(f"Waktu Serial (CPU): {cpu_serial_time:.4f}s")
    print(f"Waktu Threads (CPU): {cpu_threads_time:.4f}s")
    print(f"Waktu Processes (CPU): {cpu_processes_time:.4f}s\n")
    
    cpu_speedup_threads = cpu_serial_time / cpu_threads_time
    cpu_speedup_processes = cpu_serial_time / cpu_processes_time


    print("--- Tabel Hasil Perbandingan ---")
    table_headers = ["Jenis Aplikasi", "Serial (s)", "Threads (s)", "Processes (s)", "Speedup Threads", "Speedup Processes"]
    table_data = [
        [
            "I/O-Bound",
            f"{io_serial_time:.4f}",
            f"{io_threads_time:.4f}",
            f"{io_processes_time:.4f}",
            f"{io_speedup_threads:.2f}x",
            f"{io_speedup_processes:.2f}x"
        ],
        [
            "CPU-Bound",
            f"{cpu_serial_time:.4f}",
            f"{cpu_threads_time:.4f}",
            f"{cpu_processes_time:.4f}",
            f"{cpu_speedup_threads:.2f}x",
            f"{cpu_speedup_processes:.2f}x"
        ]
    ]
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


if __name__ == "__main__":
    main()