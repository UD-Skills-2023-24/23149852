import os

def rename_png_images(directory, start_number):
    # 获取指定目录下的所有文件，并过滤出PNG图片，然后按文件名排序
    files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.png')])
    i = start_number
    
    for filename in files:
        # 构建新的文件名和旧的文件路径
        new_filename = f"{i}.png"  # 格式为数字.png
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # 重命名文件
        os.rename(old_file, new_file)
        print(f"Renamed {old_file} to {new_file}")
        i += 1

if __name__ == '__main__':
    # 输入目录路径
    target_directory = 'D:/UD/ddl5.9/ML/pix2pixbefore/train' 
    start_num = 0 # 起始编号设为0

    # 调用函数
    rename_png_images(target_directory, start_num)
   