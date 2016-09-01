


a = 9.010;
b = 8.926;
c = 5.344;


alpha = 44 + 27/60;
beta = 116 + 43/60;
gamma = 119 + 34/60;

deg2rad = pi/180.0;


% Convert angles to radians...
alpha *= deg2rad;
beta *= deg2rad;
gamma *= deg2rad;


% Convert to cartesian coords...
conversion = [ a b*cos(gamma)
               0 b*sin(gamma) ];
 
point = [  3 
          -1 ];
           
           
point_cc = conversion * point;
 
 
point_cc

% point_cc =    (31.434, -7.7637)

det_conversion = det(conversion);

det_conversion
