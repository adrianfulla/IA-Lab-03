import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sensor_color_distribution = pd.read_csv('./Sensor_Color_Distribution.csv')

tablero = 10
prior = np.full((tablero, tablero), 1/(tablero**2))

def update_probabilities(prior, evidence_position, evidence_color):
    likelihood = np.zeros_like(prior)
    
    for i in range(tablero):
        for j in range(tablero):
            distance = np.abs(i - evidence_position[0]) + np.abs(j - evidence_position[1])
            if distance < len(sensor_color_distribution):
                likelihood[i, j] = sensor_color_distribution.loc[distance, evidence_color]
            else:
                likelihood[i, j] = 0 
    posterior = likelihood * prior
    posterior /= np.sum(posterior)
    return posterior

def plot_distribution(probabilities, title='Probability Distribution'):
    plt.figure(figsize=(8, 6))
    sns.heatmap(probabilities, annot=True, fmt=".2f", cmap="Blues", cbar=False)
    plt.title(title)
    plt.show()


position = (5, 5)  
color = 'R'         
updated_probabilities = update_probabilities(prior, position, color)

plot_distribution(updated_probabilities, 'Distribución de probabilidades')


localizacion_mas_probable = np.unravel_index(np.argmax(updated_probabilities), updated_probabilities.shape)
print("La celda más probable donde se encuentra el fantasma es:", most_probable_location)
