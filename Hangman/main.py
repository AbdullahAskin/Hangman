import pygame
import math
import random
from tkinter import *
from tkinter import messagebox

pygame.init()
GENISLIK, UZUNLUK = 1366, 768
panel = pygame.display.set_mode((GENISLIK, UZUNLUK))
pygame.display.set_caption("Adam Asmaca")

JOKERYARICAP = 45
JOKERBOSLUK = 25
jokerlerString = ["IpucuJoker", "HarfJoker"]
jokerler = []

YARICAP = 30
BOSLUK = 10
harfler = []
alfabeString = []
alfabeString = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
basKonumx = 25
basKonumy = 25

ipucuPenceresi = Tk()

ipucuGorunurlugu = 0

for i in range(29):
    x = basKonumx + YARICAP + (BOSLUK + YARICAP * 2) * (i % 3)
    y = basKonumy + YARICAP + (BOSLUK + YARICAP * 2) * (i // 3)
    harfler.append([x, y, alfabeString[i], True])

for i in range(2):
    x = 250 + JOKERYARICAP + (JOKERBOSLUK + JOKERYARICAP * 2) * i
    y = 675
    jokerler.append([x, y, jokerlerString[i], True])

HARF_FONTU = pygame.font.SysFont('courier-new', 40)
KELIME_FONTU = pygame.font.SysFont('courier-new', 80)
IPUCU_FONTU = pygame.font.SysFont('courier-new', 50)

jokerResimler = []
for i in range(2):
    jokerResim = pygame.image.load("Joker-" + str(i) + ".png")
    jokerResimler.append(jokerResim)

buttonBackground = pygame.image.load("buttonBackground.png")

resimler = []
for i in range(8):
    resim = pygame.image.load("AdamAsmaca-" + str(i) + ".png")
    resimler.append(resim)

hata_sayisi = 0
kelimeler = ["AYAKKABI", "EL ARABASI", "KİTAP KURDU", "BULMACA", "FUTBOL SAHASI", "SOSYAL MEDYA", "MÜZİK KUTUSU",
             "BAĞIMSIZ", "ŞÖMİNE", "RÖNTGEN",
             "AÇIKLAMA", "FIRTINA ÖNCESİ SESSİZLİK", "KARDAN ADAM", "ASPARAGAS", "ZAR ATMAK", "PEMBE YALAN",
             "MİLLİ PİYANGO", "ASABİYET", "HOPARLÖR", "KÜPLERE BİNMEK"]
ipuclari = ["Giyilir", "Taş, kum taşımaya yarar", "Çok okuyan", "İnsanı düşünmeye sevk eder",
            "22 kişinin oyun oynadığı alan", "İnsanların karşlıklı paylaşım yapabildiği platform",
            "Genelde tek melodiyle sınırlıdır",
            "Hareket kabiliyetinin ve karar verme limitinin yüksek olması", "Isınmayı sağlar",
            "Hastalık teşhisinde kullanılan test", "Bir şeyin anlaşılması için sözcüklerle basitleştirilmesi",
            "Alışılmışın dışındaki bir süreçten sonra geleceği tahmin edilen olay",
            "Kışın herkesin yaptığı eğlence aracı", "Gerçeğe dayanmayan",
            "Oyunlardaki durumları belirlemek için kullanılan şans şartı",
            "Günü veya durumu kurtarmak için söylenen ve fayda gözeten davranış ",
            "Parayı insan hayali ve umuduna dönüştüren bir şans oyunu", "Kısa süreli öfke", "Sesi yükselten aygıt",
            "Çok öfkelenmek"]

kelime = random.choice(kelimeler)
tahmin = []

BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
TURKUAZ = (94, 192, 198)
TURUNCU = (250, 139, 13)


def draw():
    # Ilk once resmi cizdik.
    panel.blit(resimler[hata_sayisi], (0, 0))

    harfX = 250
    harfY = 100
    tempHarfX = harfX

    for harf in kelime:
        if harf in tahmin:
            stringMevcutHarf = harf
        elif harf.__eq__(" "):
            stringMevcutHarf = " "
        else:
            stringMevcutHarf = "_"
        if (stringMevcutHarf.__eq__(" ")):
            harfY += 100
            tempHarfX = harfX
        else:
            if stringMevcutHarf.__eq__("_"):
                metinHarf = KELIME_FONTU.render(stringMevcutHarf, 1, TURKUAZ)
            else:
                metinHarf = KELIME_FONTU.render(stringMevcutHarf, 1, TURUNCU)

            panel.blit(metinHarf, (tempHarfX, harfY))
            tempHarfX += 55

    for harf in harfler:
        x, y, ltr, visible = harf
        if visible:
            panel.blit(buttonBackground, (x - buttonBackground.get_width() / 2, y - buttonBackground.get_height() / 2))
            pygame.draw.circle(panel, SIYAH, (x, y), YARICAP, 5)
            metinAlfabe = HARF_FONTU.render(ltr, 1, SIYAH)
            panel.blit(metinAlfabe, (x - metinAlfabe.get_width() / 2, y - metinAlfabe.get_height() / 2))

    counter = 0
    for joker in jokerler:
        x, y, ltr, visible = joker
        if visible:
            panel.blit(jokerResimler[counter],
                       (x - jokerResimler[counter].get_width() / 2, y - jokerResimler[counter].get_height() / 2))
            pygame.draw.circle(panel, SIYAH, (x, y), JOKERYARICAP, 3)
        counter += 1

    pygame.display.update()


def display_message(mesaj):
    pygame.time.delay(1000)
    metin = KELIME_FONTU.render(mesaj, 1, SIYAH)
    panel.blit(metin, (GENISLIK / 2 - metin.get_width() / 2, UZUNLUK / 2 - metin.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def joker_calistir(jokerTuru):
    if jokerTuru.__eq__("IpucuJoker"):
        kelimeIndis = kelimeler.index(kelime)
        iKelime = ipuclari[kelimeIndis]
        ipucuPenceresi.overrideredirect(1)
        ipucuPenceresi.withdraw()
        messagebox.showinfo("İPUCU", iKelime)
        ipucuPenceresi.destroy()

    elif jokerTuru.__eq__("HarfJoker"):
        randomHarf = " "
        while randomHarf.__eq__(" ") or randomHarf in tahmin:
            randomHarf = random.choice(kelime)
        tahmin.append(randomHarf)


def main():
    global hata_sayisi

    run = True

    while run:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for harf in harfler:  # Harfler icin geziyoruz
                    x, y, ltr, visible = harf
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < YARICAP:
                            harf[3] = False
                            tahmin.append(ltr)
                            if ltr not in kelime:
                                hata_sayisi += 1
                for joker in jokerler:  # Jokerler icin geziyoruz
                    x, y, ltr, visible = joker
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < JOKERYARICAP:
                            joker[3] = False
                            joker_calistir(joker[2])

        draw()

        won = True
        for harf in kelime:
            if harf not in " ":
                if harf not in tahmin:
                    won = False
                    break

        if won:
            display_message("KAZANDINIZ")
            break

        if hata_sayisi == 7:
            display_message("ADAM ÖLMEDİ")
            break

main()
pygame.quit()
