function ret = velocityCheck(vel1, vel2)

ret = 1;

if (vel1 >= 0 && vel2 >= 0)
    if(abs(vel1) <= (vel2))
        ret = 0;
    end
end

end