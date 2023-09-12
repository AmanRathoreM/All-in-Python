# Date 18-06-2021

import matplotlib.pyplot as plt
import matplotlib.animation as anime

plt.style.use('ggplot')

# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('This is a title\nSub title')


def plot_live_graph(file_name='example.txt', interval_for_graph_refreshing_in_miliseconds=500, whole_file_data_seperator='\n', split_symbol=',', title='live Graph', lablex='X Axis', labley='Y Axis', colour='r'):
    '''
Use:
    This function Shows you live graph

Requirnements:
    import matplotlib.pyplot as plt
    import matplotlib.animation as anime

Parameters:
    file_name='example.txt' (give the name of your file in which you need to get data for live plotting)

    whole_file_data_seperator='\\n'(seperates multiple x,y from each other)

    split_symbol=',' (seperates x,y from each other)

    interval_for_graph_refreshing_in_miliseconds=500 (In how much time you need to refresh your graph)

    title='live Graph'

    lablex='X Axis'

    labley='Y Axis'

    colour='r'


Returns:
    None
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        graph_data = open(file_name, 'r').read()
        lines = graph_data.split(whole_file_data_seperator)
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(split_symbol)
                xs.append(float(x))
                ys.append(float(y))
        ax1.clear()
        plt.xlabel(lablex)
        plt.ylabel(labley)
        plt.title(title)
        ax1.plot(xs, ys, color=colour)

    ani = anime.FuncAnimation(
        fig, animate, interval=interval_for_graph_refreshing_in_miliseconds)
    plt.show()


plot_live_graph("tutorial_16.txt", 100, whole_file_data_seperator='\n',
                split_symbol='|', title='LIVE GRAPH', lablex='X AXIS', labley='Y AXIS', colour='#1155cc')
