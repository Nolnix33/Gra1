import pygame
import sys
import random
from pygame.locals import *


pygame.init()
czy_moge = 0
postac_x_gravity = 0
mode = 'menu'
tekst_font_50 = pygame.font.Font(None , 50)
tekst_font_75 = pygame.font.Font(None,75)
tekst_font_100 = pygame.font.Font(None,100)
wybrane_miejsce_bonusu_1 = 'brak'
wybrane_miejsce_bonusu_2 = 'brak'
rect = pygame.image.load('rect.png')
rect_rect = rect.get_rect(bottomright=(1000,425))
czy_na_czas = 'tak'
krysztaly = 0
miejsce1 = pygame.image.load('gra_bonus_brak.png')
miejsce2 = pygame.image.load('gra_bonus_brak.png')
miejsce3 = pygame.image.load('gra_bonus_brak.png')
czy_miejsce_brak_1 = 1
czy_miejsce_brak_2 = 1
czy_miejsce_brak_3 = 1
poziom_5_czy_wzieto_medalion = 'nie'
kierunek_bossa = 'lewo'
ile_razy = 0
ktore_pokazac = 'gora'
ruch = 0
martwy = 'nie'
czy_masz_bonus_1 = 'nie'
czy_masz_bonus_2 = 'nie'
pasek_ruchu_wczytywania = pygame.image.load('pasek_ruchu_wczytywania.png')
pasek_ruchu_wczytywania_rect = pasek_ruchu_wczytywania.get_rect(center=(550,375))
piksel_wczytywania = pygame.image.load('jeden_piksel_wczytywania.png')
piksel_wczytywania_rect = piksel_wczytywania.get_rect(topleft=(0,0))
kierunek_wczytywania = 10
ile_masz_skoku = 1




generator_1 = pygame.image.load('generator_1.png')
generator_1_rect = generator_1.get_rect(midbottom=(550,740))

faza_kodu = 1
zadanie_swiatelka = 'nie'
zadanie_radar = 'nie'
zadanie_kod = 'nie'
zadanie_suwak_1 = 'nie'
zadanie_suwak_2 = 'nie'
wykonywanie_generatora_tlo = pygame.image.load('wykonywanie_generatora_tło.png')
guzik_konca_wykonywania = pygame.image.load('guzik_zakończenia_generatora.png')
guzik_konca_wykonywania_rect = guzik_konca_wykonywania.get_rect(topright=(1050,150))
przycisk_1_generatora = pygame.image.load('przycisk_1_generatora.png')
przycisk_1_generatora_rect = przycisk_1_generatora.get_rect(center=(350,75))
przycisk_2_generatora = pygame.image.load('przycisk_2_generatora.png')
przycisk_2_generatora_rect = przycisk_2_generatora.get_rect(center=(450,75))
przycisk_3_generatora = pygame.image.load('przycisk_3_generatora.png')
przycisk_3_generatora_rect = przycisk_3_generatora.get_rect(center=(550,75))
przycisk_4_generatora = pygame.image.load('przycisk_4_generatora.png')
przycisk_4_generatora_rect = przycisk_4_generatora.get_rect(center=(650,75))
przycisk_5_generatora = pygame.image.load('przycisk_5_generatora.png')
przycisk_5_generatora_rect = przycisk_5_generatora.get_rect(center=(750,75))
panel_cyferek = pygame.image.load('kod_generatora.png')
obrazek_radaru = 'radar_generatora_1.png'
radar_generatora = pygame.image.load(obrazek_radaru)
radar_generatora_rect = radar_generatora.get_rect(midbottom=(690,730))
miejsce_suwaka_1 = 'przełącznik_generatora_lewo.png'
miejsce_suwaka_2 = 'przełącznik_generatora_lewo.png'
suwak_1 = pygame.image.load(miejsce_suwaka_1)
suwak_1_rect = suwak_1.get_rect(topleft=(390,150))
suwak_2 = pygame.image.load(miejsce_suwaka_2)
suwak_2_rect = suwak_2.get_rect(topleft=(390,300))
liczba_1 = pygame.image.load('cyfra_1.png')
liczba_1_rect = liczba_1.get_rect(topleft=(60,135))
liczba_2 = pygame.image.load('cyfra_2.png')
liczba_2_rect = liczba_2.get_rect(topleft=(158,135))
liczba_3 = pygame.image.load('cyfra_3.png')
liczba_3_rect = liczba_3.get_rect(topleft=(256,130))
liczba_4 = pygame.image.load('cyfra_4.png')
liczba_4_rect = liczba_4.get_rect(topleft=(60,228))
liczba_5 = pygame.image.load('cyfra_5.png')
liczba_5_rect = liczba_5.get_rect(topleft=(158,228))
liczba_6 = pygame.image.load('cyfra_6.png')
liczba_6_rect = liczba_6.get_rect(topleft=(256,228))
liczba_7 = pygame.image.load('cyfra_7.png')
liczba_7_rect = liczba_7.get_rect(topleft=(60,331))
liczba_8 = pygame.image.load('cyfra_8.png')
liczba_8_rect = liczba_8.get_rect(topleft=(158,331))
liczba_9 = pygame.image.load('cyfra_9.png')
liczba_9_rect = liczba_9.get_rect(topleft=(256,331))
ktory_kolor_wybrac = random.randint(1,5)
ktory_kolor_wybrano = 'żaden'
if ktory_kolor_wybrac == 1:
    ktory_kolor_wyswietlac = 'przycisk_1_generatora.png'
elif ktory_kolor_wybrac == 2:
    ktory_kolor_wyswietlac = 'przycisk_2_generatora.png'
elif ktory_kolor_wybrac == 3:
    ktory_kolor_wyswietlac = 'przycisk_3_generatora.png'
elif ktory_kolor_wybrac == 4:
    ktory_kolor_wyswietlac = 'przycisk_4_generatora.png'
elif ktory_kolor_wybrac == 5:
    ktory_kolor_wyswietlac = 'przycisk_5_generatora.png'
podpowiadajacy_kolor = pygame.image.load(ktory_kolor_wyswietlac)
podpowiadajacy_kolor_rect = podpowiadajacy_kolor.get_rect(center=(550,75))
tablica_z_kodem = pygame.image.load('tablica_z_kodem.png')
tablica_z_kodem_rect = tablica_z_kodem.get_rect(midtop=(550,50))
ktora_cyfre_w_kodzie_wybrac_1 = random.randint(1,9)
ktora_cyfre_w_kodzie_wybrac_2 = random.randint(1,9)
ktora_cyfre_w_kodzie_wybrac_3 = random.randint(1,9)
tekst_cyfra_1_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_1}", False, 'Black')
tekst_cyfra_2_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_2}", False, 'Black')
tekst_cyfra_3_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_3}", False, 'Black')
tekst_cyfra_1_kodu_rect = tekst_cyfra_1_kodu.get_rect(bottomleft=(480,300))
tekst_cyfra_2_kodu_rect = tekst_cyfra_2_kodu.get_rect(midbottom=(550,300))
tekst_cyfra_3_kodu_rect = tekst_cyfra_3_kodu.get_rect(bottomright=(620,300))
kierunek_suwaka_1 = random.randint(1,2)
niebieskie_swiatlo_1 = pygame.image.load('niebieskie_światło.png')
if kierunek_suwaka_1 == 1:
    niebieskie_swiatlo_1_rect = niebieskie_swiatlo_1.get_rect(midleft=(50,300))
elif kierunek_suwaka_1 == 2:
    niebieskie_swiatlo_1_rect = niebieskie_swiatlo_1.get_rect(midright=(1050,300))
kierunek_suwaka_2 = random.randint(1,2)
niebieskie_swiatlo_2 = pygame.image.load('niebieskie_światło.png')
if kierunek_suwaka_2 == 1:
    niebieskie_swiatlo_2_rect = niebieskie_swiatlo_2.get_rect(midleft=(50,450))
elif kierunek_suwaka_2 == 2:
    niebieskie_swiatlo_2_rect = niebieskie_swiatlo_2.get_rect(midright=(1050,450))
cel_radaru = random.randint(1,4)
if cel_radaru == 1:
    slupek_radarowy = pygame.image.load('słupek_ziemia.png')
    slupek_radarowy_rect = slupek_radarowy.get_rect(midbottom=(100,740))
elif cel_radaru == 2:
    slupek_radarowy = pygame.image.load('słupek_ziemia.png')
    slupek_radarowy_rect = slupek_radarowy.get_rect(midbottom=(1000,740))
elif cel_radaru == 3:
    slupek_radarowy = pygame.image.load('słupek_sufit.png')
    slupek_radarowy_rect = slupek_radarowy.get_rect(midtop=(100,50))
elif cel_radaru == 4:
    slupek_radarowy = pygame.image.load('słupek_sufit.png')
    slupek_radarowy_rect = slupek_radarowy.get_rect(midtop=(1000,50))
if obrazek_radaru == 'radar_generatora_1.png':
    if cel_radaru == 4:
        zadanie_radar = 'wykonano'
    elif not cel_radaru == 4:
        zadanie_radar = 'nie'

if miejsce_suwaka_1 == 'przełącznik_generatora_prawo.png':
    if kierunek_suwaka_1 == 1:
        zadanie_suwak_1 = 'nie'
    elif kierunek_suwaka_1 == 2:
        zadanie_suwak_1 = 'wykonano'
elif miejsce_suwaka_1 == 'przełącznik_generatora_lewo.png':
    if kierunek_suwaka_1 == 1:
        zadanie_suwak_1 = 'wykonano'
    elif kierunek_suwaka_1 == 2:
        zadanie_suwak_1 = 'nie'
if miejsce_suwaka_2 == 'przełącznik_generatora_prawo.png':
    if kierunek_suwaka_2 == 1:
        zadanie_suwak_2 = 'nie'
    elif kierunek_suwaka_2 == 2:
        zadanie_suwak_2 = 'wykonano'
elif miejsce_suwaka_2 == 'przełącznik_generatora_lewo.png':
    if kierunek_suwaka_2 == 1:
        zadanie_suwak_2 = 'wykonano'
    elif kierunek_suwaka_2 == 2:
        zadanie_suwak_2 = 'nie'




kupowanie_bonusu_1 = pygame.image.load('kupowanie.png')
kupowanie_bonusu_1_rect = kupowanie_bonusu_1.get_rect(topright=(825,220))
kupowanie_bonusu_2 = pygame.image.load('kupowanie.png')
kupowanie_bonusu_2_rect = kupowanie_bonusu_2.get_rect(topright=(825,220))
ile_niebieskich_kosztuje_bonus_1 = 500
ile_niebieskich_kosztuje_bonus_2 = 500
ile_czerwonych_kosztuje_bonus_1 = 300
ile_czerwonych_kosztuje_bonus_2 = 300
ile_zielonkawych_kosztuje_bonus_1 = 100
ile_zielonkawych_kosztuje_bonus_2 = 100

rect_ukonczenia_poziomu_1 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_1_rect = rect_ukonczenia_poziomu_1.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_2 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_2_rect = rect_ukonczenia_poziomu_2.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_3 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_3_rect = rect_ukonczenia_poziomu_3.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_4 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_4_rect = rect_ukonczenia_poziomu_4.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_6 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_6_rect = rect_ukonczenia_poziomu_6.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_7 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_7_rect = rect_ukonczenia_poziomu_7.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_8 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_8_rect = rect_ukonczenia_poziomu_8.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_9 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_9_rect = rect_ukonczenia_poziomu_9.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_11 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_11_rect = rect_ukonczenia_poziomu_11.get_rect(bottomright=(1100,750))
rect_ukonczenia_poziomu_13 = pygame.image.load('rect_ukończenia_poziomu.png')
rect_ukonczenia_poziomu_13_rect = rect_ukonczenia_poziomu_13.get_rect(bottomright=(1100,750))

status_poziomu_2 = 'blokada'
status_poziomu_3 = 'blokada'
status_poziomu_4 = 'blokada'
status_poziomu_5 = 'blokada'
status_poziomu_6 = 'blokada'
status_poziomu_7 = 'blokada'
status_poziomu_8 = 'blokada'
status_poziomu_9 = 'blokada'
status_poziomu_10 = 'blokada'
status_poziomu_11 = 'blokada'
status_poziomu_12 = 'blokada'
status_poziomu_13 = 'blokada'
status_poziomu_14 = 'blokada'
status_poziomu_15 = 'blokada'
status_poziomu_16 = 'blokada'
status_poziomu_17 = 'blokada'
status_poziomu_18 = 'blokada'
status_poziomu_19 = 'blokada'
status_poziomu_20 = 'blokada'
status_poziomu_21 = 'blokada'
status_poziomu_22 = 'blokada'
status_poziomu_23 = 'blokada'
status_poziomu_24 = 'blokada'
status_poziomu_25 = 'blokada'


klodka_poziomu_2 = pygame.image.load('kłódka.png')
klodka_poziomu_3 = pygame.image.load('kłódka.png')
klodka_poziomu_4 = pygame.image.load('kłódka.png')
klodka_poziomu_5 = pygame.image.load('kłódka.png')
klodka_poziomu_6 = pygame.image.load('kłódka.png')
klodka_poziomu_7 = pygame.image.load('kłódka.png')
klodka_poziomu_8 = pygame.image.load('kłódka.png')
klodka_poziomu_9 = pygame.image.load('kłódka.png')
klodka_poziomu_10 = pygame.image.load('kłódka.png')
klodka_poziomu_11 = pygame.image.load('kłódka.png')
klodka_poziomu_12 = pygame.image.load('kłódka.png')
klodka_poziomu_13 = pygame.image.load('kłódka.png')
klodka_poziomu_14 = pygame.image.load('kłódka.png')
klodka_poziomu_15 = pygame.image.load('kłódka.png')
klodka_poziomu_16 = pygame.image.load('kłódka.png')
klodka_poziomu_17 = pygame.image.load('kłódka.png')
klodka_poziomu_18 = pygame.image.load('kłódka.png')
klodka_poziomu_19 = pygame.image.load('kłódka.png')
klodka_poziomu_20 = pygame.image.load('kłódka.png')
klodka_poziomu_21 = pygame.image.load('kłódka.png')
klodka_poziomu_22 = pygame.image.load('kłódka.png')
klodka_poziomu_23 = pygame.image.load('kłódka.png')
klodka_poziomu_24 = pygame.image.load('kłódka.png')
klodka_poziomu_25 = pygame.image.load('kłódka.png')



poziom_1_tlo = pygame.image.load('tło_do_poziomu_1_planszy_1.png')
poziom_1_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_1_stalaktyt_1_rect = poziom_1_stalaktyt_1.get_rect(midtop=(400,50))
poziom_1_stalaktyt_1_gravity = 0
poziom_1_stalaktyt_2 = pygame.image.load('stalaktyt1.png')
poziom_1_stalaktyt_2_rect = poziom_1_stalaktyt_2.get_rect(midtop=(800,50))
poziom_1_stalaktyt_2_gravity = 0

powrot_z_przegranej_poziomu_1 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_1_rect = powrot_z_przegranej_poziomu_1.get_rect(topright=(1100,0))
powtorka_poziomu_1 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_1_rect = powtorka_poziomu_1.get_rect(center=(550,375))

pauza_poziomu_1 = pygame.image.load('pauza.png')
pauza_poziomu_1_rect = pauza_poziomu_1.get_rect(center=(550,375))
pauza_poziomu_1_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_1_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_1_powrot_rect = pauza_poziomu_1_powrot.get_rect(center=(550,275))
pauza_poziomu_1_wyjdz_rect = pauza_poziomu_1_wyjdz.get_rect(center=(550,400))

poziom_1_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_1_nastepny_poziom_rect = poziom_1_nastepny_poziom.get_rect(topleft=(575,375))
poziom_1_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_1_zagraj_ponownie_poziom_rect = poziom_1_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_1_powrot_do_menu = pygame.image.load('powrót.png')
poziom_1_powrot_do_menu_rect = poziom_1_powrot_do_menu.get_rect(topright=(1100,0))


poziom_2_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_2_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_2_stalaktyt_1_rect = poziom_1_stalaktyt_1.get_rect(midtop=(500,50))
poziom_2_stalaktyt_1_gravity = 0
poziom_2_enemy_1 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_2_enemy_1_rect = poziom_2_enemy_1.get_rect(midbottom=(1000,730))
poziom_2_enemy_1_speed = 10

powrot_z_przegranej_poziomu_2 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_2_rect = powrot_z_przegranej_poziomu_2.get_rect(topright=(1100,0))
powtorka_poziomu_2 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_2_rect = powtorka_poziomu_2.get_rect(center=(550,375))

pauza_poziomu_2 = pygame.image.load('pauza.png')
pauza_poziomu_2_rect = pauza_poziomu_2.get_rect(center=(550,375))
pauza_poziomu_2_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_2_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_2_powrot_rect = pauza_poziomu_2_powrot.get_rect(center=(550,275))
pauza_poziomu_2_wyjdz_rect = pauza_poziomu_2_wyjdz.get_rect(center=(550,400))

poziom_2_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_2_nastepny_poziom_rect = poziom_2_nastepny_poziom.get_rect(topleft=(575,375))
poziom_2_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_2_zagraj_ponownie_poziom_rect = poziom_2_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_2_powrot_do_menu = pygame.image.load('powrót.png')
poziom_2_powrot_do_menu_rect = poziom_2_powrot_do_menu.get_rect(topright=(1100,0))


poziom_3_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_3_slup_1 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_3_slup_1_rect = poziom_3_slup_1.get_rect(midbottom=(430,740))
poziom_3_slup_2 = pygame.image.load('plansza_1_słup_2_200px.png')
poziom_3_slup_2_rect = poziom_3_slup_2.get_rect(midbottom=(590,740))
poziom_3_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_3_stalaktyt_1_rect = poziom_1_stalaktyt_1.get_rect(midtop=(750,50))

powrot_z_przegranej_poziomu_3 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_3_rect = powrot_z_przegranej_poziomu_3.get_rect(topright=(1100,0))
powtorka_poziomu_3 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_3_rect = powtorka_poziomu_3.get_rect(center=(550,375))

pauza_poziomu_3 = pygame.image.load('pauza.png')
pauza_poziomu_3_rect = pauza_poziomu_3.get_rect(center=(550,375))
pauza_poziomu_3_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_3_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_3_powrot_rect = pauza_poziomu_3_powrot.get_rect(center=(550,275))
pauza_poziomu_3_wyjdz_rect = pauza_poziomu_3_wyjdz.get_rect(center=(550,400))

poziom_3_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_3_nastepny_poziom_rect = poziom_3_nastepny_poziom.get_rect(topleft=(575,375))
poziom_3_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_3_zagraj_ponownie_poziom_rect = poziom_3_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_3_powrot_do_menu = pygame.image.load('powrót.png')
poziom_3_powrot_do_menu_rect = poziom_3_powrot_do_menu.get_rect(topright=(1100,0))


poziom_4_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_4_slup_1 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_4_slup_1_rect = poziom_4_slup_1.get_rect(midbottom=(430,740))
poziom_4_slup_2 = pygame.image.load('plansza_1_słup_2_200px.png')
poziom_4_slup_2_rect = poziom_4_slup_2.get_rect(midbottom=(530,740))
poziom_4_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_4_sciana_1_rect = poziom_4_sciana_1.get_rect(midbottom=(650,750))
poziom_4_polka_1 = pygame.image.load('plansza_1_półka_1_250px.png')
poziom_4_polka_1_rect = poziom_4_polka_1.get_rect(midleft=(50,500))
poziom_4_wyrwa_wejscie = pygame.image.load('plansza_1_wyrwa_wejście_1.png')
poziom_4_wyrwa_wyjscie = pygame.image.load('plansza_1_wyrwa_wyjście_1.png')
poziom_4_wyrwa_wejscie_rect = poziom_4_wyrwa_wejscie.get_rect(topleft=(70,160))
poziom_4_wyrwa_wyjscie_rect = poziom_4_wyrwa_wyjscie.get_rect(topleft=(750,300))
poziom_4_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_4_stalaktyt_1_rect = poziom_4_stalaktyt_1.get_rect(topright=(1050,50))
poziom_4_stalaktyt_1_gravity = 0

powrot_z_przegranej_poziomu_4 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_4_rect = powrot_z_przegranej_poziomu_4.get_rect(topright=(1100,0))
powtorka_poziomu_4 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_4_rect = powtorka_poziomu_4.get_rect(center=(550,375))

pauza_poziomu_4 = pygame.image.load('pauza.png')
pauza_poziomu_4_rect = pauza_poziomu_4.get_rect(center=(550,375))
pauza_poziomu_4_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_4_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_4_powrot_rect = pauza_poziomu_4_powrot.get_rect(center=(550,275))
pauza_poziomu_4_wyjdz_rect = pauza_poziomu_4_wyjdz.get_rect(center=(550,400))

poziom_4_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_4_nastepny_poziom_rect = poziom_4_nastepny_poziom.get_rect(topleft=(575,375))
poziom_4_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_4_zagraj_ponownie_poziom_rect = poziom_4_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_4_powrot_do_menu = pygame.image.load('powrót.png')
poziom_4_powrot_do_menu_rect = poziom_4_powrot_do_menu.get_rect(topright=(1100,0))


poziom_5_tlo = pygame.image.load('tło_do_bossów_planszy_1.png')
poziom_5_medalion = pygame.image.load('medalion_wejścia.png')
poziom_5_medalion_rect = poziom_5_medalion.get_rect(midbottom=(400,710))
poziom_5_boss_1 = pygame.image.load('plansza_1_boss_1_lewo.png')
poziom_5_boss_1_rect = poziom_5_boss_1.get_rect(midbottom=(980,740))
poziom_5_faza_bossa = 0
poziom_5_wybicie_1 = pygame.image.load('plansza_1_wybicie_1.png')
poziom_5_wybicie_1_rect = poziom_5_wybicie_1.get_rect(midbottom=(300,740))
poziom_5_wybicie_2 = pygame.image.load('plansza_1_wybicie_1.png')
poziom_5_wybicie_2_rect = poziom_5_wybicie_2.get_rect(midbottom=(800,740))
poziom_5_kamien_1 = pygame.image.load('plansza_1_kamien_1.png')
poziom_5_kamien_1_rect = poziom_5_kamien_1.get_rect(midbottom=(random.randint(100,1000),-1000))
poziom_5_kamien_1_gravity = 11
poziom_5_kamien_2 = pygame.image.load('plansza_1_kamien_1.png')
poziom_5_kamien_2_rect = poziom_5_kamien_2.get_rect(midbottom=(random.randint(100,1000),-1000))
poziom_5_kamien_2_gravity = 11
poziom_5_kamien_3 = pygame.image.load('plansza_1_kamien_1.png')
poziom_5_kamien_3_rect = poziom_5_kamien_3.get_rect(midbottom=(random.randint(100,1000),-1000))
poziom_5_kamien_3_gravity = 11
poziom_5_kamien_4 = pygame.image.load('plansza_1_kamien_1.png')
poziom_5_kamien_4_rect = poziom_5_kamien_4.get_rect(midbottom=(random.randint(100,1000),-1000))
poziom_5_kamien_4_gravity = 11
poziom_5_kamien_5 = pygame.image.load('plansza_1_kamien_1.png')
poziom_5_kamien_5_rect = poziom_5_kamien_5.get_rect(midbottom=(random.randint(100,1000),-1000))
poziom_5_kamien_5_gravity = 11
poziom_5_guzik = pygame.image.load('guzik.png')
poziom_5_guzik_rect = poziom_5_guzik.get_rect(midleft=(50,700))
poziom_5_portal = pygame.image.load('portal.png')
poziom_5_portal_rect = poziom_5_portal.get_rect(midbottom=(900,740))

powrot_z_przegranej_poziomu_5 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_5_rect = powrot_z_przegranej_poziomu_1.get_rect(topright=(1100,0))
powtorka_poziomu_5 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_5_rect = powtorka_poziomu_5.get_rect(center=(550,375))

pauza_poziomu_5 = pygame.image.load('pauza.png')
pauza_poziomu_5_rect = pauza_poziomu_1.get_rect(center=(550,375))
pauza_poziomu_5_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_5_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_5_powrot_rect = pauza_poziomu_1_powrot.get_rect(center=(550,275))
pauza_poziomu_5_wyjdz_rect = pauza_poziomu_1_wyjdz.get_rect(center=(550,400))

poziom_5_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_5_nastepny_poziom_rect = poziom_5_nastepny_poziom.get_rect(topleft=(575,375))
poziom_5_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_5_zagraj_ponownie_poziom_rect = poziom_5_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_5_powrot_do_menu = pygame.image.load('powrót.png')
poziom_5_powrot_do_menu_rect = poziom_5_powrot_do_menu.get_rect(topright=(1100,0))


poziom_6_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_6_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_6_stalaktyt_1_rect = poziom_6_stalaktyt_1.get_rect(midtop=(400,50))
poziom_6_stalaktyt_1_gravity = 0
poziom_6_stalaktyt_2 = pygame.image.load('stalaktyt1.png')
poziom_6_stalaktyt_2_rect = poziom_6_stalaktyt_2.get_rect(midtop=(800,50))
poziom_6_stalaktyt_2_gravity = 0
poziom_6_kolec_1 = pygame.image.load('poziom_5_kolec_1.png')
poziom_6_kolec_1_rect = poziom_6_kolec_1.get_rect(midbottom=(500,740))
poziom_6_kolec_2 = pygame.image.load('poziom_5_kolec_1.png')
poziom_6_kolec_2_rect = poziom_6_kolec_2.get_rect(midbottom=(550,740))

powrot_z_przegranej_poziomu_6 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_6_rect = powrot_z_przegranej_poziomu_6.get_rect(topright=(1100,0))
powtorka_poziomu_6 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_6_rect = powtorka_poziomu_6.get_rect(center=(550,375))

pauza_poziomu_6 = pygame.image.load('pauza.png')
pauza_poziomu_6_rect = pauza_poziomu_6.get_rect(center=(550,375))
pauza_poziomu_6_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_6_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_6_powrot_rect = pauza_poziomu_6_powrot.get_rect(center=(550,275))
pauza_poziomu_6_wyjdz_rect = pauza_poziomu_6_wyjdz.get_rect(center=(550,400))

poziom_6_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_6_nastepny_poziom_rect = poziom_6_nastepny_poziom.get_rect(topleft=(575,375))
poziom_6_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_6_zagraj_ponownie_poziom_rect = poziom_6_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_6_powrot_do_menu = pygame.image.load('powrót.png')
poziom_6_powrot_do_menu_rect = poziom_6_powrot_do_menu.get_rect(topright=(1100,0))


poziom_7_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_7_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_7_stalaktyt_1_rect = poziom_7_stalaktyt_1.get_rect(midtop=(500,50))
poziom_7_stalaktyt_1_gravity = 0
poziom_7_enemy_1 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_7_enemy_1_rect = poziom_7_enemy_1.get_rect(midbottom=(2000,730))
poziom_7_enemy_1_speed = 12
poziom_7_enemy_2 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_7_enemy_2_rect = poziom_7_enemy_2.get_rect(midbottom=(4000,630))
poziom_7_enemy_2_speed = 12
poziom_7_enemy_3 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_7_enemy_3_rect = poziom_7_enemy_3.get_rect(midbottom=(5000,730))
poziom_7_enemy_3_speed = 12
poziom_7_enemy_4 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_7_enemy_4_rect = poziom_7_enemy_4.get_rect(midbottom=(6000,630))
poziom_7_enemy_4_speed = 12
poziom_7_enemy_5 = pygame.image.load('plansza_1_przeciwnik_1.png')
poziom_7_enemy_5_rect = poziom_7_enemy_5.get_rect(midbottom=(8000,730))
poziom_7_enemy_5_speed = 12
poziom_7_slup_1 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_7_slup_1_rect = poziom_7_slup_1.get_rect(midbottom=(430,740))

powrot_z_przegranej_poziomu_7 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_7_rect = powrot_z_przegranej_poziomu_2.get_rect(topright=(1100,0))
powtorka_poziomu_7 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_7_rect = powtorka_poziomu_7.get_rect(center=(550,375))

pauza_poziomu_7 = pygame.image.load('pauza.png')
pauza_poziomu_7_rect = pauza_poziomu_7.get_rect(center=(550,375))
pauza_poziomu_7_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_7_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_7_powrot_rect = pauza_poziomu_7_powrot.get_rect(center=(550,275))
pauza_poziomu_7_wyjdz_rect = pauza_poziomu_7_wyjdz.get_rect(center=(550,400))

poziom_7_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_7_nastepny_poziom_rect = poziom_7_nastepny_poziom.get_rect(topleft=(575,375))
poziom_7_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_7_zagraj_ponownie_poziom_rect = poziom_7_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_7_powrot_do_menu = pygame.image.load('powrót.png')
poziom_7_powrot_do_menu_rect = poziom_7_powrot_do_menu.get_rect(topright=(1100,0))


poziom_8_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_8_slup_1 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_8_slup_1_rect = poziom_8_slup_1.get_rect(bottomright=(330,740))
poziom_8_slup_2 = pygame.image.load('plansza_1_słup_2_200px.png')
poziom_8_slup_2_rect = poziom_8_slup_2.get_rect(bottomright=(380,740))
poziom_8_slup_3 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_8_slup_3_rect = poziom_8_slup_3.get_rect(bottomright=(730,740))
poziom_8_slup_4 = pygame.image.load('plansza_1_słup_2_200px.png')
poziom_8_slup_4_rect = poziom_8_slup_4.get_rect(bottomright=(680,740))
poziom_8_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_8_stalaktyt_1_rect = poziom_8_stalaktyt_1.get_rect(midtop=(800,50))
poziom_8_stalaktyt_1_gravity = 0
poziom_8_kolec_1 = pygame.image.load('poziom_5_kolec_1.png')
poziom_8_kolec_1_rect = poziom_8_kolec_1.get_rect(bottomleft=(385,740))
poziom_8_kolec_2 = pygame.image.load('poziom_5_kolec_1.png')
poziom_8_kolec_2_rect = poziom_8_kolec_2.get_rect(bottomleft=(435,740))
poziom_8_kolec_3 = pygame.image.load('poziom_5_kolec_1.png')
poziom_8_kolec_3_rect = poziom_8_kolec_3.get_rect(bottomleft=(485,740))
poziom_8_kolec_4 = pygame.image.load('poziom_5_kolec_1.png')
poziom_8_kolec_4_rect = poziom_8_kolec_4.get_rect(bottomleft=(535,740))
poziom_8_kolec_5 = pygame.image.load('poziom_5_kolec_1.png')
poziom_8_kolec_5_rect = poziom_8_kolec_5.get_rect(bottomleft=(585,740))

powrot_z_przegranej_poziomu_8 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_8_rect = powrot_z_przegranej_poziomu_8.get_rect(topright=(1100,0))
powtorka_poziomu_8 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_8_rect = powtorka_poziomu_8.get_rect(center=(550,375))

pauza_poziomu_8 = pygame.image.load('pauza.png')
pauza_poziomu_8_rect = pauza_poziomu_8.get_rect(center=(550,375))
pauza_poziomu_8_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_8_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_8_powrot_rect = pauza_poziomu_8_powrot.get_rect(center=(550,275))
pauza_poziomu_8_wyjdz_rect = pauza_poziomu_8_wyjdz.get_rect(center=(550,400))

poziom_8_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_8_nastepny_poziom_rect = poziom_8_nastepny_poziom.get_rect(topleft=(575,375))
poziom_8_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_8_zagraj_ponownie_poziom_rect = poziom_8_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_8_powrot_do_menu = pygame.image.load('powrót.png')
poziom_8_powrot_do_menu_rect = poziom_8_powrot_do_menu.get_rect(topright=(1100,0))


poziom_9_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_9_slup_1 = pygame.image.load('plansza_1_słup_1_100px.png')
poziom_9_slup_1_rect = poziom_9_slup_1.get_rect(midbottom=(430,740))
poziom_9_slup_2 = pygame.image.load('plansza_1_słup_2_200px.png')
poziom_9_slup_2_rect = poziom_9_slup_2.get_rect(midbottom=(530,740))
poziom_9_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_9_sciana_1_rect = poziom_9_sciana_1.get_rect(midbottom=(650,750))
poziom_9_polka_1 = pygame.image.load('plansza_1_półka_1_250px.png')
poziom_9_polka_1_rect = poziom_9_polka_1.get_rect(midleft=(50,500))
poziom_9_wyrwa_wejscie = pygame.image.load('plansza_1_wyrwa_wejście_1.png')
poziom_9_wyrwa_wyjscie = pygame.image.load('plansza_1_wyrwa_wyjście_1.png')
poziom_9_wyrwa_wejscie_rect = poziom_9_wyrwa_wejscie.get_rect(topleft=(50,330))
poziom_9_wyrwa_wyjscie_rect = poziom_9_wyrwa_wyjscie.get_rect(topleft=(450,50))
poziom_9_polka_2 = pygame.image.load('plansza_1_półka_2_525px.png')
poziom_9_polka_2_rect = poziom_9_polka_2.get_rect(midleft=(50,230))
poziom_9_dzwignia_w_dol = pygame.image.load('dźwignia_w_dół.png')
poziom_9_dzwignia_do_gory = pygame.image.load('dźwignia_do_góry.png')
poziom_9_dzwignia_w_dol_rect = poziom_9_dzwignia_w_dol.get_rect(midleft=(50,150))
poziom_9_dzwignia_do_gory_rect = poziom_9_dzwignia_do_gory.get_rect(midleft=(50,150))

powrot_z_przegranej_poziomu_9 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_9_rect = powrot_z_przegranej_poziomu_9.get_rect(topright=(1100,0))
powtorka_poziomu_9 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_9_rect = powtorka_poziomu_9.get_rect(center=(550,375))

pauza_poziomu_9 = pygame.image.load('pauza.png')
pauza_poziomu_9_rect = pauza_poziomu_9.get_rect(center=(550,375))
pauza_poziomu_9_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_9_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_9_powrot_rect = pauza_poziomu_9_powrot.get_rect(center=(550,275))
pauza_poziomu_9_wyjdz_rect = pauza_poziomu_9_wyjdz.get_rect(center=(550,400))

poziom_9_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_9_nastepny_poziom_rect = poziom_9_nastepny_poziom.get_rect(topleft=(575,375))
poziom_9_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_9_zagraj_ponownie_poziom_rect = poziom_9_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_9_powrot_do_menu = pygame.image.load('powrót.png')
poziom_9_powrot_do_menu_rect = poziom_9_powrot_do_menu.get_rect(topright=(1100,0))


poziom_10_tlo = pygame.image.load('tło_ogólne_zamknięte_planszy_1.png')
poziom_10_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_10_sciana_1_rect = poziom_10_sciana_1.get_rect(midtop=(550,0))
ruch2 = 0
poziom_10_dzwignia_w_dol_1 = pygame.image.load('dźwignia_w_dół.png')
poziom_10_dzwignia_do_gory_1 = pygame.image.load('dźwignia_do_góry.png')
poziom_10_dzwignia_w_dol_1_rect = poziom_10_dzwignia_w_dol_1.get_rect(midleft=(50,670))
poziom_10_dzwignia_do_gory_1_rect = poziom_10_dzwignia_do_gory_1.get_rect(midleft=(50,670))
poziom_10_dzwignia_w_dol_2 = pygame.image.load('dźwignia_w_dół_2.png')
poziom_10_dzwignia_do_gory_2 = pygame.image.load('dźwignia_do_góry_2.png')
poziom_10_dzwignia_w_dol_2_rect = poziom_10_dzwignia_w_dol_2.get_rect(midright=(1050,670))
poziom_10_dzwignia_do_gory_2_rect = poziom_10_dzwignia_do_gory_2.get_rect(midright=(1050,670))
ktora1 = 'gora'
ktora2 = 'gora'
poziom_10_swiatlo_lewe = pygame.image.load('światło_wył.png')
poziom_10_swiatlo_prawe = pygame.image.load('światło_wył.png')
poziom_10_medalion = pygame.image.load('medalion_wejścia.png')
poziom_10_medalion_rect = poziom_10_medalion.get_rect(midbottom=(700,710))
poziom_10_czy_wzieto_medalion = 'nie'
obraz_bossa = 'plansza_1_boss_2_prawo.png'
poziom_10_boss_1 = pygame.image.load(obraz_bossa)
poziom_10_boss_1_rect = poziom_10_boss_1.get_rect(midbottom=(-1500,740))
boss_kierunek = 1
boss_speed = 8
za_ile_koniec_bossa = 0
kupa_gruzu = pygame.image.load('kupa_gruzu.png')
kupa_gruzu_rect = kupa_gruzu.get_rect(midbottom=(-1000,-1000))

powrot_z_przegranej_poziomu_10 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_10_rect = powrot_z_przegranej_poziomu_1.get_rect(topright=(1100,0))
powtorka_poziomu_10 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_10_rect = powtorka_poziomu_10.get_rect(center=(550,375))

pauza_poziomu_10 = pygame.image.load('pauza.png')
pauza_poziomu_10_rect = pauza_poziomu_10.get_rect(center=(550,375))
pauza_poziomu_10_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_10_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_10_powrot_rect = pauza_poziomu_10_powrot.get_rect(center=(550,275))
pauza_poziomu_10_wyjdz_rect = pauza_poziomu_10_wyjdz.get_rect(center=(550,400))

poziom_10_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_10_nastepny_poziom_rect = poziom_10_nastepny_poziom.get_rect(topleft=(575,375))
poziom_10_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_10_zagraj_ponownie_poziom_rect = poziom_10_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_10_powrot_do_menu = pygame.image.load('powrót.png')
poziom_10_powrot_do_menu_rect = poziom_10_powrot_do_menu.get_rect(topright=(1100,0))


poziom_11_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_11_stalaktyt_1 = pygame.image.load('stalaktyt1.png')
poziom_11_stalaktyt_1_rect = poziom_11_stalaktyt_1.get_rect(midtop=(400,50))
poziom_11_stalaktyt_1_gravity = 0
poziom_11_polka_1 = pygame.image.load('plansza_1_półka_1_250px.png')
poziom_11_polka_1_rect = poziom_11_polka_1.get_rect(midleft=(50,400))
poziom_11_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_11_sciana_1_rect = poziom_11_sciana_1.get_rect(midtop=(800,0))
poziom_11_sciana_2 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_11_sciana_2_rect = poziom_11_sciana_2.get_rect(midtop=(500,0))
poziom_11_wybicie_1 = pygame.image.load('plansza_1_wybicie_1.png')
poziom_11_wybicie_1_rect = poziom_11_wybicie_1.get_rect(midbottom=(400,740))
poziom_11_wyrwa_wejscie = pygame.image.load('plansza_1_wyrwa_wejście_1.png')
poziom_11_wyrwa_wyjscie = pygame.image.load('plansza_1_wyrwa_wyjście_1.png')
poziom_11_wyrwa_wejscie_rect = poziom_11_wyrwa_wejscie.get_rect(topleft=(70,160))
poziom_11_wyrwa_wyjscie_rect = poziom_11_wyrwa_wyjscie.get_rect(topleft=(580,100))
poziom_11_wyrwa_wejscie_2 = pygame.image.load('plansza_1_wyrwa_wejście_2.png')
poziom_11_wyrwa_wyjscie_2 = pygame.image.load('plansza_1_wyrwa_wyjście_2.png')
poziom_11_wyrwa_wejscie_2_rect = poziom_11_wyrwa_wejscie_2.get_rect(topleft=(580,580))
poziom_11_wyrwa_wyjscie_2_rect = poziom_11_wyrwa_wyjscie_2.get_rect(topleft=(870,100))



powrot_z_przegranej_poziomu_11 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_11_rect = powrot_z_przegranej_poziomu_11.get_rect(topright=(1100,0))
powtorka_poziomu_11 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_11_rect = powtorka_poziomu_11.get_rect(center=(550,375))

pauza_poziomu_11 = pygame.image.load('pauza.png')
pauza_poziomu_11_rect = pauza_poziomu_11.get_rect(center=(550,375))
pauza_poziomu_11_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_11_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_11_powrot_rect = pauza_poziomu_11_powrot.get_rect(center=(550,275))
pauza_poziomu_11_wyjdz_rect = pauza_poziomu_11_wyjdz.get_rect(center=(550,400))

poziom_11_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_11_nastepny_poziom_rect = poziom_11_nastepny_poziom.get_rect(topleft=(575,375))
poziom_11_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_11_zagraj_ponownie_poziom_rect = poziom_11_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_11_powrot_do_menu = pygame.image.load('powrót.png')
poziom_11_powrot_do_menu_rect = poziom_11_powrot_do_menu.get_rect(topright=(1100,0))


poziom_12_tlo = pygame.image.load('tło_do_poziomu_1_planszy_1.png')

powrot_z_przegranej_poziomu_12 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_12_rect = powrot_z_przegranej_poziomu_12.get_rect(topright=(1100,0))
powtorka_poziomu_12 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_12_rect = powtorka_poziomu_12.get_rect(center=(550,375))

pauza_poziomu_12 = pygame.image.load('pauza.png')
pauza_poziomu_12_rect = pauza_poziomu_12.get_rect(center=(550,375))
pauza_poziomu_12_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_12_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_12_powrot_rect = pauza_poziomu_12_powrot.get_rect(center=(550,275))
pauza_poziomu_12_wyjdz_rect = pauza_poziomu_12_wyjdz.get_rect(center=(550,400))

poziom_12_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_12_nastepny_poziom_rect = poziom_12_nastepny_poziom.get_rect(topleft=(575,375))
poziom_12_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_12_zagraj_ponownie_poziom_rect = poziom_12_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_12_powrot_do_menu = pygame.image.load('powrót.png')
poziom_12_powrot_do_menu_rect = poziom_12_powrot_do_menu.get_rect(topright=(1100,0))


poziom_13_tlo = pygame.image.load('tło_ogólne_otwarte_planszy_1.png')
poziom_13_generator_1 = pygame.image.load('generator_2.png')
poziom_13_generator_1_rect = poziom_13_generator_1.get_rect(midbottom=(500,740))
poziom_13_guzik_generatora_1 = pygame.image.load('guzik_zakończenia_generatora.png')
poziom_13_guzik_generatora_1_rect = poziom_13_guzik_generatora_1.get_rect(center=(750,375))
poziom_13_suwak_generatora_1 = pygame.image.load('przełącznik_generatora_lewo.png')
poziom_13_suwak_generatora_1_rect = poziom_13_suwak_generatora_1.get_rect(midleft=(200,375))
poziom_13_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
poziom_13_sciana_1_rect = poziom_13_sciana_1.get_rect(midtop=(800,0))
czy_wlaczono = 'nie'
ruch_bramy = 0

powrot_z_przegranej_poziomu_13 = pygame.image.load('powrót.png')
powrot_z_przegranej_poziomu_13_rect = powrot_z_przegranej_poziomu_13.get_rect(topright=(1100,0))
powtorka_poziomu_13 = pygame.image.load('zagraj_ponownie_poziom.png')
powtorka_poziomu_13_rect = powtorka_poziomu_13.get_rect(center=(550,375))

pauza_poziomu_13 = pygame.image.load('pauza.png')
pauza_poziomu_13_rect = pauza_poziomu_13.get_rect(center=(550,375))
pauza_poziomu_13_powrot = pygame.image.load('pauza_powrót.png')
pauza_poziomu_13_wyjdz = pygame.image.load('pauza_wyjdź_do_poziomów.png')
pauza_poziomu_13_powrot_rect = pauza_poziomu_13_powrot.get_rect(center=(550,275))
pauza_poziomu_13_wyjdz_rect = pauza_poziomu_13_wyjdz.get_rect(center=(550,400))

poziom_13_nastepny_poziom = pygame.image.load('następny_poziom.png')
poziom_13_nastepny_poziom_rect = poziom_13_nastepny_poziom.get_rect(topleft=(575,375))
poziom_13_zagraj_ponownie_poziom = pygame.image.load('zagraj_ponownie_poziom.png')
poziom_13_zagraj_ponownie_poziom_rect = poziom_13_zagraj_ponownie_poziom.get_rect(topright=(525,375))
poziom_13_powrot_do_menu = pygame.image.load('powrót.png')
poziom_13_powrot_do_menu_rect = poziom_13_powrot_do_menu.get_rect(topright=(1100,0))



krysztaly_niebieskie_count = 0
krysztaly_czerwone_count = 0
krysztaly_zielonkawe_count = 0
poziom_trudnosci_krysztalow = 1
rozne_krysztaly = []
rozne_krysztaly_rect = []
rozne_krysztaly_kolory = []
ile_masz_niebieskich_krysztalow = 0
ile_masz_czerwonych_krysztalow = 0
ile_masz_zielonkawych_krysztalow = 0
ile_masz_medalionow = 0

powrot_z_wymiany_1 = pygame.image.load('powrót.png')
powrot_z_wymiany_2 = pygame.image.load('powrót.png')
powrot_z_wymiany_3 = pygame.image.load('powrót.png')
powrot_z_wymiany_4 = pygame.image.load('powrót.png')
powrot_z_wymiany_1_rect = powrot_z_wymiany_1.get_rect(topright=(1100,0))
powrot_z_wymiany_2_rect = powrot_z_wymiany_2.get_rect(topright=(1100,0))
powrot_z_wymiany_3_rect = powrot_z_wymiany_3.get_rect(topright=(1100,0))
powrot_z_wymiany_4_rect = powrot_z_wymiany_4.get_rect(topright=(1100,0))

strzalka_w_gore_wymiana_1 = pygame.image.load('dodawanie_strzałka_w_górę.png')
strzalka_w_dol_wymiana_1 = pygame.image.load('odejmowanie_strzałka_w_dół.png')
strzalka_w_gore_wymiana_2 = pygame.image.load('dodawanie_strzałka_w_górę.png')
strzalka_w_dol_wymiana_2 = pygame.image.load('odejmowanie_strzałka_w_dół.png')
strzalka_w_gore_wymiana_3 = pygame.image.load('dodawanie_strzałka_w_górę.png')
strzalka_w_dol_wymiana_3 = pygame.image.load('odejmowanie_strzałka_w_dół.png')
strzalka_w_gore_wymiana_4 = pygame.image.load('dodawanie_strzałka_w_górę.png')
strzalka_w_dol_wymiana_4 = pygame.image.load('odejmowanie_strzałka_w_dół.png')
strzalka_w_gore_wymiana_1_rect = strzalka_w_gore_wymiana_1.get_rect(topleft=(150,200))
strzalka_w_dol_wymiana_1_rect = strzalka_w_dol_wymiana_1.get_rect(bottomleft=(150,400))
strzalka_w_gore_wymiana_2_rect = strzalka_w_gore_wymiana_2.get_rect(topleft=(150,200))
strzalka_w_dol_wymiana_2_rect = strzalka_w_dol_wymiana_2.get_rect(bottomleft=(150,400))
strzalka_w_gore_wymiana_3_rect = strzalka_w_gore_wymiana_3.get_rect(topleft=(150,200))
strzalka_w_dol_wymiana_3_rect = strzalka_w_dol_wymiana_3.get_rect(bottomleft=(150,400))
strzalka_w_gore_wymiana_4_rect = strzalka_w_gore_wymiana_4.get_rect(topleft=(150,200))
strzalka_w_dol_wymiana_4_rect = strzalka_w_dol_wymiana_4.get_rect(bottomleft=(150,400))

wymiana_n_na_c_liczba_N = 5
wymiana_c_na_z_liczba_C = 5
wymiana_z_na_c_liczba_Z = 1
wymiana_c_na_n_liczba_C = 1

wymiana_GOTOWE_1 = pygame.image.load('GOTOWE.png')
wymiana_GOTOWE_2 = pygame.image.load('GOTOWE.png')
wymiana_GOTOWE_3 = pygame.image.load('GOTOWE.png')
wymiana_GOTOWE_4 = pygame.image.load('GOTOWE.png')
wymiana_GOTOWE_1_rect = wymiana_GOTOWE_1.get_rect(center=(550,550))
wymiana_GOTOWE_2_rect = wymiana_GOTOWE_2.get_rect(center=(550,550))
wymiana_GOTOWE_3_rect = wymiana_GOTOWE_3.get_rect(center=(550,550))
wymiana_GOTOWE_4_rect = wymiana_GOTOWE_4.get_rect(center=(550,550))

zdobyte_krysztaly_1_niebieski = pygame.image.load('kryształ_1_niebieski.png')
zdobyte_krysztaly_2_czerwony = pygame.image.load('kryształ_2_czerwony.png')
zdobyte_krysztaly_3_zielonkawy = pygame.image.load('kryształ_3_zielonkawy.png')
zdobyte_krysztaly_1_niebieski_rect = zdobyte_krysztaly_1_niebieski.get_rect(topleft=(100,550))
zdobyte_krysztaly_2_czerwony_rect = zdobyte_krysztaly_2_czerwony.get_rect(topleft=(400,550))
zdobyte_krysztaly_3_zielonkawy_rect = zdobyte_krysztaly_3_zielonkawy.get_rect(topleft=(700,550))

wymiana_niebieski_na_czerwony = pygame.image.load('kryształy_wymiany_wymiana_kryształów_niebieskie_na_czerwone_mode.png')
wymiana_zielonkawy_na_czerwony = pygame.image.load('kryształy_wymiany_wymiana_kryształów_zielonkawe_na_czerwone_mode.png')
wymiana_czerwony_na_zielonkawy = pygame.image.load('kryształy_wymiany_wymiana_kryształów_czerwone_na_zielonkawe_mode.png')
wymiana_czerwony_na_niebieski = pygame.image.load('kryształy_wymiany_wymiana_kryształów_czerwone_na_niebieskie_mode.png')

gra_plansza_1 = pygame.image.load('gra_plansza_1.png')

gra_zdobywanie_krysztalow = pygame.image.load('gra_plansza_1.png')
graj_krysztaly = pygame.image.load('graj_kryształy.png')
graj_krysztaly_rect = graj_krysztaly.get_rect(midtop=(550,200))
krysztal_1_niebieski_ilosc = pygame.image.load('kryształ_1_niebieski.png')
krysztal_2_czerwony_ilosc = pygame.image.load('kryształ_2_czerwony.png')
krysztal_3_zielonkawy_ilosc = pygame.image.load('kryształ_3_zielonkawy.png')
medalion_wejscia_ilosc = pygame.image.load('medalion_wejścia.png')
gra_krysztaly_zasady = pygame.image.load('gra_kryształy_zasady.png')
gra_krysztaly_zasady_rect = gra_krysztaly_zasady.get_rect(topleft=(25,150))
gra_krysztaly_wymiany = pygame.image.load('gra_kryształy_wymiany.png')
gra_krysztaly_wymiany_rect = gra_krysztaly_wymiany.get_rect(topright=(1075,150))
gra_krysztaly_zasady_tlo = pygame.image.load('gra_kryształy_zasady_tekst.png')
powrot_gra_krysztaly_zasady_tlo = pygame.image.load('powrót.png')
powrot_gra_krysztaly_zasady_tlo_rect = powrot_gra_krysztaly_zasady_tlo.get_rect(topright=(1100,0))
przegrana_koniec_gry = pygame.image.load('przegrana_koniec_gry.png')
powrot_przegrana = pygame.image.load('powrót.png')
powrot_przegrana_rect = powrot_przegrana.get_rect(topright=(1100,0))
gra_krysztaly_wymiany_tlo = pygame.image.load('gra_kryształy_wymiany_tło.png')
wymiana_krysztalu_niebieski_na_czerwony = pygame.image.load('wymiana_kryształów_niebieski_na_czerwony.png')
wymiana_krysztalu_czerwony_na_zielonkawy = pygame.image.load('wymiana_kryształów_czerwony_na_zielony.png')
wymiana_krysztalu_zielonkawy_na_czerwony = pygame.image.load('wymiana_kryształów_zielony_na_czerwony.png')
wymiana_krysztalu_czerwony_na_niebieski = pygame.image.load('wymiana_kryształów_czerwony_na_niebieski.png')
wymiana_krysztalu_niebieski_na_czerwony_rect = wymiana_krysztalu_niebieski_na_czerwony.get_rect(topleft=(125,300))
wymiana_krysztalu_czerwony_na_zielonkawy_rect = wymiana_krysztalu_czerwony_na_zielonkawy.get_rect(topleft=(575,300))
wymiana_krysztalu_zielonkawy_na_czerwony_rect = wymiana_krysztalu_zielonkawy_na_czerwony.get_rect(topleft=(125,450))
wymiana_krysztalu_czerwony_na_niebieski_rect = wymiana_krysztalu_czerwony_na_niebieski.get_rect(topleft=(575,450))
powrot_gra_krysztaly_wymiany = pygame.image.load('powrót.png')
gra_krysztaly_wymiany_informacje = pygame.image.load('gra_wymiana_informacje.png')
gra_krysztaly_wymiany_informacje_rect = gra_krysztaly_wymiany_informacje.get_rect(topleft=(0,0))
powrot_gra_krysztaly_wymiany_rect = powrot_gra_krysztaly_wymiany.get_rect(topright=(1100,0))

plansza_1_poziom_1 = pygame.image.load('poziom1.png')
plansza_1_poziom_2 = pygame.image.load('poziom2.png')
plansza_1_poziom_3 = pygame.image.load('poziom3.png')
plansza_1_poziom_4 = pygame.image.load('poziom4.png')
plansza_1_poziom_5 = pygame.image.load('poziom5.png')
plansza_1_poziom_6 = pygame.image.load('poziom6.png')
plansza_1_poziom_7 = pygame.image.load('poziom7.png')
plansza_1_poziom_8 = pygame.image.load('poziom8.png')
plansza_1_poziom_9 = pygame.image.load('poziom9.png')
plansza_1_poziom_10 = pygame.image.load('poziom10.png')
plansza_1_poziom_11 = pygame.image.load('poziom11.png')
plansza_1_poziom_12 = pygame.image.load('poziom12.png')
plansza_1_poziom_13 = pygame.image.load('poziom13.png')
plansza_1_poziom_14 = pygame.image.load('poziom14.png')
plansza_1_poziom_15 = pygame.image.load('poziom15.png')
plansza_1_poziom_16 = pygame.image.load('poziom16.png')
plansza_1_poziom_17 = pygame.image.load('poziom17.png')
plansza_1_poziom_18 = pygame.image.load('poziom18.png')
plansza_1_poziom_19 = pygame.image.load('poziom19.png')
plansza_1_poziom_20 = pygame.image.load('poziom20.png')
plansza_1_poziom_21 = pygame.image.load('poziom21.png')
plansza_1_poziom_22 = pygame.image.load('poziom22.png')
plansza_1_poziom_23 = pygame.image.load('poziom23.png')
plansza_1_poziom_24 = pygame.image.load('poziom24.png')
plansza_1_poziom_25 = pygame.image.load('poziom25.png')
plansza_1_poziom_1_rect = plansza_1_poziom_1.get_rect(topleft=(250,125))
plansza_1_poziom_2_rect = plansza_1_poziom_2.get_rect(topleft=(375,125))
plansza_1_poziom_3_rect = plansza_1_poziom_3.get_rect(topleft=(500,125))
plansza_1_poziom_4_rect = plansza_1_poziom_4.get_rect(topleft=(625,125))
plansza_1_poziom_5_rect = plansza_1_poziom_5.get_rect(topleft=(750,125))
plansza_1_poziom_6_rect = plansza_1_poziom_6.get_rect(topleft=(250,250))
plansza_1_poziom_7_rect = plansza_1_poziom_7.get_rect(topleft=(375,250))
plansza_1_poziom_8_rect = plansza_1_poziom_8.get_rect(topleft=(500,250))
plansza_1_poziom_9_rect = plansza_1_poziom_9.get_rect(topleft=(625,250))
plansza_1_poziom_10_rect = plansza_1_poziom_10.get_rect(topleft=(750,250))
plansza_1_poziom_11_rect = plansza_1_poziom_11.get_rect(topleft=(250,375))
plansza_1_poziom_12_rect = plansza_1_poziom_12.get_rect(topleft=(375,375))
plansza_1_poziom_13_rect = plansza_1_poziom_13.get_rect(topleft=(500,375))
plansza_1_poziom_14_rect = plansza_1_poziom_14.get_rect(topleft=(625,375))
plansza_1_poziom_15_rect = plansza_1_poziom_15.get_rect(topleft=(750,375))
plansza_1_poziom_16_rect = plansza_1_poziom_16.get_rect(topleft=(250,500))
plansza_1_poziom_17_rect = plansza_1_poziom_17.get_rect(topleft=(375,500))
plansza_1_poziom_18_rect = plansza_1_poziom_18.get_rect(topleft=(500,500))
plansza_1_poziom_19_rect = plansza_1_poziom_19.get_rect(topleft=(625,500))
plansza_1_poziom_20_rect = plansza_1_poziom_20.get_rect(topleft=(750,500))
plansza_1_poziom_21_rect = plansza_1_poziom_21.get_rect(topleft=(250,625))
plansza_1_poziom_22_rect = plansza_1_poziom_22.get_rect(topleft=(375,625))
plansza_1_poziom_23_rect = plansza_1_poziom_23.get_rect(topleft=(500,625))
plansza_1_poziom_24_rect = plansza_1_poziom_24.get_rect(topleft=(625,625))
plansza_1_poziom_25_rect = plansza_1_poziom_25.get_rect(topleft=(750,625))

strzalka_w_prawo_gra_krysztaly = pygame.image.load('strzałka_w_prawo.png')
strzalka_w_prawo_gra_krysztaly_rect = strzalka_w_prawo_gra_krysztaly.get_rect(midright=(1075,375))
strzalka_w_lewo_plansza_1 = pygame.image.load('strzałka_w_lewo.png')
strzalka_w_lewo_plansza_1_rect = strzalka_w_lewo_plansza_1.get_rect(midleft=(25,375))
strzalka_w_prawo_plansza_1 = pygame.image.load('strzałka_w_prawo.png')
strzalka_w_prawo_plansza_1_rect = strzalka_w_prawo_plansza_1.get_rect(midright=(1075,375))
powrot_gra_krzyszaly = pygame.image.load('powrót.png')
powrot_gra_krzyszaly_rect = powrot_gra_krzyszaly.get_rect(topright=(1095,5))
powrot_gra_plansza_1 = pygame.image.load('powrót.png')
powrot_gra_plansza_1_rect = powrot_gra_plansza_1.get_rect(topright=(1095,5))

pauza = pygame.image.load('pauza.png')
pauza_rect = pauza.get_rect(center=(550,375))
pauza_powrot_do_gry = pygame.image.load('pauza_powrót.png')
pauza_wyjdz_do_menu = pygame.image.load('pauza_wyjdź.png')
pauza_powrot_do_gry_rect = pauza_powrot_do_gry.get_rect(center=(550,275))
pauza_wyjdz_do_menu_rect = pauza_wyjdz_do_menu.get_rect(center=(550,400))

obraz_postaci = 'postać_stop.png'
albumy_albumy = pygame.image.load('albumy_albumy.png')
okno = pygame.display.set_mode((1100 , 750))
zamek = pygame.image.load('zamek.png')
postac = pygame.image.load(obraz_postaci)
menu = pygame.image.load('menu.png')
menu_gra = pygame.image.load('gra.png')
menu_gra_rect = menu_gra.get_rect(topleft=(350,200))
menu_albumy = pygame.image.load('albumy.png')
menu_albumy_rect = menu_albumy.get_rect(topleft=(350,350))
menu_exit = pygame.image.load('wyjdź.png')
menu_exit_rect = menu_exit.get_rect(topleft=(350,500))
albumy_umiejetnosci = pygame.image.load('umiejętności.png')
powrot_albumy_umiejetnosci = pygame.image.load('powrót.png')
powrot_albumy_umiejetnosci_rect = powrot_albumy_umiejetnosci.get_rect(topright=(1095,5))
powrot_albumy = pygame.image.load('powrót.png')
powrot_albumy_rect = powrot_albumy.get_rect(topleft=(5,5))
bonus_1_info = pygame.image.load('albumy_umiejętności_bonus_1.png')
bonus_2_info = pygame.image.load('albumy_umiejętności_bonus_2.png')
powrot_albumy_umiejetnosci_bonus_1_info = pygame.image.load('powrót.png')
powrot_albumy_umiejetnosci_bonus_1_info_rect = powrot_albumy_umiejetnosci.get_rect(topright=(980,45))
powrot_albumy_umiejetnosci_bonus_2_info = pygame.image.load('powrót.png')
powrot_albumy_umiejetnosci_bonus_2_info_rect = powrot_albumy_umiejetnosci.get_rect(topright=(980,45))

miejsce_1_bonusu_1 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_2_bonusu_1 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_3_bonusu_1 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_1_bonusu_2 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_2_bonusu_2 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_3_bonusu_2 = pygame.image.load('albumy_umiejętności_miejsce_Q_W_E.png')
miejsce_1_bonusu_1_rect = miejsce_1_bonusu_1.get_rect(center=(591,590))
miejsce_2_bonusu_1_rect = miejsce_2_bonusu_1.get_rect(center=(721,590))
miejsce_3_bonusu_1_rect = miejsce_3_bonusu_1.get_rect(center=(857,590))
miejsce_1_bonusu_2_rect = miejsce_1_bonusu_2.get_rect(center=(591,590))
miejsce_2_bonusu_2_rect = miejsce_2_bonusu_2.get_rect(center=(721,590))
miejsce_3_bonusu_2_rect = miejsce_3_bonusu_2.get_rect(center=(857,590))

pole1 = pygame.image.load('albumy_pole.png')
pole2 = pygame.image.load('albumy_pole.png')
pole3 = pygame.image.load('albumy_pole.png')
pole1_rect = pole1.get_rect(center=(550,200))
pole2_rect = pole2.get_rect(center=(550,400))
pole3_rect = pole3.get_rect(center=(550,600))

krysztal_1_niebieski_ilosc_rect = krysztal_1_niebieski_ilosc.get_rect(topleft=(100,500))
krysztal_2_czerwony_ilosc_rect = krysztal_2_czerwony_ilosc.get_rect(topleft=(100,625))
krysztal_3_zielonkawy_ilosc_rect = krysztal_3_zielonkawy_ilosc.get_rect(topleft=(600,500))
medalion_wejscia_ilosc_rect = medalion_wejscia_ilosc.get_rect(topleft=(600,625))

albumy_umiejetnosci_bonus_1_skok = pygame.image.load('bonus_1_skok.png')
albumy_umiejetnosci_bonus_1_skok_rect = albumy_umiejetnosci_bonus_1_skok.get_rect(topleft=(75,85))
albumy_umiejetnosci_bonus_1_i = pygame.image.load('informacje_mini.png')
albumy_umiejetnosci_bonus_1_i_rect = albumy_umiejetnosci_bonus_1_i.get_rect(topright=(187,85))
czy_posiadasz_bonus_1 = pygame.image.load('posiadasz.png')
czy_posiadasz_bonus_1_rect = czy_posiadasz_bonus_1.get_rect(bottomright=(95,197))

albumy_umiejetnosci_bonus_2_dash = pygame.image.load('bonus_2_dash.png')
albumy_umiejetnosci_bonus_2_dash_rect = albumy_umiejetnosci_bonus_2_dash.get_rect(topleft=(194,85))
albumy_umiejetnosci_bonus_2_i = pygame.image.load('informacje_mini.png')
albumy_umiejetnosci_bonus_2_i_rect = albumy_umiejetnosci_bonus_2_i.get_rect(topright=(306,85))
czy_posiadasz_bonus_2 = pygame.image.load('posiadasz.png')
czy_posiadasz_bonus_2_rect = czy_posiadasz_bonus_2.get_rect(bottomright=(216,197))

miejsce_wybranego_bonusu_1 = pygame.image.load('wybór_miejsca_bonusu.png')
miejsce_wybranego_bonusu_2 = pygame.image.load('wybór_miejsca_bonusu.png')
miejsce_wybranego_bonusu_1_rect = miejsce_wybranego_bonusu_1.get_rect(center=(721,400))
miejsce_wybranego_bonusu_2_rect = miejsce_wybranego_bonusu_1.get_rect(center=(721,400))

miejsce3_rect = miejsce1.get_rect(center=(1050,35))

miejsce2_rect = miejsce2.get_rect(center=(975,35))

miejsce1_rect = miejsce1.get_rect(center=(900,35))

postac_gravity = 0
wyspy = []
wyspy_rect = []
kierunki = []
szybkosc = []


clock = pygame.time.Clock()
pygame.display.set_caption('gra')

tekst_krysztaly_gura_75 = tekst_font_75.render('Tutaj możesz zdobyć kryształy.', False, 'Black')
tekst_krysztaly_gura_50 = tekst_font_50.render('Graj za 1 medalion.', False, 'Black')
tekst_krysztaly_gura_75_rect = tekst_krysztaly_gura_75.get_rect(midtop=(550,25))
tekst_krysztaly_gura_50_rect = tekst_krysztaly_gura_50.get_rect(midtop=(550,150))

tekst_kupowanie_bonusu = tekst_font_75.render('Kup:', False, 'Black')

tekst_ile_niebieskich_kosztuje_bonus_1 = tekst_font_50.render(f"{ile_niebieskich_kosztuje_bonus_1}", False, 'Black')
tekst_ile_niebieskich_kosztuje_bonus_2 = tekst_font_50.render(f"{ile_niebieskich_kosztuje_bonus_2}", False, 'Black')
tekst_ile_czerwonych_kosztuje_bonus_1 = tekst_font_50.render(f"{ile_czerwonych_kosztuje_bonus_1}", False, 'Black')
tekst_ile_czerwonych_kosztuje_bonus_2 = tekst_font_50.render(f"{ile_czerwonych_kosztuje_bonus_2}", False, 'Black')
tekst_ile_zielonkawych_kosztuje_bonus_1 = tekst_font_50.render(f"{ile_zielonkawych_kosztuje_bonus_1}", False, 'Black')
tekst_ile_zielonkawych_kosztuje_bonus_2 = tekst_font_50.render(f"{ile_zielonkawych_kosztuje_bonus_2}", False, 'Black')

tekst_pole1 = tekst_font_50.render('UMIEJĘTNOŚCI', False, 'Black')
tekst_pole2 = tekst_font_50.render('POSTACIE', False, 'Black')
tekst_pole3 = tekst_font_50.render('OSIĄGNIĘCIA', False, 'Black')
tekst_pole1_rect = tekst_pole1.get_rect(center=(550,200))
tekst_pole2_rect = tekst_pole2.get_rect(center=(550,400))
tekst_pole3_rect = tekst_pole3.get_rect(center=(550,600))

tekst_brak_przypisanego_miejsca_bonus_1 = tekst_font_50.render('Brak przypisanego miejsca.', False, 'Black')
tekst_brak_przypisanego_miejsca_bonus_2 = tekst_font_50.render('Brak przypisanego miejsca.', False, 'Black')
tekst_brak_przypisanego_miejsca_bonus_1_rect = tekst_brak_przypisanego_miejsca_bonus_1.get_rect(center=(721,350))
tekst_brak_przypisanego_miejsca_bonus_2_rect = tekst_brak_przypisanego_miejsca_bonus_2.get_rect(center=(721,350))

tekst_bonus_E = tekst_font_50.render('E' , False , 'Black')
tekst_bonus_E_rect = tekst_bonus_E.get_rect(center=(1050,80))
tekst_bonus_Q = tekst_font_50.render('Q' , False , 'Black')
tekst_bonus_Q_rect = tekst_bonus_Q.get_rect(center=(900,80))
tekst_bonus_W = tekst_font_50.render('W' , False , 'Black')
tekst_bonus_W_rect = tekst_bonus_W.get_rect(center=(975,80))
postac_rect = postac.get_rect(midbottom = (300,750))
zamek_rect = zamek.get_rect(topleft = (0,50))

pasek = pygame.image.load('pasek.png')

wyspa_ratunku = pygame.image.load('wyspa.png')
strona = random.randint(0,1)
if strona == 0:
    x = 0
    kierunek_ratunku = 1
elif strona == 1:
    x = 1100
    kierunek_ratunku = -1
wyspa_ratunku_speed = random.randint(2,5)
wyspa_ratunku_rect = wyspa_ratunku.get_rect(midtop=(x,650))

for i in range(8):
    if random.randint(0,1) == 0:
        x = 0
        kierunki.append(1)
    else:
        x = 1100
        kierunki.append(-1)
    y = random.randint(250,650)
    wyspa_speed = random.randint(2,5)
    szybkosc.append(wyspa_speed)
    wyspa = pygame.image.load('wyspa.png')
    wyspa_rect = wyspa.get_rect(midtop = (x,y))
    wyspy.append(wyspa)
    wyspy_rect.append(wyspa_rect)

pygame.time.set_timer(pygame.USEREVENT + 1, 300)
pygame.time.set_timer(pygame.USEREVENT + 2, 3000)
pygame.time.set_timer(pygame.USEREVENT + 0, 1832)

exit = False
speed = 6
while not exit:
    radar_generatora = pygame.image.load(obrazek_radaru)
    suwak_1 = pygame.image.load(miejsce_suwaka_1)
    suwak_2 = pygame.image.load(miejsce_suwaka_2)
    keys = pygame.key.get_pressed()
    if ile_masz_niebieskich_krysztalow >= wymiana_n_na_c_liczba_N:
        wymiana_GOTOWE_1 = pygame.image.load('GOTOWE.png')
    else:
        wymiana_GOTOWE_1 = pygame.image.load('GOTOWE_ZABLOKOWANE.png')
    if ile_masz_czerwonych_krysztalow >= wymiana_c_na_z_liczba_C:
        wymiana_GOTOWE_2 = pygame.image.load('GOTOWE.png')
    else:
        wymiana_GOTOWE_2 = pygame.image.load('GOTOWE_ZABLOKOWANE.png')
    if ile_masz_zielonkawych_krysztalow >= wymiana_z_na_c_liczba_Z:
        wymiana_GOTOWE_3 = pygame.image.load('GOTOWE.png')
    else:
        wymiana_GOTOWE_3 = pygame.image.load('GOTOWE_ZABLOKOWANE.png')
    if ile_masz_czerwonych_krysztalow >= wymiana_c_na_n_liczba_C:
        wymiana_GOTOWE_4 = pygame.image.load('GOTOWE.png')
    else:
        wymiana_GOTOWE_4 = pygame.image.load('GOTOWE_ZABLOKOWANE.png')
    if wymiana_n_na_c_liczba_N < 5:
        wymiana_n_na_c_liczba_N = 5
    if wymiana_c_na_z_liczba_C < 5:
        wymiana_c_na_z_liczba_C = 5
    if wymiana_z_na_c_liczba_Z < 1:
        wymiana_z_na_c_liczba_Z = 1
    if wymiana_c_na_n_liczba_C < 1:
        wymiana_c_na_n_liczba_C = 1
    wymiana_n_na_c_liczba_C = wymiana_n_na_c_liczba_N // 5
    wymiana_c_na_z_liczba_Z = wymiana_c_na_z_liczba_C // 5
    wymiana_z_na_c_liczba_C = wymiana_z_na_c_liczba_Z * 5
    wymiana_c_na_n_liczba_N = wymiana_c_na_n_liczba_C * 5
    tekst_wymiana_n_na_c_liczba_C = tekst_font_100.render(f"{wymiana_n_na_c_liczba_C}", False, 'Black')
    tekst_wymiana_c_na_z_liczba_Z = tekst_font_100.render(f"{wymiana_c_na_z_liczba_Z}", False, 'Black')
    tekst_wymiana_z_na_c_liczba_C = tekst_font_100.render(f"{wymiana_z_na_c_liczba_C}", False, 'Black')
    tekst_wymiana_c_na_n_liczba_N = tekst_font_100.render(f"{wymiana_c_na_n_liczba_N}", False, 'Black')
    tekst_wymiana_n_na_c_liczba_C_rect = tekst_wymiana_n_na_c_liczba_C.get_rect(topright=(825, 270))
    tekst_wymiana_c_na_z_liczba_Z_rect = tekst_wymiana_c_na_z_liczba_Z.get_rect(topright=(825, 270))
    tekst_wymiana_z_na_c_liczba_C_rect = tekst_wymiana_z_na_c_liczba_C.get_rect(topright=(825, 270))
    tekst_wymiana_c_na_n_liczba_N_rect = tekst_wymiana_c_na_n_liczba_N.get_rect(topright=(825, 270))
    tekst_wynik_niebieskie_krysztaly = tekst_font_100.render(f"{krysztaly_niebieskie_count}", False, 'Black')
    tekst_wynik_czerwone_krysztaly = tekst_font_100.render(f"{krysztaly_czerwone_count}", False, 'Black')
    tekst_wynik_zielonkawe_krysztaly = tekst_font_100.render(f"{krysztaly_zielonkawe_count}", False, 'Black')
    tekst_ile_masz_niebieskich_krysztalow = tekst_font_100.render(f"{ile_masz_niebieskich_krysztalow}", False, 'Black')
    tekst_ile_masz_czerwonych_krysztalow = tekst_font_100.render(f"{ile_masz_czerwonych_krysztalow}", False, 'Black')
    tekst_ile_masz_zielonkawych_krysztalow = tekst_font_100.render(f"{ile_masz_zielonkawych_krysztalow}", False, 'Black')
    tekst_ile_masz_medalionow = tekst_font_100.render(f"{ile_masz_medalionow}", False, 'Black')
    tekst_wymiana_n_na_c_liczba_N = tekst_font_100.render(f"{wymiana_n_na_c_liczba_N}", False, 'Black')
    tekst_wymiana_c_na_z_liczba_C = tekst_font_100.render(f"{wymiana_c_na_z_liczba_C}", False, 'Black')
    tekst_wymiana_z_na_c_liczba_Z = tekst_font_100.render(f"{wymiana_z_na_c_liczba_Z}", False, 'Black')
    tekst_wymiana_c_na_n_liczba_C = tekst_font_100.render(f"{wymiana_c_na_n_liczba_C}", False, 'Black')
    tekst_wymiana_n_na_c_liczba_N_rect = tekst_wymiana_n_na_c_liczba_N.get_rect(topleft=(275,270))
    tekst_wymiana_c_na_z_liczba_C_rect = tekst_wymiana_c_na_z_liczba_C.get_rect(topleft=(275, 270))
    tekst_wymiana_z_na_c_liczba_Z_rect = tekst_wymiana_z_na_c_liczba_Z.get_rect(topleft=(275, 270))
    tekst_wymiana_c_na_n_liczba_C_rect = tekst_wymiana_c_na_n_liczba_C.get_rect(topleft=(275, 270))
    if czy_miejsce_brak_1 == 1:
        miejsce1 = pygame.image.load('gra_bonus_brak.png')
    if czy_miejsce_brak_2 == 1:
        miejsce2 = pygame.image.load('gra_bonus_brak.png')
    if czy_miejsce_brak_3 == 1:
        miejsce3 = pygame.image.load('gra_bonus_brak.png')
    if czy_moge == 1:
        postac_x_gravity -= 2
        postac_rect.x += postac_x_gravity
        if postac_x_gravity < 1:
            czy_moge = 0
    elif czy_moge == 2:
        postac_x_gravity += 2
        postac_rect.x += postac_x_gravity
        if postac_x_gravity > -1:
            czy_moge = 0
    postac = pygame.image.load(obraz_postaci)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and mode == 'gra':
                mode = 'pauza'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_1':
                mode = 'pauza_poziomu_1'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_2':
                mode = 'pauza_poziomu_2'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_3':
                mode = 'pauza_poziomu_3'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_4':
                mode = 'pauza_poziomu_4'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_5':
                mode = 'pauza_poziomu_5'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_6':
                mode = 'pauza_poziomu_6'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_7':
                mode = 'pauza_poziomu_7'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_8':
                mode = 'pauza_poziomu_8'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_9':
                mode = 'pauza_poziomu_9'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_10':
                mode = 'pauza_poziomu_10'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_11':
                mode = 'pauza_poziomu_11'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_12':
                mode = 'pauza_poziomu_12'
            if event.key == pygame.K_ESCAPE and mode == 'plansza_1_poziom_13':
                mode = 'pauza_poziomu_13'
            if event.key == pygame.K_SPACE and mode == 'gra' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_1' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_2' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_3' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_4' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_5' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_6' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_7' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_8' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_9' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_10' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_11' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_12' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_SPACE and mode == 'plansza_1_poziom_13' and ile_masz_skoku > 0:
                postac_gravity = -12
                ile_masz_skoku -= 1
            if event.key == pygame.K_q and mode == 'gra':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_1':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_2':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_3':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_4':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_5':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_6':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_7':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_8':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_9':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_10':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_11':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_q and mode == 'plansza_1_poziom_12':
                if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'gra':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_1':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_2':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_3':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_4':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_5':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_6':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_7':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_8':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_9':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_10':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_11':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_12':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_w and mode == 'plansza_1_poziom_13':
                if wybrane_miejsce_bonusu_2 == 'miejsce_W':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_W':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'gra':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_1':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_2':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_3':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_4':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_5':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_6':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_7':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_8':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_9':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_10':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_11':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_12':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15
            if event.key == pygame.K_e and mode == 'plansza_1_poziom_13':
                if wybrane_miejsce_bonusu_2 == 'miejsce_E':
                    if keys[pygame.K_d]:
                        czy_moge = 1
                        postac_x_gravity = 25
                    elif keys[pygame.K_a]:
                        czy_moge = 2
                        postac_x_gravity = -25
                if wybrane_miejsce_bonusu_1 == 'miejsce_E':
                    if postac_gravity < 0 or postac_rect.y < 600:
                        postac_gravity = -15

        if event.type == pygame.KEYUP:
            obraz_postaci = 'postać_stop.png'

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_gra_rect.collidepoint(event.pos) and mode == 'menu':
                mode = 'plansza_1'
            if menu_albumy_rect.collidepoint(event.pos) and mode == 'menu':
                mode = 'albumy'
            if menu_exit_rect.collidepoint(event.pos) and mode == 'menu':
                exit = True
            if powrot_albumy_umiejetnosci_rect.collidepoint(event.pos) and  mode == 'albumy_umiejętności':
                mode = 'albumy'
            if pole1_rect.collidepoint(event.pos) and  mode == 'albumy':
                mode = 'albumy_umiejętności'
            if powrot_albumy_rect.collidepoint(event.pos) and mode == 'albumy':
                mode = 'menu'
            if albumy_umiejetnosci_bonus_1_i_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności':
                mode = 'albumy_umiejętności_bonus_1_info'
            if albumy_umiejetnosci_bonus_2_i_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności':
                mode = 'albumy_umiejętności_bonus_2_info'
            if powrot_albumy_umiejetnosci_bonus_1_info_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info':
                mode = 'albumy_umiejętności'
            if powrot_albumy_umiejetnosci_bonus_2_info_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info':
                mode = 'albumy_umiejętności'

            if miejsce_1_bonusu_1_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info' and not wybrane_miejsce_bonusu_2 == 'miejsce_Q' and czy_masz_bonus_1 == 'tak':
                wybrane_miejsce_bonusu_1 = 'miejsce_Q'
            if miejsce_2_bonusu_1_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info' and not wybrane_miejsce_bonusu_2 == 'miejsce_W' and czy_masz_bonus_1 == 'tak':
                wybrane_miejsce_bonusu_1 = 'miejsce_W'
            if miejsce_3_bonusu_1_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info' and not wybrane_miejsce_bonusu_2 == 'miejsce_E' and czy_masz_bonus_1 == 'tak':
                wybrane_miejsce_bonusu_1 = 'miejsce_E'
            if rect_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info':
                wybrane_miejsce_bonusu_1 = 'brak'

            if miejsce_1_bonusu_2_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info' and not wybrane_miejsce_bonusu_1 == 'miejsce_Q' and czy_masz_bonus_2 == 'tak':
                wybrane_miejsce_bonusu_2 = 'miejsce_Q'
            if miejsce_2_bonusu_2_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info' and not wybrane_miejsce_bonusu_1 == 'miejsce_W' and czy_masz_bonus_2 == 'tak':
                wybrane_miejsce_bonusu_2 = 'miejsce_W'
            if miejsce_3_bonusu_2_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info' and not wybrane_miejsce_bonusu_1 == 'miejsce_E' and czy_masz_bonus_2 == 'tak':
                wybrane_miejsce_bonusu_2 = 'miejsce_E'
            if rect_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info':
                wybrane_miejsce_bonusu_2 = 'brak'

            if pauza_powrot_do_gry_rect.collidepoint(event.pos) and mode == 'pauza':
                mode = 'gra'
            if pauza_wyjdz_do_menu_rect.collidepoint(event.pos) and mode == 'pauza':
                mode = 'menu'

            if pauza_poziomu_1_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_1':
                mode = 'plansza_1_poziom_1'
            if pauza_poziomu_1_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_1':
                mode = 'plansza_1'

            if pauza_poziomu_2_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_2':
                mode = 'plansza_1_poziom_2'
            if pauza_poziomu_2_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_2':
                mode = 'plansza_1'

            if pauza_poziomu_3_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_3':
                mode = 'plansza_1_poziom_3'
            if pauza_poziomu_3_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_3':
                mode = 'plansza_1'

            if pauza_poziomu_4_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_4':
                mode = 'plansza_1_poziom_4'
            if pauza_poziomu_4_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_4':
                mode = 'plansza_1'

            if pauza_poziomu_5_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_5':
                mode = 'plansza_1_poziom_5'
            if pauza_poziomu_5_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_5':
                mode = 'plansza_1'

            if pauza_poziomu_6_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_6':
                mode = 'plansza_1_poziom_6'
            if pauza_poziomu_6_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_6':
                mode = 'plansza_1'

            if pauza_poziomu_7_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_7':
                mode = 'plansza_1_poziom_7'
            if pauza_poziomu_7_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_7':
                mode = 'plansza_1'

            if pauza_poziomu_8_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_8':
                mode = 'plansza_1_poziom_8'
            if pauza_poziomu_8_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_8':
                mode = 'plansza_1'

            if pauza_poziomu_9_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_9':
                mode = 'plansza_1_poziom_9'
            if pauza_poziomu_9_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_9':
                mode = 'plansza_1'

            if pauza_poziomu_10_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_10':
                mode = 'plansza_1_poziom_10'
            if pauza_poziomu_10_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_10':
                mode = 'plansza_1'

            if pauza_poziomu_11_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_11':
                mode = 'plansza_1_poziom_11'
            if pauza_poziomu_11_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_11':
                mode = 'plansza_1'

            if pauza_poziomu_12_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_12':
                mode = 'plansza_1_poziom_12'
            if pauza_poziomu_12_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_12':
                mode = 'plansza_1'

            if pauza_poziomu_13_powrot_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_13':
                mode = 'plansza_1_poziom_13'
            if pauza_poziomu_13_wyjdz_rect.collidepoint(event.pos) and mode == 'pauza_poziomu_13':
                mode = 'plansza_1'

            if graj_krysztaly_rect.collidepoint(event.pos) and mode == 'plansza_kryształy' and ile_masz_medalionow > 0:
                ile_masz_medalionow -= 1
                mode = 'gra'
                postac_rect.x = 100
                postac_rect.y = 750

            if strzalka_w_prawo_gra_krysztaly_rect.collidepoint(event.pos) and mode == 'plansza_kryształy':
                mode = 'plansza_1'

            if strzalka_w_lewo_plansza_1_rect.collidepoint(event.pos) and mode == 'plansza_1':
                mode = 'plansza_kryształy'

            if powrot_gra_krzyszaly_rect.collidepoint(event.pos) and mode == 'plansza_kryształy':
                mode = 'menu'
            if powrot_gra_plansza_1_rect.collidepoint(event.pos) and mode == 'plansza_1':
                mode = 'menu'

            if gra_krysztaly_zasady_rect.collidepoint(event.pos) and mode == 'plansza_kryształy':
                mode = 'kryształy_zasady'
            if powrot_gra_krysztaly_zasady_tlo_rect.collidepoint(event.pos) and mode == 'kryształy_zasady':
                mode = 'plansza_kryształy'
            if powrot_przegrana_rect.collidepoint(event.pos) and mode == 'gra_kryształy_przegrana':
                mode = 'plansza_kryształy'
                ile_masz_niebieskich_krysztalow += krysztaly_niebieskie_count
                ile_masz_czerwonych_krysztalow += krysztaly_czerwone_count
                ile_masz_zielonkawych_krysztalow += krysztaly_zielonkawe_count
                krysztaly_niebieskie_count = 0
                krysztaly_czerwone_count = 0
                krysztaly_zielonkawe_count = 0
            if gra_krysztaly_wymiany_rect.collidepoint(event.pos) and mode == 'plansza_kryształy':
                mode = 'kryształy_wymiany'
            if powrot_gra_krysztaly_wymiany_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany':
                mode = 'plansza_kryształy'

            if wymiana_krysztalu_niebieski_na_czerwony_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany':
                mode = 'kryształy_wymiany_niebieski_na_czerwony'
            if wymiana_krysztalu_czerwony_na_zielonkawy_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany':
                mode = 'kryształy_wymiany_czerwony_na_zielonkawy'
            if wymiana_krysztalu_zielonkawy_na_czerwony_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany':
                mode = 'kryształy_wymiany_zielonkawy_na_czerwony'
            if wymiana_krysztalu_czerwony_na_niebieski_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany':
                mode = 'kryształy_wymiany_czerwony_na_niebieski'

            if powrot_z_wymiany_1_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_niebieski_na_czerwony':
                mode = 'kryształy_wymiany'
            if powrot_z_wymiany_2_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_zielonkawy':
                mode = 'kryształy_wymiany'
            if powrot_z_wymiany_3_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_zielonkawy_na_czerwony':
                mode = 'kryształy_wymiany'
            if powrot_z_wymiany_4_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_niebieski':
                mode = 'kryształy_wymiany'

            if strzalka_w_gore_wymiana_1_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_niebieski_na_czerwony':
                wymiana_n_na_c_liczba_N += 5
            if strzalka_w_dol_wymiana_1_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_niebieski_na_czerwony':
                wymiana_n_na_c_liczba_N -= 5

            if strzalka_w_gore_wymiana_2_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_zielonkawy':
                wymiana_c_na_z_liczba_C += 5
            if strzalka_w_dol_wymiana_2_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_zielonkawy':
                wymiana_c_na_z_liczba_C -= 5

            if strzalka_w_gore_wymiana_3_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_zielonkawy_na_czerwony':
                wymiana_z_na_c_liczba_Z += 1
            if strzalka_w_dol_wymiana_3_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_zielonkawy_na_czerwony':
                wymiana_z_na_c_liczba_Z -= 1

            if strzalka_w_gore_wymiana_4_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_niebieski':
                wymiana_c_na_n_liczba_C += 1
            if strzalka_w_dol_wymiana_4_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_niebieski':
                wymiana_c_na_n_liczba_C -= 1

            if wymiana_GOTOWE_1_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_niebieski_na_czerwony':
                if ile_masz_niebieskich_krysztalow >= wymiana_n_na_c_liczba_N:
                    ile_masz_niebieskich_krysztalow -= wymiana_n_na_c_liczba_N
                    ile_masz_czerwonych_krysztalow += wymiana_n_na_c_liczba_C

            if wymiana_GOTOWE_2_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_zielonkawy':
                if ile_masz_czerwonych_krysztalow >= wymiana_c_na_z_liczba_C:
                    ile_masz_czerwonych_krysztalow -= wymiana_c_na_z_liczba_C
                    ile_masz_zielonkawych_krysztalow += wymiana_c_na_z_liczba_Z

            if wymiana_GOTOWE_3_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_zielonkawy_na_czerwony':
                if ile_masz_zielonkawych_krysztalow >= wymiana_z_na_c_liczba_Z:
                    ile_masz_zielonkawych_krysztalow -= wymiana_z_na_c_liczba_Z
                    ile_masz_czerwonych_krysztalow += wymiana_z_na_c_liczba_C

            if wymiana_GOTOWE_4_rect.collidepoint(event.pos) and mode == 'kryształy_wymiany_czerwony_na_niebieski':
                if ile_masz_czerwonych_krysztalow >= wymiana_c_na_n_liczba_C:
                    ile_masz_czerwonych_krysztalow -= wymiana_c_na_n_liczba_C
                    ile_masz_niebieskich_krysztalow += wymiana_c_na_n_liczba_N



            if plansza_1_poziom_1_rect.collidepoint(event.pos) and mode == 'plansza_1' or poziom_1_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_1_wygrana' or powtorka_poziomu_1_rect.collidepoint(event.pos) and mode == 'poziom_1_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_1'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_1_stalaktyt_1_gravity = 0
                poziom_1_stalaktyt_2_gravity = 0
                poziom_1_stalaktyt_1_rect = poziom_1_stalaktyt_1.get_rect(midtop=(400, 50))
                poziom_1_stalaktyt_2_rect = poziom_1_stalaktyt_2.get_rect(midtop=(800, 50))

            if powrot_z_przegranej_poziomu_1_rect.collidepoint(event.pos) and mode == 'poziom_1_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_2_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_2 == 'gotowe' or poziom_2_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_2_wygrana' or poziom_1_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_1_wygrana' or powtorka_poziomu_2_rect.collidepoint(event.pos) and mode == 'poziom_2_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_2'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_2_stalaktyt_1_gravity = 0
                poziom_2_stalaktyt_1_rect = poziom_1_stalaktyt_1.get_rect(midtop=(500, 50))
                poziom_2_enemy_1_rect = poziom_2_enemy_1.get_rect(midbottom=(1000, 730))
                poziom_2_enemy_1_speed = 10

            if powrot_z_przegranej_poziomu_2_rect.collidepoint(event.pos) and mode == 'poziom_2_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_3_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_3 == 'gotowe' or poziom_3_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_3_wygrana' or poziom_2_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_2_wygrana' or powtorka_poziomu_3_rect.collidepoint(event.pos) and mode == 'poziom_3_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_3'
                postac_rect.x = 100
                postac_rect.y = 750

            if powrot_z_przegranej_poziomu_3_rect.collidepoint(event.pos) and mode == 'poziom_3_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_4_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_4 == 'gotowe' or poziom_4_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_4_wygrana' or poziom_3_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_3_wygrana' or powtorka_poziomu_4_rect.collidepoint(event.pos) and mode == 'poziom_4_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_4'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_4_stalaktyt_1_rect = poziom_4_stalaktyt_1.get_rect(topright=(1050, 50))
                poziom_4_stalaktyt_1_gravity = 0

            if powrot_z_przegranej_poziomu_4_rect.collidepoint(event.pos) and mode == 'poziom_4_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_5_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_5 == 'gotowe' or poziom_5_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_5_wygrana' or poziom_4_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_4_wygrana' or powtorka_poziomu_5_rect.collidepoint(event.pos) and mode == 'poziom_5_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_5'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_5_kamien_1_rect = poziom_5_kamien_1.get_rect(midbottom=(random.randint(100, 1000), -1000))
                poziom_5_kamien_1_gravity = 11
                poziom_5_kamien_2_rect = poziom_5_kamien_2.get_rect(midbottom=(random.randint(100, 1000), -1000))
                poziom_5_kamien_2_gravity = 11
                poziom_5_kamien_3_rect = poziom_5_kamien_3.get_rect(midbottom=(random.randint(100, 1000), -1000))
                poziom_5_kamien_3_gravity = 11
                poziom_5_kamien_4_rect = poziom_5_kamien_4.get_rect(midbottom=(random.randint(100, 1000), -1000))
                poziom_5_kamien_4_gravity = 11
                poziom_5_kamien_5_rect = poziom_5_kamien_5.get_rect(midbottom=(random.randint(100, 1000), -1000))
                poziom_5_kamien_5_gravity = 11
                poziom_5_boss_1_rect = poziom_5_boss_1.get_rect(midbottom=(980, 740))
                poziom_5_faza_bossa = 0
                poziom_5_czy_wzieto_medalion = 'nie'
                kierunek_bossa = 'lewo'
                ile_razy = 0
                poziom_5_boss_1 = pygame.image.load('plansza_1_boss_1_lewo.png')

            if powrot_z_przegranej_poziomu_5_rect.collidepoint(event.pos) and mode == 'poziom_5_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_6_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_6 == 'gotowe' or poziom_6_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_6_wygrana' or poziom_5_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_5_wygrana' or powtorka_poziomu_6_rect.collidepoint(event.pos) and mode == 'poziom_6_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_6'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_6_stalaktyt_1_rect = poziom_6_stalaktyt_1.get_rect(midtop=(400, 50))
                poziom_6_stalaktyt_1_gravity = 0
                poziom_6_stalaktyt_2_rect = poziom_6_stalaktyt_2.get_rect(midtop=(800, 50))
                poziom_6_stalaktyt_2_gravity = 0

            if powrot_z_przegranej_poziomu_6_rect.collidepoint(event.pos) and mode == 'poziom_6_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_7_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_7 == 'gotowe' or poziom_7_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_7_wygrana' or poziom_6_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_6_wygrana' or powtorka_poziomu_7_rect.collidepoint(event.pos) and mode == 'poziom_7_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_7'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_7_stalaktyt_1_rect = poziom_7_stalaktyt_1.get_rect(midtop=(500, 50))
                poziom_7_stalaktyt_1_gravity = 0
                poziom_7_enemy_1_rect = poziom_7_enemy_1.get_rect(midbottom=(3000, 730))
                poziom_7_enemy_1_speed = 15
                poziom_7_enemy_2_rect = poziom_7_enemy_2.get_rect(midbottom=(4000, 630))
                poziom_7_enemy_2_speed = 15
                poziom_7_enemy_3_rect = poziom_7_enemy_3.get_rect(midbottom=(5000, 730))
                poziom_7_enemy_3_speed = 15
                poziom_7_enemy_4_rect = poziom_7_enemy_4.get_rect(midbottom=(6000, 630))
                poziom_7_enemy_4_speed = 15
                poziom_7_enemy_5_rect = poziom_7_enemy_5.get_rect(midbottom=(8000, 730))
                poziom_7_enemy_5_speed = 15

            if powrot_z_przegranej_poziomu_7_rect.collidepoint(event.pos) and mode == 'poziom_7_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_8_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_8 == 'gotowe' or poziom_8_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_8_wygrana' or poziom_7_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_7_wygrana' or powtorka_poziomu_8_rect.collidepoint(event.pos) and mode == 'poziom_8_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_8'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_8_stalaktyt_1_rect = poziom_8_stalaktyt_1.get_rect(midtop=(800, 50))
                poziom_8_stalaktyt_1_gravity = 0

            if powrot_z_przegranej_poziomu_8_rect.collidepoint(event.pos) and mode == 'poziom_8_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_9_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_9 == 'gotowe' or poziom_9_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_9_wygrana' or poziom_8_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_8_wygrana' or powtorka_poziomu_9_rect.collidepoint(event.pos) and mode == 'poziom_9_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_9'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_9_sciana_1_rect = poziom_9_sciana_1.get_rect(midbottom=(650, 750))
                ktore_pokazac = 'gora'
                ruch = 0

            if powrot_z_przegranej_poziomu_9_rect.collidepoint(event.pos) and mode == 'poziom_9_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_10_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_10 == 'gotowe' or poziom_10_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_10_wygrana' or poziom_9_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_9_wygrana' or powtorka_poziomu_10_rect.collidepoint(event.pos) and mode == 'poziom_10_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_10'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_10_sciana_1_rect = poziom_10_sciana_1.get_rect(midtop=(550, 0))
                ruch2 = 0
                poziom_10_dzwignia_w_dol_1 = pygame.image.load('dźwignia_w_dół.png')
                poziom_10_dzwignia_do_gory_1 = pygame.image.load('dźwignia_do_góry.png')
                poziom_10_dzwignia_w_dol_1_rect = poziom_10_dzwignia_w_dol_1.get_rect(midleft=(50, 670))
                poziom_10_dzwignia_do_gory_1_rect = poziom_10_dzwignia_do_gory_1.get_rect(midleft=(50, 670))
                poziom_10_dzwignia_w_dol_2 = pygame.image.load('dźwignia_w_dół_2.png')
                poziom_10_dzwignia_do_gory_2 = pygame.image.load('dźwignia_do_góry_2.png')
                poziom_10_dzwignia_w_dol_2_rect = poziom_10_dzwignia_w_dol_2.get_rect(midright=(1050, 670))
                poziom_10_dzwignia_do_gory_2_rect = poziom_10_dzwignia_do_gory_2.get_rect(midright=(1050, 670))
                ktora1 = 'gora'
                ktora2 = 'gora'
                poziom_10_swiatlo_lewe = pygame.image.load('światło_wył.png')
                poziom_10_swiatlo_prawe = pygame.image.load('światło_wył.png')
                poziom_10_medalion_rect = poziom_10_medalion.get_rect(midbottom=(700, 710))
                poziom_10_czy_wzieto_medalion = 'nie'
                obraz_bossa = 'plansza_1_boss_2_prawo.png'
                poziom_10_boss_1 = pygame.image.load(obraz_bossa)
                poziom_10_boss_1_rect = poziom_10_boss_1.get_rect(midbottom=(-1500, 740))
                boss_kierunek = 1
                boss_speed = 8
                za_ile_koniec_bossa = 0
                kupa_gruzu_rect = kupa_gruzu.get_rect(midbottom=(-1000, -1000))
                martwy = 'nie'

            if powrot_z_przegranej_poziomu_10_rect.collidepoint(event.pos) and mode == 'poziom_10_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_11_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_11 == 'gotowe' or poziom_11_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_11_wygrana' or poziom_10_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_10_wygrana' or powtorka_poziomu_11_rect.collidepoint(event.pos) and mode == 'poziom_11_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_11'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_11_stalaktyt_1_gravity = 0
                poziom_11_stalaktyt_1_rect = poziom_11_stalaktyt_1.get_rect(midtop=(400, 50))
                poziom_11_polka_1_rect = poziom_11_polka_1.get_rect(midleft=(50, 400))

            if powrot_z_przegranej_poziomu_11_rect.collidepoint(event.pos) and mode == 'poziom_11_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_12_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_12 == 'gotowe' or poziom_12_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_12_wygrana' or poziom_11_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_11_wygrana' or powtorka_poziomu_12_rect.collidepoint(event.pos) and mode == 'poziom_12_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_12'
                postac_rect.x = 100
                postac_rect.y = 750
                faza_kodu = 1
                zadanie_swiatelka = 'nie'
                zadanie_radar = 'nie'
                zadanie_kod = 'nie'
                zadanie_suwak_1 = 'nie'
                zadanie_suwak_2 = 'nie'
                wykonywanie_generatora_tlo = pygame.image.load('wykonywanie_generatora_tło.png')
                guzik_konca_wykonywania = pygame.image.load('guzik_zakończenia_generatora.png')
                guzik_konca_wykonywania_rect = guzik_konca_wykonywania.get_rect(topright=(1050, 150))
                przycisk_1_generatora = pygame.image.load('przycisk_1_generatora.png')
                przycisk_1_generatora_rect = przycisk_1_generatora.get_rect(center=(350, 75))
                przycisk_2_generatora = pygame.image.load('przycisk_2_generatora.png')
                przycisk_2_generatora_rect = przycisk_2_generatora.get_rect(center=(450, 75))
                przycisk_3_generatora = pygame.image.load('przycisk_3_generatora.png')
                przycisk_3_generatora_rect = przycisk_3_generatora.get_rect(center=(550, 75))
                przycisk_4_generatora = pygame.image.load('przycisk_4_generatora.png')
                przycisk_4_generatora_rect = przycisk_4_generatora.get_rect(center=(650, 75))
                przycisk_5_generatora = pygame.image.load('przycisk_5_generatora.png')
                przycisk_5_generatora_rect = przycisk_5_generatora.get_rect(center=(750, 75))
                panel_cyferek = pygame.image.load('kod_generatora.png')
                obrazek_radaru = 'radar_generatora_1.png'
                radar_generatora = pygame.image.load(obrazek_radaru)
                radar_generatora_rect = radar_generatora.get_rect(midbottom=(690, 730))
                miejsce_suwaka_1 = 'przełącznik_generatora_lewo.png'
                miejsce_suwaka_2 = 'przełącznik_generatora_lewo.png'
                suwak_1 = pygame.image.load(miejsce_suwaka_1)
                suwak_1_rect = suwak_1.get_rect(topleft=(390, 150))
                suwak_2 = pygame.image.load(miejsce_suwaka_2)
                suwak_2_rect = suwak_2.get_rect(topleft=(390, 300))
                liczba_1 = pygame.image.load('cyfra_1.png')
                liczba_1_rect = liczba_1.get_rect(topleft=(60, 135))
                liczba_2 = pygame.image.load('cyfra_2.png')
                liczba_2_rect = liczba_2.get_rect(topleft=(158, 135))
                liczba_3 = pygame.image.load('cyfra_3.png')
                liczba_3_rect = liczba_3.get_rect(topleft=(256, 130))
                liczba_4 = pygame.image.load('cyfra_4.png')
                liczba_4_rect = liczba_4.get_rect(topleft=(60, 228))
                liczba_5 = pygame.image.load('cyfra_5.png')
                liczba_5_rect = liczba_5.get_rect(topleft=(158, 228))
                liczba_6 = pygame.image.load('cyfra_6.png')
                liczba_6_rect = liczba_6.get_rect(topleft=(256, 228))
                liczba_7 = pygame.image.load('cyfra_7.png')
                liczba_7_rect = liczba_7.get_rect(topleft=(60, 331))
                liczba_8 = pygame.image.load('cyfra_8.png')
                liczba_8_rect = liczba_8.get_rect(topleft=(158, 331))
                liczba_9 = pygame.image.load('cyfra_9.png')
                liczba_9_rect = liczba_9.get_rect(topleft=(256, 331))
                ktory_kolor_wybrac = random.randint(1, 5)
                ktory_kolor_wybrano = 'żaden'
                if ktory_kolor_wybrac == 1:
                    ktory_kolor_wyswietlac = 'przycisk_1_generatora.png'
                elif ktory_kolor_wybrac == 2:
                    ktory_kolor_wyswietlac = 'przycisk_2_generatora.png'
                elif ktory_kolor_wybrac == 3:
                    ktory_kolor_wyswietlac = 'przycisk_3_generatora.png'
                elif ktory_kolor_wybrac == 4:
                    ktory_kolor_wyswietlac = 'przycisk_4_generatora.png'
                elif ktory_kolor_wybrac == 5:
                    ktory_kolor_wyswietlac = 'przycisk_5_generatora.png'
                podpowiadajacy_kolor = pygame.image.load(ktory_kolor_wyswietlac)
                podpowiadajacy_kolor_rect = podpowiadajacy_kolor.get_rect(center=(550, 75))
                tablica_z_kodem = pygame.image.load('tablica_z_kodem.png')
                tablica_z_kodem_rect = tablica_z_kodem.get_rect(midtop=(550, 50))
                ktora_cyfre_w_kodzie_wybrac_1 = random.randint(1, 9)
                ktora_cyfre_w_kodzie_wybrac_2 = random.randint(1, 9)
                ktora_cyfre_w_kodzie_wybrac_3 = random.randint(1, 9)
                tekst_cyfra_1_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_1}", False, 'Black')
                tekst_cyfra_2_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_2}", False, 'Black')
                tekst_cyfra_3_kodu = tekst_font_100.render(f"{ktora_cyfre_w_kodzie_wybrac_3}", False, 'Black')
                tekst_cyfra_1_kodu_rect = tekst_cyfra_1_kodu.get_rect(bottomleft=(480, 300))
                tekst_cyfra_2_kodu_rect = tekst_cyfra_2_kodu.get_rect(midbottom=(550, 300))
                tekst_cyfra_3_kodu_rect = tekst_cyfra_3_kodu.get_rect(bottomright=(620, 300))
                kierunek_suwaka_1 = random.randint(1, 2)
                niebieskie_swiatlo_1 = pygame.image.load('niebieskie_światło.png')
                if kierunek_suwaka_1 == 1:
                    niebieskie_swiatlo_1_rect = niebieskie_swiatlo_1.get_rect(midleft=(50, 300))
                elif kierunek_suwaka_1 == 2:
                    niebieskie_swiatlo_1_rect = niebieskie_swiatlo_1.get_rect(midright=(1050, 300))
                kierunek_suwaka_2 = random.randint(1, 2)
                niebieskie_swiatlo_2 = pygame.image.load('niebieskie_światło.png')
                if kierunek_suwaka_2 == 1:
                    niebieskie_swiatlo_2_rect = niebieskie_swiatlo_2.get_rect(midleft=(50, 450))
                elif kierunek_suwaka_2 == 2:
                    niebieskie_swiatlo_2_rect = niebieskie_swiatlo_2.get_rect(midright=(1050, 450))
                cel_radaru = random.randint(1, 4)
                if cel_radaru == 1:
                    slupek_radarowy = pygame.image.load('słupek_ziemia.png')
                    slupek_radarowy_rect = slupek_radarowy.get_rect(midbottom=(100, 740))
                elif cel_radaru == 2:
                    slupek_radarowy = pygame.image.load('słupek_ziemia.png')
                    slupek_radarowy_rect = slupek_radarowy.get_rect(midbottom=(1000, 740))
                elif cel_radaru == 3:
                    slupek_radarowy = pygame.image.load('słupek_sufit.png')
                    slupek_radarowy_rect = slupek_radarowy.get_rect(midtop=(100, 50))
                elif cel_radaru == 4:
                    slupek_radarowy = pygame.image.load('słupek_sufit.png')
                    slupek_radarowy_rect = slupek_radarowy.get_rect(midtop=(1000, 50))
                if obrazek_radaru == 'radar_generatora_1.png':
                    if cel_radaru == 4:
                        zadanie_radar = 'wykonano'
                    elif not cel_radaru == 4:
                        zadanie_radar = 'nie'

                if miejsce_suwaka_1 == 'przełącznik_generatora_prawo.png':
                    if kierunek_suwaka_1 == 1:
                        zadanie_suwak_1 = 'nie'
                    elif kierunek_suwaka_1 == 2:
                        zadanie_suwak_1 = 'wykonano'
                elif miejsce_suwaka_1 == 'przełącznik_generatora_lewo.png':
                    if kierunek_suwaka_1 == 1:
                        zadanie_suwak_1 = 'wykonano'
                    elif kierunek_suwaka_1 == 2:
                        zadanie_suwak_1 = 'nie'
                if miejsce_suwaka_2 == 'przełącznik_generatora_prawo.png':
                    if kierunek_suwaka_2 == 1:
                        zadanie_suwak_2 = 'nie'
                    elif kierunek_suwaka_2 == 2:
                        zadanie_suwak_2 = 'wykonano'
                elif miejsce_suwaka_2 == 'przełącznik_generatora_lewo.png':
                    if kierunek_suwaka_2 == 1:
                        zadanie_suwak_2 = 'wykonano'
                    elif kierunek_suwaka_2 == 2:
                        zadanie_suwak_2 = 'nie'

            if powrot_z_przegranej_poziomu_12_rect.collidepoint(event.pos) and mode == 'poziom_12_przegrana':
                mode = 'plansza_1'


            if plansza_1_poziom_13_rect.collidepoint(event.pos) and mode == 'plansza_1' and status_poziomu_13 == 'gotowe' or poziom_13_zagraj_ponownie_poziom_rect.collidepoint(event.pos) and mode == 'poziom_13_wygrana' or poziom_12_nastepny_poziom_rect.collidepoint(event.pos) and mode == 'poziom_12_wygrana' or powtorka_poziomu_13_rect.collidepoint(event.pos) and mode == 'poziom_13_przegrana':
                postac_gravity = 0
                mode = 'plansza_1_poziom_13'
                postac_rect.x = 100
                postac_rect.y = 750
                poziom_13_generator_1 = pygame.image.load('generator_2.png')
                poziom_13_generator_1_rect = poziom_13_generator_1.get_rect(midbottom=(500, 740))
                poziom_13_guzik_generatora_1 = pygame.image.load('guzik_zakończenia_generatora.png')
                poziom_13_guzik_generatora_1_rect = poziom_13_guzik_generatora_1.get_rect(center=(750, 375))
                poziom_13_suwak_generatora_1 = pygame.image.load('przełącznik_generatora_lewo.png')
                poziom_13_suwak_generatora_1_rect = poziom_13_suwak_generatora_1.get_rect(midleft=(200, 375))
                poziom_13_sciana_1 = pygame.image.load('plansza_1_ściana_750px.png')
                poziom_13_sciana_1_rect = poziom_13_sciana_1.get_rect(midtop=(800, 0))
                czy_wlaczono = 'nie'
                ruch_bramy = 0

            if powrot_z_przegranej_poziomu_13_rect.collidepoint(event.pos) and mode == 'poziom_13_przegrana':
                mode = 'plansza_1'


            if poziom_1_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_1_wygrana':
                mode = 'plansza_1'

            if poziom_2_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_2_wygrana':
                mode = 'plansza_1'

            if poziom_3_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_3_wygrana':
                mode = 'plansza_1'

            if poziom_4_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_4_wygrana':
                mode = 'plansza_1'

            if poziom_5_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_5_wygrana':
                mode = 'plansza_1'

            if poziom_6_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_6_wygrana':
                mode = 'plansza_1'

            if poziom_7_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_7_wygrana':
                mode = 'plansza_1'

            if poziom_8_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_8_wygrana':
                mode = 'plansza_1'

            if poziom_9_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_9_wygrana':
                mode = 'plansza_1'

            if poziom_10_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_10_wygrana':
                mode = 'plansza_1'

            if poziom_11_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_11_wygrana':
                mode = 'plansza_1'

            if poziom_12_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_12_wygrana':
                mode = 'plansza_1'

            if poziom_13_powrot_do_menu_rect.collidepoint(event.pos) and mode ==  'poziom_13_wygrana':
                mode = 'plansza_1'

            if kupowanie_bonusu_1_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_1_info' and czy_masz_bonus_1 == 'nie':
                if ile_masz_niebieskich_krysztalow >= ile_niebieskich_kosztuje_bonus_1:
                    if ile_masz_czerwonych_krysztalow >= ile_czerwonych_kosztuje_bonus_1:
                        if ile_masz_zielonkawych_krysztalow >= ile_zielonkawych_kosztuje_bonus_1:
                            ile_masz_niebieskich_krysztalow -= ile_niebieskich_kosztuje_bonus_1
                            ile_masz_czerwonych_krysztalow -= ile_czerwonych_kosztuje_bonus_1
                            ile_masz_zielonkawych_krysztalow -= ile_zielonkawych_kosztuje_bonus_1
                            czy_masz_bonus_1 = 'tak'

            if kupowanie_bonusu_2_rect.collidepoint(event.pos) and mode == 'albumy_umiejętności_bonus_2_info' and czy_masz_bonus_2 == 'nie':
                if ile_masz_niebieskich_krysztalow >= ile_niebieskich_kosztuje_bonus_2:
                    if ile_masz_czerwonych_krysztalow >= ile_czerwonych_kosztuje_bonus_2:
                        if ile_masz_zielonkawych_krysztalow >= ile_zielonkawych_kosztuje_bonus_2:
                            ile_masz_niebieskich_krysztalow -= ile_niebieskich_kosztuje_bonus_2
                            ile_masz_czerwonych_krysztalow -= ile_czerwonych_kosztuje_bonus_2
                            ile_masz_zielonkawych_krysztalow -= ile_zielonkawych_kosztuje_bonus_2
                            czy_masz_bonus_2 = 'tak'

            if mode == 'wykonywanie_generatora':
                if przycisk_1_generatora_rect.collidepoint(event.pos) and ktory_kolor_wyswietlac == 'przycisk_1_generatora.png':
                    zadanie_swiatelka = 'wykonano'
                elif przycisk_1_generatora_rect.collidepoint(event.pos) and not ktory_kolor_wyswietlac == 'przycisk_1_generatora.png':
                    zadanie_swiatelka = 'nie'
                if przycisk_2_generatora_rect.collidepoint(event.pos) and ktory_kolor_wyswietlac == 'przycisk_2_generatora.png':
                    zadanie_swiatelka = 'wykonano'
                elif przycisk_2_generatora_rect.collidepoint(event.pos) and not ktory_kolor_wyswietlac == 'przycisk_2_generatora.png':
                    zadanie_swiatelka = 'nie'
                if przycisk_3_generatora_rect.collidepoint(event.pos) and ktory_kolor_wyswietlac == 'przycisk_3_generatora.png':
                    zadanie_swiatelka = 'wykonano'
                elif przycisk_3_generatora_rect.collidepoint(event.pos) and not ktory_kolor_wyswietlac == 'przycisk_3_generatora.png':
                    zadanie_swiatelka = 'nie'
                if przycisk_4_generatora_rect.collidepoint(event.pos) and ktory_kolor_wyswietlac == 'przycisk_4_generatora.png':
                    zadanie_swiatelka = 'wykonano'
                elif przycisk_4_generatora_rect.collidepoint(event.pos) and not ktory_kolor_wyswietlac == 'przycisk_4_generatora.png':
                    zadanie_swiatelka = 'nie'
                if przycisk_5_generatora_rect.collidepoint(event.pos) and ktory_kolor_wyswietlac == 'przycisk_5_generatora.png':
                    zadanie_swiatelka = 'wykonano'
                elif przycisk_5_generatora_rect.collidepoint(event.pos) and not ktory_kolor_wyswietlac == 'przycisk_5_generatora.png':
                    zadanie_swiatelka = 'nie'

                if suwak_1_rect.collidepoint(event.pos):
                    if miejsce_suwaka_1 == 'przełącznik_generatora_lewo.png':
                        miejsce_suwaka_1 = 'przełącznik_generatora_prawo.png'
                        if kierunek_suwaka_1 == 1:
                            zadanie_suwak_1 = 'nie'
                        elif kierunek_suwaka_1 == 2:
                            zadanie_suwak_1 = 'wykonano'
                    elif miejsce_suwaka_1 == 'przełącznik_generatora_prawo.png':
                        miejsce_suwaka_1 = 'przełącznik_generatora_lewo.png'
                        if kierunek_suwaka_1 == 1:
                            zadanie_suwak_1 = 'wykonano'
                        elif kierunek_suwaka_1 == 2:
                            zadanie_suwak_1 = 'nie'
                if suwak_2_rect.collidepoint(event.pos):
                    if miejsce_suwaka_2 == 'przełącznik_generatora_lewo.png':
                        miejsce_suwaka_2 = 'przełącznik_generatora_prawo.png'
                        if kierunek_suwaka_2 == 1:
                            zadanie_suwak_2 = 'nie'
                        elif kierunek_suwaka_2 == 2:
                            zadanie_suwak_2 = 'wykonano'
                    elif miejsce_suwaka_2 == 'przełącznik_generatora_prawo.png':
                        miejsce_suwaka_2 = 'przełącznik_generatora_lewo.png'
                        if kierunek_suwaka_2 == 1:
                            zadanie_suwak_2 = 'wykonano'
                        elif kierunek_suwaka_2 == 2:
                            zadanie_suwak_2 = 'nie'

                if faza_kodu == 1:
                    if liczba_1_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 1:
                        faza_kodu = 2
                    elif liczba_1_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 1:
                        mode = 'poziom_12_przegrana'
                    elif liczba_2_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 2:
                        faza_kodu = 2
                    elif liczba_2_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 2:
                        mode = 'poziom_12_przegrana'
                    elif liczba_3_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 3:
                        faza_kodu = 2
                    elif liczba_3_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 3:
                        mode = 'poziom_12_przegrana'
                    elif liczba_4_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 4:
                        faza_kodu = 2
                    elif liczba_4_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 4:
                        mode = 'poziom_12_przegrana'
                    elif liczba_5_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 5:
                        faza_kodu = 2
                    elif liczba_5_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 5:
                        mode = 'poziom_12_przegrana'
                    elif liczba_6_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 6:
                        faza_kodu = 2
                    elif liczba_6_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 6:
                        mode = 'poziom_12_przegrana'
                    elif liczba_7_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 7:
                        faza_kodu = 2
                    elif liczba_7_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 7:
                        mode = 'poziom_12_przegrana'
                    elif liczba_8_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 8:
                        faza_kodu = 2
                    elif liczba_8_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 8:
                        mode = 'poziom_12_przegrana'
                    elif liczba_9_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_1 == 9:
                        faza_kodu = 2
                    elif liczba_9_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_1 == 9:
                        mode = 'poziom_12_przegrana'
                elif faza_kodu == 2:
                    if liczba_1_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 1:
                        faza_kodu = 3
                    elif liczba_1_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 1:
                        mode = 'poziom_12_przegrana'
                    elif liczba_2_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 2:
                        faza_kodu = 3
                    elif liczba_2_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 2:
                        mode = 'poziom_12_przegrana'
                    elif liczba_3_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 3:
                        faza_kodu = 3
                    elif liczba_3_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 3:
                        mode = 'poziom_12_przegrana'
                    elif liczba_4_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 4:
                        faza_kodu = 3
                    elif liczba_4_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 4:
                        mode = 'poziom_12_przegrana'
                    elif liczba_5_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 5:
                        faza_kodu = 3
                    elif liczba_5_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 5:
                        mode = 'poziom_12_przegrana'
                    elif liczba_6_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 6:
                        faza_kodu = 3
                    elif liczba_6_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 6:
                        mode = 'poziom_12_przegrana'
                    elif liczba_7_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 7:
                        faza_kodu = 3
                    elif liczba_7_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 7:
                        mode = 'poziom_12_przegrana'
                    elif liczba_8_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 8:
                        faza_kodu = 3
                    elif liczba_8_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 8:
                        mode = 'poziom_12_przegrana'
                    elif liczba_9_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_2 == 9:
                        faza_kodu = 3
                    elif liczba_9_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_2 == 9:
                        mode = 'poziom_12_przegrana'
                elif faza_kodu == 3:
                    if liczba_1_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 1:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_1_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 1:
                        mode = 'poziom_12_przegrana'
                    elif liczba_2_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 2:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_2_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 2:
                        mode = 'poziom_12_przegrana'
                    elif liczba_3_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 3:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_3_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 3:
                        mode = 'poziom_12_przegrana'
                    elif liczba_4_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 4:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_4_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 4:
                        mode = 'poziom_12_przegrana'
                    elif liczba_5_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 5:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_5_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 5:
                        mode = 'poziom_12_przegrana'
                    elif liczba_6_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 6:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_6_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 6:
                        mode = 'poziom_12_przegrana'
                    elif liczba_7_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 7:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_7_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 7:
                        mode = 'poziom_12_przegrana'
                    elif liczba_8_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 8:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_8_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 8:
                        mode = 'poziom_12_przegrana'
                    elif liczba_9_rect.collidepoint(event.pos) and ktora_cyfre_w_kodzie_wybrac_3 == 9:
                        zadanie_kod = 'wykonano'
                        ktora_cyfre_w_kodzie_wybrac_3 = 0
                    elif liczba_9_rect.collidepoint(event.pos) and not ktora_cyfre_w_kodzie_wybrac_3 == 9:
                        mode = 'poziom_12_przegrana'

                if radar_generatora_rect.collidepoint(event.pos):
                    if obrazek_radaru == 'radar_generatora_1.png':
                        obrazek_radaru = 'radar_generatora_2.png'
                        if cel_radaru ==  3:
                            zadanie_radar = 'wykonano'
                        elif not cel_radaru ==  3:
                            zadanie_radar = 'nie'
                    elif obrazek_radaru == 'radar_generatora_2.png':
                        obrazek_radaru = 'radar_generatora_3.png'
                        if cel_radaru ==  1:
                            zadanie_radar = 'wykonano'
                        elif not cel_radaru ==  1:
                            zadanie_radar = 'nie'
                    elif obrazek_radaru == 'radar_generatora_3.png':
                        obrazek_radaru = 'radar_generatora_4.png'
                        if cel_radaru ==  2:
                            zadanie_radar = 'wykonano'
                        elif not cel_radaru ==  2:
                            zadanie_radar = 'nie'
                    elif obrazek_radaru == 'radar_generatora_4.png':
                        obrazek_radaru = 'radar_generatora_1.png'
                        if cel_radaru ==  4:
                            zadanie_radar = 'wykonano'
                        elif not cel_radaru ==  4:
                            zadanie_radar = 'nie'

                if guzik_konca_wykonywania_rect.collidepoint(event.pos):
                    if mode == 'wykonywanie_generatora':
                        if zadanie_radar == 'wykonano' and zadanie_suwak_1 == 'wykonano' and zadanie_suwak_2 == 'wykonano' and zadanie_kod == 'wykonano' and zadanie_swiatelka == 'wykonano':
                            mode = 'poziom_12_wygrana'
                            status_poziomu_13 = 'gotowe'
                        else:
                            mode = 'poziom_12_przegrana'

            if mode == 'włącz_generator_1':
                if poziom_13_suwak_generatora_1_rect.collidepoint(event.pos):
                    poziom_13_suwak_generatora_1 = pygame.image.load('przełącznik_generatora_prawo.png')
                    czy_wlaczono = 'tak'
                if poziom_13_guzik_generatora_1_rect.collidepoint(event.pos) and czy_wlaczono == 'tak':
                    mode = 'plansza_1_poziom_13'
                    ruch_bramy = 3

        if event.type == pygame.USEREVENT + 1:
            keys = pygame.key.get_pressed()
            if mode == 'gra' or mode == 'plansza_1_poziom_1' or mode == 'plansza_1_poziom_2' or mode == 'plansza_1_poziom_3' or mode == 'plansza_1_poziom_4' or mode == 'plansza_1_poziom_5' or mode == 'plansza_1_poziom_6' or mode == 'plansza_1_poziom_7' or mode == 'plansza_1_poziom_8' or mode == 'plansza_1_poziom_9' or mode == 'plansza_1_poziom_10' or mode == 'plansza_1_poziom_11' or mode == 'plansza_1_poziom_12' or mode == 'plansza_1_poziom_13':
                if keys[pygame.K_d]:
                    pygame.time.set_timer(pygame.USEREVENT, 300)
                    if obraz_postaci == 'postać_ruch_prawo_4.png' or obraz_postaci == 'postać_stop.png':
                        obraz_postaci = 'postać_ruch_prawo_1.png'
                    elif obraz_postaci == 'postać_ruch_prawo_1.png':
                        obraz_postaci = 'postać_ruch_prawo_2.png'
                    elif obraz_postaci == 'postać_ruch_prawo_2.png':
                        obraz_postaci = 'postać_ruch_prawo_3.png'
                    elif obraz_postaci == 'postać_ruch_prawo_3.png':
                        obraz_postaci = 'postać_ruch_prawo_4.png'
                if keys[pygame.K_a]:
                    pygame.time.set_timer(pygame.USEREVENT, 300)
                    if obraz_postaci == 'postać_ruch_lewo_1.png' or obraz_postaci == 'postać_stop.png':
                        obraz_postaci = 'postać_ruch_lewo_4.png'
                    elif obraz_postaci == 'postać_ruch_lewo_4.png':
                        obraz_postaci = 'postać_ruch_lewo_3.png'
                    elif obraz_postaci == 'postać_ruch_lewo_3.png':
                        obraz_postaci = 'postać_ruch_lewo_2.png'
                    elif obraz_postaci == 'postać_ruch_lewo_2.png':
                        obraz_postaci = 'postać_ruch_lewo_1.png'

        if event.type == USEREVENT + 2 and mode == 'gra':
            if czy_na_czas == 'tak':
                for i in range(len(rozne_krysztaly)):
                    rozne_krysztaly.remove(krysztal)
                    rozne_krysztaly_rect.remove(krysztal_rect)
                    rozne_krysztaly_kolory.remove(krysztal_kolor)
                for i in range(poziom_trudnosci_krysztalow):
                    rodzaj_krysztalu = random.randint(1,11)
                    if rodzaj_krysztalu >= 2 and rodzaj_krysztalu <= 3:
                        krysztal = pygame.image.load('kryształ_3_zielonkawy.png')
                        x = random.randint(50,1050)
                        y = random.randint(150, 700)
                        krysztal_rect = krysztal.get_rect(center=(x,y))
                        krysztal_kolor = 'zielonkawy'
                        rozne_krysztaly.append(krysztal)
                        rozne_krysztaly_rect.append(krysztal_rect)
                        rozne_krysztaly_kolory.append(krysztal_kolor)
                    elif rodzaj_krysztalu >= 3 and rodzaj_krysztalu <= 6:
                        krysztal = pygame.image.load('kryształ_2_czerwony.png')
                        x = random.randint(50,1050)
                        y = random.randint(150, 700)
                        krysztal_rect = krysztal.get_rect(center=(x,y))
                        krysztal_kolor = 'czerwony'
                        rozne_krysztaly.append(krysztal)
                        rozne_krysztaly_rect.append(krysztal_rect)
                        rozne_krysztaly_kolory.append(krysztal_kolor)
                    elif rodzaj_krysztalu >= 7 and rodzaj_krysztalu <= 11:
                        krysztal = pygame.image.load('kryształ_1_niebieski.png')
                        x = random.randint(50,1050)
                        y = random.randint(150, 700)
                        krysztal_rect = krysztal.get_rect(center=(x,y))
                        krysztal_kolor = 'niebieski'
                        rozne_krysztaly.append(krysztal)
                        rozne_krysztaly_rect.append(krysztal_rect)
                        rozne_krysztaly_kolory.append(krysztal_kolor)
            elif czy_na_czas == 'nie':
                mode = 'gra_kryształy_przegrana'

        if event.type == USEREVENT + 0 and mode == 'ekran_wczytywania':
            if piksel_wczytywania_rect.x < 1099:
                mode = 'plansza_1'
            else:
                piksel_wczytywania_rect.x = 0

    if mode == 'menu':
        okno.blit(menu,dest=(0,0))
        okno.blit(menu_gra,menu_gra_rect)
        okno.blit(menu_albumy,menu_albumy_rect)
        okno.blit(menu_exit,menu_exit_rect)

    elif mode == 'pauza':
        okno.blit(pauza,pauza_rect)
        okno.blit(pauza_powrot_do_gry,pauza_powrot_do_gry_rect)
        okno.blit(pauza_wyjdz_do_menu, pauza_wyjdz_do_menu_rect)

    elif mode == 'plansza_kryształy':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(graj_krysztaly,graj_krysztaly_rect)
        okno.blit(strzalka_w_prawo_gra_krysztaly,strzalka_w_prawo_gra_krysztaly_rect)
        okno.blit(powrot_gra_krzyszaly,powrot_gra_krzyszaly_rect)
        okno.blit(tekst_krysztaly_gura_75,tekst_krysztaly_gura_75_rect)
        okno.blit(tekst_krysztaly_gura_50, tekst_krysztaly_gura_50_rect)
        okno.blit(krysztal_1_niebieski_ilosc,krysztal_1_niebieski_ilosc_rect)
        okno.blit(krysztal_2_czerwony_ilosc,krysztal_2_czerwony_ilosc_rect)
        okno.blit(krysztal_3_zielonkawy_ilosc,krysztal_3_zielonkawy_ilosc_rect)
        okno.blit(medalion_wejscia_ilosc,medalion_wejscia_ilosc_rect)
        okno.blit(gra_krysztaly_zasady,gra_krysztaly_zasady_rect)
        okno.blit(gra_krysztaly_wymiany, gra_krysztaly_wymiany_rect)

        res4 = tuple(map(sum, zip(krysztal_1_niebieski_ilosc_rect.topright, (0, 20))))
        res5 = tuple(map(sum, zip(krysztal_2_czerwony_ilosc_rect.topright, (0, 20))))
        res6 = tuple(map(sum, zip(krysztal_3_zielonkawy_ilosc_rect.topright, (0, 20))))
        res7 = tuple(map(sum, zip(medalion_wejscia_ilosc_rect.topright, (0, 20))))

        okno.blit(tekst_ile_masz_niebieskich_krysztalow,dest=res4)
        okno.blit(tekst_ile_masz_czerwonych_krysztalow,dest=res5)
        okno.blit(tekst_ile_masz_zielonkawych_krysztalow,dest=res6)
        okno.blit(tekst_ile_masz_medalionow, dest=res7)

    elif mode == 'kryształy_zasady':
        okno.blit(gra_krysztaly_zasady_tlo,dest=(0,0))
        okno.blit(powrot_gra_krysztaly_zasady_tlo,powrot_gra_krysztaly_zasady_tlo_rect)

    elif mode == 'kryształy_wymiany':
        okno.blit(gra_krysztaly_wymiany_tlo,dest=(0,0))
        okno.blit(powrot_gra_krysztaly_wymiany,powrot_gra_krysztaly_wymiany_rect)
        okno.blit(gra_krysztaly_wymiany_informacje,gra_krysztaly_wymiany_informacje_rect)
        okno.blit(wymiana_krysztalu_niebieski_na_czerwony,wymiana_krysztalu_niebieski_na_czerwony_rect)
        okno.blit(wymiana_krysztalu_czerwony_na_zielonkawy,wymiana_krysztalu_czerwony_na_zielonkawy_rect)
        okno.blit(wymiana_krysztalu_zielonkawy_na_czerwony,wymiana_krysztalu_zielonkawy_na_czerwony_rect)
        okno.blit(wymiana_krysztalu_czerwony_na_niebieski,wymiana_krysztalu_czerwony_na_niebieski_rect)

    elif mode == 'kryształy_wymiany_niebieski_na_czerwony':
        okno.blit(gra_krysztaly_wymiany_tlo, dest=(0, 0))
        okno.blit(wymiana_niebieski_na_czerwony,dest=(150,200))
        okno.blit(powrot_z_wymiany_1,powrot_z_wymiany_1_rect)
        okno.blit(strzalka_w_gore_wymiana_1,strzalka_w_gore_wymiana_1_rect)
        okno.blit(strzalka_w_dol_wymiana_1, strzalka_w_dol_wymiana_1_rect)
        okno.blit(tekst_wymiana_n_na_c_liczba_N,tekst_wymiana_n_na_c_liczba_N_rect)
        okno.blit(tekst_wymiana_n_na_c_liczba_C, tekst_wymiana_n_na_c_liczba_C_rect)
        okno.blit(wymiana_GOTOWE_1,wymiana_GOTOWE_1_rect)

    elif mode == 'kryształy_wymiany_czerwony_na_zielonkawy':
        okno.blit(gra_krysztaly_wymiany_tlo, dest=(0, 0))
        okno.blit(wymiana_czerwony_na_zielonkawy, dest=(150, 200))
        okno.blit(powrot_z_wymiany_2, powrot_z_wymiany_2_rect)
        okno.blit(strzalka_w_gore_wymiana_2, strzalka_w_gore_wymiana_2_rect)
        okno.blit(strzalka_w_dol_wymiana_2, strzalka_w_dol_wymiana_2_rect)
        okno.blit(tekst_wymiana_c_na_z_liczba_C, tekst_wymiana_c_na_z_liczba_C_rect)
        okno.blit(tekst_wymiana_c_na_z_liczba_Z, tekst_wymiana_c_na_z_liczba_Z_rect)
        okno.blit(wymiana_GOTOWE_2, wymiana_GOTOWE_2_rect)

    elif mode == 'kryształy_wymiany_zielonkawy_na_czerwony':
        okno.blit(gra_krysztaly_wymiany_tlo, dest=(0, 0))
        okno.blit(wymiana_zielonkawy_na_czerwony, dest=(150, 200))
        okno.blit(powrot_z_wymiany_3, powrot_z_wymiany_3_rect)
        okno.blit(strzalka_w_gore_wymiana_3, strzalka_w_gore_wymiana_3_rect)
        okno.blit(strzalka_w_dol_wymiana_3, strzalka_w_dol_wymiana_3_rect)
        okno.blit(tekst_wymiana_z_na_c_liczba_Z, tekst_wymiana_z_na_c_liczba_Z_rect)
        okno.blit(tekst_wymiana_z_na_c_liczba_C, tekst_wymiana_z_na_c_liczba_C_rect)
        okno.blit(wymiana_GOTOWE_3, wymiana_GOTOWE_3_rect)

    elif mode == 'kryształy_wymiany_czerwony_na_niebieski':
        okno.blit(gra_krysztaly_wymiany_tlo, dest=(0, 0))
        okno.blit(wymiana_czerwony_na_niebieski, dest=(150, 200))
        okno.blit(powrot_z_wymiany_4, powrot_z_wymiany_4_rect)
        okno.blit(strzalka_w_gore_wymiana_4, strzalka_w_gore_wymiana_4_rect)
        okno.blit(strzalka_w_dol_wymiana_4, strzalka_w_dol_wymiana_4_rect)
        okno.blit(tekst_wymiana_c_na_n_liczba_N, tekst_wymiana_c_na_n_liczba_N_rect)
        okno.blit(tekst_wymiana_c_na_n_liczba_C, tekst_wymiana_c_na_n_liczba_C_rect)
        okno.blit(wymiana_GOTOWE_4, wymiana_GOTOWE_4_rect)

    elif mode == 'gra_kryształy_przegrana':
        okno.blit(przegrana_koniec_gry,dest=(0,0))
        okno.blit(powrot_przegrana,powrot_przegrana_rect)
        okno.blit(zdobyte_krysztaly_1_niebieski,zdobyte_krysztaly_1_niebieski_rect)
        okno.blit(zdobyte_krysztaly_2_czerwony,zdobyte_krysztaly_2_czerwony_rect)
        okno.blit(zdobyte_krysztaly_3_zielonkawy,zdobyte_krysztaly_3_zielonkawy_rect)

        res1 = tuple(map(sum, zip(zdobyte_krysztaly_1_niebieski_rect.topright, (0,20))))
        res2 = tuple(map(sum, zip(zdobyte_krysztaly_2_czerwony_rect.topright, (0, 20))))
        res3 = tuple(map(sum, zip(zdobyte_krysztaly_3_zielonkawy_rect.topright, (0, 20))))

        okno.blit(tekst_wynik_niebieskie_krysztaly,dest=res1)
        okno.blit(tekst_wynik_czerwone_krysztaly, dest=res2)
        okno.blit(tekst_wynik_zielonkawe_krysztaly, dest=res3)

    elif mode == 'plansza_1':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(strzalka_w_lewo_plansza_1,strzalka_w_lewo_plansza_1_rect)
        okno.blit(strzalka_w_prawo_plansza_1, strzalka_w_prawo_plansza_1_rect)
        okno.blit(powrot_gra_plansza_1, powrot_gra_plansza_1_rect)
        okno.blit(plansza_1_poziom_1, plansza_1_poziom_1_rect)
        okno.blit(plansza_1_poziom_2, plansza_1_poziom_2_rect)
        okno.blit(plansza_1_poziom_3, plansza_1_poziom_3_rect)
        okno.blit(plansza_1_poziom_4, plansza_1_poziom_4_rect)
        okno.blit(plansza_1_poziom_5, plansza_1_poziom_5_rect)
        okno.blit(plansza_1_poziom_6, plansza_1_poziom_6_rect)
        okno.blit(plansza_1_poziom_7, plansza_1_poziom_7_rect)
        okno.blit(plansza_1_poziom_8, plansza_1_poziom_8_rect)
        okno.blit(plansza_1_poziom_9, plansza_1_poziom_9_rect)
        okno.blit(plansza_1_poziom_10, plansza_1_poziom_10_rect)
        okno.blit(plansza_1_poziom_11, plansza_1_poziom_11_rect)
        okno.blit(plansza_1_poziom_12, plansza_1_poziom_12_rect)
        okno.blit(plansza_1_poziom_13, plansza_1_poziom_13_rect)
        okno.blit(plansza_1_poziom_14, plansza_1_poziom_14_rect)
        okno.blit(plansza_1_poziom_15, plansza_1_poziom_15_rect)
        okno.blit(plansza_1_poziom_16, plansza_1_poziom_16_rect)
        okno.blit(plansza_1_poziom_17, plansza_1_poziom_17_rect)
        okno.blit(plansza_1_poziom_18, plansza_1_poziom_18_rect)
        okno.blit(plansza_1_poziom_19, plansza_1_poziom_19_rect)
        okno.blit(plansza_1_poziom_20, plansza_1_poziom_20_rect)
        okno.blit(plansza_1_poziom_21, plansza_1_poziom_21_rect)
        okno.blit(plansza_1_poziom_22, plansza_1_poziom_22_rect)
        okno.blit(plansza_1_poziom_23, plansza_1_poziom_23_rect)
        okno.blit(plansza_1_poziom_24, plansza_1_poziom_24_rect)
        okno.blit(plansza_1_poziom_25, plansza_1_poziom_25_rect)
        if status_poziomu_2 == 'blokada':
            okno.blit(klodka_poziomu_2,dest=plansza_1_poziom_2_rect.topleft)
        if status_poziomu_3 == 'blokada':
            okno.blit(klodka_poziomu_3,dest=plansza_1_poziom_3_rect.topleft)
        if status_poziomu_4 == 'blokada':
            okno.blit(klodka_poziomu_4,dest=plansza_1_poziom_4_rect.topleft)
        if status_poziomu_5 == 'blokada':
            okno.blit(klodka_poziomu_5,dest=plansza_1_poziom_5_rect.topleft)
        if status_poziomu_6 == 'blokada':
            okno.blit(klodka_poziomu_6,dest=plansza_1_poziom_6_rect.topleft)
        if status_poziomu_7 == 'blokada':
            okno.blit(klodka_poziomu_7,dest=plansza_1_poziom_7_rect.topleft)
        if status_poziomu_8 == 'blokada':
            okno.blit(klodka_poziomu_8,dest=plansza_1_poziom_8_rect.topleft)
        if status_poziomu_9 == 'blokada':
            okno.blit(klodka_poziomu_9,dest=plansza_1_poziom_9_rect.topleft)
        if status_poziomu_10 == 'blokada':
            okno.blit(klodka_poziomu_10,dest=plansza_1_poziom_10_rect.topleft)
        if status_poziomu_11 == 'blokada':
            okno.blit(klodka_poziomu_11,dest=plansza_1_poziom_11_rect.topleft)
        if status_poziomu_12 == 'blokada':
            okno.blit(klodka_poziomu_12,dest=plansza_1_poziom_12_rect.topleft)
        if status_poziomu_13 == 'blokada':
            okno.blit(klodka_poziomu_13,dest=plansza_1_poziom_13_rect.topleft)
        if status_poziomu_14 == 'blokada':
            okno.blit(klodka_poziomu_14,dest=plansza_1_poziom_14_rect.topleft)
        if status_poziomu_15 == 'blokada':
            okno.blit(klodka_poziomu_15,dest=plansza_1_poziom_15_rect.topleft)
        if status_poziomu_16 == 'blokada':
            okno.blit(klodka_poziomu_16,dest=plansza_1_poziom_16_rect.topleft)
        if status_poziomu_17 == 'blokada':
            okno.blit(klodka_poziomu_17,dest=plansza_1_poziom_17_rect.topleft)
        if status_poziomu_18 == 'blokada':
            okno.blit(klodka_poziomu_18,dest=plansza_1_poziom_18_rect.topleft)
        if status_poziomu_19 == 'blokada':
            okno.blit(klodka_poziomu_19,dest=plansza_1_poziom_19_rect.topleft)
        if status_poziomu_20 == 'blokada':
            okno.blit(klodka_poziomu_20,dest=plansza_1_poziom_20_rect.topleft)
        if status_poziomu_21 == 'blokada':
            okno.blit(klodka_poziomu_21,dest=plansza_1_poziom_21_rect.topleft)
        if status_poziomu_22 == 'blokada':
            okno.blit(klodka_poziomu_22,dest=plansza_1_poziom_22_rect.topleft)
        if status_poziomu_23 == 'blokada':
            okno.blit(klodka_poziomu_23,dest=plansza_1_poziom_23_rect.topleft)
        if status_poziomu_24 == 'blokada':
            okno.blit(klodka_poziomu_24,dest=plansza_1_poziom_24_rect.topleft)
        if status_poziomu_25 == 'blokada':
            okno.blit(klodka_poziomu_25,dest=plansza_1_poziom_25_rect.topleft)

    elif mode == 'albumy':
        okno.blit(albumy_albumy,dest=(0,0))
        okno.blit(pole1,pole1_rect)
        okno.blit(pole2, pole2_rect)
        okno.blit(pole3, pole3_rect)
        okno.blit(tekst_pole1,tekst_pole1_rect)
        okno.blit(tekst_pole2, tekst_pole2_rect)
        okno.blit(tekst_pole3, tekst_pole3_rect)
        okno.blit(powrot_albumy,powrot_albumy_rect)

    elif mode == 'albumy_umiejętności_bonus_1_info':
        okno.blit(bonus_1_info,dest=(100,25))
        okno.blit(powrot_albumy_umiejetnosci_bonus_1_info,powrot_albumy_umiejetnosci_bonus_1_info_rect)
        okno.blit(miejsce_1_bonusu_1,miejsce_1_bonusu_1_rect)
        okno.blit(miejsce_2_bonusu_1, miejsce_2_bonusu_1_rect)
        okno.blit(miejsce_3_bonusu_1, miejsce_3_bonusu_1_rect)
        okno.blit(tekst_brak_przypisanego_miejsca_bonus_1,tekst_brak_przypisanego_miejsca_bonus_1_rect)
        okno.blit(miejsce_wybranego_bonusu_1,miejsce_wybranego_bonusu_1_rect)
        okno.blit(kupowanie_bonusu_1,kupowanie_bonusu_1_rect)
        okno.blit(tekst_kupowanie_bonusu,dest=(670,165))
        okno.blit(tekst_ile_niebieskich_kosztuje_bonus_1,dest=(665,230))
        okno.blit(tekst_ile_czerwonych_kosztuje_bonus_1, dest=(760, 230))
        okno.blit(tekst_ile_zielonkawych_kosztuje_bonus_1, dest=(720, 280))
        if wybrane_miejsce_bonusu_1 == 'brak':
            miejsce_wybranego_bonusu_1_rect.center = (721,400)
        elif wybrane_miejsce_bonusu_1 == 'miejsce_Q':
            miejsce_wybranego_bonusu_1_rect.center = miejsce_1_bonusu_1_rect.center
        elif wybrane_miejsce_bonusu_1 == 'miejsce_W':
            miejsce_wybranego_bonusu_1_rect.center = miejsce_2_bonusu_1_rect.center
        elif wybrane_miejsce_bonusu_1 == 'miejsce_E':
            miejsce_wybranego_bonusu_1_rect.center = miejsce_3_bonusu_1_rect.center

    elif mode == 'albumy_umiejętności_bonus_2_info':
        okno.blit(bonus_2_info,dest=(100,25))
        okno.blit(powrot_albumy_umiejetnosci_bonus_2_info,powrot_albumy_umiejetnosci_bonus_2_info_rect)
        okno.blit(miejsce_1_bonusu_2, miejsce_1_bonusu_2_rect)
        okno.blit(miejsce_2_bonusu_2, miejsce_2_bonusu_2_rect)
        okno.blit(miejsce_3_bonusu_2, miejsce_3_bonusu_2_rect)
        okno.blit(tekst_brak_przypisanego_miejsca_bonus_2, tekst_brak_przypisanego_miejsca_bonus_2_rect)
        okno.blit(miejsce_wybranego_bonusu_2, miejsce_wybranego_bonusu_2_rect)
        okno.blit(kupowanie_bonusu_2, kupowanie_bonusu_2_rect)
        okno.blit(tekst_kupowanie_bonusu, dest=(670, 165))
        okno.blit(tekst_ile_niebieskich_kosztuje_bonus_2,dest=(665,230))
        okno.blit(tekst_ile_czerwonych_kosztuje_bonus_2, dest=(760, 230))
        okno.blit(tekst_ile_zielonkawych_kosztuje_bonus_2, dest=(720, 280))
        if wybrane_miejsce_bonusu_2 == 'brak':
            miejsce_wybranego_bonusu_2_rect.center = (721,400)
        elif wybrane_miejsce_bonusu_2 == 'miejsce_Q':
            miejsce_wybranego_bonusu_2_rect.center = miejsce_1_bonusu_2_rect.center
        elif wybrane_miejsce_bonusu_2 == 'miejsce_W':
            miejsce_wybranego_bonusu_2_rect.center = miejsce_2_bonusu_2_rect.center
        elif wybrane_miejsce_bonusu_2 == 'miejsce_E':
            miejsce_wybranego_bonusu_2_rect.center = miejsce_3_bonusu_2_rect.center

    elif mode == 'albumy_umiejętności':
        okno.blit(albumy_umiejetnosci,dest=(0,0))
        okno.blit(albumy_umiejetnosci_bonus_1_skok,albumy_umiejetnosci_bonus_1_skok_rect)
        okno.blit(albumy_umiejetnosci_bonus_1_i,albumy_umiejetnosci_bonus_1_i_rect)
        okno.blit(albumy_umiejetnosci_bonus_2_dash, albumy_umiejetnosci_bonus_2_dash_rect)
        okno.blit(albumy_umiejetnosci_bonus_2_i, albumy_umiejetnosci_bonus_2_i_rect)
        okno.blit(powrot_albumy_umiejetnosci,powrot_albumy_umiejetnosci_rect)
        okno.blit(czy_posiadasz_bonus_1,czy_posiadasz_bonus_1_rect)
        if czy_masz_bonus_1 == 'tak':
            czy_posiadasz_bonus_1 = pygame.image.load('posiadasz.png')
        elif czy_masz_bonus_1 == 'nie':
            czy_posiadasz_bonus_1 = pygame.image.load('nieposiadasz.png')
        okno.blit(czy_posiadasz_bonus_2,czy_posiadasz_bonus_2_rect)
        if czy_masz_bonus_2 == 'tak':
            czy_posiadasz_bonus_2 = pygame.image.load('posiadasz.png')
        elif czy_masz_bonus_2 == 'nie':
            czy_posiadasz_bonus_2 = pygame.image.load('nieposiadasz.png')

    elif mode == 'gra':
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 0:
            postac_rect.bottom = 0
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 0:
            postac_rect.x = 0
        if postac_rect.x >= 1000:
            postac_rect.x = 1000
        okno.blit(zamek,zamek_rect)
        okno.blit(postac,postac_rect)
        okno.blit(pasek,dest= (0,0))

        if wybrane_miejsce_bonusu_1 == 'miejsce_Q':
            miejsce1 = pygame.image.load('gra_bonus_1_skok.png')
            czy_miejsce_brak_1 = 0
        elif wybrane_miejsce_bonusu_1 == 'miejsce_W':
            miejsce2 = pygame.image.load('gra_bonus_1_skok.png')
            czy_miejsce_brak_2 = 0
        elif wybrane_miejsce_bonusu_1 == 'miejsce_E':
            miejsce3 = pygame.image.load('gra_bonus_1_skok.png')
            czy_miejsce_brak_3 = 0

        if wybrane_miejsce_bonusu_2 == 'miejsce_Q':
            miejsce1 = pygame.image.load('gra_bonus_2_dash.png')
            czy_miejsce_brak_1 = 0
        elif wybrane_miejsce_bonusu_2 == 'miejsce_W':
            miejsce2 = pygame.image.load('gra_bonus_2_dash.png')
            czy_miejsce_brak_2 = 0
        elif wybrane_miejsce_bonusu_2 == 'miejsce_E':
            miejsce3 = pygame.image.load('gra_bonus_2_dash.png')
            czy_miejsce_brak_3 = 0

        if not wybrane_miejsce_bonusu_1 == 'miejsce_Q' and not wybrane_miejsce_bonusu_2 == 'miejsce_Q':
            czy_miejsce_brak_1 = 1
        if not wybrane_miejsce_bonusu_1 == 'miejsce_W' and not wybrane_miejsce_bonusu_2 == 'miejsce_W':
            czy_miejsce_brak_2 = 1
        if not wybrane_miejsce_bonusu_1 == 'miejsce_E' and not wybrane_miejsce_bonusu_2 == 'miejsce_E':
            czy_miejsce_brak_3 = 1

        okno.blit(tekst_bonus_E,tekst_bonus_E_rect)
        okno.blit(tekst_bonus_Q, tekst_bonus_Q_rect)
        okno.blit(tekst_bonus_W,tekst_bonus_W_rect)
        okno.blit(miejsce1, miejsce1_rect)
        okno.blit(miejsce2, miejsce2_rect)
        okno.blit(miejsce3,miejsce3_rect)
        okno.blit(wyspa_ratunku,wyspa_ratunku_rect)
        if pygame.Rect.colliderect(postac_rect, wyspa_ratunku_rect):
            if postac_rect.bottom > wyspa_ratunku_rect.top and postac_rect.bottom < wyspa_ratunku_rect.top + 20:
                postac_rect.bottom = wyspa_ratunku_rect.top
                postac_gravity = 0
                ile_masz_skoku = 1
        wyspa_ratunku_rect.x += kierunek_ratunku * wyspa_ratunku_speed
        if wyspa_ratunku_rect.x < -150 or wyspa_ratunku_rect.x > 1100:
            kierunek_ratunku *= -1
            wyspa_ratunku_speed = random.randint(2, 5)

        for i in range(len(wyspy)):
            if pygame.Rect.colliderect(postac_rect,wyspy_rect[i]):
                if postac_rect.bottom > wyspy_rect[i].top and postac_rect.bottom < wyspy_rect[i].top + 20:
                    postac_rect.bottom = wyspy_rect[i].top
                    postac_gravity = 0
                    ile_masz_skoku = 1
                elif postac_rect.bottom >= 750:
                    ile_masz_skoku = 1
                elif postac_rect.colliderect(wyspa_ratunku_rect):
                    ile_masz_skoku = 1
            wyspy_rect[i].x += kierunki[i] * szybkosc[i]
            okno.blit(wyspy[i],wyspy_rect[i])
            if wyspy_rect[i].x < -150:
                wyspy_rect[i].x = -150
                wyspy_rect[i].y = random.randint(250,630)
                kierunki[i] *= -1
                szybkosc[i] = random.randint(2,5)
            elif wyspy_rect[i].x > 1100:
                wyspy_rect[i].x = 1100
                wyspy_rect[i].y = random.randint(250, 630)
                kierunki[i] *= -1
                szybkosc[i] = random.randint(2, 5)

        for i in range(len(rozne_krysztaly)):
            okno.blit(rozne_krysztaly[i],rozne_krysztaly_rect[i])
            if pygame.Rect.colliderect(postac_rect, rozne_krysztaly_rect[i]):
                czy_na_czas = 'tak'
                if rozne_krysztaly_kolory[i] == 'zielonkawy':
                    krysztaly_zielonkawe_count += 1
                if rozne_krysztaly_kolory[i] == 'czerwony':
                    krysztaly_czerwone_count += 1
                if rozne_krysztaly_kolory[i] == 'niebieski':
                    krysztaly_niebieskie_count += 1
                rozne_krysztaly.remove(krysztal)
                rozne_krysztaly_rect.remove(krysztal_rect)
                rozne_krysztaly_kolory.remove(krysztal_kolor)
            else:
                czy_na_czas = 'tak'

    elif mode == 'ekran_wczytywania':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(pasek_ruchu_wczytywania, pasek_ruchu_wczytywania_rect)
        piksel_wczytywania_rect.x += 10
        pasek_ruchu_wczytywania_rect.x += kierunek_wczytywania
        if pasek_ruchu_wczytywania_rect.x < 300:
            kierunek_wczytywania *= -1
        if pasek_ruchu_wczytywania_rect.x > 700:
            kierunek_wczytywania *= -1



    elif mode == 'plansza_1_poziom_1':
        okno.blit(poziom_1_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_1_stalaktyt_1,poziom_1_stalaktyt_1_rect)
        okno.blit(poziom_1_stalaktyt_2, poziom_1_stalaktyt_2_rect)
        poziom_1_stalaktyt_1_rect.y -= poziom_1_stalaktyt_1_gravity
        poziom_1_stalaktyt_2_rect.y -= poziom_1_stalaktyt_2_gravity
        if postac_rect.x > poziom_1_stalaktyt_1_rect.x - 150:
            poziom_1_stalaktyt_1_gravity = -25
        if postac_rect.x > poziom_1_stalaktyt_2_rect.x - 150:
            poziom_1_stalaktyt_2_gravity = -25
        if poziom_1_stalaktyt_1_rect.y > 900:
            poziom_1_stalaktyt_1_gravity = 0
        if poziom_1_stalaktyt_2_rect.y > 900:
            poziom_1_stalaktyt_2_gravity = 0
        if postac_rect.colliderect(poziom_1_stalaktyt_1_rect):
            mode = 'poziom_1_przegrana'
        if postac_rect.colliderect(poziom_1_stalaktyt_2_rect):
            mode = 'poziom_1_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_1_rect):
            mode = 'poziom_1_wygrana'
            status_poziomu_2 = 'gotowe'

    elif mode == 'poziom_1_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_1,powrot_z_przegranej_poziomu_1_rect)
        okno.blit(powtorka_poziomu_1,powtorka_poziomu_1_rect)

    elif mode == 'pauza_poziomu_1':
        okno.blit(pauza_poziomu_1,pauza_poziomu_1_rect)
        okno.blit(pauza_poziomu_1_wyjdz, pauza_poziomu_1_wyjdz_rect)
        okno.blit(pauza_poziomu_1_powrot, pauza_poziomu_1_powrot_rect)

    elif mode == 'poziom_1_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_1_zagraj_ponownie_poziom,poziom_1_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_1_nastepny_poziom, poziom_1_nastepny_poziom_rect)
        okno.blit(poziom_1_powrot_do_menu, poziom_1_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_2':
        okno.blit(poziom_2_tlo,dest=(0,0))
        postac_gravity += 0.5
        poziom_2_enemy_1_rect.x -= poziom_2_enemy_1_speed
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_2_stalaktyt_1,poziom_2_stalaktyt_1_rect)
        okno.blit(poziom_2_enemy_1,poziom_2_enemy_1_rect)
        poziom_2_stalaktyt_1_rect.y -= poziom_2_stalaktyt_1_gravity
        if postac_rect.x > poziom_2_stalaktyt_1_rect.x - 150:
            poziom_2_stalaktyt_1_gravity = -25
        if poziom_2_stalaktyt_1_rect.y > 900:
            poziom_2_stalaktyt_1_gravity = 0
        if postac_rect.colliderect(poziom_2_stalaktyt_1_rect):
            mode = 'poziom_2_przegrana'

        if poziom_2_enemy_1_rect.x < -100:
            poziom_2_enemy_1_speed = 0
        if postac_rect.colliderect(poziom_2_enemy_1_rect):
            mode = 'poziom_2_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_2_rect):
            mode = 'poziom_2_wygrana'
            status_poziomu_3 = 'gotowe'

    elif mode == 'poziom_2_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_2,powrot_z_przegranej_poziomu_2_rect)
        okno.blit(powtorka_poziomu_2, powtorka_poziomu_2_rect)

    elif mode == 'pauza_poziomu_2':
        okno.blit(pauza_poziomu_2,pauza_poziomu_2_rect)
        okno.blit(pauza_poziomu_2_wyjdz, pauza_poziomu_2_wyjdz_rect)
        okno.blit(pauza_poziomu_2_powrot, pauza_poziomu_2_powrot_rect)

    elif mode == 'poziom_2_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_2_zagraj_ponownie_poziom,poziom_2_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_2_nastepny_poziom, poziom_2_nastepny_poziom_rect)
        okno.blit(poziom_2_powrot_do_menu, poziom_2_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_3':
        okno.blit(poziom_3_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(poziom_3_slup_1,poziom_3_slup_1_rect)
        okno.blit(poziom_3_slup_2, poziom_3_slup_2_rect)
        okno.blit(poziom_3_stalaktyt_1,poziom_3_stalaktyt_1_rect)
        okno.blit(postac, postac_rect)
        if pygame.Rect.colliderect(postac_rect,poziom_3_slup_1_rect):
            if postac_rect.bottom > poziom_3_slup_1_rect.top and postac_rect.bottom < poziom_3_slup_1_rect.top + 20:
                if postac_rect.x > poziom_3_slup_1_rect.x - 60 and postac_rect.x < poziom_3_slup_1_rect.x + 5:
                    postac_rect.bottom = poziom_3_slup_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_3_slup_1_rect.top and postac_rect.bottom < poziom_3_slup_1_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_3_slup_1_rect.right - 50:
                postac_rect.left = poziom_3_slup_1_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_3_slup_1_rect.left + 50:
                postac_rect.right = poziom_3_slup_1_rect.left + 20
        elif pygame.Rect.colliderect(postac_rect,poziom_3_slup_2_rect):
            if postac_rect.bottom > poziom_3_slup_2_rect.top and postac_rect.bottom < poziom_3_slup_2_rect.top + 20:
                if postac_rect.x > poziom_3_slup_2_rect.x - 60 and postac_rect.x < poziom_3_slup_2_rect.x + 5:
                    postac_rect.bottom = poziom_3_slup_2_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_3_slup_2_rect.top and postac_rect.bottom < poziom_3_slup_2_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_3_slup_2_rect.right - 50:
                postac_rect.left = poziom_3_slup_2_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_3_slup_2_rect.left + 50:
                postac_rect.right = poziom_3_slup_2_rect.left + 20
        if postac_rect.colliderect(rect_ukonczenia_poziomu_3_rect):
            mode = 'poziom_3_wygrana'
            status_poziomu_4 = 'gotowe'

    elif mode == 'poziom_3_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_3,powrot_z_przegranej_poziomu_3_rect)
        okno.blit(powtorka_poziomu_3, powtorka_poziomu_3_rect)

    elif mode == 'pauza_poziomu_3':
        okno.blit(pauza_poziomu_3,pauza_poziomu_3_rect)
        okno.blit(pauza_poziomu_3_wyjdz, pauza_poziomu_3_wyjdz_rect)
        okno.blit(pauza_poziomu_3_powrot, pauza_poziomu_3_powrot_rect)

    elif mode == 'poziom_3_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_3_zagraj_ponownie_poziom,poziom_3_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_3_nastepny_poziom, poziom_3_nastepny_poziom_rect)
        okno.blit(poziom_3_powrot_do_menu, poziom_3_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_4':
        okno.blit(poziom_4_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(poziom_4_slup_1,poziom_4_slup_1_rect)
        okno.blit(poziom_4_slup_2, poziom_4_slup_2_rect)
        okno.blit(poziom_4_polka_1,poziom_4_polka_1_rect)
        okno.blit(poziom_4_wyrwa_wejscie,poziom_4_wyrwa_wejscie_rect)
        okno.blit(poziom_4_wyrwa_wyjscie, poziom_4_wyrwa_wyjscie_rect)
        okno.blit(poziom_4_stalaktyt_1,poziom_4_stalaktyt_1_rect)
        poziom_4_stalaktyt_1_rect.y -= poziom_4_stalaktyt_1_gravity
        okno.blit(postac, postac_rect)
        okno.blit(poziom_4_sciana_1,poziom_4_sciana_1_rect)
        if pygame.Rect.colliderect(postac_rect,poziom_4_slup_1_rect):
            if postac_rect.bottom > poziom_4_slup_1_rect.top and postac_rect.bottom < poziom_4_slup_1_rect.top + 20:
                if postac_rect.x > poziom_4_slup_1_rect.x - 60 and postac_rect.x < poziom_4_slup_1_rect.x + 5:
                    postac_rect.bottom = poziom_4_slup_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_4_slup_1_rect.top and postac_rect.bottom < poziom_4_slup_1_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_4_slup_1_rect.right - 50:
                postac_rect.left = poziom_4_slup_1_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_4_slup_1_rect.left + 50:
                postac_rect.right = poziom_4_slup_1_rect.left + 20
        if pygame.Rect.colliderect(postac_rect,poziom_4_slup_2_rect):
            if postac_rect.bottom > poziom_4_slup_2_rect.top and postac_rect.bottom < poziom_4_slup_2_rect.top + 20:
                if postac_rect.x > poziom_4_slup_2_rect.x - 60 and postac_rect.x < poziom_4_slup_2_rect.x + 5:
                    postac_rect.bottom = poziom_4_slup_2_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_4_slup_2_rect.top and postac_rect.bottom < poziom_4_slup_2_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_4_slup_2_rect.right - 50:
                postac_rect.left = poziom_4_slup_2_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_4_slup_2_rect.left + 50:
                postac_rect.right = poziom_4_slup_2_rect.left + 20
        if pygame.Rect.colliderect(postac_rect, poziom_4_sciana_1_rect):
            if keys[pygame.K_a] and postac_rect.left > poziom_4_sciana_1_rect.right - 20:
                postac_rect.left = poziom_4_sciana_1_rect.right
            elif keys[pygame.K_d] and  postac_rect.right < poziom_4_sciana_1_rect.left + 20:
                postac_rect.right = poziom_4_sciana_1_rect.left
        if pygame.Rect.colliderect(postac_rect,poziom_4_polka_1_rect):
            if postac_rect.bottom > poziom_4_polka_1_rect.top and postac_rect.bottom < poziom_4_polka_1_rect.top + 20:
                if postac_rect.x > poziom_4_polka_1_rect.x - 60 and postac_rect.x < poziom_4_polka_1_rect.x + 220:
                    postac_rect.bottom = poziom_4_polka_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_4_polka_1_rect.top and postac_rect.bottom < poziom_4_polka_1_rect.top + 20:
                ile_masz_skoku = 0
            if postac_rect.top > poziom_4_polka_1_rect.y and postac_rect.top < poziom_4_polka_1_rect.y + 70:
                if postac_rect.x > poziom_4_polka_1_rect.x - 60 and postac_rect.x < poziom_4_polka_1_rect.x + 220:
                    postac_rect.top = poziom_4_polka_1_rect.bottom + 10
                    postac_gravity = 3
            elif keys[pygame.K_a] and postac_rect.left > poziom_4_polka_1_rect.right - 50:
                postac_rect.left = poziom_4_polka_1_rect.right - 20
        if postac_rect.colliderect(poziom_4_wyrwa_wejscie_rect):
            postac_rect.center = poziom_4_wyrwa_wyjscie_rect.center
            postac_gravity = 1
        if postac_rect.x > poziom_4_stalaktyt_1_rect.x - 150:
            poziom_4_stalaktyt_1_gravity = -25
        if poziom_4_stalaktyt_1_rect.y > 900:
            poziom_4_stalaktyt_1_gravity = 0
        if postac_rect.colliderect(poziom_4_stalaktyt_1_rect):
            mode = 'poziom_4_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_4_rect):
            mode = 'poziom_4_wygrana'
            status_poziomu_5 = 'gotowe'

    elif mode == 'poziom_4_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_4,powrot_z_przegranej_poziomu_4_rect)
        okno.blit(powtorka_poziomu_4, powtorka_poziomu_4_rect)

    elif mode == 'pauza_poziomu_4':
        okno.blit(pauza_poziomu_4,pauza_poziomu_4_rect)
        okno.blit(pauza_poziomu_4_wyjdz, pauza_poziomu_4_wyjdz_rect)
        okno.blit(pauza_poziomu_4_powrot, pauza_poziomu_4_powrot_rect)

    elif mode == 'poziom_4_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_4_zagraj_ponownie_poziom,poziom_4_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_4_nastepny_poziom, poziom_4_nastepny_poziom_rect)
        okno.blit(poziom_4_powrot_do_menu, poziom_4_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_5':
        okno.blit(poziom_5_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        if poziom_5_czy_wzieto_medalion == 'nie':
            okno.blit(poziom_5_medalion,poziom_5_medalion_rect)
        if poziom_5_czy_wzieto_medalion == 'tak':
            okno.blit(poziom_5_boss_1,poziom_5_boss_1_rect)
        if poziom_5_faza_bossa == 1:
            okno.blit(poziom_5_wybicie_1,poziom_5_wybicie_1_rect)
            okno.blit(poziom_5_wybicie_2,poziom_5_wybicie_2_rect)
        if poziom_5_faza_bossa == 2:
            okno.blit(poziom_5_kamien_1,poziom_5_kamien_1_rect)
            okno.blit(poziom_5_kamien_2, poziom_5_kamien_2_rect)
            okno.blit(poziom_5_kamien_3, poziom_5_kamien_3_rect)
            okno.blit(poziom_5_kamien_4, poziom_5_kamien_4_rect)
            okno.blit(poziom_5_kamien_5, poziom_5_kamien_5_rect)
        if poziom_5_faza_bossa == 3:
            okno.blit(poziom_5_guzik,poziom_5_guzik_rect)
        if poziom_5_czy_wzieto_medalion == 'po':
            okno.blit(poziom_5_portal,poziom_5_portal_rect)
            if postac_rect.colliderect(poziom_5_portal_rect):
                mode = 'poziom_5_wygrana'
                status_poziomu_6 = 'gotowe'
        okno.blit(postac, postac_rect)
        if postac_rect.colliderect(poziom_5_medalion_rect) and  poziom_5_czy_wzieto_medalion == 'nie':
            ile_masz_medalionow += 5
            poziom_5_czy_wzieto_medalion = 'tak'
            poziom_5_faza_bossa = 1
        if postac_rect.colliderect(poziom_5_boss_1_rect) and poziom_5_czy_wzieto_medalion == 'tak':
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_wybicie_1_rect) and poziom_5_faza_bossa == 1:
            postac_gravity = -21.5
            ile_masz_skoku -= 1
        if postac_rect.colliderect(poziom_5_wybicie_2_rect) and poziom_5_faza_bossa == 1:
            postac_gravity = -21.5
            ile_masz_skoku -= 1
        if poziom_5_faza_bossa == 1 and kierunek_bossa == 'lewo':
            poziom_5_boss_1_rect.x -= 6
        if poziom_5_faza_bossa == 1 and kierunek_bossa == 'prawo':
            poziom_5_boss_1_rect.x += 6
        if poziom_5_boss_1_rect.x < 100:
            kierunek_bossa = 'prawo'
            poziom_5_boss_1 = pygame.image.load('plansza_1_boss_1_prawo.png')
            ile_razy += 1
        if poziom_5_boss_1_rect.x > 1000:
            kierunek_bossa = 'lewo'
            poziom_5_boss_1 = pygame.image.load('plansza_1_boss_1_lewo.png')
            ile_razy += 1
        if ile_razy == 6:
            poziom_5_faza_bossa = 2
        if poziom_5_faza_bossa == 2 and poziom_5_kamien_1_rect.y < -500:
            poziom_5_kamien_1_rect.y = -200
        if poziom_5_faza_bossa == 2 and poziom_5_kamien_2_rect.y < -500:
            poziom_5_kamien_2_rect.y = -200
        if poziom_5_faza_bossa == 2 and poziom_5_kamien_3_rect.y < -500:
            poziom_5_kamien_3_rect.y = -200
        if poziom_5_faza_bossa == 2 and poziom_5_kamien_4_rect.y < -500:
            poziom_5_kamien_4_rect.y = -200
        if poziom_5_faza_bossa == 2 and poziom_5_kamien_5_rect.y < -500:
            poziom_5_kamien_5_rect.y = -200
        if poziom_5_kamien_1_rect.y > -500:
            poziom_5_kamien_1_rect.y += poziom_5_kamien_1_gravity
        if poziom_5_kamien_1_rect.y > 500:
            poziom_5_kamien_2_rect.y += poziom_5_kamien_2_gravity
        if poziom_5_kamien_2_rect.y > 500:
            poziom_5_kamien_3_rect.y += poziom_5_kamien_3_gravity
        if poziom_5_kamien_3_rect.y > 500:
            poziom_5_kamien_4_rect.y += poziom_5_kamien_4_gravity
        if poziom_5_kamien_4_rect.y > 500:
            poziom_5_kamien_5_rect.y += poziom_5_kamien_5_gravity
        if poziom_5_kamien_5_rect.y > 1000:
            poziom_5_faza_bossa = 3
        if poziom_5_faza_bossa == 3:
            poziom_5_boss_1_rect.x -= 6
        if postac_rect.colliderect(poziom_5_kamien_1_rect) and poziom_5_faza_bossa == 2:
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_kamien_2_rect) and poziom_5_faza_bossa == 2:
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_kamien_3_rect) and poziom_5_faza_bossa == 2:
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_kamien_4_rect) and poziom_5_faza_bossa == 2:
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_kamien_5_rect) and poziom_5_faza_bossa == 2:
            mode = 'poziom_5_przegrana'
        if postac_rect.colliderect(poziom_5_guzik_rect) and poziom_5_faza_bossa == 3:
            poziom_5_czy_wzieto_medalion = 'po'
            poziom_5_faza_bossa = 4

    elif mode == 'poziom_5_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_5,powrot_z_przegranej_poziomu_5_rect)
        okno.blit(powtorka_poziomu_5, powtorka_poziomu_5_rect)

    elif mode == 'pauza_poziomu_5':
        okno.blit(pauza_poziomu_5,pauza_poziomu_5_rect)
        okno.blit(pauza_poziomu_5_wyjdz, pauza_poziomu_5_wyjdz_rect)
        okno.blit(pauza_poziomu_5_powrot, pauza_poziomu_5_powrot_rect)

    elif mode == 'poziom_5_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_5_zagraj_ponownie_poziom,poziom_5_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_5_nastepny_poziom, poziom_5_nastepny_poziom_rect)
        okno.blit(poziom_5_powrot_do_menu, poziom_5_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_6':
        okno.blit(poziom_6_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_6_stalaktyt_1,poziom_6_stalaktyt_1_rect)
        okno.blit(poziom_6_stalaktyt_2, poziom_6_stalaktyt_2_rect)
        okno.blit(poziom_6_kolec_1,poziom_6_kolec_1_rect)
        okno.blit(poziom_6_kolec_2, poziom_6_kolec_2_rect)
        poziom_6_stalaktyt_1_rect.y -= poziom_6_stalaktyt_1_gravity
        poziom_6_stalaktyt_2_rect.y -= poziom_6_stalaktyt_2_gravity
        if postac_rect.x > poziom_6_stalaktyt_1_rect.x - 150:
            poziom_6_stalaktyt_1_gravity = -25
        if postac_rect.x > poziom_6_stalaktyt_2_rect.x - 150:
            poziom_6_stalaktyt_2_gravity = -25
        if poziom_6_stalaktyt_1_rect.y > 900:
            poziom_6_stalaktyt_1_gravity = 0
        if poziom_6_stalaktyt_2_rect.y > 900:
            poziom_6_stalaktyt_2_gravity = 0
        if postac_rect.colliderect(poziom_6_stalaktyt_1_rect):
            mode = 'poziom_6_przegrana'
        if postac_rect.colliderect(poziom_6_stalaktyt_2_rect):
            mode = 'poziom_6_przegrana'
        if postac_rect.colliderect(poziom_6_kolec_1_rect):
            if postac_rect.right - 40 > poziom_6_kolec_1_rect.left:
                mode = 'poziom_6_przegrana'
        if postac_rect.colliderect(poziom_6_kolec_2_rect):
            if postac_rect.left + 20 < poziom_6_kolec_2_rect.right:
                mode = 'poziom_6_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_6_rect):
            mode = 'poziom_6_wygrana'
            status_poziomu_7 = 'gotowe'

    elif mode == 'poziom_6_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_6,powrot_z_przegranej_poziomu_6_rect)
        okno.blit(powtorka_poziomu_6, powtorka_poziomu_6_rect)

    elif mode == 'pauza_poziomu_6':
        okno.blit(pauza_poziomu_6,pauza_poziomu_6_rect)
        okno.blit(pauza_poziomu_6_wyjdz, pauza_poziomu_6_wyjdz_rect)
        okno.blit(pauza_poziomu_6_powrot, pauza_poziomu_6_powrot_rect)

    elif mode == 'poziom_6_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_6_zagraj_ponownie_poziom,poziom_6_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_6_nastepny_poziom, poziom_6_nastepny_poziom_rect)
        okno.blit(poziom_6_powrot_do_menu, poziom_6_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_7':
        okno.blit(poziom_7_tlo,dest=(0,0))
        postac_gravity += 0.5
        poziom_7_enemy_1_rect.x -= poziom_7_enemy_1_speed
        poziom_7_enemy_2_rect.x -= poziom_7_enemy_2_speed
        poziom_7_enemy_3_rect.x -= poziom_7_enemy_3_speed
        poziom_7_enemy_4_rect.x -= poziom_7_enemy_4_speed
        poziom_7_enemy_5_rect.x -= poziom_7_enemy_5_speed
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_7_stalaktyt_1,poziom_7_stalaktyt_1_rect)
        okno.blit(poziom_7_enemy_1,poziom_7_enemy_1_rect)
        okno.blit(poziom_7_enemy_2, poziom_7_enemy_2_rect)
        okno.blit(poziom_7_enemy_3, poziom_7_enemy_3_rect)
        okno.blit(poziom_7_enemy_4, poziom_7_enemy_4_rect)
        okno.blit(poziom_7_enemy_5, poziom_7_enemy_5_rect)
        okno.blit(poziom_7_slup_1,poziom_7_slup_1_rect)
        poziom_7_stalaktyt_1_rect.y -= poziom_7_stalaktyt_1_gravity
        if postac_rect.x > poziom_7_stalaktyt_1_rect.x - 150:
            poziom_7_stalaktyt_1_gravity = -25
        if poziom_7_stalaktyt_1_rect.y > 900:
            poziom_7_stalaktyt_1_gravity = 0
        if postac_rect.colliderect(poziom_7_stalaktyt_1_rect):
            mode = 'poziom_7_przegrana'
        if pygame.Rect.colliderect(postac_rect,poziom_7_slup_1_rect):
            if postac_rect.bottom > poziom_7_slup_1_rect.top and postac_rect.bottom < poziom_7_slup_1_rect.top + 20:
                if postac_rect.x > poziom_7_slup_1_rect.x - 60 and postac_rect.x < poziom_7_slup_1_rect.x + 5:
                    postac_rect.bottom = poziom_7_slup_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_7_slup_1_rect.top and postac_rect.bottom < poziom_7_slup_1_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_7_slup_1_rect.right - 50:
                postac_rect.left = poziom_7_slup_1_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_7_slup_1_rect.left + 50:
                postac_rect.right = poziom_7_slup_1_rect.left + 20

        if poziom_7_enemy_1_rect.x < -100:
            poziom_7_enemy_1_speed = 0
        if postac_rect.colliderect(poziom_7_enemy_1_rect):
            mode = 'poziom_7_przegrana'
        if poziom_7_enemy_2_rect.x < -100:
            poziom_7_enemy_2_speed = 0
        if postac_rect.colliderect(poziom_7_enemy_2_rect):
            mode = 'poziom_7_przegrana'
        if poziom_7_enemy_3_rect.x < -100:
            poziom_7_enemy_3_speed = 0
        if postac_rect.colliderect(poziom_7_enemy_3_rect):
            mode = 'poziom_7_przegrana'
        if poziom_7_enemy_4_rect.x < -100:
            poziom_7_enemy_4_speed = 0
        if postac_rect.colliderect(poziom_7_enemy_4_rect):
            mode = 'poziom_7_przegrana'
        if poziom_7_enemy_5_rect.x < -100:
            poziom_7_enemy_5_speed = 0
        if postac_rect.colliderect(poziom_7_enemy_5_rect):
            mode = 'poziom_7_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_7_rect):
            mode = 'poziom_7_wygrana'
            status_poziomu_8 = 'gotowe'

    elif mode == 'poziom_7_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_7,powrot_z_przegranej_poziomu_7_rect)
        okno.blit(powtorka_poziomu_7, powtorka_poziomu_7_rect)

    elif mode == 'pauza_poziomu_7':
        okno.blit(pauza_poziomu_7,pauza_poziomu_7_rect)
        okno.blit(pauza_poziomu_7_wyjdz, pauza_poziomu_7_wyjdz_rect)
        okno.blit(pauza_poziomu_7_powrot, pauza_poziomu_7_powrot_rect)

    elif mode == 'poziom_7_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_7_zagraj_ponownie_poziom,poziom_7_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_7_nastepny_poziom, poziom_7_nastepny_poziom_rect)
        okno.blit(poziom_7_powrot_do_menu, poziom_7_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_8':
        okno.blit(poziom_8_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(poziom_8_slup_1,poziom_8_slup_1_rect)
        okno.blit(poziom_8_slup_2, poziom_8_slup_2_rect)
        okno.blit(poziom_8_slup_3, poziom_8_slup_3_rect)
        okno.blit(poziom_8_slup_4, poziom_8_slup_4_rect)
        okno.blit(poziom_8_stalaktyt_1,poziom_8_stalaktyt_1_rect)
        okno.blit(poziom_8_kolec_1,poziom_8_kolec_1_rect)
        okno.blit(poziom_8_kolec_2, poziom_8_kolec_2_rect)
        okno.blit(poziom_8_kolec_3, poziom_8_kolec_3_rect)
        okno.blit(poziom_8_kolec_4, poziom_8_kolec_4_rect)
        okno.blit(poziom_8_kolec_5, poziom_8_kolec_5_rect)
        okno.blit(postac, postac_rect)
        poziom_8_stalaktyt_1_rect.y -= poziom_8_stalaktyt_1_gravity
        if pygame.Rect.colliderect(postac_rect,poziom_8_slup_1_rect):
            if postac_rect.bottom > poziom_8_slup_1_rect.top and postac_rect.bottom < poziom_8_slup_1_rect.top + 20:
                if postac_rect.x > poziom_8_slup_1_rect.x - 60 and postac_rect.x < poziom_8_slup_1_rect.x + 5:
                    postac_rect.bottom = poziom_8_slup_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_8_slup_1_rect.top and postac_rect.bottom < poziom_8_slup_1_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_8_slup_1_rect.right - 50:
                postac_rect.left = poziom_8_slup_1_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_8_slup_1_rect.left + 50:
                postac_rect.right = poziom_8_slup_1_rect.left + 20
        if pygame.Rect.colliderect(postac_rect,poziom_8_slup_2_rect):
            if postac_rect.bottom > poziom_8_slup_2_rect.top and postac_rect.bottom < poziom_8_slup_2_rect.top + 20:
                if postac_rect.x > poziom_8_slup_2_rect.x - 60 and postac_rect.x < poziom_8_slup_2_rect.x + 5:
                    postac_rect.bottom = poziom_8_slup_2_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_8_slup_2_rect.top and postac_rect.bottom < poziom_8_slup_2_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_8_slup_2_rect.right - 50:
                postac_rect.left = poziom_8_slup_2_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_8_slup_2_rect.left + 50:
                postac_rect.right = poziom_8_slup_2_rect.left + 20

        if pygame.Rect.colliderect(postac_rect,poziom_8_slup_3_rect):
            if postac_rect.bottom > poziom_8_slup_3_rect.top and postac_rect.bottom < poziom_8_slup_3_rect.top + 20:
                if postac_rect.x > poziom_8_slup_3_rect.x - 60 and postac_rect.x < poziom_8_slup_3_rect.x + 5:
                    postac_rect.bottom = poziom_8_slup_3_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_8_slup_3_rect.top and postac_rect.bottom < poziom_8_slup_3_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_8_slup_3_rect.right - 50:
                postac_rect.left = poziom_8_slup_3_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_8_slup_3_rect.left + 50:
                postac_rect.right = poziom_8_slup_3_rect.left + 20
        if pygame.Rect.colliderect(postac_rect,poziom_8_slup_4_rect):
            if postac_rect.bottom > poziom_8_slup_4_rect.top and postac_rect.bottom < poziom_8_slup_4_rect.top + 20:
                if postac_rect.x > poziom_8_slup_4_rect.x - 60 and postac_rect.x < poziom_8_slup_4_rect.x + 5:
                    postac_rect.bottom = poziom_8_slup_4_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_8_slup_4_rect.top and postac_rect.bottom < poziom_8_slup_4_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_8_slup_4_rect.right - 50:
                postac_rect.left = poziom_8_slup_4_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_8_slup_4_rect.left + 50:
                postac_rect.right = poziom_8_slup_4_rect.left + 20

        if postac_rect.colliderect(poziom_8_kolec_1_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.colliderect(poziom_8_kolec_2_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.colliderect(poziom_8_kolec_3_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.colliderect(poziom_8_kolec_4_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.colliderect(poziom_8_kolec_5_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.x > poziom_8_stalaktyt_1_rect.x - 150:
            poziom_8_stalaktyt_1_gravity = -25
        if poziom_8_stalaktyt_1_rect.y > 900:
            poziom_8_stalaktyt_1_gravity = 0
        if postac_rect.colliderect(poziom_8_stalaktyt_1_rect):
            mode = 'poziom_8_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_8_rect):
            mode = 'poziom_8_wygrana'
            status_poziomu_9 = 'gotowe'

    elif mode == 'poziom_8_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_8,powrot_z_przegranej_poziomu_8_rect)
        okno.blit(powtorka_poziomu_8, powtorka_poziomu_8_rect)

    elif mode == 'pauza_poziomu_8':
        okno.blit(pauza_poziomu_8,pauza_poziomu_8_rect)
        okno.blit(pauza_poziomu_8_wyjdz, pauza_poziomu_8_wyjdz_rect)
        okno.blit(pauza_poziomu_8_powrot, pauza_poziomu_8_powrot_rect)

    elif mode == 'poziom_8_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_8_zagraj_ponownie_poziom,poziom_8_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_8_nastepny_poziom, poziom_8_nastepny_poziom_rect)
        okno.blit(poziom_8_powrot_do_menu, poziom_8_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_9':
        okno.blit(poziom_9_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(poziom_9_slup_1,poziom_9_slup_1_rect)
        okno.blit(poziom_9_slup_2, poziom_9_slup_2_rect)
        okno.blit(poziom_9_polka_1,poziom_9_polka_1_rect)
        okno.blit(poziom_9_polka_2, poziom_9_polka_2_rect)
        okno.blit(poziom_9_wyrwa_wejscie,poziom_9_wyrwa_wejscie_rect)
        okno.blit(poziom_9_wyrwa_wyjscie, poziom_9_wyrwa_wyjscie_rect)
        poziom_9_sciana_1_rect.y -= ruch
        if ktore_pokazac == 'gora':
            okno.blit(poziom_9_dzwignia_do_gory,poziom_9_dzwignia_do_gory_rect)
        if ktore_pokazac == 'dol':
            okno.blit(poziom_9_dzwignia_w_dol,poziom_9_dzwignia_w_dol_rect)
        okno.blit(postac, postac_rect)
        okno.blit(poziom_9_sciana_1,poziom_9_sciana_1_rect)
        if postac_rect.colliderect(poziom_9_dzwignia_do_gory_rect):
            ktore_pokazac = 'dol'
            ruch = 3
        if poziom_9_sciana_1_rect.y < -800:
            ruch = 0
        if pygame.Rect.colliderect(postac_rect,poziom_9_slup_1_rect):
            if postac_rect.bottom > poziom_9_slup_1_rect.top and postac_rect.bottom < poziom_9_slup_1_rect.top + 20:
                if postac_rect.x > poziom_9_slup_1_rect.x - 60 and postac_rect.x < poziom_9_slup_1_rect.x + 5:
                    postac_rect.bottom = poziom_9_slup_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_9_slup_1_rect.top and postac_rect.bottom < poziom_9_slup_1_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_9_slup_1_rect.right - 50:
                postac_rect.left = poziom_9_slup_1_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_9_slup_1_rect.left + 50:
                postac_rect.right = poziom_9_slup_1_rect.left + 20
        if pygame.Rect.colliderect(postac_rect,poziom_9_slup_2_rect):
            if postac_rect.bottom > poziom_9_slup_2_rect.top and postac_rect.bottom < poziom_9_slup_2_rect.top + 20:
                if postac_rect.x > poziom_9_slup_2_rect.x - 60 and postac_rect.x < poziom_9_slup_2_rect.x + 5:
                    postac_rect.bottom = poziom_9_slup_2_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_9_slup_2_rect.top and postac_rect.bottom < poziom_9_slup_2_rect.top + 20:
                ile_masz_skoku = 0
            if keys[pygame.K_a] and postac_rect.left > poziom_9_slup_2_rect.right - 50:
                postac_rect.left = poziom_9_slup_2_rect.right - 20
            elif keys[pygame.K_d] and  postac_rect.right < poziom_9_slup_2_rect.left + 50:
                postac_rect.right = poziom_9_slup_2_rect.left + 20
        if pygame.Rect.colliderect(postac_rect, poziom_9_sciana_1_rect):
            if keys[pygame.K_a] and postac_rect.left > poziom_9_sciana_1_rect.right - 20:
                postac_rect.left = poziom_9_sciana_1_rect.right
            elif keys[pygame.K_d] and  postac_rect.right < poziom_9_sciana_1_rect.left + 20:
                postac_rect.right = poziom_9_sciana_1_rect.left
        if pygame.Rect.colliderect(postac_rect,poziom_9_polka_1_rect):
            if postac_rect.bottom > poziom_9_polka_1_rect.top and postac_rect.bottom < poziom_9_polka_1_rect.top + 20:
                if postac_rect.x > poziom_9_polka_1_rect.x - 60 and postac_rect.x < poziom_9_polka_1_rect.x + 220:
                    postac_rect.bottom = poziom_9_polka_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_9_polka_1_rect.top and postac_rect.bottom < poziom_9_polka_1_rect.top + 20:
                ile_masz_skoku = 0
            if postac_rect.top > poziom_9_polka_1_rect.y and postac_rect.top < poziom_9_polka_1_rect.y + 70:
                if postac_rect.x > poziom_9_polka_1_rect.x - 60 and postac_rect.x < poziom_9_polka_1_rect.x + 220:
                    postac_rect.top = poziom_9_polka_1_rect.bottom + 10
                    postac_gravity = 3
            elif keys[pygame.K_a] and postac_rect.left > poziom_9_polka_1_rect.right - 50:
                postac_rect.left = poziom_9_polka_1_rect.right - 20
        if postac_rect.colliderect(poziom_9_wyrwa_wejscie_rect):
            postac_rect.center = poziom_9_wyrwa_wyjscie_rect.center
            postac_gravity = 1
        if pygame.Rect.colliderect(postac_rect,poziom_9_polka_2_rect):
            if postac_rect.bottom > poziom_9_polka_2_rect.top and postac_rect.bottom < poziom_9_polka_2_rect.top + 20:
                if postac_rect.x > poziom_9_polka_2_rect.x - 60 and postac_rect.x < poziom_9_polka_2_rect.right - 30:
                    postac_rect.bottom = poziom_9_polka_2_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_9_polka_2_rect.top and postac_rect.bottom < poziom_9_polka_2_rect.top + 20:
                ile_masz_skoku = 0
            if postac_rect.top > poziom_9_polka_2_rect.y and postac_rect.top < poziom_9_polka_2_rect.y + 70:
                if postac_rect.x > poziom_9_polka_2_rect.x - 60 and postac_rect.x < poziom_9_polka_2_rect.right - 30:
                    postac_rect.top = poziom_9_polka_2_rect.bottom + 10
                    postac_gravity = 3
            elif keys[pygame.K_a] and postac_rect.left > poziom_9_polka_2_rect.right - 50:
                postac_rect.left = poziom_9_polka_2_rect.right - 20
        if postac_rect.colliderect(poziom_9_wyrwa_wejscie_rect):
            postac_rect.center = poziom_9_wyrwa_wyjscie_rect.center
            postac_gravity = 1
        if postac_rect.colliderect(rect_ukonczenia_poziomu_9_rect):
            mode = 'poziom_9_wygrana'
            status_poziomu_10 = 'gotowe'

    elif mode == 'poziom_9_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_9,powrot_z_przegranej_poziomu_9_rect)
        okno.blit(powtorka_poziomu_9, powtorka_poziomu_9_rect)

    elif mode == 'pauza_poziomu_9':
        okno.blit(pauza_poziomu_9,pauza_poziomu_9_rect)
        okno.blit(pauza_poziomu_9_wyjdz, pauza_poziomu_9_wyjdz_rect)
        okno.blit(pauza_poziomu_9_powrot, pauza_poziomu_9_powrot_rect)

    elif mode == 'poziom_9_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_9_zagraj_ponownie_poziom,poziom_9_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_9_nastepny_poziom, poziom_9_nastepny_poziom_rect)
        okno.blit(poziom_9_powrot_do_menu, poziom_9_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_10':
        okno.blit(poziom_10_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_10_sciana_1,poziom_10_sciana_1_rect)
        okno.blit(kupa_gruzu, kupa_gruzu_rect)
        okno.blit(poziom_10_swiatlo_prawe,dest=(610,60))
        okno.blit(poziom_10_swiatlo_lewe, dest=(440,60))
        if poziom_10_czy_wzieto_medalion == 'tak' and martwy == 'nie':
            poziom_10_boss_1_rect.x += boss_kierunek * boss_speed
        if ktora1 == 'gora':
            okno.blit(poziom_10_dzwignia_do_gory_1,poziom_10_dzwignia_do_gory_1_rect)
        if ktora2 == 'gora':
            okno.blit(poziom_10_dzwignia_do_gory_2, poziom_10_dzwignia_do_gory_2_rect)
        if ktora1 == 'dol':
            okno.blit(poziom_10_dzwignia_w_dol_1, poziom_10_dzwignia_w_dol_1_rect)
        if ktora2 == 'dol':
            okno.blit(poziom_10_dzwignia_w_dol_2, poziom_10_dzwignia_w_dol_2_rect)
        poziom_10_sciana_1_rect.y -= ruch2
        if poziom_10_sciana_1_rect.y < -500:
            ruch2 = 0
        if poziom_10_sciana_1_rect.y > -1:
            ruch2 = 0
        if pygame.Rect.colliderect(postac_rect, poziom_10_sciana_1_rect):
            if keys[pygame.K_a] and postac_rect.left > poziom_10_sciana_1_rect.right - 20:
                postac_rect.left = poziom_10_sciana_1_rect.right
            elif keys[pygame.K_d] and  postac_rect.right < poziom_10_sciana_1_rect.left + 20:
                postac_rect.right = poziom_10_sciana_1_rect.left
        if postac_rect.colliderect(poziom_10_dzwignia_do_gory_1_rect) and ktora1 == 'gora' and ruch2 == 0:
            ktora1 = 'dol'
            ruch2 = 6
        if postac_rect.colliderect(poziom_10_dzwignia_do_gory_2_rect) and ktora2 == 'gora' and ruch2 == 0:
            ktora2 = 'dol'
            ruch2 = -6
        if postac_rect.colliderect(poziom_10_dzwignia_do_gory_1_rect) and ktora1 == 'dol' and ruch2 == 0:
            ktora1 = 'gora'
            ruch2 = -6
        if postac_rect.colliderect(poziom_10_dzwignia_do_gory_2_rect) and ktora2 == 'dol' and ruch2 == 0:
            ktora2 = 'gora'
            ruch2 = 6
        if poziom_10_czy_wzieto_medalion == 'nie':
            okno.blit(poziom_10_medalion,poziom_10_medalion_rect)
        if poziom_10_czy_wzieto_medalion == 'tak' and martwy == 'nie':
            okno.blit(poziom_10_boss_1,poziom_10_boss_1_rect)
        if postac_rect.colliderect(poziom_10_medalion_rect) and poziom_10_czy_wzieto_medalion == 'nie':
            poziom_10_czy_wzieto_medalion = 'tak'
            ile_masz_medalionow += 3
        if postac_rect.colliderect(poziom_10_boss_1_rect) and poziom_10_czy_wzieto_medalion == 'tak' and martwy == 'nie':
            mode = 'poziom_10_przegrana'
        if poziom_10_boss_1_rect.colliderect(poziom_10_sciana_1_rect):
            m_bossa = random.randint(1,2)
            if m_bossa == 1:
                boss_kierunek = -1
                poziom_10_swiatlo_prawe = pygame.image.load('światło_wł.png')
                poziom_10_swiatlo_lewe = pygame.image.load('światło_wył.png')
                obraz_bossa = 'plansza_1_boss_2_lewo.png'
                poziom_10_boss_1 = pygame.image.load(obraz_bossa)
                poziom_10_boss_1_rect.x = 2600
                za_ile_koniec_bossa += 1
                if za_ile_koniec_bossa >= 10:
                    poziom_10_boss_1_rect.x = 592
            if m_bossa == 2:
                boss_kierunek = 1
                poziom_10_swiatlo_prawe = pygame.image.load('światło_wył.png')
                poziom_10_swiatlo_lewe = pygame.image.load('światło_wł.png')
                obraz_bossa = 'plansza_1_boss_2_prawo.png'
                poziom_10_boss_1 = pygame.image.load(obraz_bossa)
                poziom_10_boss_1_rect.x = -1500
                za_ile_koniec_bossa += 1
                if za_ile_koniec_bossa >= 10:
                    poziom_10_boss_1_rect.x = 353
        if za_ile_koniec_bossa >= 10:
            martwy = 'tak'
            poziom_10_swiatlo_prawe = pygame.image.load('światło_wył.png')
            poziom_10_swiatlo_lewe = pygame.image.load('światło_wył.png')
            kupa_gruzu_rect.midbottom = (550,750)
        if postac_rect.colliderect(kupa_gruzu_rect):
            mode = 'poziom_10_wygrana'
            status_poziomu_11 = 'gotowe'

    elif mode == 'poziom_10_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_10,powrot_z_przegranej_poziomu_10_rect)
        okno.blit(powtorka_poziomu_10, powtorka_poziomu_10_rect)

    elif mode == 'pauza_poziomu_10':
        okno.blit(pauza_poziomu_10,pauza_poziomu_10_rect)
        okno.blit(pauza_poziomu_10_wyjdz, pauza_poziomu_10_wyjdz_rect)
        okno.blit(pauza_poziomu_10_powrot, pauza_poziomu_10_powrot_rect)

    elif mode == 'poziom_10_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_10_zagraj_ponownie_poziom,poziom_10_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_10_nastepny_poziom, poziom_10_nastepny_poziom_rect)
        okno.blit(poziom_10_powrot_do_menu, poziom_10_powrot_do_menu_rect)


    elif mode == 'plansza_1_poziom_11':
        okno.blit(poziom_11_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(poziom_11_wybicie_1, poziom_11_wybicie_1_rect)
        okno.blit(poziom_11_stalaktyt_1,poziom_11_stalaktyt_1_rect)
        okno.blit(poziom_11_polka_1, poziom_11_polka_1_rect)
        okno.blit(poziom_11_sciana_1, poziom_11_sciana_1_rect)
        okno.blit(poziom_11_sciana_2, poziom_11_sciana_2_rect)
        okno.blit(poziom_11_wyrwa_wejscie,poziom_11_wyrwa_wejscie_rect)
        okno.blit(poziom_11_wyrwa_wejscie_2, poziom_11_wyrwa_wejscie_2_rect)
        okno.blit(poziom_11_wyrwa_wyjscie, poziom_11_wyrwa_wyjscie_rect)
        okno.blit(poziom_11_wyrwa_wyjscie_2, poziom_11_wyrwa_wyjscie_2_rect)
        okno.blit(postac, postac_rect)
        poziom_11_stalaktyt_1_rect.y -= poziom_11_stalaktyt_1_gravity
        if postac_rect.x > poziom_11_stalaktyt_1_rect.x - 150:
            poziom_11_stalaktyt_1_gravity = -25
        if poziom_11_stalaktyt_1_rect.y > 900:
            poziom_11_stalaktyt_1_gravity = 0
        if postac_rect.colliderect(poziom_11_stalaktyt_1_rect):
            mode = 'poziom_11_przegrana'
        if postac_rect.colliderect(rect_ukonczenia_poziomu_11_rect):
            mode = 'poziom_11_wygrana'
            status_poziomu_12 = 'gotowe'
        if pygame.Rect.colliderect(postac_rect,poziom_11_polka_1_rect):
            if postac_rect.bottom > poziom_11_polka_1_rect.top and postac_rect.bottom < poziom_11_polka_1_rect.top + 20:
                if postac_rect.x > poziom_11_polka_1_rect.x - 60 and postac_rect.x < poziom_11_polka_1_rect.x + 220:
                    postac_rect.bottom = poziom_11_polka_1_rect.top
                    postac_gravity = 0
                    ile_masz_skoku = 1
            elif not postac_rect.bottom > poziom_11_polka_1_rect.top and postac_rect.bottom < poziom_11_polka_1_rect.top + 20:
                ile_masz_skoku = 0
            if postac_rect.top > poziom_11_polka_1_rect.y and postac_rect.top < poziom_11_polka_1_rect.y + 70:
                if postac_rect.x > poziom_11_polka_1_rect.x - 60 and postac_rect.x < poziom_11_polka_1_rect.x + 220:
                    postac_rect.top = poziom_11_polka_1_rect.bottom + 10
                    postac_gravity = 3
            elif keys[pygame.K_a] and postac_rect.left > poziom_11_polka_1_rect.right - 50:
                postac_rect.left = poziom_11_polka_1_rect.right - 20
        if postac_rect.colliderect(poziom_11_wybicie_1_rect):
            postac_gravity = -21.5
            ile_masz_skoku -= 1
        if pygame.Rect.colliderect(postac_rect, poziom_11_sciana_1_rect):
            if keys[pygame.K_a] and postac_rect.left > poziom_11_sciana_1_rect.right - 20:
                postac_rect.left = poziom_11_sciana_1_rect.right
            elif keys[pygame.K_d] and  postac_rect.right < poziom_11_sciana_1_rect.left + 20:
                postac_rect.right = poziom_11_sciana_1_rect.left
        if pygame.Rect.colliderect(postac_rect, poziom_11_sciana_2_rect):
            if keys[pygame.K_a] and postac_rect.left > poziom_11_sciana_2_rect.right - 20:
                postac_rect.left = poziom_11_sciana_2_rect.right
            elif keys[pygame.K_d] and  postac_rect.right < poziom_11_sciana_2_rect.left + 20:
                postac_rect.right = poziom_11_sciana_2_rect.left
        if postac_rect.colliderect(poziom_11_wyrwa_wejscie_rect):
            postac_rect.center = poziom_11_wyrwa_wyjscie_rect.center
            postac_gravity = 1
        if postac_rect.colliderect(poziom_11_wyrwa_wejscie_2_rect):
            postac_rect.center = poziom_11_wyrwa_wyjscie_2_rect.center
            postac_gravity = 1


    elif mode == 'poziom_11_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_11,powrot_z_przegranej_poziomu_11_rect)
        okno.blit(powtorka_poziomu_11,powtorka_poziomu_11_rect)

    elif mode == 'pauza_poziomu_11':
        okno.blit(pauza_poziomu_11,pauza_poziomu_11_rect)
        okno.blit(pauza_poziomu_11_wyjdz, pauza_poziomu_11_wyjdz_rect)
        okno.blit(pauza_poziomu_11_powrot, pauza_poziomu_11_powrot_rect)

    elif mode == 'poziom_11_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_11_zagraj_ponownie_poziom,poziom_11_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_11_nastepny_poziom, poziom_11_nastepny_poziom_rect)
        okno.blit(poziom_11_powrot_do_menu, poziom_11_powrot_do_menu_rect)

    elif mode == 'plansza_1_poziom_12':
        okno.blit(poziom_12_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(generator_1,generator_1_rect)
        okno.blit(podpowiadajacy_kolor,podpowiadajacy_kolor_rect)
        okno.blit(tablica_z_kodem,tablica_z_kodem_rect)
        okno.blit(tekst_cyfra_1_kodu,tekst_cyfra_1_kodu_rect)
        okno.blit(tekst_cyfra_2_kodu, tekst_cyfra_2_kodu_rect)
        okno.blit(tekst_cyfra_3_kodu, tekst_cyfra_3_kodu_rect)
        okno.blit(niebieskie_swiatlo_1,niebieskie_swiatlo_1_rect)
        okno.blit(niebieskie_swiatlo_2, niebieskie_swiatlo_2_rect)
        okno.blit(slupek_radarowy,slupek_radarowy_rect)
        if postac_rect.colliderect(generator_1_rect):
            mode = 'wykonywanie_generatora'

    elif mode == 'poziom_12_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_12,powrot_z_przegranej_poziomu_12_rect)
        okno.blit(powtorka_poziomu_12,powtorka_poziomu_12_rect)

    elif mode == 'pauza_poziomu_12':
        okno.blit(pauza_poziomu_12,pauza_poziomu_12_rect)
        okno.blit(pauza_poziomu_12_wyjdz, pauza_poziomu_12_wyjdz_rect)
        okno.blit(pauza_poziomu_12_powrot, pauza_poziomu_12_powrot_rect)

    elif mode == 'poziom_12_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_12_zagraj_ponownie_poziom,poziom_12_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_12_nastepny_poziom, poziom_12_nastepny_poziom_rect)
        okno.blit(poziom_12_powrot_do_menu, poziom_12_powrot_do_menu_rect)

    elif mode == 'wykonywanie_generatora':
        okno.blit(wykonywanie_generatora_tlo,dest=(0,0))
        okno.blit(guzik_konca_wykonywania,guzik_konca_wykonywania_rect)
        okno.blit(przycisk_1_generatora,przycisk_1_generatora_rect)
        okno.blit(przycisk_2_generatora, przycisk_2_generatora_rect)
        okno.blit(przycisk_3_generatora, przycisk_3_generatora_rect)
        okno.blit(przycisk_4_generatora, przycisk_4_generatora_rect)
        okno.blit(przycisk_5_generatora, przycisk_5_generatora_rect)
        okno.blit(panel_cyferek,dest=(50,125))
        okno.blit(radar_generatora,radar_generatora_rect)
        okno.blit(suwak_1,suwak_1_rect)
        okno.blit(suwak_2, suwak_2_rect)
        okno.blit(liczba_1,liczba_1_rect)
        okno.blit(liczba_2, liczba_2_rect)
        okno.blit(liczba_3, liczba_3_rect)
        okno.blit(liczba_4, liczba_4_rect)
        okno.blit(liczba_5, liczba_5_rect)
        okno.blit(liczba_6, liczba_6_rect)
        okno.blit(liczba_7, liczba_7_rect)
        okno.blit(liczba_8, liczba_8_rect)
        okno.blit(liczba_9, liczba_9_rect)


    elif mode == 'plansza_1_poziom_13':
        okno.blit(poziom_13_tlo,dest=(0,0))
        postac_gravity += 0.5
        postac_rect.y += postac_gravity
        if keys[pygame.K_d]:
            postac_rect.x += speed
        if keys[pygame.K_a]:
            postac_rect.x -= speed
        if postac_rect.bottom < 200:
            postac_rect.bottom = 200
        if postac_rect.bottom >= 750:
            postac_rect.bottom = 750
            ile_masz_skoku = 1
        if postac_rect.x <= 40:
            postac_rect.x = 40
        if postac_rect.x >= 960:
            postac_rect.x = 960
        okno.blit(postac, postac_rect)
        okno.blit(poziom_13_generator_1,poziom_13_generator_1_rect)
        okno.blit(poziom_13_sciana_1,poziom_13_sciana_1_rect)
        poziom_13_sciana_1_rect.y -= ruch_bramy
        if poziom_13_sciana_1_rect.y < -400:
            ruch_bramy = 0
        if postac_rect.colliderect(rect_ukonczenia_poziomu_13_rect):
            mode = 'poziom_13_wygrana'
            status_poziomu_14 = 'gotowe'
        if postac_rect.colliderect(poziom_13_generator_1_rect) and czy_wlaczono == 'nie':
            mode = 'włącz_generator_1'

    elif mode == 'poziom_13_przegrana':
        okno.blit(gra_plansza_1,dest=(0,0))
        okno.blit(powrot_z_przegranej_poziomu_13,powrot_z_przegranej_poziomu_13_rect)
        okno.blit(powtorka_poziomu_13,powtorka_poziomu_13_rect)

    elif mode == 'pauza_poziomu_13':
        okno.blit(pauza_poziomu_13,pauza_poziomu_13_rect)
        okno.blit(pauza_poziomu_13_wyjdz, pauza_poziomu_13_wyjdz_rect)
        okno.blit(pauza_poziomu_13_powrot, pauza_poziomu_13_powrot_rect)

    elif mode == 'poziom_13_wygrana':
        okno.blit(gra_plansza_1, dest=(0, 0))
        okno.blit(poziom_13_zagraj_ponownie_poziom,poziom_13_zagraj_ponownie_poziom_rect)
        okno.blit(poziom_13_nastepny_poziom, poziom_13_nastepny_poziom_rect)
        okno.blit(poziom_13_powrot_do_menu, poziom_13_powrot_do_menu_rect)

    elif mode == 'włącz_generator_1':
        okno.blit(wykonywanie_generatora_tlo,dest=(0,0))
        okno.blit(poziom_13_guzik_generatora_1,poziom_13_guzik_generatora_1_rect)
        okno.blit(poziom_13_suwak_generatora_1, poziom_13_suwak_generatora_1_rect)

    pygame.display.update()
    clock.tick(60)



