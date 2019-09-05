from sklearn import tree;

# features
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#labels
labels = [0, 0, 1, 1]
#classifier
clf = tree.DecisionTreeClassifier()
# fit the classifier base on features and labels
# fit (synonyms of find pattern and data)
clf = clf.fit(features, labels)

#print the output base on classifier
print clf.predict([[150, 0]])