import matplotlib.pyplot as plt

def plot_graph_with_coordinates():
    my_file = open('C:/Users/Daniel/PycharmProjects/pythonProject3/x_y_coordinates.txt','r')

    x_coordinates = []# calling x and y coordinates
    y_coordinates = []
    my_file.readline()
    for line in my_file.readlines():
       x_coordinates.append(float(line.split(',')[0]))
       y_coordinates.append(float(line.split(',')[1]))

    plt.scatter(x_coordinates, y_coordinates)# plotting the graph
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatter Plot of Coordinates')
    plt.grid(True)
    plt.show()

# Specify the path to the file and call the function
plot_graph_with_coordinates()


