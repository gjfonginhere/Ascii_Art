import os
from test import ascii_art

# inputfile 放置图片的目录，outputfile放置处理后的图片的目录
def pTov(inputfile,outputfile):
    # 没有输出目录就创建一个输出目录
    if not os.path.exists(outputfile):
        os.makedirs(outputfile)
    # 设置路径

    for filename in os.listdir(inputfile):
        if filename.endswith('.jpg'):
            input_path = os.path.join(inputfile,filename)
            processed_image = ascii_art(input_path)
            output_path = os.path.join(outputfile,filename)
            processed_image.save(output_path)


    print("已完成程序")

pTov("input","output")


