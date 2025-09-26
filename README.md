# Praktikum Komputasi Paralel & Terdistribusi

Repositori ini berisi kumpulan kode dari tugas praktikum mata kuliah Komputasi Paralel & Terdistribusi. Proyek ini bertujuan untuk memahami dan mengimplementasikan konsep **Thread Parallelism** dan **Task Parallelism** menggunakan Python, khususnya dengan modul `threading` dan `concurrent.futures`.

Praktikum ini disusun secara bertahap, mulai dari simulasi sederhana hingga membangun pipeline pemrosesan data hibrida yang kompleks.

## Konsep Utama yang Dipelajari

-   **Thread Parallelism:** Menggunakan *multithreading* untuk menangani tugas-tugas yang bersifat **I/O-Bound**.
-   **Task Parallelism:** Menggunakan *multiprocessing* untuk menangani tugas-tugas yang bersifat **CPU-Bound**.
-   **Perbedaan Aplikasi I/O-Bound vs CPU-Bound:** Menganalisis secara empiris mengapa setiap jenis tugas memerlukan model paralelisme yang berbeda.
-   **Global Interpreter Lock (GIL):** Memahami dampak dan batasan GIL pada *multithreading* di Python untuk tugas CPU-bound.
-   **Desain Pipeline Hibrida:** Merancang arsitektur yang menggabungkan kekuatan *threads* (untuk I/O) dan *processes* (untuk CPU) dalam satu alur kerja.
-   **Metrik Kinerja:** Mengukur dan menganalisis performa sistem menggunakan metrik seperti *Speedup*, *Efisiensi*, *Throughput*, dan *Latensi*.

## Prasyarat

-   Python 3.x
-   Pustaka `tabulate` untuk menampilkan hasil dalam bentuk tabel yang rapi.

### Instalasi Pustaka

Anda dapat menginstal pustaka yang diperlukan menggunakan `pip`:

```bash
pip install tabulate
```

## Struktur Praktikum

Repositori ini terdiri dari empat tugas utama, masing-masing dengan fokus yang berbeda.

### 1. Tugas Praktikum 1: Thread Parallelism (I/O-Bound)

-   **File:** `praktikum_1.py`
-   **Tujuan:** Membuktikan efektivitas *multithreading* untuk tugas yang didominasi oleh waktu tunggu (I/O-bound), seperti simulasi unduhan file.
-   **Deskripsi:** Skrip ini membandingkan waktu eksekusi pengunduhan 10 file secara serial vs secara konkuren menggunakan `threading.Thread`.
-   **Cara Menjalankan:**
    ```bash
    python praktikum_1.py
    ```
-   **Hasil & Pembelajaran Utama:** Terbukti bahwa *threading* secara dramatis mengurangi waktu eksekusi total dengan cara tumpang tindih (overlapping) waktu tunggu I/O.

### 2. Tugas Praktikum 2: Task Parallelism (CPU-Bound)

-   **File:** `praktikum_2.py`
-   **Tujuan:** Menunjukkan kekuatan *multiprocessing* untuk tugas komputasi berat (CPU-bound) dan memahami konsep *speedup* serta *efisiensi*.
-   **Deskripsi:** Skrip ini menjalankan fungsi komputasi berat secara serial dan secara paralel menggunakan 2, 4, dan 8 proses dengan `ProcessPoolExecutor`.
-   **Cara Menjalankan:**
    ```bash
    python praktikum_2.py
    ```
-   **Hasil & Pembelajaran Utama:** *Multiprocessing* berhasil memberikan percepatan yang signifikan dengan memanfaatkan semua core CPU yang tersedia, sebuah hal yang tidak dapat dicapai oleh *multithreading* untuk tugas CPU-bound karena adanya GIL.

### 3. Tugas Praktikum 3: Perbandingan Threads vs Tasks

-   **File:** `praktikum_3.py`
-   **Tujuan:** Melakukan perbandingan langsung (*head-to-head*) antara *threads* dan *processes* pada kedua jenis beban kerja (I/O-bound dan CPU-bound).
-   **Deskripsi:** Skrip ini menjalankan fungsi simulasi I/O dan fungsi komputasi CPU dalam tiga mode: serial, *threaded*, dan *multiprocess*, lalu merangkum hasilnya dalam satu tabel.
-   **Cara Menjalankan:**
    ```bash
    python praktikum_3.py
    ```
-   **Hasil & Pembelajaran Utama:** Menguatkan aturan praktis: **"Gunakan Threads untuk I/O, dan Processes untuk CPU"**.

### 4. Tugas Praktikum 4: Hybrid Pipeline (Threads + Processes)

-   **File:** `praktikum_4.py`
-   **Tujuan:** Mengaplikasikan semua konsep yang telah dipelajari untuk membangun pipeline pemrosesan data multi-tahap yang efisien.
-   **Deskripsi:** Skrip ini membangun pipeline di mana *threads* digunakan untuk membaca file dari disk (I/O) dan *processes* digunakan untuk mengolah konten file tersebut (CPU). Kinerjanya dibandingkan dengan baseline *single-process*.
-   **Cara Menjalankan:**
    ```bash
    python praktikum_4.py
    ```
-   **Hasil & Pembelajaran Utama:** Model hibrida menunjukkan peningkatan performa yang luar biasa (diukur dari *throughput* dan *latency*), membuktikan bahwa arsitektur ini sangat efektif untuk aplikasi dunia nyata yang memiliki campuran tugas I/O dan CPU.

## Kesimpulan Umum

Proyek ini memberikan pemahaman mendalam dan praktis tentang bagaimana memilih dan menerapkan strategi paralelisme yang tepat di Python. Melalui serangkaian eksperimen, menjadi jelas bahwa tidak ada satu solusi "terbaik" untuk semua masalah; sebaliknya, pilihan antara *threads* dan *processes* sangat bergantung pada sifat beban kerja aplikasi.

