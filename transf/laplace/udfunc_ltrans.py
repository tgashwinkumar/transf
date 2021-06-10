from transf.expression_nodes.exponential_expnode import ExponentialExpNode
from transf.expression_nodes.power1_expnode import Power1ExpNode
from transf.definitions.symbol import Symbol
from transf.definitions.tokentype import TT
from transf.definitions.token import LexicalToken
from transf.expression_nodes.udfunc_expnode import UdFuncExpNode


def UDFuncLTrans(expNode: UdFuncExpNode):
    symbolToken = LexicalToken(TT.SYMBOL, tval=Symbol('s').val)
    param = expNode.param
    funcType = expNode.funcType
    if funcType == TT.DDELTA:

        if param.tokenVal == 0:
            return LexicalToken(TT.INT, 1)

        power = Power1ExpNode(
            root=LexicalToken(TT.MULTI),
            leftNode=LexicalToken(param.tokenType, param.tokenVal, isNeg=not param.isTokenNegative),
            rightNode=symbolToken
        )

        return ExponentialExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=LexicalToken(TT.EXP),
            rightNode=power
        )

    elif funcType == TT.USTEP:
        return 