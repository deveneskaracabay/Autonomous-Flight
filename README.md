# Otonom Uçuş
Verdiğim kod ile beraber okulum olan Yıldız Teknik Üniversitesinde bir tur atmış olacağız.

## Yol Haritası
1. A kapısından başlıyoruz.
2. Motorlarımız açıp, uçuşa hazır olmak için yükseliyoruz.
3. İlk hedefimiz Yemekhane Binası.
4. İkinci hedef olarak Kütüphane binasına gidiyoruz.
5. Son olarak da B kapısına giderek görevi tamamlıyoruz.

## Gereksinimler
`pip install -r requirements.txt` kodu ile gerekli olan Mavproxy, Pymavlink, Dronekit ve Dronekit-sitl paketlerine sahip olabilirsiniz.

## Simulasyonu Başlatmak
`dronekit-sitl copter --home=41.0207561,28.8988495,0,180` kodu ile simülasyonumuzu başlatıyoruz. Bu koordinatlar Yıldız Teknik Üniversitesinin **A Kapısı** adresini belirtmektedir.
<br/> 

`mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:<PC ID NUMARASI>:14550` kodu sayesinde de dronekit simulasyon programımız ve drone kodlarımızı birbirine bağlıyoruz. Simulasyonu görüntülemek için **apm planner2** veya **mission planner** gibi uygulamaları kullanabilirsiniz.
<br/> 
### Not :
Simulasyon programlarımızı bu uygulamalar mavproxy.py sayesinde bağlarız. Bu işlemin başarıyla gerçekleşmesi için mavproxy.py uygulamasına **udp:----:14550** kısmında kendi bilgisayarımızın id numarasını parametre olarak vermeliyiz. 
