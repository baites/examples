function fig = resource_ceiling(x, y, z, atitle, model, mtitle, file)

% Set off plotting figures
set(0, 'DefaultFigureVisible', 'off')

% Substract initial time to the serie 
itime = x(1);
x = x - itime;

% Fit the curve with a given model
fitresult = fit(x, y, model);
% Get the function
f = fittype(model);
% Get parameters of the function
c = coeffvalues(fitresult);
p = mat2cell(c, 1, ones(1, numel(c)));
% Get confidence and predition intervals
ci = confint(fitresult, 0.95);
band = predint(fitresult, x, 0.95, 'observation', 'off');

% Plot the fit
fig = figure();
subplot(2,1,1)
fp = plot(fitresult, x, y, 'o');
set(fp, 'MarkerSize', 3)
set(fp, 'LineWidth', 1)
hold on
plot(x,band,'m--', 'LineWidth', 1)
title(mtitle, 'Color', 'r')
xlabel('Time [years]')
ylabel(atitle)
legend('data', model, 'upper', 'lower')
legend('boxoff')
legend('Location', 'NorthWest')
ylims = ylim();
ylim([0 ylims(2)*1.5])

% Plot the extrapolation
subplot(2,1,2)

% Compute the range of the plot
mx = x(1) + 10.0 * (x(end)-x(1));
ex = 0:1:mx;
ey = f(p{:}, ex');
[mR, iR] = min(abs(ey - 1.5*z));
ex = 0:1:ex(iR);
ey = f(p{:}, ex');

% Compute the ceiling point
[mR, iR] = min(abs(ey - z));
zx = ex(iR);
zy = ey(iR);

% Compute extrapolated predictions and plot
eband = predint(fitresult, ex, 0.95, 'observation', 'off');

fp = plot(fitresult, x, y, 'o');
set(fp, 'MarkerSize', 3)
set(fp, 'LineWidth', 1)
hold on
plot(ex, eband,'m--', 'LineWidth', 1)
ep = plot(ex, ey, 'Color', 'r');
set(ep, 'LineWidth', 1)

% Plot ceiling lines
xlims = xlim();
ylims = ylim();
plot(xlims, [zy zy], 'LineWidth', 1, 'Color', 'k')
[mA, iA] = min(abs(eband(:,2) - zy));
[mB, iB] = min(abs(eband(:,1) - zy));
rp = plot([zx zx], [0.0 ylims(2)], 'LineWidth', 1, 'Color', 'k');
rb = area([ex(iA) ex(iB)], [ylims(2) ylims(2)]);
set(rb, 'FaceColor', [0.9 0.9 0.9])
set(rb, 'EdgeColor', 'none')
xlabel('Time [years]')
ylabel(atitle)

% Invert the other of the plots and put axis on top
set(gca,'Children',flipud(get(gca,'Children')))
set(gca,'Layer','top')

ceilingPeriod = zx + itime;
ceilingPeriodRangeA = ex(iA) + itime;
ceilingPeriodRangeB = ex(iB) + itime;
ceilingPeriodStr = sprintf('Ceiling date %d\n', ceilingPeriod);
ceilingPeriodRangeStr = sprintf('Ceiling range [%d,%d]\n', ceilingPeriodRangeA, ceilingPeriodRangeB);

leg = legend([rp rb], ceilingPeriodStr, ceilingPeriodRangeStr);
set(leg, 'Box', 'off')
set(leg, 'Location', 'NorthWest')

rect = [0 0 1120 840];
set(gcf, 'OuterPosition', rect);
r = 100;
set(gcf, 'PaperPosition', rect/r);
print(fig, '-dsvg', file);
fprintf(ceilingPeriodStr)
fprintf(ceilingPeriodRangeStr)
