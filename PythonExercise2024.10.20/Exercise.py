import os
import shutil
import random


def select_random_images(src_folder, dest_folder, num_images):
    # 遍历源文件夹
    for root, dirs, files in os.walk(src_folder):
        # 过滤出图片文件
        images = []
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                images.append(f)

        # 选择图片
        if len(images) <= num_images:
            selected_images = images
        else:
            selected_images = random.sample(images, num_images)

        # 创建目标文件夹路径
        relative_path = os.path.relpath(root, src_folder)
        target_path = os.path.join(dest_folder, relative_path)

        # 创建目标文件夹
        os.makedirs(target_path, exist_ok=True)

        # 复制选中的图片到目标文件夹
        for image in selected_images:
            src_image_path = os.path.join(root, image)
            dest_image_path = os.path.join(target_path, image)
            shutil.copyfile(src_image_path, dest_image_path)


if __name__ == '__main__':
    # 定义源文件夹和目标文件夹
    source_folder = "C:/Users/wzb/Desktop/wzb/Achievement"
    destination_folder = "C:/Users/wzb/Desktop/new"

    # 定义每个文件夹要抽取的图片数量
    num_images = 1

    # 执行图片选择和复制操作
    select_random_images(source_folder, destination_folder, num_images)
