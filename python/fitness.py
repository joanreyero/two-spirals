from selenium import webdriver
import time
import numpy as np
from config import *

def build_url(hlhu, algorithm, activation, inputs, seed=False, noise='0', reg='0'):
    if not seed:
        seed = str(0.41030)
    else:
        seed = str(seed)
    return f'http://localhost:5000/#activation={activation}&regularization=L2&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate={reg}&noise={noise}&networkShape={hlhu}&seed={seed}&showTestData=false&discretize=true&percTrainData=50&x=true&y=true&xTimesY=false&xSquared={inputs}&ySquared={inputs}&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=true&problem=classification&algorithm={algorithm}&initZero=false&hideText=false'


def parse_hlhu(hlhu):
    hlhu = [h for h in hlhu if h != 0]
    return ','.join(map(str, hlhu))

def parse_algorithm(marker):
    if marker:
        return 'particleswarm'
    return 'sdg'

def parse_activation(marker):
    dic = {
        0: 'relu',
        1: 'tanh',
        2: 'sigmoid',
        3: 'sin',
        4: 'rbf'
    }
    return dic[marker]

def parse_inputs(marker):
    if marker == 1:
        return 'true'
    return 'false'

def get_fitness(params, max_epochs=300, sanity_check=100, checked_ok=False, repeat=1, report=False, noise='0', reg='0'):
    """
    Input: list of 7 elements
    """

    rng = np.random.RandomState(seed=424242)
    hlhu = parse_hlhu(params[:6])
    algorithm = parse_algorithm(params[6])
    activation = parse_activation(params[7])
    inputs = parse_inputs(params[8])
    loses = []
    for i in range(repeat):
        seed = rng.rand()
        url = build_url(hlhu, algorithm, activation, inputs, seed=seed, noise=noise, reg=reg)
        driver = webdriver.Chrome(PATH_TO_DRIVER)  
        driver.get(url)
        time.sleep(0.2)
        button = driver.find_element_by_id('play-pause-button')
        button.click()

        while True:
            epoch_num = driver.find_element_by_id('iter-number').text
            epoch_num = int(epoch_num.replace(',', ''))

            if epoch_num > max_epochs:
                testloss = driver.find_element_by_id('loss-test').text
                loses.append(float(testloss))
                break

            if epoch_num > sanity_check and not checked_ok:
                testloss = driver.find_element_by_id('loss-test').text
                if float(testloss) > 0.4:
                    testloss = driver.find_element_by_id('loss-test').text
                    loses.append(float(testloss))
                    break
                else: checked_ok = True


        driver.quit()

    if report:
        return np.mean(loses), np.std(loses)
    return np.mean(loses)





if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-g','--genome', nargs='+', type=int,
                        help='genome', required=True)
    parser.add_argument('--max_epochs', '-m', type=int, default=1000,
                        help='max epochs')
    parser.add_argument('--repeat', '-r', type=int, default=5,
                        help="Times to run the PSO")
    parser.add_argument('--noise', '-n', type=str, default='0',
                        help='noise')
    parser.add_argument('--reg', type=str, default='0',
                        help='regularisation')
    args = parser.parse_args()

    r = get_fitness(args.genome, max_epochs=args.max_epochs, 
                    checked_ok=True, repeat=args.repeat, 
                    report=True, noise=args.noise, reg=args.reg)

    print(r)