function ret = velocityCheck(vel1, vel2)

ret = True;
if (vel1 <= 0 && vel2 <=0)
    if(abs(vel1) >= abs(vel2))
        ret = False;
    end
end

end