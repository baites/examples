m = csvread('world-population.csv');
x = m(1:end,1);
y = m(1:end,2);
resource_ceiling(x, y, 15000000000, 'Population size', 'poly2', 'Population ceiling at 15B', 'world-population-projection.svg')
