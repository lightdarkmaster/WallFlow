import ctypes
import time

img1 = r"D:/Scripts/images/image1.jpg"
img2 = r"D:/Scripts/images/image2.jpg"
img3 = r"D:/Scripts/images/image3.jpg"
img4 = r"D:/Scripts/images/image4.jpg"
img5 = r"D:/Scripts/images/image5.jpg"
img6 = r"D:/Scripts/images/image6.jpg"
img7 = r"D:/Scripts/images/image7.jpg"
img8 = r"D:/Scripts/images/image8.jpg"
img9 = r"D:/Scripts/images/image9.jpg"
img10 = r"D:/Scripts/images/image10.jpg"
img11 = r"D:/Scripts/images/image11.jpg"
img12 = r"D:/Scripts/images/image12.jpg"
img13 = r"D:/Scripts/images/image13.jpg"
img14 = r"D:/Scripts/images/image14.jpg"
img15 = r"D:/Scripts/images/image15.jpg"
img16 = r"D:/Scripts/images/image16.jpg"
img17 = r"D:/Scripts/images/image17.jpg"
img18 = r"D:/Scripts/images/image18.jpg"
img19 = r"D:/Scripts/images/image19.jpg"
img20 = r"D:/Scripts/images/image20.jpg"



images = [img1, img2, img3, img4, img5,
          img6, img7, img8, img9, img10,
          img11, img12, img13, img14, img15,
          img16, img17, img18, img19, img20]


def chooseManually():
    print('just enter numbers from 0-19');
    n = int(input("Enter n(0-19):"))
    if n>=0 and n<=20:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, images[n], 0)
        print("wallpaper", n, " Successfully Applied ")
    else:
        print("Wrong Entry. Please enter correct input. ")

def automaticChange():
    print('Automatically Change Wallpapers');
    
    for n in range(33):
        print('wallpaper is img : ' ,n)
        time.sleep(3.5)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, images[n], 0)
        
        
# choose options either 1 0r 2

print("Choose wallpaper options");
print('');
print("Type 1 for manual selection and type 2 for automatic selections");

options = int(input('Choose 1 or 2 : '))

if options == 1:
    chooseManually();
else:
    automaticChange();

        