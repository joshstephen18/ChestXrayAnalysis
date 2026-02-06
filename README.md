Chest X-ray Pneumonia Analysis 

Project Description: This project analyzes chest X-ray images to compare normal lungs with lungs affected by pneumonia using Python. It calculates quantitative features such as mean intensity, standard deviation, and edge density to highlight structural and brightness differences between the two classes. The results are visualized with edge maps and boxplots, demonstrating clinically meaningful trends in lung opacity and tissue structure.

Methods: A total of 10 chest X-ray images (5 normal and 5 pneumonia) were loaded in grayscale using Python and OpenCV. For each image, the program calculates mean pixel intensity, standard deviation, and edge density (via Canny edge detection) to quantify brightness, contrast, and structural clarity. The program also calculates an average of each metric from all the normal images and all the pneumonia images. Visualizations include original images with edges as well as boxplots to compare the two classes across all metrics.

Results:

Normal Single Example- normal5.jpeg:
Mean intensity: 103.17,
Std intensity: 65.65,
Edge density: 0.7990

Pneumonia Single Example- pneumonia5.jpeg:
Mean intensity: 167.46,
Std intensity: 33.16,
Edge density: 0.1945



Average Statistics (for 5 normal and 5 pneumonia xray images):

-Normal Lungs - Mean intensity: 115.03, Std intensity: 61.46, Edge density: 0.7032
    
-Pneumonia lungs - Mean intensity: 142.64, Std intensity: 51.03, Edge density: 0.6302



Analysis: 
From the statistics and visualizations, we can see that lungs with pneumonia have a higher mean intensity (how bright the image is), a lower standard deviation of intensity (how much contrast or variation there is in pixel brightness), and a lower edge density (fraction of pixels identified as edges) relative to normal lungs. This makes sense clinically as pneumonia can cause fluid accumulation which appears brighter on X-ray, thus reflecting a higher mean intensity. Furthermore, inflammation from pneumonia blurs out normal lung structure on X-ray, so there is less variation in pixel intensity (less contrast) and therefore a lower standard deviation of the intensity. Lastly, since pneumonia X-rays are more blurred and lung structures are less distinct, there are less identifiable edges, and thus a lower edge density.


Libraries used: 
1. OpenCV (cv2) – for loading images and performing edge detection

2. NumPy – for numerical calculations 

3. Matplotlib – for visualization

4. os – for navigating directories and managing file paths








