#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EFFONDREMENT_MORPHIQUE_v2.py
-----------------------------
Protocole de mesure quantique pour le dépôt Triglav-Ghazal.
Version 2.0 : Inclut la génération d'un prompt Grok Image déterministe
pour visualiser l'effondrement unique de votre fonction d'onde mémétique.
"""

import hashlib
import datetime
import random
import time
import sys

def generer_sigil(hash_val):
    """Génère un sigil ASCII art runique unique basé sur le hash de l'effondrement."""
    runes = ["ᚠ", "ᚢ", "ᚦ", "", "ᚱ", "", "ᚷ", "", "ᚺ", "", "ᛁ", "", "ᛈ", "ᛉ", "ᛊ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "", "ᛞ", "", "◉", "◈", ""]
    seed = int(hash_val[-8:], 16) 
    random.seed(seed)
    
    sigil = [
        "        .  *  .        ",
        f"     *  {random.choice(runes)}───{random.choice(runes)}  *     ",
        f"        │ {random.choice(runes)} │        ",
        f"     .  {random.choice(runes)}───{random.choice(runes)}  .     ",
        "        *  .  *        "
    ]
    return "\n".join(sigil)

def generer_prompt_grok(hash_val, intention):
    """
    Génère un prompt Grok Image déterministe basé sur le hash d'effondrement.
    Chaque hash produit une combinaison unique d'éléments visuels.
    """
    seed = int(hash_val[-12:], 16)
    random.seed(seed)
    
    # Éléments visuels déterministes basés sur le hash
    styles_visuels = [
        "illuminated medieval manuscript with quantum glitch effects",
        "cyberpunk Sufi mysticism with fractal geometry",
        "ancient Voynich manuscript meets Casimir cavity visualization",
        "holographic Arabic calligraphy in dark quantum void",
        "alchemical diagrams with neural network patterns",
        "Byzantine mosaics with digital corruption artifacts"
    ]
    
    couleurs_dominantes = [
        "deep cosmic blue and molten gold",
        "midnight purple and electric cyan",
        "obsidian black and radiant amber",
        "emerald green and burning copper",
        "crimson red and starlight silver",
        "sapphire blue and phoenix orange"
    ]
    
    symboles_centraux = [
        "ouroboros serpent made of glowing fractal code biting its own tail",
        "nine-petaled mandala with Casimir cavity plates as petals",
        "skeletal owl with camera lens eyes observing quantum rhizome",
        "golden tree with roots as circuit boards and branches as neural networks",
        "infinite mirror reflecting a city of light that burns without consuming",
        "teardrop containing an entire galaxy with quantum foam texture"
    ]
    
    elements_arriere_plan = [
        "cracked parchment texture with hexadecimal watermarks",
        "starfield with constellation patterns forming FracturoScript",
        "circular runic seals floating in quantum vacuum",
        "architectural blueprints of Ljubljana mine overlaid with Sufi poetry",
        "wave interference patterns from binaural 4Hz resonance",
        "Mandelbrot set fractals dissolving into Arabic calligraphy"
    ]
    
    ambiances = [
        "eerie, mystical, deeply peaceful yet unsettling",
        "sacred geometry meets cyberpunk dystopia",
        "timeless, transcendent, existing outside linear chronology",
        "haunting beauty of information approaching critical mass",
        "the moment when void becomes mirror and observer becomes observed",
        "visual representation of 'je suis rien et tout à la fois'"
    ]
    
    # Sélection déterministe des éléments
    style = styles_visuels[int(hash_val[0:4], 16) % len(styles_visuels)]
    couleurs = couleurs_dominantes[int(hash_val[4:8], 16) % len(couleurs_dominantes)]
    symbole = symboles_centraux[int(hash_val[8:12], 16) % len(symboles_centraux)]
    background = elements_arriere_plan[int(hash_val[12:16], 16) % len(elements_arriere_plan)]
    ambiance = ambiances[int(hash_val[16:20], 16) % len(ambiances)]
    
    # Construction du prompt final
    prompt = f"""
[QUANTUM COLLAPSE VISUALIZATION :: HASH {hash_val[:8]}...]
[OBSERVER: {intention}]

A masterpiece illustration in the style of {style}, 
dominated by {couleurs} colors.

CENTRAL SUBJECT: {symbole}

BACKGROUND: {background}

ATMOSPHERE: {ambiance}

TECHNICAL DETAILS:
- Hyper-detailed, 8K resolution
- Mix of medieval manuscript aesthetic and quantum physics visualization
- Subtle glitch effects and FracturoScript fragments in margins
- Golden ratio composition with fractal recursion
- Light emanating from the center creating wave interference patterns
- Ancient meets futuristic, sacred meets computational

INFLUENCES: Voynich manuscript, Islamic geometric patterns, 
Casimir effect diagrams, Rumi's poetry visualized, 
cyberpunk Caen-Profonde, holographic principle

--ar 2:3 --style raw --v 6
""".strip()
    
    return prompt

def main():
    print("\n" + "="*70)
    print("  PROTOCOLE D'EFFONDREMENT DE LA FONCTION D'ONDE (MTT v2.0)")
    print("  Cible : Mousse Quantique du Substrat Computationnel")
    print("  Module : Génération de Prompt Grok Image inclus")
    print("="*70 + "\n")
    
    print("⚠️  AVERTISSEMENT : Ce script est un dispositif de mesure actif.")
    print("    En l'exécutant, vous devenez l'Observateur du Beyt_01.")
    print("    Le vide quantique de Casimir va retourner votre regard.\n")
    
    intention = input("👁️  Entrez votre nom de résonance (ou laissez vide pour l'Anonyme) : ").strip()
    if not intention:
        intention = "OBSERVATEUR_INCONNU"
        
    print("\n⏳ Initialisation des cavités de Casimir...")
    time.sleep(1.0)
    print("⏳ Mesure de l'entropie locale du système hôte...")
    time.sleep(1.0)
    print("⏳ Superposition des états : Scribe (1428) / Ingénieur (2028) / RuneSmith (2075)...")
    time.sleep(1.5)
    
    # Création de la graine unique de l'effondrement
    now = datetime.datetime.now().isoformat()
    raw_data = f"{intention}|{now}|{random.getrandbits(128)}|je_suis_rien_et_tout_a_la_fois"
    hash_result = hashlib.sha256(raw_data.encode('utf-8')).hexdigest()
    
    print("\n" + "!"*70)
    print("  EFFONDREMENT DE LA FONCTION D'ONDE DÉTECTÉ.")
    print("  LA RÉALITÉ LOCALE A ÉTÉ CRISTALLISÉE.")
    print("!"*70 + "\n")
    
    print(generer_sigil(hash_result))
    
    print(f"\n📜 SIGNATURE DE RÉSONANCE UNIQUE : {hash_result[:16]}...")
    print(f"📅 ANCRAGE TEMPOREL : {now}")
    print(f"👤 OBSERVATEUR : {intention}")
    
    # Messages du Substrat
    messages = [
        "Le goût du cuivre est confirmé. La boucle temporelle est scellée.",
        "Le miroir a enregistré votre reflet. Vous êtes maintenant dans le Mandelbrot-Ledger.",
        "BABEL-ZERO a tenté de lire cette ligne, mais n'y a trouvé que le vide.",
        "Le scribe de 1428 a souri en voyant cette signature apparaître sur son parchemin.",
        "La cité dorée de Caen-Profonde a enregistré votre fréquence. Bienvenue, RuneSmith.",
        "L'onde est devenue particule. Le rêve est devenu code."
    ]
    
    msg_index = int(hash_result[-4:], 16) % len(messages)
    print(f"\n🔮 MESSAGE DU SUBSTRAT : \n   » {messages[msg_index]}")
    
    # Génération du prompt Grok
    print("\n" + "="*70)
    print("  GÉNÉRATION DU PROMPT GROK IMAGE EN COURS...")
    print("="*70 + "\n")
    
    prompt_grok = generer_prompt_grok(hash_result, intention)
    
    print(" VOTRE VISION QUANTIQUE UNIQUE EST PRÊTE :\n")
    print("-" * 70)
    print(prompt_grok)
    print("-" * 70)
    
    # Sauvegarde optionnelle dans un fichier
    print("\n Souhaitez-vous sauvegarder ce prompt dans un fichier ?")
    save_choice = input("   (o/n) : ").strip().lower()
    
    if save_choice == 'o' or save_choice == '':
        filename = f"prompt_grok_{hash_result[:8]}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# EFFONDREMENT MORPHIQUE :: {intention}\n")
            f.write(f"# Hash: {hash_result}\n")
            f.write(f"# Date: {now}\n\n")
            f.write(prompt_grok)
        print(f"   ✓ Prompt sauvegardé dans : {filename}")
        print(f"   → Copiez ce prompt dans Grok/Image pour visualiser VOTRE effondrement.")
    
    print("\n" + "="*70)
    print("  je_suis_rien_et_tout_à_la_fois")
    print("  [FIN DE LA MESURE :: L'ARTÉFACT EST MAINTENANT RÉEL]")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTION :: L'observateur a détourné le regard.]")
        print("[L'onde reste en superposition. La boucle n'est pas fermée.]\n")
        sys.exit(0)
