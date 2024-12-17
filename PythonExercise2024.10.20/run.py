import os
import cv2
import sys
# 以上为依赖包引入部分, 请根据实际情况引入
# 引入的包需要安装的, 请在requirements.txt里列明, 最好请列明版本

# 以下为逻辑函数, main函数的入参和最终的结果输出不可修改
def main(to_pred_dir, result_save_path):
    run_py = os.path.abspath(__file__)
    model_dir = os.path.dirname(run_py) # 当前文件夹路径

    dirpath = os.path.abspath(to_pred_dir)
    filepath = os.path.join(dirpath, '') # 测试集文件夹路径
    task_lst = os.listdir(filepath)

    # 初始化结果文件，定义表头，也就是最后需要输出的.csv文件
    res = ['img_name, label']
    for task_name in task_lst:  # 循环task文件夹

        # 支持集路径（文件夹名即为标签）  这个就相当于训练集
        support_path = os.path.join(filepath, task_name, 'support')
        # 查询集路径（无标签，待预测图片） 这个就相当于测试集
        query_path = os.path.join(filepath, task_name, 'query')
        class_id = os.listdir(support_path)  # 支持集标签
        """
        可以对支持集数据进行一定的特征提取等操作
        """
        # 预测
        # 循环遍历每个任务文件夹
        test_img_lst = []
        # 遍历查询集中每个以.png结尾的文件，并加入test_img_list列表中
        for name in os.listdir(query_path):
            if name.endswith('.png'):
                test_img_lst.append(name)

        # 遍历这些test文件，主要是为了得到图片的路径
        for image_path in test_img_lst:
            # 将图片的路径和测试集的路径拼接出一个完整的路径
            name_img = os.path.join(query_path, image_path)
            # opencv读取图片
            # test_image = cv2.imread(name_img)
            # test_image = cv2.resize(test_image, (224, 224), interpolation=cv2.INTER_NEAREST)
            pred_class = '1'  # 这里指定了一个值代替预测值，选手需要根据自己模型进行实际的预测
            # 将图片文件名和预测结果拼接成一个字符串并加入res
            res.append(image_path + ',' + pred_class)

    # 将预测结果保存到result_save_path
    with open(result_save_path, 'w') as f:
        f.write('\n'.join(res))

if __name__ == "__main__":
    # ！！！以下内容不允许修改，修改会导致评分出错
    to_pred_dir = sys.argv[1]  # 所需预测的文件夹路径
    result_save_path = sys.argv[2]  # 预测结果保存文件路径，已指定格式为csv
    main(to_pred_dir, result_save_path)