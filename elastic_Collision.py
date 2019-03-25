import matplotlib.plot as plt`
import numpy as np

mass1 = 1;
mass2 = mass1 * 1e2;

initVelocityVec = [0 -1];

initialVelocity1 = initVelocityVec[0];
initialVelocity2 = initVelocityVec[1];

massConst1 = mass1 + mass2;
massConst2 = mass2 - mass1;
massConst3 = mass1 - mass2;

collisionCount = 0;

collisionDirection = 'e';

finalVelocityVec = initVelocityVec;

def collisionwithBox(velocityVec):
    finalVelocity1 = (2 * mass2 * initialVelocity2) / massConst1 + (initialVelocity1 * massConst3) / massConst1;

    finalVelocity2 = (2 * mass1 * initialVelocity1) / massConst1 +
    (initialVelocity2 * massConst2) / massConst1;

    return[finalVelocity1, finalVelocity2]

def collisionwithWall(velocityVec):

    finalVelocity1 = -1*initialVelocity1;
    return[finalVelocity1]


def velocityCheck(vel1, vel2):

    ret = True;

    if (vel1 >= 0 && vel2 >= 0):
        if(abs(vel1) <= (vel2)):
            ret = False;


while (velocityCheck(initialVelocity1, initialVelocity2)):

    if  (collisionDirection == 'e'):
