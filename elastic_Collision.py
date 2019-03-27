import matplotlib.pyplot as plt
import numpy as np
import math
import sys

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


def collisionwithWall(vel1, vel2):

    finalVelocity1 = -1 * vel1
    finalVelocity2 = vel2

    return[finalVelocity1, finalVelocity2]


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

        finalVelocity1, finalVelocity2 = collisionwithWall(initialVelocity1, initialVelocity2)
        initialVelocity1 = finalVelocity1

        collisionDirection = 'e'


    finalVelocityVec = np.row_stack((finalVelocityVec, [finalVelocity1, finalVelocity2]))

    collisionCount += 1

    print("No. of Collisions: {}\n" .format(collisionCount))
    print("Vf1 = {0}\n Vf2 = {1}" .format(finalVelocity1, finalVelocity2))

finalVelocity1 = finalVelocityVec[:, 0]
finalVelocity2 = finalVelocityVec[:, 1]

vecLen = finalVelocityVec.shape[0]

for i in range(vecLen - 2):

    plt.axis([1.2 * initVelocityVec[1], 1.2 * abs(initVelocityVec[1]), -1.2 * math.sqrt(mass2), 1.2 * math.sqrt(mass2)])
    plt.title(r'$Vf_2 vs. Vf_1$')
    plt.xlabel(r'$V_2$')
    plt.ylabel(r'$V_1$')
    if (i < range(vecLen - 1)):
        plt.plot(finalVelocity2[i:i+2], finalVelocity1[i:i+2],'ro-')

plt.grid()
plt.show()
