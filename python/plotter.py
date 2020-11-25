import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ITER, FITNESS, TIME = 'iter', 'best_fitness', 'time'

def plot_fitness_time(ts, f, title, save):
    start_t = ts[0]
    ts = [int(t - start_t) for t in ts]
    plt.plot(ts, f, '-o', color='orange')
    plt.xlabel('Time (s)')
    plt.title('Fitness over time for a ' + title)
    plt.savefig(f'figures/time-{save}.pdf')
    #plt.show()


def plot_joint(ts, f, interval, title, save):

    start_t = ts[0]
    ts = [int(t - start_t) for t in ts]
    print(int(ts[-1] - ts[0]) / 3600.0)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax2.grid(which='both', alpha=0.5)

    ax1.plot(ts, f, '-o', color='green', markersize=3)

    ax1.set_xlabel("Time (s)")

    new_tick_locations = [t for i, t in enumerate(ts) if i % interval == 0]

    def tick_function(X, interval):
        return interval * np.array(range(len(X)))

    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(new_tick_locations)
    ax2.set_xticklabels(tick_function(new_tick_locations, interval))
    ax2.set_xlabel("Iteration")
    
    fig.suptitle('Evolution of a ' + title)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    plt.savefig(f'figures/joint-{save}.pdf')
    #plt.show()


def plot_fitness_iter(i, f, title, save):
    fig = plt.figure()
    plt.plot(i, f, '-o', color='green')
    plt.xlabel('Iteration')
    plt.title('Fitness per iteration for a ' + title)
    plt.savefig(f'figures/iter-{save}.pdf')
    #plt.show()
    

def main(file, interval, title, save=True):
    if save:
        save = file
    data = pd.read_csv(f'csv/{file}.csv')
    #plot_fitness_iter(data[ITER], data[FITNESS], title, save)
    #plot_fitness_time(data[TIME], data[FITNESS], title, save)
    plot_joint(data[TIME], data[FITNESS], interval, title, save)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, default='temp',
                        help="filename (without .csv)")
    parser.add_argument('--save', '-s', type=bool, default=True,
                        help="save?")
    parser.add_argument('--title', '-t', type=str, default="GP with maximum 3 HLs",
                        help="figure title")
    parser.add_argument('--interval', '-i', type=int, default=2,
                        help="Interval for joint plotting")

    args = parser.parse_args()
    main(args.file, args.interval, args.title, args.save)