import xgboost as xgb
import sys
# read in data
dtrain = xgb.DMatrix(sys.argv[1])
dtest = xgb.DMatrix(sys.argv[2])
# specify parameters via map
# dep 3 round 200 eta 0.1 best
param = {'max_depth':3, 'eta':0.1, 'silent':1, 'objective':'reg:linear', 'eval_metric':'rmse'}
watchlist  = [(dtrain,'train'), (dtest, 'test')]
num_round = 200
bst = xgb.train(param, dtrain, num_round, watchlist)
# make prediction
pred_outfile = open(sys.argv[3], 'w')
preds = bst.predict(dtest)
for pred_val in preds:
    pred_outfile.write(str(pred_val) + '\n')
