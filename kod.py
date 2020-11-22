# Enes Karacabay 
# Drone hedefe uçuş kodları


# Kütüphanelerin içe aktarılması

from __future__ import print_function
import time
from dronekit import VehicleMode, LocationGlobalRelative, connect


# Bağlantı kuruluyor
drone = connect("udp:127.0.0.1:14551", wait_ready=True)



# uçuş kontrolü ve yükselme 
def Hazırlan(hedef_yükseklik):
    print("Uçuşa hazırlık kontrol ediliyor...")
    while not drone.is_armable:
        print("Uçuş için hazırlıklar yapılıyor...")
        time.sleep(1)
    
    print("İlk aşama başarıyla tamamlandı!")
    drone.mode = VehicleMode("GUIDED")
    drone.armed = True

    while not drone.mode.name=='GUIDED' and not drone.armed :
        print("Son kontroller yapılıyor..")
        time.sleep(1)

    print("Uçuş Başlasın !!")
    drone.simple_takeoff(hedef_yükseklik)

    while True:

        print("Yükseklik : ", drone.location.global_relative_frame.alt)
        if drone.location.global_relative_frame.alt >= hedef_yükseklik*0.95:
            print("Hedef yüksekliğe ulaşıldı...")
            break
        time.sleep(3)
#A Kapısı
#41.0207561
#28.8988495

Hazırlan(50)
drone.airspeed = 3

print("İlk hedef : Yemekhane Binası")
hedef1 = LocationGlobalRelative(41.0270615 ,28.8880241 ,50)
drone.simple_goto(hedef1)
time.sleep(0.5)
drone.simple_goto(hedef1)
time.sleep(25)
print("Hedefe Başarıyla Ulaşıldı")

print("İkinci Hedef : Kütüphane Binası")
hedef2 = LocationGlobalRelative(41.0219298,28.8941610 ,50)
drone.simple_goto(hedef2)
time.sleep(0.5)
drone.simple_goto(hedef2)
time.sleep(25)
print("Hedefe Başarıyla Ulaşıldı")


print("Son Hedef : B Kapısı ")
hedef3 = LocationGlobalRelative( 41.0297162, 28.8903093, 50)
drone.simple_goto(hedef3)
time.sleep(0.5)
drone.simple_goto(hedef3)
time.sleep(25)
print("Hedefe Başarıyla Ulaşıldı")


drone.mode = VehicleMode("LAND")
drone.mode = VehicleMode("LAND")

drone.close

##  609  dronekit-sitl copter --home=41.0207561,28.8988495,0,180
## mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:192.168.1.39:14550
