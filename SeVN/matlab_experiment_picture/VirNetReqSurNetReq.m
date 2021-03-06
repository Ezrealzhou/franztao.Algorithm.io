main;

experimentNodeUsed=DataProcess('Data\\Request_VirNet_');
experimentEdgeUsed=DataProcess('Data\\Request_SurNet_');
experimentNode=DataProcess('Data\\Request_VirNet_Accumulate_');
experimentEdge=DataProcess('Data\\Request_SurNet_Accumulate_');

experimentNodeUsed(:,1)=NaN;
experimentEdgeUsed(:,1)=NaN;

subplot(1,4,1);
hold on;
grid on;
axis tight
for i=1:1:AlgNum
    plot(plotXaxisValue,experimentNodeUsed(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end

subplot(1,4,2);
hold on;
grid on;
axis tight
for i=1:1:AlgNum
    plot(plotXaxisValue,experimentEdgeUsed(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end

subplot(1,4,3);
hold on;
grid on;
axis tight
for i=1:1:AlgNum-1
    plot(plotXaxisValue,experimentNode(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end

subplot(1,4,4);
hold on;
grid on;
axis tight
for i=1:1:AlgNum-1
    plot(plotXaxisValue,experimentEdge(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end

h=legend(LegendString,'Orientation','horizontal','FontSize',LegendSize);

set(h,'Fontsize',pictureLegendFont);
hold off;
if ~exist([FileAbsolutePath,'Data\\Fig'])
    mkdir([FileAbsolutePath,'Data\\Fig'])
end
saveas(gcf,[FileAbsolutePath,'Data\\Fig','\\VirNetReqSurNetReq','.eps']);
saveas(gcf,[FileAbsolutePath,'Data\\Fig','\\VirNetReqSurNetReq','.jpg']);
