Simulated Pep-seq Data

Simulated_arff_1:
Contains simulated data from two motifs:
Toxic motif: C**VY**F
Antitoxic motif: HVV***G*
nuetral peptides are randomly generated and checked
to make sure they don't match with one of the above motifs

Model performance:
NaiveBayes TP Rate: 0.999
	   FP Rate: 0.001
	   Confusion Matrix:
	   toxic neutral antitoxic <--calssified as
	   968     0        0      | antitoxic
	     2   995        2      | neutral
	     0     0      970      | toxic

J48 Tree TP Rate: 0.998
	 FP Rate: 0.001
	 Confusion Matrix:
	 toxic neutral antitoxic <--calssified as
	   968     0        0      | antitoxic
	     4   994        1      | neutral
	     0     0      970      | toxic

SMO   	 TP Rate: 0.999
	 FP Rate: 0.000
	 Confusion Matrix:
           toxic neutral antitoxic <--calssified as
	   968     0        0      | antitoxic
	     4   997        2      | neutral
	     0     0      970      | toxic
 

simulated_arff_2:
contains same motifs as simulated_arff_1, but introduces more noise
into the neutral data. Half of the neutral peptides contain partial
matches to one of the toxic or antitoxic motifs

In this simulated data set the partial matches share 3 of the 4 positions 
of the toxic or antitoxic motif

Model performance:
NaiveBayes:	TP Rate: 0.999
		FP Rate: 0.000
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        974     0        0      | antitoxic
	        1     1909       3      | neutral
	        0       0       971     | toxic

J48 Tree:	TP Rate: 0.997
		FP Rate: 0.001
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        974     0        0      | antitoxic
	        6     1902       5      | neutral
	        0       0      971      | toxic

SMO: 		TP Rate: 1.000
		FP Rate: 0.000
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        974     0        0      | antitoxic
	        0     1912       1      | neutral
	        0       0      971      | toxic


simulated_arff_3:
Increases the number of toxic motifs in the data set
And increases noise. Note One of the toxic motifs is a partial
match to an antitoxic motif!!

Toxic motifs: 	C**VY**F
		**IL*D*S
		HV***NF*
Antitoxic motif: HVV***G*
		 **RRVR**

Model performance:
NaiveBayes:	TP Rate: 0.915
		FP Rate: 0.039
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        1961     1        12     | antitoxic
	        216     2393      291    | neutral
	        0        80      2136    | toxic

J48 Tree:	TP Rate: 0.974
		FP Rate: 0.015
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        1974     0      0      | antitoxic
	         2     2824     74     | neutral
	         0      105    2111    | toxic

SMO: 		TP Rate: 1.000
		FP Rate: 0.000
		Confusion Matrix:
		toxic neutral antitoxic <--calssified as
	        1974     0        0      | antitoxic
	         27    2982      81      | neutral
	         0       0      2216     | toxic


simulated_arff_4:
Created 100 toxic motifs, 100 antitoxic motifs, and 100 neutral motifs
For each motif created 100 peptides that matched that motif
Machine learning results showed significantly worse results
Naive Bayes: 0.517 TP Rate
J48 Tree: 0.746 
Random Forrest: 0.965


Appears that when the number of motifs increase the motif space becomes more
convoluted, Random Forrest still can calssify peptides correctly. Random
Forrest vastly outperforms other models.


Simulated_arff_5:
Scaled back the number of motifs in simulated_arff_4, instead only creating 10
of each motif. 
Machine Learning models did much better classifying!!
SMO: 0.964 TP Rate
Naive Bayes: 0.937
J48 Tree: 0.909
Random Forest: 0.994

J48 Tree was able to accurately classify most of them by looking only at 3
positions, even when there were four different essential positions in the
motif


