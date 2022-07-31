"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempaterkini

if __name__ == '__main__':
    print(f'Aplikasi utama menggunakan package ang memiliki deskripsi {gempaterkini.description}')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)