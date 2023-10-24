import subprocess

try:
    subprocess.check_output(['pip3', 'install', 'pymongo'])
    print("pymongo modülü başarıyla indirildi.")
except Exception as e:
    print("pymongo modülü indirilirken bir hata oluştu:", e)

import pymongo

kullanici_adi = ""
kullanici_parolasi = ""
host = "localhost"
port = 27017

try:
    client = pymongo.MongoClient(host, port, username=kullanici_adi, password=kullanici_parolasi)
    db = client.get_database("selam")

    collection = db.get_collection("test_tablosu")
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    collection.insert_one(sample_data)
    print("Test DB ve Test Tablosu oluşturuldu.")

except pymongo.errors.ConnectionFailure:
    print("MongoDB bağlantısı başarısız.")
