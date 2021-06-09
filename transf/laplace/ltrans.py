from transf.expression_nodes.udfunc_expnode import UdFuncExpNode
from transf.expression_nodes.powern_expnode import PowerNExpNode
from transf.expression_nodes.constevalconst_expnode import ConstEvalConstExpNode
from transf.definitions.symbol import Symbol
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode
from transf.definitions.tokentype import TT
from transf.expression_nodes.trigfunc_expnode import TrigFuncExpNode

class LTrans:

    @staticmethod
    def trigFunc(expNode: TrigFuncExpNode):
        symbolToken = LexicalToken(TT.SYMBOL, tval=Symbol('s').val)
        param = expNode.param
        funcType = expNode.funcType

        if funcType == TT.SIN or funcType == TT.SINH:
            numer = param
        elif funcType == TT.COS or funcType == TT.COSH:
            numer = symbolToken

        if funcType == TT.SINH or funcType == TT.COSH:
            denom = BinaryNode(root=LexicalToken(TT.MINUS))
        elif funcType == TT.SIN or funcType == TT.COS:
            denom = BinaryNode(root=LexicalToken(TT.PLUS))

        denom.leftNode = PowerNExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=symbolToken,
            rightNode=LexicalToken(TT.INT, 2)
        )

        denom.rightNode = ConstEvalConstExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=param,
            rightNode=LexicalToken(TT.INT, 2)
        )

        return BinaryNode(
            root=LexicalToken(TT.DIVID),
            leftNode=numer,
            rightNode=denom
        )

    @staticmethod
    def udfunc(expNode: UdFuncExpNode):
        return 

        
