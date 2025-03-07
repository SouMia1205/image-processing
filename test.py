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

def afficher_images_et_histogrammes(image1, titre1, image2, titre2):
    """ 
    Affiche deux images et leurs histogrammes détaillés côte à côte.
    
    Paramètres :
    - image1 (Image) : Première image à afficher.
    - titre1 (str) : Titre de la première image.
    - image2 (Image) : Deuxième image à afficher.
    - titre2 (str) : Titre de la deuxième image.
    """
    plt.figure(figsize=(12, 6))

    # Affichage de la première image
    plt.subplot(2, 2, 1)
    plt.imshow(image1, cmap="gray" if image1.mode == "L" else None)
    plt.axis("off")  # Supprime les axes
    plt.title(titre1)

    # Histogramme détaillé de la première image
    plt.subplot(2, 2, 2)
    afficher_histogramme_detaille(image1)

    # Affichage de la deuxième image
    plt.subplot(2, 2, 3)
    plt.imshow(image2, cmap="gray" if image2.mode == "L" else None)
    plt.axis("off")  # Supprime les axes
    plt.title(titre2)

    # Histogramme détaillé de la deuxième image
    plt.subplot(2, 2, 4)
    afficher_histogramme_detaille(image2)

    plt.tight_layout()  # Ajuste automatiquement la disposition pour éviter le chevauchement
    plt.show()

def afficher_histogramme_detaille(image):
    """ 
    Affiche un histogramme détaillé en affichant chaque pixel avec plt.scatter().
    
    Paramètre :
    - image (Image) : L'image pour laquelle afficher l'histogramme.
    """
    largeur, hauteur = image.size

    valeurs_pixels = []
    frequences = [0] * 256  # Stocke la fréquence de chaque valeur de pixel (0-255)

    # Calcul de l'histogramme détaillé
    if image.mode == "RGB":
        for x in range(largeur):
            for y in range(hauteur):
                r, g, b = image.getpixel((x, y))  # Obtenir les valeurs RGB
                intensite = int(0.299 * r + 0.587 * g + 0.114 * b)  # Conversion en niveaux de gris
                valeurs_pixels.append(intensite)
                frequences[intensite] += 1  # Incrémenter la fréquence du pixel

    else:  # Si l'image est déjà en niveaux de gris
        for x in range(largeur):
            for y in range(hauteur):
                intensite = image.getpixel((x, y))  # Récupérer la valeur de gris
                valeurs_pixels.append(intensite)
                frequences[intensite] += 1  # Incrémenter la fréquence du pixel

    # Affichage sous forme de points (chaque pixel est un point sur le graphique)
    plt.scatter(range(256), frequences, color="black", s=10)
    plt.xlabel("Valeurs des pixels (0-255)")
    plt.ylabel("Nombre de pixels")
    plt.title("Histogramme DÉTAILLÉ des pixels")
    plt.grid(True)

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

def ajuster_luminosite(image, facteur):
    """ 
    Ajuste la luminosité d'une image sans utiliser de bibliothèque externe.
    
    Paramètres :
    - image (Image) : L'image à modifier.
    - facteur (float) : Facteur d'ajustement (>1 pour augmenter la luminosité, <1 pour diminuer).

    Retour :
    - Image avec luminosité ajustée.
    """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))  # Création d'une nouvelle image en RGB

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            # Ajuster la luminosité (en s'assurant que les valeurs restent dans [0,255])
            r = min(max(int(r * facteur), 0), 255)
            g = min(max(int(g * facteur), 0), 255)
            b = min(max(int(b * facteur), 0), 255)

            nouvelle_image.putpixel((x, y), (r, g, b))  # Appliquer les nouveaux pixels

    return nouvelle_image

# --- Programme principal ---
chemin_image = "C:/Users/HP/Desktop/RF/lovepik-simple-picture_500447536.jpg"

# Lire l’image originale
image_originale = lire_image(chemin_image)

# Convertir l’image en niveaux de gris
image_gris = convertir_en_niveaux_de_gris(image_originale)

# Augmenter et diminuer la luminosité
image_plus_lumineuse = ajuster_luminosite(image_originale, 1.5)  # +50% de luminosité
image_moins_lumineuse = ajuster_luminosite(image_originale, 0.5)  # -50% de luminosité

# Afficher l'image originale et en niveaux de gris avec leurs histogrammes détaillés
afficher_images_et_histogrammes(image_originale, "Image Originale", image_gris, "Image en Niveaux de Gris")

# Afficher l'image avec luminosité augmentée et diminuée avec leurs histogrammes détaillés
afficher_images_et_histogrammes(image_plus_lumineuse, "Image Luminosité Augmentée", image_moins_lumineuse, "Image Luminosité Diminuée")

# Affichage final
print("✅ Toutes les modifications sont affichées avec leurs histogrammes détaillés.")
