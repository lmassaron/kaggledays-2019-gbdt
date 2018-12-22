File descriptions
training.csv - Training set of 250000 events, with an ID column, 30 feature columns, a weight column and a label column.
test.csv - Test set of 550000 events with an ID column and 30 feature columns.
random_submission - Sample submission file in the correct format. File format is described on the Evaluation page.
HiggsBosonCompetition_AMSMetric - Python script to calculate the competition evaluation metric.
For detailed information on the semantics of the features, labels, and weights, see the technical documentation from the LAL website on the task.

Some details to get started:

all variables are floating point, except PRI_jet_num which is integer
variables prefixed with PRI (for PRImitives) are “raw” quantities about the bunch collision as measured by the detector.
variables prefixed with DER (for DERived) are quantities computed from the primitive features, which were selected by  the physicists of ATLAS
it can happen that for some entries some variables are meaningless or cannot be computed; in this case, their value is −999.0, which is outside the normal range of all variables