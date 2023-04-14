# Pypi for Class

Library ini disusun dengan menggunakan struktur direktori yang terorganisir dan mengimplementasikan penggunaan class secara penuh untuk modularitas dan fleksibilitas.

### Fitur Utama
- Struktur direktori yang terorganisir dengan subfolder untuk modul-modul terkait.
- Penggunaan class untuk memisahkan fungsionalitas menjadi bagian-bagian yang terpisah dan dapat digunakan secara mandiri.
- Dokumentasi lengkap dan contoh penggunaan yang disertakan dalam setiap modul.
- Dukungan untuk Python 3.6, 3.7, 3.8, 3.9, dan 3.10.

### Struktur Direktori

```bash
pypi-class
├── __init__.py
├── module1.py
├── module2.py
├── subpackage1
│   ├── __init__.py
│   ├── module3.py
│   └── module4.py
├── subpackage2
│   ├── __init__.py
│   └── module5.py
├── LICENSE
├── README.md
└── module5.py
```

### Penggunaan

#### 1. Menggunakan import:
```python
import pypi_class

pypi_class.Module1().greet()
pypi_class.Module2().greet()
pypi_class.subpackage1.Module3().greet()
pypi_class.subpackage1.Module4().greet()
pypi_class.subpackage2.Module5().greet()
```

#### 2. Menggunakan from import:
```python
from pypi_class import Module1, Module2
from pypi_class.subpackage1 import Module3, Module4
from pypi_class.subpackage2 import Module5

Module1().greet()
Module2().greet()
Module3().greet()
Module4().greet()
Module5().greet()
```

Untuk informasi lebih lanjut dan contoh penggunaan, silakan eksplorasi sendiri.

### Lisensi:
**PYPI-CLASS** dikeluarkan di bawah Lisensi MIT.

Harap diingat bahwa contoh ini hanya sebagai referensi dan Anda perlu menggantikan informasi yang diberikan, seperti nama library, struktur direktori, nama modul, kelas, metode, dan atribut sesuai dengan kebutuhan dan implementasi proyek Anda sendiri.