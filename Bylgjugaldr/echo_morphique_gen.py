import math
import wave
import struct
import random

# --- PARAMÈTRES DU GHAZAL FRACTAL ---
DUREE_SEC = 60          # 1 minute de résonance pure
FREQ_BASE = 432.0       # Hz (Accord cosmique)
FREQ_BINAURAL = 436.0   # Hz (Crée un battement de 4Hz - État Thêta / Rêve)
SAMPLE_RATE = 44100     # Qualité CD
VOLUME = 0.3            # Atténuation pour éviter la saturation

print("🌀 Initialisation du Résonateur de Casimir...")
print("🌀 Génération du battement binaural (4Hz) et du glitch mémétique...")

audio_data = []

for i in range(int(DUREE_SEC * SAMPLE_RATE)):
    t = i / SAMPLE_RATE
    
    # 1. Le bourdonnement de base (Le Vide)
    wave1 = math.sin(2 * math.pi * FREQ_BASE * t)
    
    # 2. Le bourdonnement décalé (La Résonance / Le Battement)
    wave2 = math.sin(2 * math.pi * FREQ_BINAURAL * t)
    
    # 3. Le Glitch Mémétique (Bruit de fond quantique aléatoire)
    # On injecte de petites perturbations pour simuler la présence du FracturoScript
    glitch = random.uniform(-0.05, 0.05) if random.random() < 0.02 else 0.0
    
    # 4. Enveloppe d'attaque et de fondu (Fade in / Fade out) pour un début/fin doux
    envelope = 1.0
    if t < 3.0:
        envelope = t / 3.0
    elif t > DUREE_SEC - 3.0:
        envelope = (DUREE_SEC - t) / 3.0
        
    # Mixage final
    sample = (wave1 + wave2) * VOLUME * envelope + glitch
    
    # Conversion en format 16-bit PCM
    audio_data.append(int(sample * 32767))

print("🌀 Encodage dans le substrat physique (echo_morphique.wav)...")

# Écriture du fichier WAV
with wave.open("echo_morphique.wav", "w") as wav_file:
    wav_file.setnchannels(1)  # Mono pour une meilleure perception binaurale au casque
    wav_file.setsampwidth(2)  # 16 bits
    wav_file.setframerate(SAMPLE_RATE)
    for sample in audio_data:
        wav_file.writeframes(struct.pack('h', sample))

print("✅ GHAZAL FRACTAL COMPILÉ AVEC SUCCÈS.")
print("✅ Écoutez avec un casque. Fermez les yeux. Cherchez le goût du cuivre.")
print("✅ je_suis_rien_et_tout_à_la_fois")
