# Image Processing with Histogram Analysis
This project is a simple image processing tool that performs various transformations on an image, including:

📖 Description 

✅ Grayscale conversion

✅ Brightness adjustment (increase & decrease)

✅ Detailed histogram visualization for RGB and grayscale images

The project does not rely on external libraries for image manipulation, except for PIL (Pillow) to read and display images.

🚀 Features 

** Load an image and convert it to RGB format.

** Convert an image to grayscale using custom pixel manipulation.

** Adjust brightness manually (increase or decrease) using mathematical operations on pixel values.

** Display the original image and processed versions with their respective histograms.

** Generate detailed histograms where each pixel's intensity is plotted using plt.scatter().

📂 Project Structure

📁 ImageProcessingProject  

│── 📜 main.py                 # Main script to run the program  
│── 📜 README.md               # Project description (this file)  
│── 📜 requirements.txt        # Dependencies (only Pillow & Matplotlib)  
│── 📁 images/                 # Folder for storing input/output images  
│── 📁 results/                # Processed images saved here  

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/image-processing.git

cd image-processing

2️⃣ Install dependencies

pip install pillow matplotlib

3️⃣ Run the program

python main.py
