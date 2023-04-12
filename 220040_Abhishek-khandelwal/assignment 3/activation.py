import math
def sigmoid(z) :
    result = 1/(1+(math.exp(-z)))
    return result
z = float(input("Write the z value: "))
print("sigmoid(" + str(z) + "): " + str(sigmoid(z)))
def Tanh(z) :
    result = (math.exp(z) - math.exp(-z))/(math.exp(z) + math.exp(-z))
    return result
print("Tanh(" + str(z) + "): " + str(Tanh(z)))
