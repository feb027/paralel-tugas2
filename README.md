# Tugas Praktikum 1: Thread Parallelism (I/O-Bound)

Repositori ini berisi implementasi untuk Tugas Praktikum 1 mata kuliah Komputasi Paralel & Terdistribusi.

## Prasyarat

- Python 
- Library `tabulate`

Anda dapat menginstal pustaka yang diperlukan menggunakan pip:
```bash
pip install tabulate```
```
## Cara Menjalankan Program

Untuk menjalankan simulasi, buka terminal atau command prompt, navigasi ke direktori tempat file ini berada, dan jalankan perintah berikut:

```bash
python praktikum_1.py
```

## Tugas Praktikum 2: Task Parallelism (CPU-Bound)

Script untuk tugas ini akan menjalankan komputasi berat secara serial dan kemudian secara paralel menggunakan 2, 4, dan 8 proses.
Jalankan perintah berikut di terminal:

```bash
python praktikum_2.py
```

# Tugas Praktikum 3: Perbandingan Threads vs Tasks


Script ini akan menjalankan perbandingan komprehensif antara eksekusi serial, berbasis thread, dan berbasis proses untuk tugas I/O-bound dan CPU-bound.

```bash
python praktikum_3.py
```

# Tugas Praktikum 4: Hybrid Pipeline (Threads + Processes)


Skrip ini akan membuat folder data_temp berisi file-file dummy untuk diproses. Folder ini akan dihapus secara otomatis setelah program selesai.

```bash
python praktikum_4.py
```