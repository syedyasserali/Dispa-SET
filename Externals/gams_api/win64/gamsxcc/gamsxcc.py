# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_gamsxcc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_gamsxcc')
    _gamsxcc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gamsxcc', [dirname(__file__)])
        except ImportError:
            import _gamsxcc
            return _gamsxcc
        try:
            _mod = imp.load_module('_gamsxcc', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _gamsxcc = swig_import_helper()
    del swig_import_helper
else:
    import _gamsxcc
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _gamsxcc.new_intArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gamsxcc.delete_intArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _gamsxcc.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _gamsxcc.intArray___setitem__(self, index, value)

    def cast(self):
        return _gamsxcc.intArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_gamsxcc.intArray_frompointer)
    else:
        frompointer = _gamsxcc.intArray_frompointer
intArray_swigregister = _gamsxcc.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(t):
    return _gamsxcc.intArray_frompointer(t)
intArray_frompointer = _gamsxcc.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _gamsxcc.new_doubleArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gamsxcc.delete_doubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _gamsxcc.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _gamsxcc.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _gamsxcc.doubleArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_gamsxcc.doubleArray_frompointer)
    else:
        frompointer = _gamsxcc.doubleArray_frompointer
doubleArray_swigregister = _gamsxcc.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(t):
    return _gamsxcc.doubleArray_frompointer(t)
doubleArray_frompointer = _gamsxcc.doubleArray_frompointer


def new_intp():
    return _gamsxcc.new_intp()
new_intp = _gamsxcc.new_intp

def copy_intp(value):
    return _gamsxcc.copy_intp(value)
copy_intp = _gamsxcc.copy_intp

def delete_intp(obj):
    return _gamsxcc.delete_intp(obj)
delete_intp = _gamsxcc.delete_intp

def intp_assign(obj, value):
    return _gamsxcc.intp_assign(obj, value)
intp_assign = _gamsxcc.intp_assign

def intp_value(obj):
    return _gamsxcc.intp_value(obj)
intp_value = _gamsxcc.intp_value

def new_doublep():
    return _gamsxcc.new_doublep()
new_doublep = _gamsxcc.new_doublep

def copy_doublep(value):
    return _gamsxcc.copy_doublep(value)
copy_doublep = _gamsxcc.copy_doublep

def delete_doublep(obj):
    return _gamsxcc.delete_doublep(obj)
delete_doublep = _gamsxcc.delete_doublep

def doublep_assign(obj, value):
    return _gamsxcc.doublep_assign(obj, value)
doublep_assign = _gamsxcc.doublep_assign

def doublep_value(obj):
    return _gamsxcc.doublep_value(obj)
doublep_value = _gamsxcc.doublep_value

def new_gamsxHandle_tp():
    return _gamsxcc.new_gamsxHandle_tp()
new_gamsxHandle_tp = _gamsxcc.new_gamsxHandle_tp

def copy_gamsxHandle_tp(value):
    return _gamsxcc.copy_gamsxHandle_tp(value)
copy_gamsxHandle_tp = _gamsxcc.copy_gamsxHandle_tp

def delete_gamsxHandle_tp(obj):
    return _gamsxcc.delete_gamsxHandle_tp(obj)
delete_gamsxHandle_tp = _gamsxcc.delete_gamsxHandle_tp

def gamsxHandle_tp_assign(obj, value):
    return _gamsxcc.gamsxHandle_tp_assign(obj, value)
gamsxHandle_tp_assign = _gamsxcc.gamsxHandle_tp_assign

def gamsxHandle_tp_value(obj):
    return _gamsxcc.gamsxHandle_tp_value(obj)
gamsxHandle_tp_value = _gamsxcc.gamsxHandle_tp_value

def new_TBrkPCallBack1_tp():
    return _gamsxcc.new_TBrkPCallBack1_tp()
new_TBrkPCallBack1_tp = _gamsxcc.new_TBrkPCallBack1_tp

def copy_TBrkPCallBack1_tp(value):
    return _gamsxcc.copy_TBrkPCallBack1_tp(value)
copy_TBrkPCallBack1_tp = _gamsxcc.copy_TBrkPCallBack1_tp

def delete_TBrkPCallBack1_tp(obj):
    return _gamsxcc.delete_TBrkPCallBack1_tp(obj)
delete_TBrkPCallBack1_tp = _gamsxcc.delete_TBrkPCallBack1_tp

def TBrkPCallBack1_tp_assign(obj, value):
    return _gamsxcc.TBrkPCallBack1_tp_assign(obj, value)
TBrkPCallBack1_tp_assign = _gamsxcc.TBrkPCallBack1_tp_assign

def TBrkPCallBack1_tp_value(obj):
    return _gamsxcc.TBrkPCallBack1_tp_value(obj)
TBrkPCallBack1_tp_value = _gamsxcc.TBrkPCallBack1_tp_value

def new_TBrkPCallBack2_tp():
    return _gamsxcc.new_TBrkPCallBack2_tp()
new_TBrkPCallBack2_tp = _gamsxcc.new_TBrkPCallBack2_tp

def copy_TBrkPCallBack2_tp(value):
    return _gamsxcc.copy_TBrkPCallBack2_tp(value)
copy_TBrkPCallBack2_tp = _gamsxcc.copy_TBrkPCallBack2_tp

def delete_TBrkPCallBack2_tp(obj):
    return _gamsxcc.delete_TBrkPCallBack2_tp(obj)
delete_TBrkPCallBack2_tp = _gamsxcc.delete_TBrkPCallBack2_tp

def TBrkPCallBack2_tp_assign(obj, value):
    return _gamsxcc.TBrkPCallBack2_tp_assign(obj, value)
TBrkPCallBack2_tp_assign = _gamsxcc.TBrkPCallBack2_tp_assign

def TBrkPCallBack2_tp_value(obj):
    return _gamsxcc.TBrkPCallBack2_tp_value(obj)
TBrkPCallBack2_tp_value = _gamsxcc.TBrkPCallBack2_tp_value

def gamsxHandleToPtr(pgamsx):
    """gamsxHandleToPtr(pgamsx) -> void *"""
    return _gamsxcc.gamsxHandleToPtr(pgamsx)

def ptrTogamsxHandle(vptr):
    """ptrTogamsxHandle(vptr) -> gamsxHandle_t"""
    return _gamsxcc.ptrTogamsxHandle(vptr)

def gamsxGetReady(msgBufSize):
    """gamsxGetReady(msgBufSize) -> int"""
    return _gamsxcc.gamsxGetReady(msgBufSize)

def gamsxGetReadyD(dirName, msgBufSize):
    """gamsxGetReadyD(dirName, msgBufSize) -> int"""
    return _gamsxcc.gamsxGetReadyD(dirName, msgBufSize)

def gamsxGetReadyL(libName, msgBufSize):
    """gamsxGetReadyL(libName, msgBufSize) -> int"""
    return _gamsxcc.gamsxGetReadyL(libName, msgBufSize)

def gamsxCreate(pgamsx, msgBufSize):
    """gamsxCreate(pgamsx, msgBufSize) -> int"""
    return _gamsxcc.gamsxCreate(pgamsx, msgBufSize)

def gamsxCreateD(pgamsx, dirName, msgBufSize):
    """gamsxCreateD(pgamsx, dirName, msgBufSize) -> int"""
    return _gamsxcc.gamsxCreateD(pgamsx, dirName, msgBufSize)

def gamsxCreateL(pgamsx, libName, msgBufSize):
    """gamsxCreateL(pgamsx, libName, msgBufSize) -> int"""
    return _gamsxcc.gamsxCreateL(pgamsx, libName, msgBufSize)

def gamsxFree(pgamsx):
    """gamsxFree(pgamsx) -> int"""
    return _gamsxcc.gamsxFree(pgamsx)

def gamsxLibraryLoaded():
    """gamsxLibraryLoaded() -> int"""
    return _gamsxcc.gamsxLibraryLoaded()

def gamsxLibraryUnload():
    """gamsxLibraryUnload() -> int"""
    return _gamsxcc.gamsxLibraryUnload()

def gamsxGetScreenIndicator():
    """gamsxGetScreenIndicator() -> int"""
    return _gamsxcc.gamsxGetScreenIndicator()

def gamsxSetScreenIndicator(scrind):
    """gamsxSetScreenIndicator(scrind)"""
    return _gamsxcc.gamsxSetScreenIndicator(scrind)

def gamsxGetExceptionIndicator():
    """gamsxGetExceptionIndicator() -> int"""
    return _gamsxcc.gamsxGetExceptionIndicator()

def gamsxSetExceptionIndicator(excind):
    """gamsxSetExceptionIndicator(excind)"""
    return _gamsxcc.gamsxSetExceptionIndicator(excind)

def gamsxGetExitIndicator():
    """gamsxGetExitIndicator() -> int"""
    return _gamsxcc.gamsxGetExitIndicator()

def gamsxSetExitIndicator(extind):
    """gamsxSetExitIndicator(extind)"""
    return _gamsxcc.gamsxSetExitIndicator(extind)

def gamsxGetErrorCallback():
    """gamsxGetErrorCallback() -> gamsxErrorCallback_t"""
    return _gamsxcc.gamsxGetErrorCallback()

def gamsxSetErrorCallback(func):
    """gamsxSetErrorCallback(func)"""
    return _gamsxcc.gamsxSetErrorCallback(func)

def gamsxGetAPIErrorCount():
    """gamsxGetAPIErrorCount() -> int"""
    return _gamsxcc.gamsxGetAPIErrorCount()

def gamsxSetAPIErrorCount(ecnt):
    """gamsxSetAPIErrorCount(ecnt)"""
    return _gamsxcc.gamsxSetAPIErrorCount(ecnt)

def gamsxErrorHandling(msg):
    """gamsxErrorHandling(msg)"""
    return _gamsxcc.gamsxErrorHandling(msg)

def gamsxRunExecDLL(pgamsx, optPtr, sysDir, AVerbose):
    """gamsxRunExecDLL(pgamsx, optPtr, sysDir, AVerbose) -> int"""
    return _gamsxcc.gamsxRunExecDLL(pgamsx, optPtr, sysDir, AVerbose)

def gamsxShowError(pgamsx, fNameLog):
    """gamsxShowError(pgamsx, fNameLog) -> int"""
    return _gamsxcc.gamsxShowError(pgamsx, fNameLog)

def gamsxAddBreakPoint(pgamsx, fn, lineNr):
    """gamsxAddBreakPoint(pgamsx, fn, lineNr)"""
    return _gamsxcc.gamsxAddBreakPoint(pgamsx, fn, lineNr)

def gamsxClearBreakPoints(pgamsx):
    """gamsxClearBreakPoints(pgamsx)"""
    return _gamsxcc.gamsxClearBreakPoints(pgamsx)

def gamsxSystemInfo(pgamsx, arg2, arg3):
    """gamsxSystemInfo(pgamsx, arg2, arg3) -> int"""
    return _gamsxcc.gamsxSystemInfo(pgamsx, arg2, arg3)

def gamsxSymbolInfo(pgamsx, SyNr, arg5, arg6, arg7, arg8):
    """gamsxSymbolInfo(pgamsx, SyNr, arg5, arg6, arg7, arg8) -> int"""
    return _gamsxcc.gamsxSymbolInfo(pgamsx, SyNr, arg5, arg6, arg7, arg8)

def gamsxUelName(pgamsx, uel):
    """gamsxUelName(pgamsx, uel) -> char *"""
    return _gamsxcc.gamsxUelName(pgamsx, uel)

def gamsxFindSymbol(pgamsx, SyName):
    """gamsxFindSymbol(pgamsx, SyName) -> int"""
    return _gamsxcc.gamsxFindSymbol(pgamsx, SyName)

def gamsxDataReadRawStart(pgamsx, SyNr, INOUT):
    """gamsxDataReadRawStart(pgamsx, SyNr, INOUT) -> int"""
    return _gamsxcc.gamsxDataReadRawStart(pgamsx, SyNr, INOUT)

def gamsxDataReadRaw(pgamsx, INOUT):
    """gamsxDataReadRaw(pgamsx, INOUT) -> int"""
    return _gamsxcc.gamsxDataReadRaw(pgamsx, INOUT)

def gamsxDataReadDone(pgamsx):
    """gamsxDataReadDone(pgamsx) -> int"""
    return _gamsxcc.gamsxDataReadDone(pgamsx)

def gamsxDataWriteRawStart(pgamsx, SyNr, DoMerge):
    """gamsxDataWriteRawStart(pgamsx, SyNr, DoMerge) -> int"""
    return _gamsxcc.gamsxDataWriteRawStart(pgamsx, SyNr, DoMerge)

def gamsxDataWriteRaw(pgamsx, Elements, Vals):
    """gamsxDataWriteRaw(pgamsx, Elements, Vals) -> int"""
    return _gamsxcc.gamsxDataWriteRaw(pgamsx, Elements, Vals)

def gamsxDataWriteDone(pgamsx):
    """gamsxDataWriteDone(pgamsx) -> int"""
    return _gamsxcc.gamsxDataWriteDone(pgamsx)

def gamsxRegisterCB1(pgamsx, CB1, userMem):
    """gamsxRegisterCB1(pgamsx, CB1, userMem)"""
    return _gamsxcc.gamsxRegisterCB1(pgamsx, CB1, userMem)

def gamsxRegisterCB2(pgamsx, CB2, userMem1, userMem2):
    """gamsxRegisterCB2(pgamsx, CB2, userMem1, userMem2)"""
    return _gamsxcc.gamsxRegisterCB2(pgamsx, CB2, userMem1, userMem2)

def gamsxGetCB1(pgamsx):
    """gamsxGetCB1(pgamsx) -> TBrkPCallBack1_t"""
    return _gamsxcc.gamsxGetCB1(pgamsx)

def gamsxGetCB2(pgamsx):
    """gamsxGetCB2(pgamsx) -> TBrkPCallBack2_t"""
    return _gamsxcc.gamsxGetCB2(pgamsx)

def gamsxGetCB1UM(pgamsx):
    """gamsxGetCB1UM(pgamsx) -> void *"""
    return _gamsxcc.gamsxGetCB1UM(pgamsx)

def gamsxGetCB2UM1(pgamsx):
    """gamsxGetCB2UM1(pgamsx) -> void *"""
    return _gamsxcc.gamsxGetCB2UM1(pgamsx)

def gamsxGetCB2UM2(pgamsx):
    """gamsxGetCB2UM2(pgamsx) -> void *"""
    return _gamsxcc.gamsxGetCB2UM2(pgamsx)

def gamsxSWSet(pgamsx, x):
    """gamsxSWSet(pgamsx, x)"""
    return _gamsxcc.gamsxSWSet(pgamsx, x)

def gamsxStepThrough(pgamsx):
    """gamsxStepThrough(pgamsx) -> int"""
    return _gamsxcc.gamsxStepThrough(pgamsx)

def gamsxStepThroughSet(pgamsx, x):
    """gamsxStepThroughSet(pgamsx, x)"""
    return _gamsxcc.gamsxStepThroughSet(pgamsx, x)

def gamsxRunToEnd(pgamsx):
    """gamsxRunToEnd(pgamsx) -> int"""
    return _gamsxcc.gamsxRunToEnd(pgamsx)

def gamsxRunToEndSet(pgamsx, x):
    """gamsxRunToEndSet(pgamsx, x)"""
    return _gamsxcc.gamsxRunToEndSet(pgamsx, x)

def gamsxCB1Defined(pgamsx):
    """gamsxCB1Defined(pgamsx) -> int"""
    return _gamsxcc.gamsxCB1Defined(pgamsx)

def gamsxCB2Defined(pgamsx):
    """gamsxCB2Defined(pgamsx) -> int"""
    return _gamsxcc.gamsxCB2Defined(pgamsx)
GLOBAL_MAX_INDEX_DIM = _gamsxcc.GLOBAL_MAX_INDEX_DIM
GLOBAL_UEL_IDENT_SIZE = _gamsxcc.GLOBAL_UEL_IDENT_SIZE
ITERLIM_INFINITY = _gamsxcc.ITERLIM_INFINITY
GMS_MAX_INDEX_DIM = _gamsxcc.GMS_MAX_INDEX_DIM
GMS_UEL_IDENT_SIZE = _gamsxcc.GMS_UEL_IDENT_SIZE
GMS_SSSIZE = _gamsxcc.GMS_SSSIZE
GMS_VARTYPE_UNKNOWN = _gamsxcc.GMS_VARTYPE_UNKNOWN
GMS_VARTYPE_BINARY = _gamsxcc.GMS_VARTYPE_BINARY
GMS_VARTYPE_INTEGER = _gamsxcc.GMS_VARTYPE_INTEGER
GMS_VARTYPE_POSITIVE = _gamsxcc.GMS_VARTYPE_POSITIVE
GMS_VARTYPE_NEGATIVE = _gamsxcc.GMS_VARTYPE_NEGATIVE
GMS_VARTYPE_FREE = _gamsxcc.GMS_VARTYPE_FREE
GMS_VARTYPE_SOS1 = _gamsxcc.GMS_VARTYPE_SOS1
GMS_VARTYPE_SOS2 = _gamsxcc.GMS_VARTYPE_SOS2
GMS_VARTYPE_SEMICONT = _gamsxcc.GMS_VARTYPE_SEMICONT
GMS_VARTYPE_SEMIINT = _gamsxcc.GMS_VARTYPE_SEMIINT
GMS_VARTYPE_MAX = _gamsxcc.GMS_VARTYPE_MAX
GMS_EQUTYPE_E = _gamsxcc.GMS_EQUTYPE_E
GMS_EQUTYPE_G = _gamsxcc.GMS_EQUTYPE_G
GMS_EQUTYPE_L = _gamsxcc.GMS_EQUTYPE_L
GMS_EQUTYPE_N = _gamsxcc.GMS_EQUTYPE_N
GMS_EQUTYPE_X = _gamsxcc.GMS_EQUTYPE_X
GMS_EQUTYPE_C = _gamsxcc.GMS_EQUTYPE_C
GMS_EQUTYPE_MAX = _gamsxcc.GMS_EQUTYPE_MAX
GMS_VAL_LEVEL = _gamsxcc.GMS_VAL_LEVEL
GMS_VAL_MARGINAL = _gamsxcc.GMS_VAL_MARGINAL
GMS_VAL_LOWER = _gamsxcc.GMS_VAL_LOWER
GMS_VAL_UPPER = _gamsxcc.GMS_VAL_UPPER
GMS_VAL_SCALE = _gamsxcc.GMS_VAL_SCALE
GMS_VAL_MAX = _gamsxcc.GMS_VAL_MAX
sv_valund = _gamsxcc.sv_valund
sv_valna = _gamsxcc.sv_valna
sv_valpin = _gamsxcc.sv_valpin
sv_valmin = _gamsxcc.sv_valmin
sv_valeps = _gamsxcc.sv_valeps
sv_normal = _gamsxcc.sv_normal
sv_acronym = _gamsxcc.sv_acronym
GMS_SVIDX_UNDEF = _gamsxcc.GMS_SVIDX_UNDEF
GMS_SVIDX_NA = _gamsxcc.GMS_SVIDX_NA
GMS_SVIDX_PINF = _gamsxcc.GMS_SVIDX_PINF
GMS_SVIDX_MINF = _gamsxcc.GMS_SVIDX_MINF
GMS_SVIDX_EPS = _gamsxcc.GMS_SVIDX_EPS
GMS_SVIDX_NORMAL = _gamsxcc.GMS_SVIDX_NORMAL
GMS_SVIDX_ACR = _gamsxcc.GMS_SVIDX_ACR
GMS_SVIDX_MAX = _gamsxcc.GMS_SVIDX_MAX
dt_set = _gamsxcc.dt_set
dt_par = _gamsxcc.dt_par
dt_var = _gamsxcc.dt_var
dt_equ = _gamsxcc.dt_equ
dt_alias = _gamsxcc.dt_alias
GMS_DT_SET = _gamsxcc.GMS_DT_SET
GMS_DT_PAR = _gamsxcc.GMS_DT_PAR
GMS_DT_VAR = _gamsxcc.GMS_DT_VAR
GMS_DT_EQU = _gamsxcc.GMS_DT_EQU
GMS_DT_ALIAS = _gamsxcc.GMS_DT_ALIAS
GMS_DT_MAX = _gamsxcc.GMS_DT_MAX
GMS_SV_UNDEF = _gamsxcc.GMS_SV_UNDEF
GMS_SV_NA = _gamsxcc.GMS_SV_NA
GMS_SV_PINF = _gamsxcc.GMS_SV_PINF
GMS_SV_MINF = _gamsxcc.GMS_SV_MINF
GMS_SV_EPS = _gamsxcc.GMS_SV_EPS
GMS_SV_ACR = _gamsxcc.GMS_SV_ACR
GMS_SV_NAINT = _gamsxcc.GMS_SV_NAINT
# This file is compatible with both classic and new-style classes.

