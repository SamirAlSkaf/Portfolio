import math

#Sigmoid-Aktivierungsfunktion
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

#Berechnung des Neuronenausgangs
def forward(inputs, weights, bias):
    weighted_sum = sum(weight * inp for weight, inp in zip(weights, inputs)) + bias
    output = sigmoid(weighted_sum)
    return output

#Hauptfunktion
if __name__ == "__main__":
    weights = [0.5] * 2  #Gewichtungen
    bias = 0.0  #Bias
    inputs = [1.0, 2.0]  #Beispiel-Eingaben

    #Alles zusammenführen
    output = forward(inputs, weights, bias)
    
    print("Neuron Output:", output)
