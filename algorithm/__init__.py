import numpy as np
import pandas as pd
from examples import *

def getRatings():

    i = ["Universitiy", "Trum stop", "Kindergarten", "Cafe", "Post office", "Convenience shop", "Hipermarket", "Alkohol store", "Crime index"]

    frame = pd.DataFrame({
        "students": [1, 0.8, 0, 0.3/4, .25, .3, .5, .7, 0.05],
        "couples": [0.2, 0.3, 0.2, 0.6/4, 0.5, 0.4, 0.2, 0.4, 0.3],
        "families": [0.3, 0.2, 0.9, 0.2, 0.75, 0.2, 0.9, 0.1, 0.9],
        "company flat": [0.05, .5, 0, .8, 1, 0.8, .2, .1, 0.7],
        "single": [0.25, 0.5, 0.1, 0.35, 0.3, 0.9, 0.1, 0.9, 0.4]
    }, index=i)

    data = [getUczelnie(), getPrzystanki(), getPrzedszkola(), getKawiarnie(), getPoczta(), getConvienience(), getHipermarket(), getMonopolowy(), getCrimes()]

    targets = {}
    for f in frame.keys():
        arr = (frame[f] * np.array([x[0] for x in data]))
        targets[f] = np.sum(arr) / sum(frame[f])
    
    results = dict(zip(i, [x[1] for x in data]))
    return targets, results

print(getRatings())