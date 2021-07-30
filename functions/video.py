import time,os
def video(file,in_dir,out_dir):
    os.popen('ffmpeg -i ' + in_dir + '/' + file + ' -b 800k ' + out_dir + '/' + file)
    while file not in os.listdir(out_dir):
        print('sleeping')
        time.sleep(.2)

    os.remove(in_dir + '/' + file)
    
    return
    





    
