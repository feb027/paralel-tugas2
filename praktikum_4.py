# Nama Lengkap: Febnawan Fatur Rochman
# NPM         : 237006029
# Kelas       : A

import os
import time
import random
import string
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tabulate import tabulate

# --- Konfigurasi Pipeline ---
DATA_DIR = "data_temp"
NUM_FILES = 100
FILE_SIZE_KB = 100
NUM_LOADER_THREADS = 4
NUM_CPU_WORKERS = 4

def create_dummy_dataset():
    print(f"--- Membuat dataset di folder '{DATA_DIR}' ---")
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_paths = []
    content_size = FILE_SIZE_KB * 1024
    for i in range(NUM_FILES):
        file_path = os.path.join(DATA_DIR, f"file_{i+1:03d}.txt")
        content = ''.join(random.choices(string.ascii_letters + string.digits + string.whitespace, k=content_size))
        with open(file_path, 'w') as f:
            f.write(content)
        file_paths.append(file_path)
    print(f"{NUM_FILES} file berhasil dibuat.\n")
    return file_paths

def loader_io_task(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def worker_cpu_task(content):
    char_counts = {}
    for char in content:
        char_counts[char] = char_counts.get(char, 0) + 1
    return len(char_counts)

def aggregator_task(results):
    return sum(results)

def run_pipeline(file_paths):
    print("--- Menjalankan Hybrid Pipeline ---")
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=NUM_LOADER_THREADS) as thread_executor:
        contents = list(thread_executor.map(loader_io_task, file_paths))
    
    with ProcessPoolExecutor(max_workers=NUM_CPU_WORKERS) as process_executor:
        results = list(process_executor.map(worker_cpu_task, contents))

    final_result = aggregator_task(results)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    print(f"Hasil agregasi: {final_result}")
    return total_time

def run_baseline(file_paths):
    print("--- Menjalankan Baseline Single-Process ---")
    start_time = time.perf_counter()
    
    results = []
    for path in file_paths:
        content = loader_io_task(path)
        result = worker_cpu_task(content)
        results.append(result)
    
    final_result = aggregator_task(results)
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    print(f"Hasil agregasi: {final_result}")
    return total_time

def cleanup_dataset():
    print(f"\n--- Membersihkan dataset dari folder '{DATA_DIR}' ---")
    if os.path.exists(DATA_DIR):
        for f in os.listdir(DATA_DIR):
            os.remove(os.path.join(DATA_DIR, f))
        os.rmdir(DATA_DIR)
        print("Pembersihan selesai.")

def main():
    file_paths = create_dummy_dataset()
    
    baseline_time = run_baseline(file_paths)
    pipeline_time = run_pipeline(file_paths)

    baseline_throughput = NUM_FILES / baseline_time
    baseline_latency = baseline_time / NUM_FILES
    
    pipeline_throughput = NUM_FILES / pipeline_time
    pipeline_latency = pipeline_time / NUM_FILES
    
    print("\n" + "="*40)
    print("--- Tabel Hasil Akhir ---")
    print("="*40)
    
    headers = ["Threads Loader", "Workers CPU", "Jumlah File", "Waktu (s)", "Throughput (file/s)", "Avg Latency (s)"]
    data = [
        ["N/A (Serial)", "N/A (Serial)", NUM_FILES, f"{baseline_time:.4f}", f"{baseline_throughput:.2f}", f"{baseline_latency:.4f}"],
        [NUM_LOADER_THREADS, NUM_CPU_WORKERS, NUM_FILES, f"{pipeline_time:.4f}", f"{pipeline_throughput:.2f}", f"{pipeline_latency:.4f}"]
    ]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    
    cleanup_dataset()

if __name__ == "__main__":
    main()