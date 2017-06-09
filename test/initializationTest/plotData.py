from matplotlib import pyplot as plt


class PlotData(object):
    def __init__(self, log_file_dir):
        self.fig = plt.figure(1)
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)

        self.log_file = open(log_file_dir)
        self.data = []
        self.critic_loss = []
        self.actor_loss = []
        self.load_data_by_txt_file()
        pass

    def load_data_by_txt_file(self):
        for lines in self.log_file:
            elements = lines.split()
            epoch = elements[2]
            critic_cost = elements[6]
            actor_cost = elements[10]
            self.critic_loss.append((epoch, critic_cost))
            self.actor_loss.append((epoch, actor_cost))
            self.data.append({'epoch': epoch, 'critic_cost': critic_cost, 'actor_cost': actor_cost})

    def plot_loss(self):
        for data in self.data:
            self.ax1.scatter(x=data['epoch'], y=data['critic_cost'])
            self.ax2.scatter(x=data['epoch'], y=data['actor_cost'])
        # self.fig.show()
        plt.show()


if __name__ == '__main__':
    data = PlotData(log_file_dir='../../log/initialTrain/6-7-22-21-38/6-7-22-21-38-epoch=500000.txt')
    data.plot_loss()
