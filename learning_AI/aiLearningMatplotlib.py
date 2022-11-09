
import matplotlib.pyplot as plt
import numpy as np

def subplot():
    x = np.arange(0, 2 * np.pi, 0.01)
    y_1 = np.cos(x)
    y_2 = x * np.sin(2 * x)

    fig, a = plt.subplots(1, 2, figsize = (40, 10))

    a[0].plot(x, y_1)
    a[0].set_xlabel('x', fontsize = 25)
    a[0].set_ylabel('y', fontsize = 25)
    a[0].set_title('y = cos(x)', fontsize = 25)

    a[1].plot(x, y_2)
    a[1].set_xlabel('x', fontsize = 25)
    a[1].set_ylabel('y', fontsize = 25)
    a[1].set_title('y = xsin(2x)', fontsize = 25)

def bar():
    os = ['Windows', 'OS X', 'Unknown', 'Chrome OS', 'Linux']
    percentage = [75.39, 15.93, 3.75, 2.57, 2.35]
    bar_width = 0.7

    plt.bar(os, percentage, width = bar_width)
    plt.xlabel('Desktop OS')
    plt.ylabel('Market percentage (%)')
    plt.title('Desktop OS market distribution')
    plt.xticks(rotation = 45)

def boxplot():
    np.random.seed(10)

    data_1 = np.random.normal(80, 30, 200)
    data_2 = np.random.normal(90, 20, 200)
    data_3 = np.random.normal(10, 100, 200)
    data_4 = np.random.normal(25, 75, 200)

    data = [data_1, data_2, data_3, data_4]
    plt.boxplot(data)

def scatter():
    data_1 = np.random.normal(80, 30, 200)
    data_2 = np.random.normal(90, 20, 200)
    colors = range(len(data_1))
    plt.scatter(data_1, data_2,colors)
    plt.xlabel('data_1')
    plt.ylabel('data_2')

def heatmap():
    fruits = ['mango', 'watermelon', 'pineapple', 'strawberry', 'cherry', 'orange']
    countries = ['India', 'Australia', 'USA', 'Canada', 'Brazil', 'Germany', 'Spain']
    harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

    fig, ax = plt.subplots()
    ax.imshow(harvest)

    #Aranging the labels
    ax.set_xticks(np.arange(len(countries)))
    ax.set_yticks(np.arange(len(fruits)))

    #Naming those labels
    ax.set_xticklabels(countries)
    ax.set_yticklabels(fruits)

    for i in range(len(fruits)):
        for j in range(len(countries)):
            
            # annotating numeric value at the center of each square
            text = ax.text(j, i, harvest[i, j], ha = 'center', va = 'center', 
                           color = 'w')

    #Setting the heatmap title
    ax.set_title('Growth of Fruits in Countries (tons / year)')

heatmap()
plt.show()
