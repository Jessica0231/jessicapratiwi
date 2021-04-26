import pandas as pd
from fastapi import FastAPI

app = FastAPI()

data = pd.read_csv('Jumlah Siswa di Kabupaten Batang 2018-2019.csv')

datas = data.drop(columns=['Laki -Laki TK', 'perempuan TK', 'Laki -Laki RA', 'perempuan RA', 'Laki -Laki SD', 'perempuan SD', 'Laki -Laki MI', 'perempuan MI', 'Laki -Laki SMP', 'perempuan SMP', 'Laki -Laki MTS', 'perempuan MTS', 'Laki -Laki SMA', 'perempuan SMA', 'Laki -Laki SMK', 'perempuan SMK', 'Laki -Laki MA', 'perempuan MA'])

datas.rename(columns = {'Kecamatan                                       ':'Kecamatan', 'jumlah_siswa_per_kecamatan':'Jumlah Siswa'}, inplace = True)

#5 Kecamatan dengan Jumlah Siswa Terbanyak di Kabupaten Batang Tahun 2018-2019
@app.get("/top5kecamatan")
def read_top5kecamatan():
    display = datas.sort_values(by='Jumlah Siswa')
    displayto = display.head(5)
    return displayto.to_dict(orient='records')