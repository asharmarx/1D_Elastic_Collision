clear; clc;

mass1 = 1;
mass2 = 10000;

initialVelocity1 = 0;
initialVelocity2 = -1;

massConst1 = mass1 + mass2;
massConst2 = mass2 - mass1;
massConst3 = mass1 - mass2;

collisionCount = 0;

collisionDirection = 'e';


while (initialVelocity2 <= abs(initialVelocity1)s)
    
    if  collisionDirection == 'e'
        finalVelocity1 = (2 * mass2 * initialVelocity2) / massConst1 + ...
            (initialVelocity1 * massConst3) / massConst1;
        
        finalVelocity2 = (2 * mass1 * initialVelocity1) / massConst1 + ...
            (initialVelocity2 * massConst2) / massConst1;
        
        initialVelocity1 = finalVelocity1;
        initialVelocity2 = finalVelocity2;
        
        collisionDirection = 'w';
        
    elseif collisionDirection == 'w'
        
        finalVelocity1 = -1*initialVelocity1;
        initialVelocity1 = finalVelocity1;
        
        collisionDirection = 'e';
        
    end
    
    
    
    
    collisionCount = collisionCount + 1;
    
    fprintf('No. of Collisions: %d\n', collisionCount)
    fprintf('Vf1: %d\n Vf2: %d\n', finalVelocity1, finalVelocity2)
    
    
end



