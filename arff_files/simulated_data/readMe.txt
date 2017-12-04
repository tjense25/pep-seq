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
into the neutral data. Half of the neutral peptides contains a half
match to one of the toxic or antitoxic motifs

Model performance:

