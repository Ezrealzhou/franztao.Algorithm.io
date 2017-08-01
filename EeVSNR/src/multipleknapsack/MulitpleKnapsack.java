/**
 * 
 */
package multipleknapsack;

import gurobi.*;

/**
 * @author franz
 *
 */
public class MulitpleKnapsack {
	public int itemNumber;
	public int knapsackNumber;
	public int matchingMatrix[][];

	public int unionKnapsackSize;
	public int ithKapsack2ithUnionKnapsack[];
	public int unionKnapsackCapacity[];
	public int capacityItem[];

	public MulitpleKnapsack(int row, int col, int unionKnapsackSize) {
		this.itemNumber = row;
		this.knapsackNumber = col;
		this.unionKnapsackSize = unionKnapsackSize;
		matchingMatrix = new int[row][col];
		ithKapsack2ithUnionKnapsack = new int[col];
		capacityItem = new int[row];
		unionKnapsackCapacity = new int[unionKnapsackSize];
	}

	public boolean optimalSoutionDP(int solution[]) {

		// int[] dims=new int[this.unionKnapsackSize+1];
		// dims[0]=this.itemNumber+1;
		// for(int i=0;i<this.unionKnapsackSize;i++){
		// dims[i+1]=this.unionKnapsackCapacity[i]+1;
		// }
		// Object dp=Array.newInstance(Integer.TYPE, dims);
		// System.out.println(dp.getClass().getName());
		// System.out.println(Array.getLength(dp));

		int dp[][];
		int select[][];
		int dimensionMultiple = 1;

		int radix[] = new int[this.unionKnapsackSize];
		for (int i = this.unionKnapsackSize - 1, j = 0; i >= 0; i--) {
			dimensionMultiple *= (this.unionKnapsackCapacity[i] + 1);
			radix[this.unionKnapsackSize - 1 - j] = dimensionMultiple;
			j++;
		}
		for (int i = 0; i < this.unionKnapsackSize - 1; i++) {
			radix[i] = radix[i + 1];
		}
		radix[this.unionKnapsackSize - 1] = 1;

		dp = new int[this.itemNumber + 1][dimensionMultiple];
		select = new int[this.itemNumber + 1][dimensionMultiple];
		// initial variable
		for (int i = 1; i <= this.itemNumber; i++) {
			for (int j = 0; j < dimensionMultiple; j++) {
				dp[i][j] = -1;
			}
		}
		for (int i = 1; i <= this.itemNumber; i++) {
			int dims[] = new int[this.unionKnapsackSize];
			int d;
			for (int j = 0; j < dimensionMultiple; j++) {
				for (int k = 0; k < this.knapsackNumber; k++) {
					if (this.matchingMatrix[i - 1][k] != Integer.MAX_VALUE) {
						int ithunionbag = this.ithKapsack2ithUnionKnapsack[k];
						if ((dims[ithunionbag] - this.capacityItem[i - 1]) > 0) {
							int newinteger = 0;
							for (int l = 0; l < this.unionKnapsackSize; l++) {
								if (l == ithunionbag) {
									newinteger += (radix[l] * (dims[l] - this.capacityItem[i - 1]));
								} else
									newinteger += (radix[l] * dims[l]);
							}
							if (dp[i - 1][newinteger] != -1) {
								if (dp[i][j] == -1) {
									dp[i][j] = dp[i - 1][newinteger] + this.matchingMatrix[i - 1][k];
									select[i][j] = ithunionbag;
								} else {
									// dp[i][j] = Math.min(dp[i][j],
									// dp[i - 1][newinteger] +
									// this.matchingMatrix[i - 1][k]);
									if (dp[i][j] > (dp[i - 1][newinteger] + this.matchingMatrix[i - 1][k])) {
										dp[i][j] = dp[i - 1][newinteger] + this.matchingMatrix[i - 1][k];
										select[i][j] = ithunionbag;
									}
								}
							}

						}
					}
				}
				d = this.unionKnapsackSize - 1;
				dims[d]++;
				//
				// for (int t = 0; t < this.unionKnapsackSize; t++) {
				// System.out.print(dims[t]+ " ");
				// }
				// System.out.println();

				while (dims[d] == (this.unionKnapsackCapacity[d] + 1)) {
					dims[d] -= (this.unionKnapsackCapacity[d] + 1);
					if (d != 0)
						dims[d - 1]++;
					else
						break;
					d--;
				}
			}
		}

		if (dp[this.itemNumber][dimensionMultiple - 1] != -1) {
			int index = this.itemNumber ;
			int recurse = dimensionMultiple - 1;
			while (index > 0) {
				solution[index-1] = select[index][recurse];
				recurse -= (radix[select[index][recurse]] * this.capacityItem[index-1]);
				index--;
			}
//			for(int i=0;i< this.itemNumber;i++){
//				System.out.println("+++"+solution[i]);
//			}
			System.out.println("----DP optimal solution: (" + dp[this.itemNumber][dimensionMultiple - 1] + ") ");
			return true;
		} else {
			System.out.println("----DP exist no optimal solution");
			return false;
		}
	}

	public boolean optimalSoutionILP(int solution[]) throws GRBException {
		GRBEnv env = new GRBEnv("franztao");
		GRBModel model = new GRBModel(env);
		GRBVar varx[][];
		varx = new GRBVar[this.itemNumber][this.knapsackNumber];

		// Create variables
		for (int i = 0; i < this.itemNumber; i++) {
			for (int j = 0; j < this.knapsackNumber; j++) {
				if (Integer.MAX_VALUE != this.matchingMatrix[i][j])
					varx[i][j] = model.addVar(0.0, 1.0, 0.0, GRB.BINARY, "r:" + i + " c:" + j);
				else

					varx[i][j] = model.addVar(0.0, 0.0, 0.0, GRB.BINARY, "r:" + i + " c:" + j);
			}
		}
		// Integrate new variables

		model.update();
		GRBLinExpr objexpr = new GRBLinExpr();
		// Set objective: minimize

		for (int i = 0; i < this.itemNumber; i++) {
			for (int j = 0; j < this.knapsackNumber; j++) {
				if (Integer.MAX_VALUE != this.matchingMatrix[i][j])
					objexpr.addTerm(this.matchingMatrix[i][j], varx[i][j]);
			}
		}
		// String path = System.getgetProperty("java.library.path");
		// System.out.println("Java path: " + path);
		model.setObjective(objexpr, GRB.MINIMIZE);
		// Add constraint
		for (int i = 0; i < this.itemNumber; i++) {
			GRBLinExpr conexpr1 = new GRBLinExpr();
			for (int j = 0; j < this.knapsackNumber; j++) {
				if (Integer.MAX_VALUE != this.matchingMatrix[i][j])
					conexpr1.addTerm(1.0, varx[i][j]);
			}
			model.addConstr(conexpr1, GRB.EQUAL, 1.0, "constraint_row =" + i);
		}
		GRBLinExpr conexpr1[] = new GRBLinExpr[this.unionKnapsackSize];

		for (int i = 0; i < this.unionKnapsackSize; i++) {
			conexpr1[i] = new GRBLinExpr();
		}
		for (int i = 0; i < this.knapsackNumber; i++) {
			for (int j = 0; j < this.itemNumber; j++) {
				if (Integer.MAX_VALUE != this.matchingMatrix[j][i])
					conexpr1[this.ithKapsack2ithUnionKnapsack[i]].addTerm(this.capacityItem[j], varx[j][i]);
			}
		}
		for (int i = 0; i < this.unionKnapsackSize; i++) {
			model.addConstr(conexpr1[i], GRB.LESS_EQUAL, this.unionKnapsackCapacity[i], "constraint_col <" + i);
		}

		model.optimize();
		int optimstatus = model.get(GRB.IntAttr.Status);
		if (optimstatus != GRB.OPTIMAL) {
			return false;
		}
		System.out.println("---ILP optimal solution: (" + model.get(GRB.DoubleAttr.ObjVal) + " )");
		for (int i = 0; i < this.itemNumber; i++) {
			for (int j = 0; j < this.knapsackNumber; j++) {
				if (1.0 == varx[i][j].get(GRB.DoubleAttr.X)) {
					solution[i] = j;
					System.out.println(j);
				}
			}
		}

		model.dispose();
		env.dispose();
		return true;
	}

}
