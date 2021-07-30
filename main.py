import os, sys, time
from functions import pdf,image,video

def main():
    if len(sys.argv) > 0:
        in_dir = sys.argv[1]
        out_dir = sys.argv[2]
        def scan_files():
            for file in os.listdir(in_dir):
                print(file)
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                    image.image(file,in_dir,out_dir)
                elif file.endswith('.pdf'):
                    pdf.pdf(file,in_dir,out_dir)
                elif file.endswith('.mp4'):
                    video.video(file,in_dir,out_dir)
            time.sleep(1)
            scan_files()
        scan_files()
        
    else:
        print('error: please input command line args (1: in dir path) (2: out dir path)')
        return

if __name__ == "__main__":
    try:
        main()
    except:
        print('the code has failed, this is likely due to dependencies or command line tools not being installed')