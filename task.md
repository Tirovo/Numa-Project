# 🚀 Liste des tâches pour le projet **Numa**

## 1. Initialisation du projet
- [ ] Créer un dépôt GitHub pour Numa
- [ ] Définir les objectifs du projet (fonctionnalités, comportement, etc.)
- [ ] Choisir et configurer un environnement de développement (Python, dépendances, outils)

## 2. Mise en place de la **Reconnaissance Vocale (STT)**
- [ ] Installer `faster-whisper` pour la transcription vocale locale
- [ ] Tester la reconnaissance vocale avec un fichier audio de test
- [ ] Intégrer `Silero VAD` pour la détection de silence et la gestion du flux audio

## 3. Mise en place de la **Synthèse Vocale (TTS)**
- [ ] Choisir un moteur TTS (Coqui TTS, VITS, pyttsx3, etc.)
- [ ] Installer et configurer le moteur TTS
- [ ] Tester la génération de voix avec du texte de test
- [ ] Créer une voix personnalisée (ou utiliser un modèle existant) et ajuster l’intonation/sarcasme

## 4. Mise en place du **Modèle de Langage Local (LLM)**
- [ ] Choisir un LLM (GPT4All, Mistral, Nous Hermes)
- [ ] Installer et configurer le LLM local (via `llama.cpp` ou `GPT4All`)
- [ ] Intégrer le modèle pour qu’il réponde à des requêtes simples

## 5. Création de la **Personnalité de Numa**
- [ ] Définir la personnalité de Numa (sarcastique, humoristique, utile)
- [ ] Écrire des **system prompts** pour donner un ton spécifique à Numa
- [ ] Tester la cohérence et le ton des réponses

## 6. Intégration de la **Mémoire**
- [ ] Créer un fichier de mémoire local (JSON ou SQLite)
- [ ] Définir les éléments que Numa doit retenir (nom, préférences, amis, etc.)
- [ ] Créer une fonction qui met à jour la mémoire après chaque échange
- [ ] Assurer l’évolution de la personnalité basée sur la mémoire

## 7. Création de la **Structure du Projet**
- [ ] Organiser les fichiers et dossiers du projet (`/core`, `/llm`, `/tts`, `/memory`, etc.)
- [ ] Mettre en place un fichier `requirements.txt` avec toutes les dépendances
- [ ] Ajouter un fichier `.gitignore` pour ignorer les fichiers volumineux comme les modèles

## 8. **Interface Utilisateur**
- [ ] Choisir un framework d’interface (Streamlit ou PyQt)
- [ ] Créer une interface simple pour interagir avec Numa (entrée vocale + affichage des réponses)
- [ ] Ajouter une interface graphique ou en ligne de commande pour tester les réponses

## 9. **Tests et Optimisations**
- [ ] Tester Numa dans des conditions réelles (capture audio, réponse, personnalité)
- [ ] Optimiser les performances pour éviter le **lag** dans les réponses
- [ ] Tester les interactions vocales avec plusieurs utilisateurs (si possible)
- [ ] Résoudre les bugs et ajuster les réponses humoristiques/sarcastiques

## 10. **Déploiement local et Documentation**
- [ ] Préparer un script d’installation (avec instructions pour l’installation locale des dépendances)
- [ ] Mettre à jour le README avec des instructions détaillées sur l’utilisation et la personnalisation
- [ ] Ajouter un fichier de licence `LICENSE.md` (Creative Commons BY-NC 4.0)
- [ ] Rédiger une documentation expliquant l’architecture du projet et la personnalisation de Numa

## 11. **Extensions futures (facultatif)**
- [ ] Connecter Numa à un serveur Discord pour répondre via des canaux vocaux
- [ ] Ajouter des fonctionnalités comme la gestion des tâches, des rappels, ou de l’ambiance musicale
- [ ] Fine-tuner Numa pour des situations spécifiques (ex : assistant personnel pour un projet donné)

## 12. **Tests finaux et déploiement**
- [ ] Tester le projet dans son intégralité, y compris les fonctionnalités vocales et de personnalité
- [ ] Préparer une version stable pour le partage (éviter les dépendances trop spécifiques)
- [ ] Publier le projet sur GitHub avec un bon README, une licence et des exemples d’utilisation

---

## 🎯 Objectifs à court terme :
1. Fonctionnalité de reconnaissance vocale et génération de texte
2. Implémentation d’une personnalité sarcastique et utile
3. Définir un fichier de mémoire persistant pour une évolution cohérente

