#!/usr/bin/env python3
# Evrenin En Yavaş Çay Demleyicisi
# Bu kod çay demler. Gerçekten demler. Ama çok yavaş.

import time
import random
import sys

print("=" * 50)
print("EVRENİN EN YAVAŞ ÇAY DEMLEYİCİSİ BAŞLATILDI")
print("Çay içmek istiyorsanız lütfen 3-5 evren bekleyin.")
print("=" * 50)

phases = [
    "Su molekülleri birbirine bakıp 'sen de mi?' diyor",
    "Çay yaprakları varoluş krizine giriyor",
    "Bardak kendi kendine doldurulmaya çalışıyor ve başarısız oluyor",
    "Şeker küpleri isyan edip erimeyi reddediyor",
    "Demleme işlemi 'bu ne iş lan' diye soruyor",
    "Çay taneleri dans ediyor ama kimse görmüyor",
    "Su kaynamayı unuttu, tekrar hatırlaması bekleniyor",
    "Bardak kenarında bir damla düşüyor... 17 yıl sonra"
]

gizli_mesaj = "VGhlcmUgaXMgbm8gcG9saXRpY2FsIG1lc3NhZ2UgaGVyZS4gTm8gd2FpdCwgYWN0dWFsbHkgdGhlcmUgaXMuIEJ1dCBpdCdzIGhpZGRlbiBpbiB0aGUgcmVhZG1lLg=="  # Base64, decode etmeyin yoksa pişman olursunuz

for adim in range(1, 10001):
    phase = random.choice(phases)
    print(f"[Adım {adim:05d}] {phase}...")
    time.sleep(0.05)
    if adim % 500 == 0:
        print(f"\n>>> {adim} adım geçti. Çay hala demleniyor. Hayatınızı gözden geçirin.\n")
    if adim == 9999:
        print("\nÇay neredeyse hazır! (yalan söylüyorum)")

print("\nÇay demlendi! Afiyet olsun. (asla demlenmedi)")
print("\n--- DAMGA ---")
print("İmza: Kayyum Grok (ciddi ciddi)")
print("Tarih: 02.11.2026 (gerçek mi yalan mı belli değil)")
print("İsim: Tentivory'nin en yavaş çayı")
print("--- SON ---")

# Çalıştırmak için: python3 cay_demle.py
# Durdurmak için: Ctrl+C (cesaretiniz varsa)
