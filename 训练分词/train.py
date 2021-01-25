import pkuseg

pkuseg.train('./firstStageTxt.txt', 'D:\数据\第一阶段文本.txt', './models')
# 训练文件为'msr_training.utf8'，测试文件为'msr_test_gold.utf8'，模型存到'./models'目录下，开20个进程训练模型
