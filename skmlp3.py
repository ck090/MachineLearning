from sklearn.neural_network import MLPClassifier

#Input as [Height, Weight, ShoeSize]
X = [[78,77,8], [180,80,10], [181,90,11], [170,70,8], [166,66,8], [187,80,9], [190,87,11], [170,70,8], 
    [168,55,7], [177,80,9], [190,90,11], [155,60,7], [177,89,7], [155,90,7], [190,70,9], [182,80,9]]

Y = ['female', 'male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male', 'female',
    'female', 'female', 'male', 'male']

#using MLP
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100,2), random_state=1)

#fitting the classified data acc to X, Y
clf = clf.fit(X, Y)

print "Enter three numbers the Height, Weight and ShoeSize"
number = raw_input()
numbers = map(int, number.split())

#perform classification on an array of test vectors X
prediction = clf.predict([numbers])

print "The person is a: "
print prediction