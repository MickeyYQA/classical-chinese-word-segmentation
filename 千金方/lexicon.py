from jiayan import PMIEntropyLexiconConstructor

constructor = PMIEntropyLexiconConstructor()
lexicon = constructor.construct_lexicon('备急千金要方.txt')
constructor.save(lexicon, '词库.csv')