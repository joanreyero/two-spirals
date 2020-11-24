import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ITER, FITNESS, TIME = 'iter', 'best_fitness', 'time'


def plot_fitness_iter(i, f, title, save):
    fig = plt.figure()
    plt.plot(i, f, '-o', color='green')
    plt.xlabel('Iteration')
    plt.title('Fitness per iteration ' + title)
    plt.savefig(f'figures/{save}.pdf')
    plt.show()
    

def main(file, title, save=True):
    if save:
        save = file
    data = pd.read_csv(f'csv/{file}.csv')
    plot_fitness_iter(data[ITER], data[FITNESS], title, save)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, default='temp',
                        help="filename (without .csv)")
    parser.add_argument('--save', '-s', type=bool, default=True,
                        help="save?")
    parser.add_argument('--title', '-t', type=str, default="for a GP with maximum 3 HL",
                        help="figure title")
    

    args = parser.parse_args()
    main(args.file, args.title, args.save)