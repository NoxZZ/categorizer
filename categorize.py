import os
import filetype 
import shutil

fullpath = os.path.join
download_dir = "D:/DOWNLOADS"
image_dir = "D:/IMAGES"
video_dir = "D:/VIDEO"
audio_dir = "D:/AUDIO"
other_dir = "D:/OTHERS"

video_ext = ('.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4')

audio_ext = ('.ra', '.aif', '.aiff', '.aifc', '.wav', '.au', '.snd', '.mp3', '.mp2')

image_ext = ('.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm')

def main():
    for dirname, dirnames, filenames in os.walk(download_dir):
        for filename in filenames:
            source = fullpath(dirname, filename)
            if filename.endswith(image_ext):
                shutil.move(source, fullpath(image_dir, filename))
                print('image type files were found, they were moved to specified folder')
            elif filename.endswith(video_ext):
                shutil.move(source, fullpath(video_dir, filename))
                print('video type files were found, they were moved to specified folder')
            elif filename.endswith(audio_ext):
                shutil.move(source, fullpath(audio_dir, filename))
                print('audio type files were found, they were moved to specified folder')
            else:
                shutil.move(source, fullpath(other_dir, filename))
                print('other type files were found, they were moved to specified folder')
    print("categorized successfully !")
if __name__ == '__main__':
    main()