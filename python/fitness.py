from selenium import webdriver
import time


def build_url(hlhu, algorithm, activation, inputs):
    return f'http://localhost:5000/#activation={activation}&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape={hlhu}&seed=0.41030&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared={inputs}&ySquared={inputs}&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=false&problem=classification&algorithm={algorithm}&initZero=false&hideText=false'


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

def get_fitness(params):
    """
    Input: list of 7 elements
    """

    hlhu = parse_hlhu(params[:4])
    algorithm = parse_algorithm(params[4])
    activation = parse_activation(params[5])
    inputs = parse_inputs(params[6])

    
    url = build_url(hlhu, algorithm, activation, inputs)
    driver = webdriver.Chrome('/Users/joanreyero/chromedriver')  
    driver.get(url)
    time.sleep(0.2)
    button = driver.find_element_by_id('play-pause-button')
    button.click()
    checked_ok = False

    while True:
        epoch_num = driver.find_element_by_id('iter-number').text
        epoch_num = int(epoch_num.replace(',', ''))

        if epoch_num > 100:
            testloss = driver.find_element_by_id('loss-test').text
            print(testloss)
            break

        if epoch_num > 20 and not checked_ok:
            testloss = driver.find_element_by_id('loss-test').text
            if float(testloss) > 0.4:
                break
            else: checked_ok = True

    driver.quit()
    return float(testloss)





if __name__ == '__main__':
    get_fitness([
        3, 3, 3, 0,  # hlhu
        1,  # algorithm
        0,  # activation
        1,  # show X**2
    ])