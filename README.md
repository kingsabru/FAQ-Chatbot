# FAQ-Chatbot
An FAQ chatbot which answers questions related to the University of Mines and Technology, Ghana.

## Getting started
The chatbot was writen in python using tensorflow and tflearn. Flask package is used for rendering the UI.

### Prerequisites
The chatbot was created using python 3.6. If you are using a different version, you can create a python 3.6 virtual environment using Anaconda. After installing and setting up Anaconda, use the following commands to create the environment:
```
# Create environment
conda create -n chatbot python=3.6
# Activate environment
activate chatbot
# Deactivate enviroment
deactivate
# List created virtual environments
conda env list
```
### Installing
The chatbot was created with the following python packages. You can install the packages using the commands:
```
pip install nltk 
pip install numpy
pip install tflearn
pip install tensorflow
pip install Flask
```
## Deployment
To start the chatbot, use the command:
```
python bot.py 
```
To retrain model after making changes to intent.json dataset, use the command:
```
python trainbot.py
```
## Built With
* [Flask](https://www.fullstackpython.com/) - The web framework used
* [Tensorflow](https://www.tensorflow.org/) - The library used to train ML model

## Authors
* **Kingsley Abru** - *Initial work* - [kingsabru](https://github.com/kingsabru)

## Acknowledgments
* Thanks to [Dinesh S](https://github.com/dineshsambasivam) for using his chatbot project as a reference guide for this project.
