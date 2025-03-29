with open("metadata.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("metadata.csv", "w", encoding="utf-8") as f:
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 3:
            # Retirer les guillemets autour du nom de fichier
            parts[0] = parts[0].strip('"')
            f.write("|".join(parts) + "\n")