from nltk.corpus import wordnet as wn
import _pickle as pickle
from keyword_sense import keywords2sense
from keyword_list import keywords_list


all_expansions = {}


for i in range(len(keywords2sense)):
    keyword = keywords_list[i]
    expansion = {}

    for j, sense in enumerate(keywords2sense[i]):
        one_sense = {}

        hyponyms = []
        instance_hyponyms = []

        # print(sense)
        one_set = wn.synset(sense)
        lemma = one_set.lemma_names()

        hyponyms_list = one_set.hyponyms()

        for k in range(len(hyponyms_list)):
            one_hyponym = one_set.hyponyms()[k]
            hyponym_lemma = one_hyponym.lemma_names()
            for idx in range(len(hyponym_lemma)):
                hyponyms.append(hyponym_lemma[idx])

        instance_hyponyms_list = one_set.instance_hyponyms()

        '''
        if len(instance_hyponyms_list)!= 0:
            print("Yes")  # 4
        '''

        for k in range(len(instance_hyponyms_list)):
            one_instance_hyponym = one_set.instance_hyponyms()[k]
            instance_hyponym_lemma = one_instance_hyponym.lemma_names()
            for idx in range(len(instance_hyponym_lemma)):
                instance_hyponyms.append(instance_hyponym_lemma[idx])

        one_sense["lemma"] = lemma
        one_sense["hyponyms"] = hyponyms
        one_sense["instance_hyponyms"] = instance_hyponyms

        expansion[sense] = one_sense

    all_expansions[keyword] = expansion

# print(all_expansions)

with open('wordnet_keyword_expansion.pickle', 'wb') as f:
    pickle.dump(all_expansions, f)










