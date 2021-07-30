from dependencies import pdf_compressor

def pdf(file,in_dir,out_dir):
    try:
        pdf_compressor.compress(in_dir + '/' + file, out_dir + '/' + file)
    except:
        print('error compressing pdf, issue may be relate to ghostscript that needs to be installed')


