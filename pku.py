import pkuseg
seg = pkuseg.pkuseg(model_name='mixed')  # 指定古汉语模型
text = "北冥有鱼其名为鲲鲲之大不知其几千里也化而为鸟其名为鹏鹏之背不知其几千里也怒而飞其翼若垂天之云是鸟也海运则将徙于南冥南冥者天池也齐谐者志怪者也谐之言曰鹏之徙于南冥也水击三千里抟扶摇而上者九万里去以六月息者也"
print(seg.cut(text))

# 分词模型。不能运行：

# Traceback (most recent call last):
#  File "/Users/***/pku.py", line 2, in <module>
#    seg = pkuseg.pkuseg(model_name='mixed')  # 指定古汉语模型
#  File "/opt/homebrew/lib/python3.13/site-packages/pkuseg/__init__.py", line 241, in __init__
#    self.feature_extractor = FeatureExtractor.load()
#                             ~~~~~~~~~~~~~~~~~~~~~^^
#  File "pkuseg/feature_extractor.pyx", line 625, in pkuseg.feature_extractor.FeatureExtractor.load
# FileNotFoundError: [Errno 2] No such file or directory: 'mixed/unigram_word.txt'