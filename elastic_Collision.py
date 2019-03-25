import matplotlib.pyplot as plt
import numpy as np

mass1 = 1
mass2 = mass1 * 1e2

initVelocityVec = [0, -1]

initialVelocity1 = initVelocityVec[0]
initialVelocity2 = initVelocityVec[1]

massConst1 = mass1 + mass2
massConst2 = mass2 - mass1
massConst3 = mass1 - mass2

collisionCount = 0

collisionDirection = 'e'

finalVelocityVec = initVelocityVec

def collisionwithBox(vel1, vel2):
    finalVelocity1 = (2 * mass2 * vel2) / massConst1 + (vel1 * massConst3) /massConst1

    finalVelocity2 = (2 * mass1 * vel1) / massConst1 + (vel2 * massConst2) / massConst1

    return[finalVelocity1, finalVelocity2]

def collisionwithWall(vel1):

    finalVelocity1 = -1*vel1

    return[finalVelocity1]


def velocityCheck(vel1, vel2):

    ret = True

    if (vel1 >= 0 and vel2 >= 0):
        if(abs(vel1) <= (vel2)):
            ret = False

    return ret


while (velocityCheck(initialVelocity1, initialVelocity2)):

    if  (collisionDirection == 'e'):
        finalVelocity1, finalVelocity2 = collisionwithBox(initialVelocity1, initialVelocity2)

        initialVelocity1 = finalVelocity1
        initialVelocity2 = finalVelocity2

        collisionDirection = 'w'

    elif (collisionDirection == 'w'):

        finalVelocity1 = collisionwithWall(initialVelocity1)
        initialVelocity1 = finalVelocity1

        collisionDirection = 'e'


    finalVelocityVec = np.concatenate((finalVelocityVec, [finalVelocity1, finalVelocity2]))

    collisionCount += 1

    print("No. of Collisions: {}\n" .format(collisionCount))
    print("Vf1 = {0}\n Vf2 = {1}" .format(finalVelocity1, finalVelocity2))
