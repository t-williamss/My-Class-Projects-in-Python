from neural import *

xorTrainingData = [([0.0, 0.0], [0.0]),
                    ([0.0, 1.0], [1.0]),
                    ([1.0, 0.0], [1.0]),
                    ([1.0, 1.0], [0.0])]

nn = NeuralNet(2 ,2, 1)
nn.train(xorTrainingData) 
#print(nn.test(xorTrainingData))           #Display options 
for triple in nn.test(xorTrainingData):
    print(triple)

nn = NeuralNet(2 ,8, 1)
nn.train(xorTrainingData) 
# print nn.test(xorTrainingData)
for triple in nn.test(xorTrainingData):
    print(triple)

nn = NeuralNet(2 ,1, 1)
nn.train(xorTrainingData) 
# print nn.test(xorTrainingData)
for triple in nn.test(xorTrainingData):
    print(triple)

voterTrainingData = [([0.9, 0.6, 0.8, 0.3, 0.1], [1.0]),
                    ([0.8, 0.8, 0.4, 0.6, 0.4], [1.0]),
                    ([0.7, 0.2, 0.4, 0.6, 0.3], [1.0]),
                    ([0.5, 0.5, 0.8, 0.4, 0.8], [0.0]),
                    ([0.3, 0.1, 0.6, 0.8, 0.8], [0.0]),
                    ([0.6, 0.3, 0.4, 0.3, 0.6], [0.0])]

nn = NeuralNet(5 ,6, 1)  #6 voters 
nn.train(voterTrainingData) 
# print(nn.test(voterTrainingData))

voterTestCases = [([1.0, 1.0, 1.0, 0.1, 0.1], [1]),
                    ([0.5, 0.2, 0.1, 0.7, 0.7], [1]),
                    ([0.8, 0.3, 0.3, 0.3, 0.8], [1]),
                    ([0.8, 0.5, 0.8, 0.4, 0.8], [1]),
                    ([0.3, 0.1, 0.6, 0.8, 0.8], [1]),
                    ([0.6, 0.3, 0.4, 0.3, 0.6], [1])]

for triple in nn.test(voterTestCases):
    print(triple)