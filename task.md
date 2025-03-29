# 🚀 Liste des tâches pour le projet **Numa**

## 1. Initialisation du projet
- [X] Créer un dépôt GitHub pour Numa
- [X] Définir les objectifs du projet (fonctionnalités, comportement, etc.)
- [X] Choisir et configurer un environnement de développement (Python, dépendances, outils)

## 2. Mise en place de la **Reconnaissance Vocale en Temps Réel (Whisper + VAD)**
- [X] Installer `faster-whisper` pour la transcription vocale locale
- [X] Installer et configurer `Silero VAD` pour la détection de silence
- [X] Tester la reconnaissance vocale avec un fichier audio de test
- [X] Implémenter la gestion des flux audio pour un traitement en temps réel (transcription en quasi temps réel utilisée au final)
    => un flux live via sounddevice
       un buffer intelligent avec queue
       une détection de début/fin de phrase avec VAD
       un déclenchement auto de la transcription

## 3. Mise en place de la **Synthèse Vocale (TTS)**
- [X] Choisir un moteur TTS (Coqui TTS, VITS, pyttsx3, etc.) => j'ai choisi Coqui TTS
- [ ] Installer et configurer le moteur TTS
- [ ] Tester la génération de voix avec du texte de test
- [ ] Créer une voix personnalisée (ou utiliser un modèle existant) et ajuster l’intonation/sarcasme

## 4. Mise en place de l’**Intégration LLM Local (Nous Hermes 2 / Mistral)**
- [ ] Choisir un LLM local (GPT4All, Nous Hermes, Mistral 7B)
- [ ] Installer et configurer le LLM pour répondre aux requêtes
- [ ] Ajouter un **système de mémoire contextuelle** (en utilisant le modèle de LLM)
- [ ] Tester la génération de réponses cohérentes et adaptées

## 5. Création de la **Personnalité de Numa**
- [ ] Définir la personnalité de Numa (sarcastique, humoristique, utile)
- [ ] Écrire des **system prompts** pour définir un ton spécifique
- [ ] Tester la cohérence et le ton des réponses

## 6. Mise en place de la **Mémoire Persistante (JSON-based)**
- [ ] Créer un fichier de mémoire local (JSON ou SQLite)
- [ ] Définir les éléments que Numa doit retenir (nom, préférences, amis, etc.)
- [ ] Créer une fonction qui met à jour la mémoire après chaque échange

## 7. Création du **Modular Memory Manager**
- [ ] Créer un gestionnaire de mémoire modulaire (`memory_manager.py`)
- [ ] Ajouter un système de **scoring** pour la mémoire (enregistrer l’importance des informations)
- [ ] Assurer la mise à jour automatique de la mémoire après chaque échange vocal
- [ ] Injecter la mémoire long terme dans le prompt du LLM pour personnaliser les réponses

## 8. Création de l’**Interface Utilisateur**
- [ ] Choisir un framework d’interface (Streamlit ou PyQt)
- [ ] Créer une interface simple pour interagir avec Numa (entrée vocale + affichage des réponses)
- [ ] Ajouter une interface graphique ou en ligne de commande pour tester les réponses

## 9. Mise en place de la **Modulation de Réponse en Fonction de l’Humeur** (basée sur le contexte)
- [ ] Définir des règles pour moduler les réponses en fonction du ton et de l’humeur
- [ ] Ajouter un système de **réponses contextuelles adaptées** (plus sarcastiques si l’utilisateur préfère, plus douces sinon)
- [ ] Tester la variation de l’humeur dans les réponses selon les demandes

## 10. **Injection de la Mémoire Long Terme dans les Prompts**
- [ ] Créer une fonction pour **injecter la mémoire long terme** (ce que Numa sait sur toi et tes habitudes) dans les prompts du LLM
- [ ] Ajouter un système pour **résumer automatiquement** la mémoire au début de chaque nouvelle conversation
- [ ] Tester l’efficacité de l’injection de mémoire dans les réponses du LLM

## 11. Création du **Système d'Activation Vocale (Hotword Detection)**
- [ ] Installer un moteur de détection de hotword (ex : `Porcupine` ou `snowboy`)
- [ ] Ajouter une fonctionnalité de **détection vocale** pour activer Numa à tout moment
- [ ] Tester l’activation vocale en mode background pour démarrer les interactions

## 12. **Fine-tuning de la Voix de Numa**
- [ ] Collecter des enregistrements de voix (si besoin, ton propre) pour **fine-tuner** un modèle TTS
- [ ] Fine-tuner le modèle TTS pour que la voix de Numa soit unique (sarcastique, chaleureuse, etc.)
- [ ] Tester la qualité de la voix générée et l’ajuster selon les retours

## 13. **Tests et Optimisations**
- [ ] Tester Numa dans des conditions réelles (capture audio, réponse, personnalité)
- [ ] Optimiser les performances pour éviter le **lag** dans les réponses
- [ ] Tester les interactions vocales avec plusieurs utilisateurs (si possible)
- [ ] Résoudre les bugs et ajuster les réponses humoristiques/sarcastiques

## 14. **Déploiement Local et Documentation**
- [ ] Préparer un script d’installation (avec instructions pour l’installation locale des dépendances)
- [ ] Mettre à jour le README avec des instructions détaillées sur l’utilisation et la personnalisation
- [ ] Ajouter un fichier de licence `LICENSE.md` (Creative Commons BY-NC 4.0)
- [ ] Rédiger une documentation expliquant l’architecture du projet et la personnalisation de Numa

## 15. **Extensions futures (facultatif)**
- [ ] Connecter Numa à un serveur Discord pour répondre via des canaux vocaux
- [ ] Ajouter des fonctionnalités comme la gestion des tâches, des rappels, ou de l’ambiance musicale
- [ ] Fine-tuner Numa pour des situations spécifiques (ex : assistant personnel pour un projet donné)

## 16. **Tests finaux et déploiement**
- [ ] Tester le projet dans son intégralité, y compris les fonctionnalités vocales et de personnalité
- [ ] Préparer une version stable pour le partage (éviter les dépendances trop spécifiques)
- [ ] Publier le projet sur GitHub avec un bon README, une licence et des exemples d’utilisation

---

## 🎯 Objectifs à court terme :
1. Fonctionnalité de reconnaissance vocale et génération de texte
2. Implémentation d’une personnalité sarcastique et utile
3. Définir un fichier de mémoire persistant pour une évolution cohérente
