"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 23 Juli 2022
    Waktu: 14:35:46 WIB
    Magnitudo: 5.7
    Kedalaman: 13 km
    Lokasi: LS=7.57 BT=122.45
    Pusat Gempa: Pusat gempa berada di laut 100 km barat laut Larantuka
    Dirasakan: Dirasakan (Skala MMI): III Ende, III Maumere, III Larantuka, III Lewoleba, II - III Pulau Kalaotoa
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '23 Juli 2022'
    hasil['waktu'] = '14:35:46 WIB'
    hasil['magnitudo'] = '5.7'
    #hasil['kedalaman'] = '13 Km'
    hasil['lokasi'] = {'ls': 7.57, 'bt': 122.45}
    hasil['pusat'] = 'Dirasakan (Skala MMI): III Ende, III Maumere, III Larantuka, III Lewoleba, II - III Pulau Kalaotoa'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)