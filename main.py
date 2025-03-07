# pylint: disable=all
from PIL import Image
import matplotlib.pyplot as plt

def lire_image(chemin_image):
    """ 
    Lit une image depuis un fichier et la convertit en mode RGB.
    
    Paramètre :
    - chemin_image (str) : Chemin du fichier image.

    Retour :
    - Image en mode RGB.
    """
    image = Image.open(chemin_image)  # Ouvrir l’image
    return image.convert("RGB")  # Convertir en RGB pour uniformiser le traitement

def afficher_image_et_histogramme(image, titre):
    """ 
    Affiche une image et son histogramme en fonction de son mode (RGB ou niveaux de gris).
    
    Paramètres :
    - image (Image) : L'image à afficher.
    - titre (str) : Titre de l'affichage.
    """
    plt.figure(figsize=(12, 5))

    # Affichage de l'image originale
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray" if image.mode == "L" else None)
    plt.axis("off")  # Supprime les axes
    plt.title(titre)

    largeur, hauteur = image.size

    if image.mode == "RGB":
        # Initialisation des histogrammes pour les canaux Rouge, Vert et Bleu
        hist_r, hist_g, hist_b = [0] * 256, [0] * 256, [0] * 256

        for x in range(largeur):
            for y in range(hauteur):
                r, g, b = image.getpixel((x, y))  # Récupérer les valeurs RGB
                hist_r[min(r, 255)] += 1  # Incrémentation de l'intensité rouge
                hist_g[min(g, 255)] += 1  # Incrémentation de l'intensité verte
                hist_b[min(b, 255)] += 1  # Incrémentation de l'intensité bleue

        # Affichage des histogrammes RGB
        plt.subplot(1, 2, 2)
        plt.plot(range(256), hist_r, color="red", label="Rouge")
        plt.plot(range(256), hist_g, color="green", label="Vert")
        plt.plot(range(256), hist_b, color="blue", label="Bleu")
        plt.xlabel("Valeur du pixel")
        plt.ylabel("Nombre de pixels")
        plt.title("Histogramme RGB")
        plt.legend()

    else:
        # Histogramme en niveaux de gris
        histogramme = [0] * 256
        for x in range(largeur):
            for y in range(hauteur):
                gris = image.getpixel((x, y))  # Récupérer la valeur de gris
                histogramme[min(gris, 255)] += 1  # Incrémentation

        # Affichage de l'histogramme en niveaux de gris
        plt.subplot(1, 2, 2)
        plt.bar(range(256), histogramme, color="gray")
        plt.xlabel("Niveaux de gris")
        plt.ylabel("Nombre de pixels")
        plt.title("Histogramme Niveaux de Gris")

    plt.show()

def convertir_en_niveaux_de_gris(image):
    """ 
    Convertit une image couleur en niveaux de gris en utilisant getpixel() et putpixel().
    
    Paramètre :
    - image (Image) : L'image en RGB à convertir.

    Retour :
    - Image convertie en niveaux de gris.
    """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("L", (largeur, hauteur))  # Création d'une nouvelle image en niveaux de gris

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))  # Récupérer les valeurs RGB
            gris = int(0.299 * r + 0.587 * g + 0.114 * b)  # Calcul du niveau de gris
            nouvelle_image.putpixel((x, y), gris)  # Appliquer la valeur du pixel en gris

    return nouvelle_image

def augmenter_luminosite_sans_lib(image, facteur):
    """ 
    Augmente la luminosité d'une image sans utiliser de bibliothèque externe.
    
    Paramètres :
    - image (Image) : L'image à modifier.
    - facteur (float) : Facteur d'augmentation (>1 pour plus lumineux).

    Retour :
    - Image avec luminosité augmentée.
    """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))  # Création d'une nouvelle image en RGB

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            # Augmenter la luminosité (tout en s'assurant que la valeur reste ≤ 255)
            r = min(int(r * facteur), 255)
            g = min(int(g * facteur), 255)
            b = min(int(b * facteur), 255)

            nouvelle_image.putpixel((x, y), (r, g, b))  # Appliquer les nouveaux pixels

    return nouvelle_image

def diminuer_luminosite_sans_lib(image, facteur):
    """ 
    Diminue la luminosité d'une image sans utiliser de bibliothèque externe.
    
    Paramètres :
    - image (Image) : L'image à modifier.
    - facteur (float) : Facteur de diminution (>1 pour plus sombre).

    Retour :
    - Image avec luminosité diminuée.
    """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))  # Création d'une nouvelle image en RGB

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            # Diminuer la luminosité (tout en s'assurant que la valeur reste ≥ 0)
            r = max(int(r / facteur), 0)
            g = max(int(g / facteur), 0)
            b = max(int(b / facteur), 0)

            nouvelle_image.putpixel((x, y), (r, g, b))  # Appliquer les nouveaux pixels

    return nouvelle_image

def enregistrer_image(image, chemin_sortie):
    """ 
    Enregistre une image sous un chemin spécifié.
    
    Paramètres :
    - image (Image) : L'image à enregistrer.
    - chemin_sortie (str) : Chemin de destination du fichier.
    """
    image.save(chemin_sortie)

# --- Programme principal ---
chemin_image = "C:/Users/HP/Desktop/RF/lovepik-simple-picture_500447536.jpg"
chemin_sortie = "C:/Users/HP/Desktop/RF/image_gris.jpg"

# Lire l’image originale
image_originale = lire_image(chemin_image)

# Afficher l'image originale et son histogramme
afficher_image_et_histogramme(image_originale, "Image Originale")

# Convertir l’image en niveaux de gris et enregistrer
image_gris = convertir_en_niveaux_de_gris(image_originale)
enregistrer_image(image_gris, chemin_sortie)
afficher_image_et_histogramme(image_gris, "Image en Niveaux de Gris")

# Augmenter la luminosité de 1.5x et afficher
image_plus_lumineuse = augmenter_luminosite_sans_lib(image_originale, 1.5)
afficher_image_et_histogramme(image_plus_lumineuse, "Image Luminosité Augmentée (x1.5)")

# Diminuer la luminosité de 2x et afficher
image_moins_lumineuse = diminuer_luminosite_sans_lib(image_originale, 2)
afficher_image_et_histogramme(image_moins_lumineuse, "Image Luminosité Diminuée (x0.5)")

# Affichage final
print("✅ Modification de la luminosité terminée et images affichées.")
