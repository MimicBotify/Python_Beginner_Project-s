# Move file automatically
import os
import glob
from time import sleep

# Change the current directory path
directory = "C:\\Users\\DELL\\OneDrive\\Desktop\\Drop"
mp3_files = glob.glob(os.path.join(directory, "*.mp3"))
mp4_files = glob.glob(os.path.join(directory, "*.mp4"))
pattern = ['*.jpg', '*.jpeg', '*.png', '*.gif']
img_file = []
img_file = img_file.extend(glob.glob(os.path.join(directory, pattern)))


def moving_files():
    # Change the destination path with your desired folder
    mp3_destination_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\Drop\\Music'
    mp4_destination_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\Drop\\Video'
    img_destination_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\Drop\\Photo'
    while True:
        for mp3 in mp3_files:
            try:
                file_name = os.path.basename(mp3)
                mp3_destination_dir = os.path.join(mp3_destination_path, file_name)
                os.rename(mp3, mp3_destination_dir)
            except Exception as e:
                print(f"Error moving {mp3}: {str(e)}")
        for mp4 in mp4_files:
            try:
                file_name = os.path.basename(mp4)
                mp4_destination_dir = os.path.join(mp4_destination_path, file_name)
                os.rename(mp4, mp4_destination_dir)
            except Exception as e:
                print(f"Error moving {mp4}: {str(e)}")
        for img in img_file:
            try:
                file_name = os.path.basename(img)
                img_destination_dir = os.path.join(img_destination_path, file_name)
                os.rename(img, img_destination_dir)
            except Exception as e:
                print(f"Error moving {img}: {str(e)}")
        sleep(60)


if __name__ == '__main__':
    moving_files()

