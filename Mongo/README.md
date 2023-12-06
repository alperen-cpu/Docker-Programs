```markdown
# MongoDB Docker Compose Projesi

Docker Compose kullanarak MongoDB veritabanı sunucusunu başlatan bir örnektir. MongoDB, `username` ve `password` ile korunmaktadır.

### Gereksinimler

- Docker: [Docker'in Resmi İndirme Sayfası](https://docs.docker.com/get-docker/)

### Projeyi Çalıştırma

1. Docker'ı yüklediğinizden emin olun.

2. Proje dizinine gidin ve Docker Compose komutunu kullanarak MongoDB konteynerini başlatın:

docker compose up
```

MongoDB sunucusunu başlatacak ve ayarladığınız kullanıcı adı ve parola ile koruyacaktır.

3. MongoDB sunucusu başladığında, MongoDB veritabanınızı kullanmaya başlayabilirsiniz.

   - MongoDB istemcisini local makinenizde kullanıyorsanız, aşağıdaki komutu kullanarak MongoDB'ye bağlanın:

```bash
mongo --username username --password password --authenticationDatabase admin
```

   - Python veya başka bir programla MongoDB'ye erişiyorsanız, ilgili sürücüyü kullanarak veritabanı işlemlerinizi gerçekleştirebilirsiniz. (Örneğin, pymongo sürücüsü Python için)

4. İşiniz bittiğinde, MongoDB sunucusunu durdurmak için aşağıdaki komutu kullanın:

```bash
docker compose down
```

### Python Çalıştırma

1. Docker'ı yüklediğinizden ve Docker Compose ile MongoDB'yi başlattığınızdan emin olun.

2. Python kullanarak test etmek için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Python betiğini çalıştırmak için aşağıdaki yazılım ve araçlara ihtiyacınız vardır:

- Python 3.x: [Python İndirme Sayfası](https://www.python.org/downloads/)

Kullanıcı adı ve parola girdikten sonra python kodunun test database ve table oluşturma için kullanabilirsiniz.

```bash
python3 connect.py
```


## Katkıda Bulunma

Eğer projeye katkıda bulunmak isterseniz, lütfen [GitHub deposunu](https://github.com/alperen-cpu/Docker-Programs.git) ziyaret edin.
