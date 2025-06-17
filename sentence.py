from jiayan import load_lm
from jiayan import CRFPunctuator

text = '北冥有鱼其名为鲲鲲之大不知其几千里也化而为鸟其名为鹏鹏之背不知其几千里也怒而飞其翼若垂天之云是鸟也海运则将徙于南冥南冥者天池也齐谐者志怪者也谐之言曰鹏之徙于南冥也水击三千里抟扶摇而上者九万里去以六月息者也'

lm = load_lm('jiayan.klm')
punctuator = CRFPunctuator(lm, 'cut_model')
punctuator.load('punc_model')
print(punctuator.punctuate(text))

# 句读模型。结果：
# 北冥有鱼，其名为鲲，鲲之大，不知其几千里也。化而为鸟，其名为鹏，鹏之背，不知其几千里也。怒而飞，其翼若垂天之云，是鸟也，海运则将徙于南冥，南冥者，天池也，齐谐者，志怪者也，谐之言曰：鹏之徙于南冥也，水击三千里，抟扶摇而上者九万里，去以六月息者也。
