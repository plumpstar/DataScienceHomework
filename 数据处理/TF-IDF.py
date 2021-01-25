from sklearn.feature_extraction.text import TfidfVectorizer
orpus = [
  'This is the first document.',
   'This document is the second document.',
   'And this is the third one.',
   'Is this the first document?',
]
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(orpus)
print(X.toarray())
print(X.shape)
print(type(X))
print(tfidf.get_feature_names())