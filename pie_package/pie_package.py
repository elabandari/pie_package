import numpy as np 

def show_pie():
    pie_list = ['https://www.epicurious.com/recipes/food/views/our-favorite-apple-pie-51248690', 
    'https://tastesbetterfromscratch.com/triple-berry-pie/',
    'https://www.bonappetit.com/recipe/pecan-rye-pumpkin-pie']
    i = np.random.randint(0,2)
    return pie_list[i]
