%MappingCost_edge_sn_FD_EVSNR_Ran_NoShared
%MappingCost_node_sn_FD_EVSNR_Ran_NoShared
main;

dataVectorEdge=[];
dataVectorNode=[];
dataVectorNodeUsed=[];
dataVectorEdgeUsed=[];
Average=[];
for i=1:1:AlgNum
    dataNodeUsed=load([FileAbsolutePath,'Data\\Utilization_SubNode_',strtrim(AlgName(i,:)),'.txt']);
    dataEdgeUsed=load([FileAbsolutePath,'Data\\Utilization_SubEdge_',strtrim(AlgName(i,:)),'.txt']);
    
    dataNode=load([FileAbsolutePath,'Data\\Cost_NodeCp_',strtrim(AlgName(i,:)),'.txt']);
    dataEdge=load([FileAbsolutePath,'Data\\Cost_NdgeBw_',strtrim(AlgName(i,:)),'.txt']);
    dataVectorEdge=[dataVectorEdge;dataEdge'];
    dataVectorNode=[dataVectorNode;dataNode'];
    dataVectorNodeUsed=[dataVectorNodeUsed;dataNodeUsed'];
    dataVectorEdgeUsed=[dataVectorEdgeUsed;dataEdgeUsed'];
    
    alg=load([FileAbsolutePath,'Data\\Request_SurNet_',strtrim(AlgName(i,:)),'.txt']);
    Average=[Average;alg']
    %dataVector=load([FileAbsolutePath,'Data\\AcceptionRatio_Edge_sn_FD_EVSNR_Ran_NoShared.txt']);
end
[r,c]=size(dataVectorEdge);

experimentEdge=zeros(AlgNum,ExperimentPicturePlotNumber);
experimentNode=zeros(AlgNum,ExperimentPicturePlotNumber);
experimentNodeUsed=zeros(AlgNum,ExperimentPicturePlotNumber);
experimentEdgeUsed=zeros(AlgNum,ExperimentPicturePlotNumber);

experimentAverage=zeros(AlgNum,ExperimentPicturePlotNumber);

for i=1:1:AlgNum
    for j=1:1:c
        experimentEdge(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentEdge(i,mod(j-1,ExperimentPicturePlotNumber)+1)+dataVectorEdge(i,j);
        experimentNode(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentNode(i,mod(j-1,ExperimentPicturePlotNumber)+1)+dataVectorNode(i,j);
        experimentNodeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentNodeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)+dataVectorNodeUsed(i,j);
        experimentEdgeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentEdgeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)+dataVectorEdgeUsed(i,j);
        
        experimentAverage(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentAverage(i,mod(j-1,ExperimentPicturePlotNumber)+1)+Average(i,j);
        
    end
end
for i=1:1:AlgNum
    for j=1:1:ExperimentPicturePlotNumber
        experimentEdge(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentEdge(i,mod(j-1,ExperimentPicturePlotNumber)+1)*1.0/ExperimentTimes;
        experimentNode(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentNode(i,mod(j-1,ExperimentPicturePlotNumber)+1)*1.0/ExperimentTimes;
        experimentNodeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentNodeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)*1.0/ExperimentTimes;
        experimentEdgeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentEdgeUsed(i,mod(j-1,ExperimentPicturePlotNumber)+1)*1.0/ExperimentTimes;
        
        experimentAverage(i,mod(j-1,ExperimentPicturePlotNumber)+1)= experimentAverage(i,mod(j-1,ExperimentPicturePlotNumber)+1)*1.0/ExperimentTimes;
        
    end
end


plotXaxisValue=0:(SubstrateNewtorkRunTimeInterval/(ExperimentPicturePlotNumber-1)):SubstrateNewtorkRunTimeInterval;

experimentEdge=experimentEdge./experimentAverage;
experimentNode=experimentNode./experimentAverage;
experimentNodeUsed=experimentNodeUsed./experimentAverage;
experimentEdgeUsed=experimentEdgeUsed./experimentAverage;


subplot(1,2,1);

title('SubstrateNewtork Current Stress');
% plot(plotXaxisValue,experimentNode);
hold on;
grid on;
for i=1:1:AlgNum
    plot(plotXaxisValue,experimentNodeUsed(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end


subplot(1,2,2);
% plot(plotXaxisValue,experimentNode);
hold on;
grid on;
for i=1:1:AlgNum
    plot(plotXaxisValue,experimentEdgeUsed(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
end

% subplot(1,4,4);
% experimentEdgebNode=experimentNodeUsed.*addNewNodeCost+experimentEdge+(experimentNode*RelativeCostbetweenComputingBandwidth);
% % plot(plotXaxisValue,experimentEdgebNode);
% hold on;
% grid on;
% for i=1:1:AlgNum
%     plot(plotXaxisValue,experimentEdgebNode(i,:),strtrim(ALgLineStyle(i,:)),'LineWidth',pictureLineWidth,'MarkerFaceColor',strtrim(ALgLineBlockColor(i,:)));
% end
h=legend(LegendString,'Orientation','horizontal','FontSize',LegendSize);
set(h,'Fontsize',pictureLegendFont);
hold off;
if ~exist([FileAbsolutePath,'Data\\Fig'])
    mkdir([FileAbsolutePath,'Data\\Fig'])
end
% picture2_StressCurrentSubstrateNewtork
saveas(gcf,[FileAbsolutePath,'Data\\Fig','\\StressCurrentSubstrateNetwork','.eps']);
saveas(gcf,[FileAbsolutePath,'Data\\Fig','\\StressCurrentSubstrateNetwork','.jpg']);

