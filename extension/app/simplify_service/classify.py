import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


# def preprocess_text(text):
# 	split_text = text.split(' ')
# 	stemmed = [stemmer.stem(word) for word in split_text]
# 	return ' '.join(stemmed)

def build_training_documents(source_dir):
	all_train = []
	all_target = []
	for train_file_name in os.listdir(source_dir):
		train_file = open(source_dir + '/' + train_file_name, 'r')
		train_file_text = train_file.read()
		train_file_text = unicode(train_file_text, 'utf-8')
		train_files = train_file_text.split('\n')
		# clean_train_files = [preprocess_text(abstract) for abstract in train_files]
		all_train.extend(train_files)
		new_targets = [train_file_name] * len(train_files)
		all_target.extend(new_targets)
		print "done building " + train_file_name
	return (all_train, all_target)

def train_vectorizer(textX):
	vectorizer = TfidfVectorizer(stop_words='english')
	X = vectorizer.fit_transform(textX)
	joblib.dump(vectorizer, '/Users/Zack/Developer/maple/extension/app/simplify_service/saved_models/vectorizer.pkl')
	return X

def train_classifier(X, y):
	alphas = np.arange(0, 1.1, 0.1)
	parameters = {'alpha':alphas}
	mnb = MultinomialNB()
	clf = GridSearchCV(mnb, parameters)
	clf.fit(X,y)
	joblib.dump(clf, '/Users/Zack/Developer/maple/extension/app/simplify_service/saved_models/naive_bayes.pkl')

def classify(test_text):
	vectorizer = joblib.load('/Users/Zack/Developer/maple/extension/app/simplify_service/saved_models/vectorizer.pkl')
	clf = joblib.load('/Users/Zack/Developer/maple/extension/app/simplify_service/saved_models/naive_bayes.pkl')
	testX = vectorizer.transform(test_text)
	predicted = clf.predict(testX)
	return predicted

def compute_accuracy(X, y):
	clf = joblib.load('/Users/Zack/Developer/maple/extension/app/simplify_service/saved_models/naive_bayes.pkl')
	return clf.score(X, y)

# print "building training documents"
# docX,y = build_training_documents('corpora')
# print "vectorizing training data"
# X = train_vectorizer(docX)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
# print "training classifier"
# train_classifier(X_train, y_train)
# print "testing classifier"
# # test_pred = classify(X_test)
# print compute_accuracy(X_test, y_test)

