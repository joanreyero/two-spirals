# Deep playground

Deep playground is an interactive visualization of neural networks, written in
TypeScript using d3.js. We use GitHub issues for tracking new requests and bugs.

This version of the playground has a button where instead of a stochastic gradient, a particle swarm can be activated for optimisation of a NN. 

## Playground

To run the playground locally, run:
- `npm i` to install dependencies
- `npm run build` to compile the app and place it in the `dist/` directory
- `npm run serve` to serve from the `dist/` directory and open a page on your browser.

For a fast edit-refresh cycle when developing run `npm run serve-watch`.
This will start an http server and automatically re-compile the TypeScript,
HTML and CSS files whenever they change.

# Genetic algorithm

To install the Pyhton code, run:
- `pip install -r requirements.txt` to install dependencies
- Download the chromedriver appropriate to your Chrome version from: https://chromedriver.chromium.org/downloads
- Add the absolute path to the driver on config.py

To run all the programs below make sure to be in the *pyhton* folder: `cd python`

Make sure to have `npm run serve` running in another terminal tab.
### Running the Genetical Algorithm

Run `python ga-two-spirals.py -t {ga or gp}`

Parameters:
- `-t` or `--type`: accepts the inputs 'ga' or 'gp' corresponding to Genetical Algorithm or Genetic Programming

- `-f` or `--file` (optional): takes a file name present in the folder csv to which it will output the report from the GA/GP. Do not add .csv. First you need to create a `.csv` file in the csv folder with the same name first. This file should have columns named: `iter,best_fitness,time`. 
 
### Computing the fitness of a network

Run `fitness.py -g [genome] -m max-epochs -r times-to-run`

Parameters:

- `-g` or `--genome` takes the genome of the model, for example `5 0 6 7 0 0 1 3 1`. See the report for more clarification.
- `-m` or `--max`: max epochs. The test loss at `m` epochs is recorded.
- `-r`:  number of times that the model will be run (the average value will be returned)
- `-n` or `--noise`: percentage of noise to generate data
- `--reg`: regularisation constant.

### Plotting files

Run `python plotter.py -f csv-file
- `-f or --file` takes the name of the csv file containing the results that will be plotted (without .csv)
- `-t` or `--title` sets the title of the plot