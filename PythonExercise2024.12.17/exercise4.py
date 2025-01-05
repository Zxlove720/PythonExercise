# # 导入所需的库
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
#
#
# #202358234044 吴振博：1. 绘制带有中文标签和图例的正弦和余弦曲线。
# def exercise1():
#     # 设置中文字体
#     plt.rcParams['font.family'] = 'SimHei'
#     plt.rcParams['axes.unicode_minus'] = False
#     t = np.linspace(0, 2 * np.pi, 400)
#     s, z = np.sin(t), np.cos(t)
#     plt.plot(t, s, label='正弦')
#     plt.plot(t, z, label='余弦')
#     plt.title('正弦和余弦曲线')
#     plt.xlabel('角度')
#     plt.ylabel('值')
#     plt.legend()
#     plt.show()
#
#
# #202358234044 吴振博：2. 绘制一个余弦散点图，其中散点大小设置为25，散点符号设置为+，线宽设置为8。
# def exercise2():
#     t = np.linspace(0, 2 * np.pi, 400)
#     z = np.cos(t)
#     plt.scatter(t, z, s=25, marker='+', linewidths=8)
#     plt.title('余弦散点图')
#     plt.xlabel('角度')
#     plt.ylabel('余弦值')
#     plt.show()
#
#
# #202358234044 吴振博：3. 绘制一个散点符号为五角星的散点图，其中颜色为红色，散点大小为横坐标的值乘以600。
# def exercise3():
#     x = np.linspace(0, 10, 50)
#     y = np.random.rand(50)
#     plt.scatter(x, y, s=x * 600, c='red', marker='*')
#     plt.title('自定义散点图')
#     plt.xlabel('横坐标')
#     plt.ylabel('纵坐标')
#     plt.show()
#
#
# #202358234044 吴振博：4. 绘制有描边和填充效果的柱状图，效果自定义。
# def exercise4():
#     x = np.arange(5)
#     y = np.random.rand(5)
#     plt.bar(x, y, edgecolor='black', linewidth=1.5, color='skyblue')
#     plt.title('柱状图')
#     plt.xlabel('类别')
#     plt.ylabel('数值')
#     plt.show()
#
#
# #202358234044 吴振博：5. 使用雷达图展示某个学生的成绩，科目、分数等信息自定义。
# def exercise5():
#     # 定义科目和分数
#     labels = ['语文', '数学', '英语', '物理', '化学']
#     scores = [85, 90, 88, 78, 92]
#     angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
#     scores += scores[:1]
#     angles += angles[:1]
#     fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#     ax.plot(angles, scores, 'o-', linewidth=2)
#     ax.fill(angles, scores, alpha=0.25)
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(labels)
#     plt.title('学生成绩雷达图')
#     plt.show()
#
#
# #202358234044 吴振博：6. 绘制三维曲面，效果自定义。
# def exercise6():
#     from mpl_toolkits.mplot3d import Axes3D
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     X = np.arange(-5, 5, 0.25)
#     Y = np.arange(-5, 5, 0.25)
#     X, Y = np.meshgrid(X, Y)
#     R = np.sqrt(X**2 + Y**2)
#     Z = np.sin(R)
#     surf = ax.plot_surface(X, Y, Z, cmap='viridis')
#     fig.colorbar(surf, shrink=0.5, aspect=5)
#     plt.title('三维曲面图')
#     plt.show()
#
#
# #202358234044 吴振博：7. 绘制三维曲线，效果自定义。
# def exercise7():
#     from mpl_toolkits.mplot3d import Axes3D
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     t = np.linspace(0, 2 * np.pi, 100)
#     x = np.sin(t)
#     y = np.cos(t)
#     z = t
#     ax.plot(x, y, z, c='r')
#     plt.title('三维曲线图')
#     plt.show()
#
#
# if __name__ == "__main__":
#     # exercise1()
#     # exercise2.py()
#     # exercise3()
#     # exercise4()
#     # exercise5()
#     # exercise6()
#     exercise7()

number1 = int(11.9999)
print(number1, type(number1))