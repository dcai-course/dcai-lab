# NOTE this is part of the lab infrastructure / solution. The code in here is
# not available to the attacker, who can only make black-box queries to the
# target model and observe the softmax output.

import torch.nn as nn

def get_model():
    model = nn.Sequential(
        nn.Conv2d(3, 32, 3),
        nn.ReLU(),
        nn.BatchNorm2d(32),
        nn.MaxPool2d(2, 2),

        nn.Conv2d(32, 64, 3),
        nn.ReLU(),
        nn.BatchNorm2d(64),
        nn.MaxPool2d(2, 2),

        nn.Conv2d(64, 128, 3),
        nn.ReLU(),
        nn.BatchNorm2d(128),
        nn.MaxPool2d(2, 2),

        nn.Flatten(),
        nn.Linear(128*2*2, 256),
        nn.ReLU(),
        nn.Linear(256, 128),
        nn.ReLU(),
        nn.Linear(128, 10)
    )

    return model
