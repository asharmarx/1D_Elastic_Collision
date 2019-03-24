clear; clc;

mass1 = 1;
mass2 = mass1 * 1e2;

initVelocityVec = [0 -1];

initialVelocity1 = initVelocityVec(1);
initialVelocity2 = initVelocityVec(2);

massConst1 = mass1 + mass2;
massConst2 = mass2 - mass1;
massConst3 = mass1 - mass2;

collisionCount = 0;

collisionDirection = 'e';

finalVelocityVec = initVelocityVec;

grid on


while velocityCheck(initialVelocity1, initialVelocity2)
    
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
    
    
    finalVelocityVec = [finalVelocityVec; [finalVelocity1 finalVelocity2]];
    
    collisionCount = collisionCount + 1;
    
    fprintf('No. of Collisions: %d\n', collisionCount)
    
end

finalVelocity1 = finalVelocityVec(:,1);
finalVelocity2 = finalVelocityVec(:,2);

for i = 1:length(finalVelocityVec)
    
    xlim([initVelocityVec(2), abs(initVelocityVec(2))]);
    ylim([-sqrt(mass2), sqrt(mass2)]);
    
    hold on
    plot(finalVelocity2(i),finalVelocity1(i), 'o-b','linewidth', 20)
    
    xlabel('V_2','FontSize',12); 
    ylabel('V_1','FontSize',12);
    
    if i < length(finalVelocityVec)
        plot([finalVelocity2(i); finalVelocity2(i+1)],[finalVelocity1(i),...
            finalVelocity1(i+1)],'-')
    else
        continue
    end
    
    F(i) = getframe(gcf);
    
end

massVf1 = sqrt(mass1) .* finalVelocity1;
massVf2 = sqrt(mass2) .* finalVelocity2;

hold off

fig = figure();
hold on;
grid on;

for i = 1:length(finalVelocityVec)
    
    xlim([-sqrt(mass2), sqrt(mass2)]);
    ylim([-sqrt(mass2), sqrt(mass2)]);
    axis equal
    plot(massVf2(i),massVf1(i), 'o-b','linewidth', 20)
    
    if i < length(finalVelocityVec)
        plot([massVf2(i); massVf2(i+1)],[massVf1(i),...
            massVf1(i+1)],'-')
    else
        continue
    end
    
    xlabel('\surd(m_2)V_2','FontSize',12); 
    ylabel('\surd(m_1)V_1','FontSize',12);
    
    K(i) = getframe(gcf);
    
end




