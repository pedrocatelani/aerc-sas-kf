import matplotlib.pyplot as plt
import numpy as np

def plot_fitness_evolution(history):
        
    generations = range(len(history))
    
    plt.figure(figsize=(10, 6))
    plt.plot(generations, history, marker='o', linestyle='-', color='b')
    plt.title('Evolução do Fitness Médio por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Fitness Médio')
    plt.grid(True)
    

    plt.xticks(generations) 
    
    plt.show() 
    
    
def plot_attribute_comparison(best_attrs: dict, worst_attrs: dict, best_name: str, worst_name: str, best_fitness: float, worst_fitness: float):
    attr_map = {
        "expectedAmber": "EA",
        "amberControl": "AC",
        "creatureControl": "CC",
        "creatureProtection": "CP",
        "effectivePower": "EP",
        "disruption": "DR"
    }
    
    attribute_keys = [
        "expectedAmber", 
        "amberControl", 
        "creatureControl", 
        "creatureProtection", 
        "effectivePower", 
        "disruption"
    ]
    
    attributes = [attr_map[key] for key in attribute_keys]
    
    best_normalized = []
    worst_normalized = []
    
    
    for key_attr_long in attribute_keys:
        best_normalized.append(best_attrs[key_attr_long])
        worst_normalized.append(worst_attrs[key_attr_long])
        
    x = np.arange(len(attributes)) 
    width = 0.35
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    def autolabel(rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{:.2f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
            
    rects1 = ax1.bar(x, best_normalized, width, label='Melhor Deck (Max Fitness)', color='g')
    ax1.set_ylabel('Valor do Atributo (Normalizado: 0 a 1)')
    ax1.set_xlabel('Atributos')
    ax1.set_title(f'Melhor Deck - {best_name} - Fitness {best_fitness}')
    ax1.set_xticks(x)
    ax1.set_xticklabels(attributes)
    ax1.set_ylim(0, 1) 
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
  
    autolabel(rects1, ax1)
    
    rects2 = ax2.bar(x, worst_normalized, width, label='Pior Deck (Min Fitness)', color='r')
    ax2.set_ylabel('Valor do Atributo (Normalizado: 0 a 1)')
    ax2.set_xlabel('Atributos')
    ax2.set_title(f'Pior Deck - {worst_name} - Fitness {worst_fitness}')
    ax2.set_xticks(x)
    ax2.set_xticklabels(attributes)
    ax2.set_ylim(0, 1) 
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    autolabel(rects2, ax2)
    
    fig.tight_layout()
    
    plt.show()