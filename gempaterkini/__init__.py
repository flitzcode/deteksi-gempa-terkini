import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        #200-299 = berhasil, 300-399 =  redirection, 500-599 = server error, 400-499 = client errors,
        print(content.text)
        #soup = BeautifulSoup(content)
        #print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = '23 Juli 2022'
        hasil['waktu'] = '14:35:46 WIB'
        hasil['magnitudo'] = '5.7'
        #hasil['kedalaman'] = '13 Km'
        hasil['lokasi'] = {'ls': 7.57, 'bt': 122.45}
        hasil['pusat'] = 'Dirasakan (Skala MMI): III Ende, III Maumere, III Larantuka, III Lewoleba, II - III Pulau Kalaotoa'

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")