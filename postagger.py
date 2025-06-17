from jiayan import PMIEntropyLexiconConstructor
from jiayan import CharHMMTokenizer
from jiayan import WordNgramTokenizer
from jiayan import CRFSentencizer
from jiayan import CRFPunctuator
from jiayan import CRFPOSTagger
from jiayan import load_lm

postagger = CRFPOSTagger()
postagger.load('/Users/you7n/Documents/jiayan_models/pos_model')
words = ['北', '冥', '有', '鱼', '其', '名', '为', '鲲', '鲲', '之', '大', '不', '知', '其', '几', '千里', '也', '化', '而', '为', '鸟', '其', '名', '为', '鹏', '鹏', '之', '背', '不', '知', '其', '几', '千里', '也', '怒', '而', '飞', '其', '翼', '若', '垂天', '之', '云', '是', '鸟', '也', '海运', '则', '将', '徙', '于', '南', '冥', '南', '冥', '者', '天池', '也', '齐谐', '者', '志怪', '者', '也', '谐', '之', '言', '曰', '鹏', '之', '徙', '于', '南', '冥', '也', '水', '击', '三', '千里', '抟扶摇', '而', '上', '者', '九', '万里', '去', '以', '六月', '息', '者', '也']
print(postagger.postag(words))

# 词性模型。结果：
# ['nd', 'n', 'v', 'n', 'r', 'n', 'v', 'v', 'n', 'u', 'd', 'd', 'v', 'r', 'm', 'q', 'd', 'v', 'c', 'v', 'n', 'r', 'n', 'v', 'n', 'v', 'u', 'n', 'd', 'v', 'r', 'm', 'q', 'd', 'v', 'c', 'v', 'r', 'n', 'c', 'v', 'u', 'n', 'v', 'n', 'd', 'v', 'c', 'd', 'v', 'p', 'nd', 'n', 'nd', 'n', 'k', 'ns', 'd', 'v', 'r', 'n', 'k', 'd', 'a', 'u', 'n', 'v', 'n', 'u', 'v', 'p', 'nd', 'n', 'd', 'n', 'v', 'm', 'q', 'n', 'c', 'v', 'k', 'm', 'q', 'v', 'p', 'nt', 'n', 'k', 'd']