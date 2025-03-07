#pylint: disable=all
from PIL import Image
import matplotlib.pyplot as plt

def lire_image(chemin_image):
    """ Lit une image et retourne l'objet Image en RGB. """
    image = Image.open(chemin_image)  # Ouvrir l’image
    return image.convert("RGB")  # S'assurer qu'elle est bien en RGB

def afficher_image_et_histogramme(image, titre):
    """ Affiche une image et son histogramme (RGB ou niveaux de gris). """
    plt.figure(figsize=(12, 5))

    # Affichage de l'image
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray" if image.mode == "L" else None)
    plt.axis("off")
    plt.title(titre)

    largeur, hauteur = image.size

    if image.mode == "RGB":
        # Histogramme en RGB
        hist_r, hist_g, hist_b = [0] * 256, [0] * 256, [0] * 256

        for x in range(largeur):
            for y in range(hauteur):
                r, g, b = image.getpixel((x, y))
                hist_r[min(r, 255)] += 1
                hist_g[min(g, 255)] += 1
                hist_b[min(b, 255)] += 1

        # Affichage des trois histogrammes
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
                gris = image.getpixel((x, y))
                histogramme[min(gris, 255)] += 1

        plt.subplot(1, 2, 2)
        plt.bar(range(256), histogramme, color="gray")
        plt.xlabel("Niveaux de gris")
        plt.ylabel("Nombre de pixels")
        plt.title("Histogramme Niveaux de Gris")

    plt.show()

def convertir_en_niveaux_de_gris(image):
    """ Convertit une image en niveaux de gris en utilisant getpixel() et putpixel(). """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("L", (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            gris = int(0.299 * r + 0.587 * g + 0.114 * b)
            nouvelle_image.putpixel((x, y), gris)

    return nouvelle_image

def augmenter_luminosite_sans_lib(image, facteur):
    """ Augmente la luminosité de l'image sans utiliser de bibliothèque externe. """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            # Augmenter la luminosité
            r = min(int(r * facteur), 255)
            g = min(int(g * facteur), 255)
            b = min(int(b * facteur), 255)

            nouvelle_image.putpixel((x, y), (r, g, b))

    return nouvelle_image

def diminuer_luminosite_sans_lib(image, facteur):
    """ Diminue la luminosité de l'image sans utiliser de bibliothèque externe. """
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))

    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))

            # Diminuer la luminosité
            r = max(int(r / facteur), 0)
            g = max(int(g / facteur), 0)
            b = max(int(b / facteur), 0)

            nouvelle_image.putpixel((x, y), (r, g, b))

    return nouvelle_image

def enregistrer_image(image, chemin_sortie):
    """ Enregistre une image. """
    image.save(chemin_sortie)

# --- Programme principal ---
chemin_image = "C:/Users/HP/Desktop/RF/lovepik-simple-picture_500447536.jpg"
chemin_sortie = "C:/Users/HP/Desktop/RF/image_gris.jpg"

# Lire l’image originale
image_originale = lire_image(chemin_image)

# Afficher l'image originale et son histogramme
afficher_image_et_histogramme(image_originale, "Image Originale")

# Convertir l’image en niveaux de gris
image_gris = convertir_en_niveaux_de_gris(image_originale)
enregistrer_image(image_gris, chemin_sortie)
afficher_image_et_histogramme(image_gris, "Image en Niveaux de Gris")

# Augmenter la luminosité de 1.5x
image_plus_lumineuse = augmenter_luminosite_sans_lib(image_originale, 1.5)
afficher_image_et_histogramme(image_plus_lumineuse, "Image Luminosité Augmentée (x1.5)")

# Diminuer la luminosité de 2x
image_moins_lumineuse = diminuer_luminosite_sans_lib(image_originale, 2)
afficher_image_et_histogramme(image_moins_lumineuse, "Image Luminosité Diminuée (x0.5)")
# Afficher les images modifiées
print("✅ Modification de la luminosité terminée et images affichées.")
