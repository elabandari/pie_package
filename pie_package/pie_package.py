import numpy as np 

def show_pie():
    """Randomly show a pie recipe

    Returns
    -------
    str
        URL to pie recipe

     Examples
    --------
    >>> from pie_package import pie_package
    >>> pie_package.show_pie()
    'https://tastesbetterfromscratch.com/triple-berry-pie/'
    """
    pie_list = ['https://www.epicurious.com/recipes/food/views/our-favorite-apple-pie-51248690', 
    'https://tastesbetterfromscratch.com/triple-berry-pie/',
    'https://www.bonappetit.com/recipe/pecan-rye-pumpkin-pie']
    i = np.random.randint(0,3)
    return pie_list[i]
