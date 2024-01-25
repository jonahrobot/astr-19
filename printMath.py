import numpy as np

if __name__ == "__main__":

    for x in np.linspace(0,2*np.pi,1000):
        print(str(np.sin(x)) + " vs. " + str(x))