import theano
import theano.tensor as T
from theano_utils import pair_euclidean

def CategoricalCrossEntropy(y_true, y_pred):
    return T.nnet.categorical_crossentropy(y_pred, y_true).mean()

def SeqCCE(y_true, y_pred):
    shape = y_true.shape
    y_true = y_true.reshape((shape[0]*shape[1], shape[2]))
    y_pred = y_pred.reshape((shape[0]*shape[1], shape[2]))
    return CategoricalCrossEntropy(y_true, y_pred).mean()

def BinaryCrossEntropy(y_true, y_pred):
    return T.nnet.binary_crossentropy(y_pred, y_true).mean()

def MeanSquaredError(y_true, y_pred):
    return T.sqr(y_pred - y_true).mean()

def MeanAbsoluteError(y_true, y_pred):
    return T.abs_(y_pred - y_true).mean()

def SquaredHinge(y_true, y_pred):
    return T.sqr(T.maximum(1. - y_true * y_pred, 0.)).mean()

def Hinge(y_true, y_pred):
    return T.maximum(1. - y_true * y_pred, 0.).mean()

def PairEuclidean(y_true, y_pred):
    return pair_euclidean(y_pred, y_true).mean()

cce = CCE = CategoricalCrossEntropy
bce = BCE = BinaryCrossEntropy
mse = MSE = MeanSquaredError
mae = MAE = MeanAbsoluteError
