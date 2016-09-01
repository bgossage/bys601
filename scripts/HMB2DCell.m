

chemical_formula = 'C_(12)H_(18)'

a = 9.010;
b = 8.926;

gamma = 170 + 34/60;

% Convert gamma to radians...
gamma *= pi/180.0;

gamma

% Convert to cartesian coords...
conversion = [ a b*cos(gamma)
               0 b*sin(gamma) ];
 
outline = [ 0 0 1 1 0
            1 0 0 1 1 ];
           
           
cc = conversion * outline;
 
x = cc(1,:);  # the first row of cc
y = cc(2,:);  # the second row of cc

x
y

cc

% Plot the unit cell...
plot( x, y, 'LineWidth', 2 ); 
axis equal
axis off
hold on           

disp( "from" ), disp( cc(2,1) )
disp( "to" ), disp( cc(2,2) )
%plot( cc(1,3)', cc(2,2)', '>', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
hold on

disp( "from" ), disp( cc(1,1) )
disp( "to" ), disp( cc(1,2) )
%plot( cc(1,1)', cc(1,2)', '>', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
