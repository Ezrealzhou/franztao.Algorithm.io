/**
 * 
 */

package evsnr;

public class Parameter {

  public static final int FailureDependent = 0;
  public static final int FailureIndependent = 1;
  public static final int One2OneProtection = 2;

  public static final int MatchMethodIP = 1;
  public static final int MatchMethodDP = 2;
  public static final int MatchMethod = MatchMethodIP;

  public static final int Ran = 0;
  public static final int Min = 1;

  // /home/franz/franzDocuments/eclipse4cworkspace/EeVSNR
  public static final String FileAbsolutePath = "C:\\Users\\Taoheng\\Desktop\\SeVN";

  //
  public static final boolean isNewCriter = true;

  // Parameter
  public static final int addNewVirNodeNewSubNodeCost = 10000000;
  public static final int addNewVirNodeCost = 100;
  public static final int transformExistedNodeCost = 100000;
  public static final int addNodeComputaionCost = 3;
  public static final int addEdgeBandwithCost = 1;
  public static final int RelativeCostbetweenComputingBandwidth = addNodeComputaionCost
      / addEdgeBandwithCost;

  public static final boolean IsSameVirNet4EveryTime = true;
  public static final boolean IsReleaseVNafterEVNFailure = false;
  public static final boolean IsMultipleNodeMapOneNode = true;
  public static final boolean IsConsiderEdgeBandwith = true;
  public static final int ExperimentTimes = 50;

  public static final long SubstrateNewtorkRunTimeInterval = 600;// 30000
  public static final long unitTimeInterval = 1;
  public static final double RequestAppearProbability = 1;// 0.1
  public static final double RequestPerTimeAppearNum = 1;// 0.1
  public static final long VirNetDuration = 1;
  public static final long VNRequestsContinueTimeMinimum = 1;
  public static final long VNRequestsContinueTimeMaximum = 100;
  public static final long VNRequestsContinueTimeAverage = VNRequestsContinueTimeMaximum / 2;
  // ExperimentPicture
  public static final int ExperimentPicturePlotNumber = 15;

  // service parameter
  public static final int ServiceNumber = 20;// 15
  public static final double SerivecProbability = 0.5;// 0.5

  // SubStrate Network Parameter
  // node parameter
  public static final int SubStrateNodeSize = 30;// 100
  public static final int SubStrateNodeComputationMinimum = 10;// 50
  public static final int SubStrateNodeComputationMaximum = 30;// 100
  // edge parameter
  public static final double SubStrateNodenodeProbability = 0.75;
  public static final int SubStrateEdgeBandwithMinimum = 100;
  public static final int SubStrateEdgeBandwithMaximum = 200;

  // Virtual Network
  // node parameter //2-5 5-8 5-10
  public static final int VirtualNodeSizeMinimum = 3;// 2
  public static final int VirtualNodeSizeMaximum = 8;// 10
  public static final int VirtualNodeComputationMinimum = 5;// 1
  public static final int VirtualNodeComputationMaximum = 10;// 5
  // edge parameter
  public static final double VirtualNodenodeProbability = 0.8;// 0.5
  public static final int VirtualEdgeBandwithMinimum = 10;// 10
  public static final int VirtualEdgeBandwithMaximum = 20;// 20

  public static final long SubStrateFacilityNodeFailDuration = SubstrateNewtorkRunTimeInterval
      / ExperimentPicturePlotNumber;

}
