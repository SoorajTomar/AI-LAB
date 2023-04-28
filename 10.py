#NLP
import nltk
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
example_string = """Amazon Elastic Compute Cloud is a part of Amazon.com's cloud-computing platform, Amazon Web Services, that allows users to rent virtual computers on which to run their own computer applications."""
print("Sentence Tokens:",sent_tokenize(example_string))
print("Word Tokens:",word_tokenize(example_string))
print(nltk.pos_tag(word_tokenize(example_string)))
pos_tags=nltk.pos_tag(word_tokenize(example_string))
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(pos_tags)
tree.draw()
