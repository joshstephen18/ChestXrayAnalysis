#import the needed libraries
import cv2          # For image loading and processing
import numpy as np
import matplotlib.pyplot as plt
import os           # For reading files from folders

#paths to folders
normal_folder = "chest_xray/train/NORMAL"
pneumonia_folder = "chest_xray/train/PNEUMONIA"

#select first 5 images from each folder
normal_images = os.listdir(normal_folder)[:5]   #.listdir returns the names of everything inside folder
pneumonia_images = os.listdir(pneumonia_folder)[:5]

print("Normal images:", normal_images)
print("Pneumonia images:", pneumonia_images)

#function to analyze a single image
#prepare image by converting to grayscale
def analyze_image(img_path, label):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    #get the metrics
    mean_intensity = np.mean(img)
    std_intensity = np.std(img)
    edges = cv2.Canny(img, 100, 200) #.canny(image, threshold 1, threshold 2) used for edge detection
    #pixels below threshold 1 are discarded. pixels between the thresholds are only kept if connected to a strong edge. Pixels above threshold 2 are kept.
    edge_density = np.sum(edges) / edges.size
                   #np.sum(edges) adds up pixel values. Edge pixels have value of 255 (white). Non-edge has value of 0 (black).
                   #.size returns total # of pixels in the image

    #print metrics
    print(f"{label} - {os.path.basename(img_path)}") #os.path.basename() strips away folder names and returns only the filename
    print(f"Mean intensity: {mean_intensity:.2f}") # :.2f means format it with 2 decimal places
    print(f"Std intensity: {std_intensity:.2f}")
    print(f"Edge density: {edge_density:.4f}\n")

    #plot original image
    plt.figure(figsize = (10,4))  #figsize is (width, height)
    plt.subplot(1,2,1) #plt.subplot divides figure into grid and uses (nrows, ncolumns, index)
    plt.imshow(img, cmap='gray') #'gray' means low values are black and high values are white
    plt.title(f"{label} X-ray")
    plt.axis('off')  #hides the x and y axes

    #plot for edges
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title(f"{label} Edges")
    plt.axis('off')
    plt.show()

    return mean_intensity, std_intensity, edge_density

#analyze 3 images for normal and 3 images for pneumonia
normal_stats = []
pneumonia_stats = []

print ("Normal Images")
for img_file in normal_images:
    img_path = os.path.join(normal_folder, img_file) #os.path.join combines the folder path and file name into one full path
    normal_stats.append(analyze_image(img_path, "Normal"))

print ("Pneumonia Images")
for img_file in pneumonia_images:
    img_path = os.path.join(pneumonia_folder, img_file)
    pneumonia_stats.append(analyze_image(img_path, "Pneumonia"))

#calculate average stats
normal_stats = np.array(normal_stats) #np.array converts the list of tuples to a numpy array for average operations
pneumonia_stats = np.array(pneumonia_stats)

print("Average Statistics")
print(f"Normal Lungs - Mean intensity: {np.mean(normal_stats[:,0]):.2f}, Std intensity: {np.mean(normal_stats[:,1]):.2f}, Edge density: {np.mean(normal_stats[:,2]):.4f}")
                                #slicing here is 2D not 1D. So use comma. before comma is which rows and after the comma is which columns
print(f"Pneumonia lungs - Mean intensity: {np.mean(pneumonia_stats[:,0]):.2f}, Std intensity: {np.mean(pneumonia_stats[:,1]):.2f}, Edge density: {np.mean(pneumonia_stats[:,2]):.4f}")



#create visual comparison with boxplots to show side by side differences between normal and pneumonia lungs
labels = ['Normal', 'Pneumonia']

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.boxplot([normal_stats[:,0], pneumonia_stats[:,0]], labels=labels) #all rows, column 0
plt.title("Mean Intensity")
plt.ylabel("Pixel Value")

plt.subplot(1,3,2)
plt.boxplot([normal_stats[:,1], pneumonia_stats[:,1]], labels=labels) #all rows, column 1
plt.title("Standard Deviation")
plt.ylabel("Pixel Value")

plt.subplot(1,3,3)
plt.boxplot([normal_stats[:,2], pneumonia_stats[:,2]], labels=labels) #all rows, column 2
plt.title("Edge Density")
plt.ylabel("Fraction of Edge Pixels")

plt.suptitle("Comparison of Normal vs Pneumonia X-rays")
plt.show()


















