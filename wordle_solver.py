#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x66c32154

# Compiled with Coconut version 1.6.0 [Vocational Guidance Counsellor]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    from __builtin__ import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_raw_input, py_xrange, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange, repr
    _coconut_py_raw_input, _coconut_py_xrange, _coconut_py_int, _coconut_py_long, _coconut_py_print, _coconut_py_str, _coconut_py_unicode, _coconut_py_repr = raw_input, xrange, int, long, print, str, unicode, repr
    from future_builtins import *
    chr, str = unichr, unicode
    from io import open
    class object(object):
        __slots__ = ()
        def __ne__(self, other):
            eq = self == other
            return _coconut.NotImplemented if eq is _coconut.NotImplemented else not eq
    class int(_coconut_py_int):
        __slots__ = ()
        if hasattr(_coconut_py_int, "__doc__"):
            __doc__ = _coconut_py_int.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return _coconut.isinstance(inst, (_coconut_py_int, _coconut_py_long))
            def __subclasscheck__(cls, subcls):
                return _coconut.issubclass(subcls, (_coconut_py_int, _coconut_py_long))
    class range(object):
        __slots__ = ("_xrange",)
        if hasattr(_coconut_py_xrange, "__doc__"):
            __doc__ = _coconut_py_xrange.__doc__
        def __init__(self, *args):
            self._xrange = _coconut_py_xrange(*args)
        def __iter__(self):
            return _coconut.iter(self._xrange)
        def __reversed__(self):
            return _coconut.reversed(self._xrange)
        def __len__(self):
            return _coconut.len(self._xrange)
        def __contains__(self, elem):
            return elem in self._xrange
        def __getitem__(self, index):
            if _coconut.isinstance(index, _coconut.slice):
                args = _coconut.slice(*self._args)
                start, stop, step = (args.start if args.start is not None else 0), args.stop, (args.step if args.step is not None else 1)
                if index.start is None:
                    new_start = start if index.step is None or index.step >= 0 else stop - step
                elif index.start >= 0:
                    new_start = start + step * index.start
                    if (step >= 0 and new_start >= stop) or (step < 0 and new_start <= stop):
                        new_start = stop
                else:
                    new_start = stop + step * index.start
                    if (step >= 0 and new_start <= start) or (step < 0 and new_start >= start):
                        new_start = start
                if index.stop is None:
                    new_stop = stop if index.step is None or index.step >= 0 else start - step
                elif index.stop >= 0:
                    new_stop = start + step * index.stop
                    if (step >= 0 and new_stop >= stop) or (step < 0 and new_stop <= stop):
                        new_stop = stop
                else:
                    new_stop = stop + step * index.stop
                    if (step >= 0 and new_stop <= start) or (step < 0 and new_stop >= start):
                        new_stop = start
                new_step = step if index.step is None else step * index.step
                return self.__class__(new_start, new_stop, new_step)
            else:
                return self._xrange[index]
        def count(self, elem):
            """Count the number of times elem appears in the range."""
            return _coconut_py_int(elem in self._xrange)
        def index(self, elem):
            """Find the index of elem in the range."""
            if elem not in self._xrange: raise _coconut.ValueError(_coconut.repr(elem) + " is not in range")
            start, _, step = self._xrange.__reduce_ex__(2)[1]
            return (elem - start) // step
        def __repr__(self):
            return _coconut.repr(self._xrange)[1:]
        @property
        def _args(self):
            return self._xrange.__reduce__()[1]
        def __reduce_ex__(self, protocol):
            return (self.__class__, self._xrange.__reduce_ex__(protocol)[1])
        def __reduce__(self):
            return self.__reduce_ex__(_coconut.pickle.DEFAULT_PROTOCOL)
        def __hash__(self):
            return _coconut.hash(self._args)
        def __copy__(self):
            return self.__class__(*self._args)
        def __eq__(self, other):
            return self.__class__ is other.__class__ and self._args == other._args
    from collections import Sequence as _coconut_Sequence
    _coconut_Sequence.register(range)
    from functools import wraps as _coconut_wraps
    @_coconut_wraps(_coconut_py_print)
    def print(*args, **kwargs):
        file = kwargs.get("file", _coconut_sys.stdout)
        if "flush" in kwargs:
            flush = kwargs["flush"]
            del kwargs["flush"]
        else:
            flush = False
        if _coconut.getattr(file, "encoding", None) is not None:
            _coconut_py_print(*(_coconut_py_unicode(x).encode(file.encoding) for x in args), **kwargs)
        else:
            _coconut_py_print(*args, **kwargs)
        if flush:
            file.flush()
    @_coconut_wraps(_coconut_py_raw_input)
    def input(*args, **kwargs):
        if _coconut.getattr(_coconut_sys.stdout, "encoding", None) is not None:
            return _coconut_py_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
        return _coconut_py_raw_input(*args, **kwargs).decode()
    @_coconut_wraps(_coconut_py_repr)
    def repr(obj):
        import __builtin__
        try:
            __builtin__.repr = _coconut_repr
            if isinstance(obj, _coconut_py_unicode):
                return _coconut_py_unicode(_coconut_py_repr(obj)[1:])
            if isinstance(obj, _coconut_py_str):
                return "b" + _coconut_py_unicode(_coconut_py_repr(obj))
            return _coconut_py_unicode(_coconut_py_repr(obj))
        finally:
            __builtin__.repr = _coconut_py_repr
    ascii = _coconut_repr = repr
    def raw_input(*args):
        """Coconut uses Python 3 'input' instead of Python 2 'raw_input'."""
        raise _coconut.NameError("Coconut uses Python 3 'input' instead of Python 2 'raw_input'")
    def xrange(*args):
        """Coconut uses Python 3 'range' instead of Python 2 'xrange'."""
        raise _coconut.NameError("Coconut uses Python 3 'range' instead of Python 2 'xrange'")
    def _coconut_exec(obj, globals=None, locals=None):
        if locals is None:
            locals = _coconut_sys._getframe(1).f_locals if globals is None else globals
        if globals is None:
            globals = _coconut_sys._getframe(1).f_globals
        exec(obj, globals, locals)
    def _coconut_default_breakpointhook(*args, **kwargs):
        hookname = _coconut.os.getenv("PYTHONBREAKPOINT")
        if hookname != "0":
            if not hookname:
                hookname = "pdb.set_trace"
            modname, dot, funcname = hookname.rpartition(".")
            if not dot:
                modname = "builtins" if _coconut_sys.version_info >= (3,) else "__builtin__"
            if _coconut_sys.version_info >= (2, 7):
                import importlib
                module = importlib.import_module(modname)
            else:
                import imp
                module = imp.load_module(modname, *imp.find_module(modname))
            hook = _coconut.getattr(module, funcname)
            return hook(*args, **kwargs)
    if not hasattr(_coconut_sys, "__breakpointhook__"):
        _coconut_sys.__breakpointhook__ = _coconut_default_breakpointhook
    def breakpoint(*args, **kwargs):
        return _coconut.getattr(_coconut_sys, "breakpointhook", _coconut_default_breakpointhook)(*args, **kwargs)
    if _coconut_sys.version_info < (2, 7):
        import functools as _coconut_functools, copy_reg as _coconut_copy_reg
        def _coconut_new_partial(func, args, keywords):
            return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
        _coconut_copy_reg.constructor(_coconut_new_partial)
        def _coconut_reduce_partial(self):
            return (_coconut_new_partial, (self.func, self.args, self.keywords))
        _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)
else:
    from builtins import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, repr
    _coconut_py_str = str
    exec("_coconut_exec = exec")
    if _coconut_sys.version_info < (3, 7):
        def _coconut_default_breakpointhook(*args, **kwargs):
            hookname = _coconut.os.getenv("PYTHONBREAKPOINT")
            if hookname != "0":
                if not hookname:
                    hookname = "pdb.set_trace"
                modname, dot, funcname = hookname.rpartition(".")
                if not dot:
                    modname = "builtins" if _coconut_sys.version_info >= (3,) else "__builtin__"
                if _coconut_sys.version_info >= (2, 7):
                    import importlib
                    module = importlib.import_module(modname)
                else:
                    import imp
                    module = imp.load_module(modname, *imp.find_module(modname))
                hook = _coconut.getattr(module, funcname)
                return hook(*args, **kwargs)
        if not hasattr(_coconut_sys, "__breakpointhook__"):
            _coconut_sys.__breakpointhook__ = _coconut_default_breakpointhook
        def breakpoint(*args, **kwargs):
            return _coconut.getattr(_coconut_sys, "breakpointhook", _coconut_default_breakpointhook)(*args, **kwargs)
    else:
        py_breakpoint = breakpoint
class _coconut(object):
    import collections, copy, functools, types, itertools, operator, threading, os, warnings, contextlib, traceback, weakref, multiprocessing
    from multiprocessing import dummy as multiprocessing_dummy
    if _coconut_sys.version_info < (3, 2):
        try:
            from backports.functools_lru_cache import lru_cache
            functools.lru_cache = lru_cache
        except ImportError:
            class you_need_to_install_backports_functools_lru_cache(object): pass
            functools.lru_cache = you_need_to_install_backports_functools_lru_cache()
    if _coconut_sys.version_info < (3, 4):
        try:
            import trollius as asyncio
        except ImportError:
            class you_need_to_install_trollius(object): pass
            asyncio = you_need_to_install_trollius()
    else:
        import asyncio
    if _coconut_sys.version_info < (3,):
        import cPickle as pickle
    else:
        import pickle
    OrderedDict = collections.OrderedDict if _coconut_sys.version_info >= (2, 7) else dict
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    if _coconut_sys.version_info < (3, 6):
        class typing(object):
            @staticmethod
            def NamedTuple(name, fields):
                return _coconut.collections.namedtuple(name, [x for x, t in fields])
    else:
        import typing
    zip_longest = itertools.zip_longest if _coconut_sys.version_info >= (3,) else itertools.izip_longest
    Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, any, bytes, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, slice, str, sum, super, tuple, type, vars, zip, repr, print, bytearray = Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, any, bytes, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, slice, str, sum, super, tuple, type, vars, zip, staticmethod(repr), staticmethod(print), bytearray
class _coconut_sentinel(object): pass
class _coconut_base_hashable(object):
    __slots__ = ()
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.__reduce__() == other.__reduce__()
    def __hash__(self):
        return _coconut.hash(self.__reduce__())
class MatchError(_coconut_base_hashable, Exception):
    """Pattern-matching error. Has attributes .pattern, .value, and .message."""
    __slots__ = ("pattern", "value", "_message")
    max_val_repr_len = 500
    def __init__(self, pattern=None, value=None):
        self.pattern = pattern
        self.value = value
        self._message = None
    @property
    def message(self):
        if self._message is None:
            value_repr = _coconut.repr(self.value)
            self._message = "pattern-matching failed for %s in %s" % (_coconut.repr(self.pattern), value_repr if _coconut.len(value_repr) <= self.max_val_repr_len else value_repr[:self.max_val_repr_len] + "...")
            Exception.__init__(self, self._message)
        return self._message
    def __repr__(self):
        self.message
        return Exception.__repr__(self)
    def __str__(self):
        self.message
        return Exception.__str__(self)
    def __unicode__(self):
        self.message
        return Exception.__unicode__(self)
    def __reduce__(self):
        return (self.__class__, (self.pattern, self.value))
class _coconut_tail_call(object):
    __slots__ = ("func", "args", "kwargs")
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
_coconut_tco_func_dict = {}
def _coconut_tco(func):
    @_coconut.functools.wraps(func)
    def tail_call_optimized_func(*args, **kwargs):
        call_func = func
        while True:
            if _coconut.isinstance(call_func, _coconut_base_pattern_func):
                call_func = call_func._coconut_tco_func
            elif _coconut.isinstance(call_func, _coconut.types.MethodType):
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func.__func__))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func.__func__:
                    if call_func.__self__ is None:
                        call_func = call_func._coconut_tco_func
                    else:
                        call_func = _coconut.functools.partial(call_func._coconut_tco_func, call_func.__self__)
            else:
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func:
                    call_func = call_func._coconut_tco_func
            result = call_func(*args, **kwargs)  # pass --no-tco to clean up your traceback
            if not isinstance(result, _coconut_tail_call):
                return result
            call_func, args, kwargs = result.func, result.args, result.kwargs
    tail_call_optimized_func._coconut_tco_func = func
    tail_call_optimized_func.__module__ = _coconut.getattr(func, "__module__", None)
    tail_call_optimized_func.__name__ = _coconut.getattr(func, "__name__", None)
    tail_call_optimized_func.__qualname__ = _coconut.getattr(func, "__qualname__", None)
    _coconut_tco_func_dict[_coconut.id(tail_call_optimized_func)] = _coconut.weakref.ref(tail_call_optimized_func)
    return tail_call_optimized_func
def _coconut_igetitem(iterable, index):
    obj_igetitem = _coconut.getattr(iterable, "__iter_getitem__", None)
    if obj_igetitem is None:
        obj_igetitem = _coconut.getattr(iterable, "__getitem__", None)
    if obj_igetitem is not None:
        try:
            result = obj_igetitem(index)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if not _coconut.isinstance(index, _coconut.slice):
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        try:
            return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
        except _coconut.StopIteration:
            raise _coconut.IndexError("$[] index out of range")
    if index.start is not None and index.start < 0 and (index.stop is None or index.stop < 0) and index.step is None:
        queue = _coconut.collections.deque(iterable, maxlen=-index.start)
        if index.stop is not None:
            queue = _coconut.list(queue)[:index.stop - index.start]
        return queue
    if (index.start is None or index.start == 0) and index.stop is None and index.step is not None and index.step == -1:
        obj_reversed = _coconut.getattr(iterable, "__reversed__", None)
        if obj_reversed is not None:
            try:
                result = obj_reversed()
            except _coconut.NotImplementedError:
                pass
            else:
                if result is not _coconut.NotImplemented:
                    return result
    if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.list(iterable)[index]
    return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_base_compose(_coconut_base_hashable):
    __slots__ = ("func", "funcstars")
    def __init__(self, func, *funcstars):
        self.func = func
        self.funcstars = []
        for f, stars in funcstars:
            if _coconut.isinstance(f, _coconut_base_compose):
                self.funcstars.append((f.func, stars))
                self.funcstars += f.funcstars
            else:
                self.funcstars.append((f, stars))
        self.funcstars = _coconut.tuple(self.funcstars)
    def __call__(self, *args, **kwargs):
        arg = self.func(*args, **kwargs)
        for f, stars in self.funcstars:
            if stars == 0:
                arg = f(arg)
            elif stars == 1:
                arg = f(*arg)
            elif stars == 2:
                arg = f(**arg)
            else:
                raise _coconut.ValueError("invalid arguments to " + _coconut.repr(self))
        return arg
    def __repr__(self):
        return _coconut.repr(self.func) + " " + " ".join(("..*> " if star == 1 else "..**>" if star == 2 else "..> ") + _coconut.repr(f) for f, star in self.funcstars)
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.funcstars)
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if _coconut_sys.version_info < (3,):
            return _coconut.types.MethodType(self, obj, objtype)
        else:
            return _coconut.types.MethodType(self, obj)
def _coconut_forward_compose(func, *funcs): return _coconut_base_compose(func, *((f, 0) for f in funcs))
def _coconut_back_compose(*funcs): return _coconut_forward_compose(*_coconut.reversed(funcs))
def _coconut_forward_star_compose(func, *funcs): return _coconut_base_compose(func, *((f, 1) for f in funcs))
def _coconut_back_star_compose(*funcs): return _coconut_forward_star_compose(*_coconut.reversed(funcs))
def _coconut_forward_dubstar_compose(func, *funcs): return _coconut_base_compose(func, *((f, 2) for f in funcs))
def _coconut_back_dubstar_compose(*funcs): return _coconut_forward_dubstar_compose(*_coconut.reversed(funcs))
def _coconut_pipe(x, f): return f(x)
def _coconut_star_pipe(xs, f): return f(*xs)
def _coconut_dubstar_pipe(kws, f): return f(**kws)
def _coconut_back_pipe(f, x): return f(x)
def _coconut_back_star_pipe(f, xs): return f(*xs)
def _coconut_back_dubstar_pipe(f, kws): return f(**kws)
def _coconut_none_pipe(x, f): return None if x is None else f(x)
def _coconut_none_star_pipe(xs, f): return None if xs is None else f(*xs)
def _coconut_none_dubstar_pipe(kws, f): return None if kws is None else f(**kws)
def _coconut_assert(cond, msg=None): assert cond, msg if msg is not None else "(assert) got falsey value " + _coconut.repr(cond)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_none_coalesce(a, b): return a if a is not None else b
def _coconut_minus(a, *rest):
    if not rest:
        return -a
    for b in rest:
        a = a - b
    return a
@_coconut.functools.wraps(_coconut.itertools.tee)
def tee(iterable, n=2):
    if n >= 0 and _coconut.isinstance(iterable, (_coconut.tuple, _coconut.frozenset)):
        return (iterable,) * n
    if n > 0 and (_coconut.isinstance(iterable, _coconut.abc.Sequence) or _coconut.getattr(iterable, "__copy__", None) is not None):
        return (iterable,) + _coconut.tuple(_coconut.copy.copy(iterable) for _ in _coconut.range(n - 1))
    return _coconut.itertools.tee(iterable, n)
class reiterable(_coconut_base_hashable):
    """Allows an iterator to be iterated over multiple times."""
    __slots__ = ("lock", "iter")
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut_reiterable):
            return iterable
        self = _coconut.object.__new__(cls)
        self.lock = _coconut.threading.Lock()
        self.iter = iterable
        return self
    def get_new_iter(self):
        with self.lock:
            self.iter, new_iter = _coconut_tee(self.iter)
        return new_iter
    def __iter__(self):
        return _coconut.iter(self.get_new_iter())
    def __getitem__(self, index):
        return _coconut_igetitem(self.get_new_iter(), index)
    def __reversed__(self):
        return _coconut_reversed(self.get_new_iter())
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reiterable(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    def __fmap__(self, func):
        return _coconut_map(func, self)
class scan(_coconut_base_hashable):
    """Reduce func over iterable, yielding intermediate results,
    optionally starting from initializer."""
    __slots__ = ("func", "iter", "initializer")
    def __init__(self, function, iterable, initializer=_coconut_sentinel):
        self.func = function
        self.iter = iterable
        self.initializer = initializer
    def __iter__(self):
        acc = self.initializer
        if acc is not _coconut_sentinel:
            yield acc
        for item in self.iter:
            if acc is _coconut_sentinel:
                acc = item
            else:
                acc = self.func(acc, item)
            yield acc
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "scan(%r, %r)" % (self.func, self.iter) if self.initializer is _coconut_sentinel else "scan(%r, %r, %r)" % (self.func, self.iter, self.initializer)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter, self.initializer))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class reversed(_coconut_base_hashable):
    __slots__ = ("iter",)
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.reversed.__doc__
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut.range):
            return iterable[::-1]
        if not _coconut.hasattr(iterable, "__reversed__") or _coconut.isinstance(iterable, (_coconut.list, _coconut.tuple)):
            return _coconut.object.__new__(cls)
        return _coconut.reversed(iterable)
    def __init__(self, iterable):
        self.iter = iterable
    def __iter__(self):
        return _coconut.iter(_coconut.reversed(self.iter))
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return _coconut_igetitem(self.iter, _coconut.slice(-(index.start + 1) if index.start is not None else None, -(index.stop + 1) if index.stop else None, -(index.step if index.step is not None else 1)))
        return _coconut_igetitem(self.iter, -(index + 1))
    def __reversed__(self):
        return self.iter
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reversed(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __contains__(self, elem):
        return elem in self.iter
    def count(self, elem):
        """Count the number of times elem appears in the reversed iterable."""
        return self.iter.count(elem)
    def index(self, elem):
        """Find the index of elem in the reversed iterable."""
        return _coconut.len(self.iter) - self.iter.index(elem) - 1
    def __fmap__(self, func):
        return self.__class__(_coconut_map(func, self.iter))
class flatten(_coconut_base_hashable):
    """Flatten an iterable of iterables into a single iterable."""
    __slots__ = ("iter",)
    def __init__(self, iterable):
        self.iter = iterable
    def __iter__(self):
        return _coconut.itertools.chain.from_iterable(self.iter)
    def __reversed__(self):
        return self.__class__(_coconut_reversed(_coconut_map(_coconut_reversed, self.iter)))
    def __repr__(self):
        return "flatten(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __contains__(self, elem):
        self.iter, new_iter = _coconut_tee(self.iter)
        return _coconut.any(elem in it for it in new_iter)
    def count(self, elem):
        """Count the number of times elem appears in the flattened iterable."""
        self.iter, new_iter = _coconut_tee(self.iter)
        return _coconut.sum(it.count(elem) for it in new_iter)
    def index(self, elem):
        self.iter, new_iter = _coconut_tee(self.iter)
        ind = 0
        for it in new_iter:
            try:
                return ind + it.index(elem)
            except _coconut.ValueError:
                ind += _coconut.len(it)
        raise ValueError("%r not in %r" % (elem, self))
    def __fmap__(self, func):
        return self.__class__(_coconut_map(_coconut.functools.partial(_coconut_map, func), self.iter))
class map(_coconut_base_hashable, _coconut.map):
    __slots__ = ("func", "iters")
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.map.__doc__
    def __new__(cls, function, *iterables):
        new_map = _coconut.map.__new__(cls, function, *iterables)
        new_map.func = function
        new_map.iters = iterables
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, *(_coconut_igetitem(i, index) for i in self.iters))
        return self.func(*(_coconut_igetitem(i, index) for i in self.iters))
    def __reversed__(self):
        return self.__class__(self.func, *(_coconut_reversed(i) for i in self.iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "map(%r, %s)" % (self.func, ", ".join((_coconut.repr(i) for i in self.iters)))
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.iters)
    def __iter__(self):
        return _coconut.iter(_coconut.map(self.func, *self.iters))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), *self.iters)
class _coconut_parallel_concurrent_map_func_wrapper(_coconut_base_hashable):
    __slots__ = ("map_cls", "func", "star")
    def __init__(self, map_cls, func, star):
        self.map_cls = map_cls
        self.func = func
        self.star = star
    def __reduce__(self):
        return (self.__class__, (self.map_cls, self.func, self.star))
    def __call__(self, *args, **kwargs):
        self.map_cls.get_pool_stack().append(None)
        try:
            if self.star:
                assert _coconut.len(args) == 1, "internal parallel/concurrent map error"
                return self.func(*args[0], **kwargs)
            else:
                return self.func(*args, **kwargs)
        except:
            _coconut.print(self.map_cls.__name__ + " error:")
            _coconut.traceback.print_exc()
            raise
        finally:
            assert self.map_cls.get_pool_stack().pop() is None, "internal parallel/concurrent map error"
class _coconut_base_parallel_concurrent_map(map):
    __slots__ = ("result", "chunksize")
    @classmethod
    def get_pool_stack(cls):
        return cls.threadlocal_ns.__dict__.setdefault("pool_stack", [None])
    def __new__(cls, function, *iterables, **kwargs):
        self = _coconut_map.__new__(cls, function, *iterables)
        self.result = None
        self.chunksize = kwargs.pop("chunksize", 1)
        if kwargs:
            raise _coconut.TypeError(cls.__name__ + "() got unexpected keyword arguments " + _coconut.repr(kwargs))
        if cls.get_pool_stack()[-1] is not None:
            return self.get_list()
        return self
    @classmethod
    @_coconut.contextlib.contextmanager
    def multiple_sequential_calls(cls, max_workers=None):
        """Context manager that causes nested calls to use the same pool."""
        if cls.get_pool_stack()[-1] is None:
            cls.get_pool_stack()[-1] = cls.make_pool(max_workers)
            try:
                yield
            finally:
                cls.get_pool_stack()[-1].terminate()
                cls.get_pool_stack()[-1] = None
        else:
            yield
    def get_list(self):
        if self.result is None:
            with self.multiple_sequential_calls():
                if _coconut.len(self.iters) == 1:
                    self.result = _coconut.list(self.get_pool_stack()[-1].imap(_coconut_parallel_concurrent_map_func_wrapper(self.__class__, self.func, False), self.iters[0], self.chunksize))
                else:
                    self.result = _coconut.list(self.get_pool_stack()[-1].imap(_coconut_parallel_concurrent_map_func_wrapper(self.__class__, self.func, True), _coconut.zip(*self.iters), self.chunksize))
        return self.result
    def __iter__(self):
        return _coconut.iter(self.get_list())
class parallel_map(_coconut_base_parallel_concurrent_map):
    """
    Multi-process implementation of map. Requires arguments to be pickleable.
    For multiple sequential calls, use:
        with parallel_map.multiple_sequential_calls():
            ...
    """
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_pool(max_workers=None):
        return _coconut.multiprocessing.Pool(max_workers)
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_base_parallel_concurrent_map):
    """
    Multi-thread implementation of map. For multiple sequential calls, use:
        with concurrent_map.multiple_sequential_calls():
            ...
    """
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_pool(max_workers=None):
        return _coconut.multiprocessing_dummy.Pool(_coconut.multiprocessing.cpu_count() * 5 if max_workers is None else max_workers)
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
class filter(_coconut_base_hashable, _coconut.filter):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.filter, "__doc__"):
        __doc__ = _coconut.filter.__doc__
    def __new__(cls, function, iterable):
        new_filter = _coconut.filter.__new__(cls, function, iterable)
        new_filter.func = function
        new_filter.iter = iterable
        return new_filter
    def __reversed__(self):
        return self.__class__(self.func, _coconut_reversed(self.iter))
    def __repr__(self):
        return "filter(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __iter__(self):
        return _coconut.iter(_coconut.filter(self.func, self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip(_coconut_base_hashable, _coconut.zip):
    __slots__ = ("iters", "strict")
    if hasattr(_coconut.zip, "__doc__"):
        __doc__ = _coconut.zip.__doc__
    def __new__(cls, *iterables, **kwargs):
        new_zip = _coconut.zip.__new__(cls, *iterables)
        new_zip.iters = iterables
        new_zip.strict = kwargs.pop("strict", False)
        if kwargs:
            raise _coconut.TypeError("zip() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return new_zip
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_igetitem(i, index) for i in self.iters), strict=self.strict)
        return _coconut.tuple(_coconut_igetitem(i, index) for i in self.iters)
    def __reversed__(self):
        return self.__class__(*(_coconut_reversed(i) for i in self.iters), strict=self.strict)
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip(%s%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), ", strict=True" if self.strict else "")
    def __reduce__(self):
        return (self.__class__, self.iters, self.strict)
    def __setstate__(self, strict):
        self.strict = strict
    def __iter__(self):
        for items in _coconut.iter(_coconut.zip(*self.iters, strict=self.strict) if _coconut_sys.version_info >= (3, 10) else _coconut.zip_longest(*self.iters, fillvalue=_coconut_sentinel) if self.strict else _coconut.zip(*self.iters)):
            if self.strict and _coconut_sys.version_info < (3, 10) and _coconut.any(x is _coconut_sentinel for x in items):
                raise _coconut.ValueError("zip(..., strict=True) arguments have mismatched lengths")
            yield items
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip_longest(zip):
    __slots__ = ("fillvalue",)
    if hasattr(_coconut.zip_longest, "__doc__"):
        __doc__ = (_coconut.zip_longest).__doc__
    def __new__(cls, *iterables, **kwargs):
        self = _coconut_zip.__new__(cls, *iterables, strict=False)
        self.fillvalue = kwargs.pop("fillvalue", None)
        if kwargs:
            raise _coconut.TypeError("zip_longest() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return self
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            new_ind = _coconut.slice(index.start + self.__len__() if index.start is not None and index.start < 0 else index.start, index.stop + self.__len__() if index.stop is not None and index.stop < 0 else index.stop, index.step)
            return self.__class__(*(_coconut_igetitem(i, new_ind) for i in self.iters))
        if index < 0:
            index += self.__len__()
        result = []
        got_non_default = False
        for it in self.iters:
            try:
                result.append(_coconut_igetitem(it, index))
            except _coconut.IndexError:
                result.append(self.fillvalue)
            else:
                got_non_default = True
        if not got_non_default:
            raise _coconut.IndexError("zip_longest index out of range")
        return _coconut.tuple(result)
    def __len__(self):
        return _coconut.max(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip_longest(%s, fillvalue=%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), self.fillvalue)
    def __reduce__(self):
        return (self.__class__, self.iters, self.fillvalue)
    def __setstate__(self, fillvalue):
        self.fillvalue = fillvalue
    def __iter__(self):
        return _coconut.iter(_coconut.zip_longest(*self.iters, fillvalue=self.fillvalue))
class enumerate(_coconut_base_hashable, _coconut.enumerate):
    __slots__ = ("iter", "start")
    if hasattr(_coconut.enumerate, "__doc__"):
        __doc__ = _coconut.enumerate.__doc__
    def __new__(cls, iterable, start=0):
        new_enumerate = _coconut.enumerate.__new__(cls, iterable, start)
        new_enumerate.iter = iterable
        new_enumerate.start = start
        return new_enumerate
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(_coconut_igetitem(self.iter, index), self.start + (0 if index.start is None else index.start if index.start >= 0 else _coconut.len(self.iter) + index.start))
        return (self.start + index, _coconut_igetitem(self.iter, index))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "enumerate(%r, %r)" % (self.iter, self.start)
    def __reduce__(self):
        return (self.__class__, (self.iter, self.start))
    def __iter__(self):
        return _coconut.iter(_coconut.enumerate(self.iter, self.start))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class count(_coconut_base_hashable):
    """count(start, step) returns an infinite iterator starting at start and increasing by step.
    If step is set to 0, count will infinitely repeat its first argument."""
    __slots__ = ("start", "step")
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
    def __iter__(self):
        while True:
            yield self.start
            if self.step:
                self.start += self.step
    def __contains__(self, elem):
        if not self.step:
            return elem == self.start
        if elem < self.start:
            return False
        return (elem - self.start) % self.step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice) and (index.start is None or index.start >= 0) and (index.stop is None or index.stop >= 0):
            new_start, new_step = self.start, self.step
            if self.step and index.start is not None:
                new_start += self.step * index.start
            if self.step and index.step is not None:
                new_step *= index.step
            if index.stop is None:
                return self.__class__(new_start, new_step)
            if self.step and _coconut.isinstance(self.start, _coconut.int) and _coconut.isinstance(self.step, _coconut.int):
                return _coconut.range(new_start, self.start + self.step * index.stop, new_step)
            return _coconut_map(self.__getitem__, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        if index < 0:
            raise _coconut.IndexError("count indices must be positive")
        return self.start + self.step * index if self.step else self.start
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        if not self.step:
            return _coconut.float("inf") if elem == self.start else 0
        return int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self:
            raise _coconut.ValueError(_coconut.repr(elem) + " not in " + _coconut.repr(self))
        return (elem - self.start) // self.step if self.step else 0
    def __reversed__(self):
        if not self.step:
            return self
        raise _coconut.TypeError(_coconut.repr(self) + " object is not reversible")
    def __repr__(self):
        return "count(%r, %r)" % (self.start, self.step)
    def __reduce__(self):
        return (self.__class__, (self.start, self.step))
    def __copy__(self):
        return self.__class__(self.start, self.step)
    def __fmap__(self, func):
        return _coconut_map(func, self)
class groupsof(_coconut_base_hashable):
    """groupsof(n, iterable) splits iterable into groups of size n.
    If the length of the iterable is not divisible by n, the last group may be of size < n."""
    __slots__ = ("group_size", "iter")
    def __init__(self, n, iterable):
        self.iter = iterable
        try:
            self.group_size = _coconut.int(n)
        except _coconut.ValueError:
            raise _coconut.TypeError("group size must be an int; not %r" % (n,))
        if self.group_size <= 0:
            raise _coconut.ValueError("group size must be > 0; not %r" % (self.group_size,))
    def __iter__(self):
        iterator = _coconut.iter(self.iter)
        loop = True
        while loop:
            group = []
            for _ in _coconut.range(self.group_size):
                try:
                    group.append(_coconut.next(iterator))
                except _coconut.StopIteration:
                    loop = False
                    break
            if group:
                yield _coconut.tuple(group)
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "groupsof(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.group_size, self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class recursive_iterator(_coconut_base_hashable):
    """Decorator that optimizes a function for iterator recursion."""
    __slots__ = ("func", "tee_store", "backup_tee_store")
    def __init__(self, func):
        self.func = func
        self.tee_store = {}
        self.backup_tee_store = []
    def __call__(self, *args, **kwargs):
        key = (args, _coconut.frozenset(kwargs.items()))
        use_backup = False
        try:
            _coconut.hash(key)
        except _coconut.Exception:
            try:
                key = _coconut.pickle.dumps(key, -1)
            except _coconut.Exception:
                use_backup = True
        if use_backup:
            for i, (k, v) in _coconut.enumerate(self.backup_tee_store):
                if k == key:
                    to_tee, store_pos = v, i
                    break
            else:
                to_tee = self.func(*args, **kwargs)
                store_pos = None
            to_store, to_return = _coconut_tee(to_tee)
            if store_pos is None:
                self.backup_tee_store.append([key, to_store])
            else:
                self.backup_tee_store[store_pos][1] = to_store
        else:
            it = self.tee_store.get(key)
            if it is None:
                it = self.func(*args, **kwargs)
            self.tee_store[key], to_return = _coconut_tee(it)
        return to_return
    def __repr__(self):
        return "@recursive_iterator(%s)" % (_coconut.repr(self.func),)
    def __reduce__(self):
        return (self.__class__, (self.func,))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if _coconut_sys.version_info < (3,):
            return _coconut.types.MethodType(self, obj, objtype)
        else:
            return _coconut.types.MethodType(self, obj)
class _coconut_FunctionMatchErrorContext(object):
    __slots__ = ("exc_class", "taken")
    threadlocal_ns = _coconut.threading.local()
    def __init__(self, exc_class):
        self.exc_class = exc_class
        self.taken = False
    @classmethod
    def get_contexts(cls):
        try:
            return cls.threadlocal_ns.contexts
        except _coconut.AttributeError:
            cls.threadlocal_ns.contexts = []
            return cls.threadlocal_ns.contexts
    def __enter__(self):
        self.get_contexts().append(self)
    def __exit__(self, type, value, traceback):
        self.get_contexts().pop()
def _coconut_get_function_match_error():
    try:
        ctx = _coconut_FunctionMatchErrorContext.get_contexts()[-1]
    except _coconut.IndexError:
        return _coconut_MatchError
    if ctx.taken:
        return _coconut_MatchError
    ctx.taken = True
    return ctx.exc_class
class _coconut_base_pattern_func(_coconut_base_hashable):
    if _coconut_sys.version_info < (3, 7):
        __slots__ = ("FunctionMatchError", "patterns", "__doc__", "__name__")
    else:
        __slots__ = ("FunctionMatchError", "patterns", "__doc__", "__name__", "__qualname__")
    _coconut_is_match = True
    def __init__(self, *funcs):
        self.FunctionMatchError = _coconut.type(_coconut_py_str("MatchError"), (_coconut_MatchError,), {})
        self.patterns = []
        self.__doc__ = None
        self.__name__ = None
        if _coconut_sys.version_info >= (3, 7):
            self.__qualname__ = None
        for func in funcs:
            self.add_pattern(func)
    def add_pattern(self, func):
        if _coconut.isinstance(func, _coconut_base_pattern_func):
            self.patterns += func.patterns
        else:
            self.patterns.append(func)
        self.__doc__ = _coconut.getattr(func, "__doc__", self.__doc__)
        self.__name__ = _coconut.getattr(func, "__name__", self.__name__)
        if _coconut_sys.version_info >= (3, 7):
            self.__qualname__ = _coconut.getattr(func, "__qualname__", self.__qualname__)
    def __call__(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return self.patterns[-1](*args, **kwargs)
    def _coconut_tco_func(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return _coconut_tail_call(self.patterns[-1], *args, **kwargs)
    def __repr__(self):
        return "addpattern(%s)(*%s)" % (_coconut.repr(self.patterns[0]), _coconut.repr(self.patterns[1:]))
    def __reduce__(self):
        return (self.__class__, _coconut.tuple(self.patterns))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if _coconut_sys.version_info < (3,):
            return _coconut.types.MethodType(self, obj, objtype)
        else:
            return _coconut.types.MethodType(self, obj)
def _coconut_mark_as_match(base_func):
    base_func._coconut_is_match = True
    return base_func
def addpattern(base_func, **kwargs):
    """Decorator to add a new case to a pattern-matching function,
    where the new case is checked last."""
    allow_any_func = kwargs.pop("allow_any_func", False)
    if not allow_any_func and not _coconut.getattr(base_func, "_coconut_is_match", False):
        _coconut.warnings.warn("Possible misuse of addpattern with non-pattern-matching function " + _coconut.repr(base_func) + " (pass allow_any_func=True to dismiss)", stacklevel=2)
    if kwargs:
        raise _coconut.TypeError("addpattern() got unexpected keyword arguments " + _coconut.repr(kwargs))
    return _coconut.functools.partial(_coconut_base_pattern_func, base_func)
_coconut_addpattern = addpattern
def prepattern(base_func, **kwargs):
    """DEPRECATED: use addpattern instead."""
    def pattern_prepender(func):
        return addpattern(func, **kwargs)(base_func)
    return pattern_prepender
class _coconut_partial(_coconut_base_hashable):
    __slots__ = ("func", "_argdict", "_arglen", "_stargs", "keywords")
    if hasattr(_coconut.functools.partial, "__doc__"):
        __doc__ = _coconut.functools.partial.__doc__
    def __init__(self, func, argdict, arglen, *args, **kwargs):
        self.func = func
        self._argdict = argdict
        self._arglen = arglen
        self._stargs = args
        self.keywords = kwargs
    def __reduce__(self):
        return (self.__class__, (self.func, self._argdict, self._arglen) + self._stargs, self.keywords)
    def __setstate__(self, keywords):
        self.keywords = keywords
    @property
    def args(self):
        return _coconut.tuple(self._argdict.get(i) for i in _coconut.range(self._arglen)) + self._stargs
    def __call__(self, *args, **kwargs):
        callargs = []
        argind = 0
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                callargs.append(self._argdict[i])
            elif argind >= _coconut.len(args):
                raise _coconut.TypeError("expected at least " + _coconut.str(self._arglen - _coconut.len(self._argdict)) + " argument(s) to " + _coconut.repr(self))
            else:
                callargs.append(args[argind])
                argind += 1
        callargs += self._stargs
        callargs += args[argind:]
        kwargs.update(self.keywords)
        return self.func(*callargs, **kwargs)
    def __repr__(self):
        args = []
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                args.append(_coconut.repr(self._argdict[i]))
            else:
                args.append("?")
        for arg in self._stargs:
            args.append(_coconut.repr(arg))
        return "%s$(%s)" % (_coconut.repr(self.func), ", ".join(args))
def consume(iterable, keep_last=0):
    """consume(iterable, keep_last) fully exhausts iterable and return the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)
class starmap(_coconut_base_hashable, _coconut.itertools.starmap):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.itertools.starmap, "__doc__"):
        __doc__ = _coconut.itertools.starmap.__doc__
    def __new__(cls, function, iterable):
        new_map = _coconut.itertools.starmap.__new__(cls, function, iterable)
        new_map.func = function
        new_map.iter = iterable
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, _coconut_igetitem(self.iter, index))
        return self.func(*_coconut_igetitem(self.iter, index))
    def __reversed__(self):
        return self.__class__(self.func, *_coconut_reversed(self.iter))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "starmap(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __iter__(self):
        return _coconut.iter(_coconut.itertools.starmap(self.func, self.iter))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), self.iter)
def makedata(data_type, *args):
    """Construct an object of the given data_type containing the given arguments."""
    if _coconut.hasattr(data_type, "_make") and _coconut.issubclass(data_type, _coconut.tuple):
        return data_type._make(args)
    if _coconut.issubclass(data_type, (_coconut.range, _coconut.abc.Iterator)):
        return args
    if _coconut.issubclass(data_type, _coconut.str):
        return "".join(args)
    return data_type(args)
def datamaker(data_type):
    """DEPRECATED: use makedata instead."""
    return _coconut.functools.partial(makedata, data_type)
def fmap(func, obj):
    """fmap(func, obj) creates a copy of obj with func applied to its contents.
    Override by defining obj.__fmap__(func). For numpy arrays, uses np.vectorize."""
    obj_fmap = _coconut.getattr(obj, "__fmap__", None)
    if obj_fmap is not None:
        try:
            result = obj_fmap(func)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if obj.__class__.__module__ in ("numpy", "pandas"):
        from numpy import vectorize
        return vectorize(func)(obj)
    return _coconut_makedata(obj.__class__, *(_coconut_starmap(func, obj.items()) if _coconut.isinstance(obj, _coconut.abc.Mapping) else _coconut_map(func, obj)))
def memoize(maxsize=None, *args, **kwargs):
    """Decorator that memoizes a function,
    preventing it from being recomputed if it is called multiple times with the same arguments."""
    return _coconut.functools.lru_cache(maxsize, *args, **kwargs)
def _coconut_call_set_names(cls):
    if _coconut_sys.version_info < (3, 6):
        for k, v in _coconut.vars(cls).items():
            set_name = _coconut.getattr(v, "__set_name__", None)
            if set_name is not None:
                set_name(cls, k)
class override(_coconut_base_hashable):
    __slots__ = ("func",)
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        if _coconut_sys.version_info < (3,):
            return _coconut.types.MethodType(self.func, obj, objtype)
        else:
            return _coconut.types.MethodType(self.func, obj)
    def __set_name__(self, obj, name):
        if not _coconut.hasattr(_coconut.super(obj, obj), name):
            raise _coconut.RuntimeError(obj.__name__ + "." + name + " marked with @override but not overriding anything")
    def __reduce__(self):
        return (self.__class__, (self.func,))
def reveal_type(obj):
    """Special function to get MyPy to print the type of the given expression.
    At runtime, reveal_type is the identity function."""
    return obj
def reveal_locals():
    """Special function to get MyPy to print the type of the current locals.
    At runtime, reveal_locals always returns None."""
    pass
def _coconut_handle_cls_kwargs(**kwargs):
    metaclass = kwargs.pop("metaclass", None)
    if kwargs and metaclass is None:
        raise _coconut.TypeError("unexpected keyword argument(s) in class definition: %s" % (kwargs,))
    def coconut_handle_cls_kwargs_wrapper(cls):
        if metaclass is None:
            return cls
        orig_vars = cls.__dict__.copy()
        slots = orig_vars.get("__slots__")
        if slots is not None:
            if _coconut.isinstance(slots, str):
                slots = [slots]
            for slots_var in slots:
                orig_vars.pop(slots_var)
        orig_vars.pop("__dict__", None)
        orig_vars.pop("__weakref__", None)
        if _coconut.hasattr(cls, "__qualname__"):
            orig_vars["__qualname__"] = cls.__qualname__
        return metaclass(cls.__name__, cls.__bases__, orig_vars, **kwargs)
    return coconut_handle_cls_kwargs_wrapper
def _coconut_handle_cls_stargs(*args):
    temp_names = ["_coconut_base_cls_%s" % (i,) for i in _coconut.range(_coconut.len(args))]
    ns = _coconut.dict(_coconut.zip(temp_names, args))
    exec("class _coconut_cls_stargs_base(" + ", ".join(temp_names) + "): pass", ns)
    return ns["_coconut_cls_stargs_base"]
def _coconut_dict_merge(*dicts, **options):
    for_func = options.pop("for_func", False)
    assert not options, "error with internal Coconut function _coconut_dict_merge (you should report this at https://github.com/evhub/coconut/issues/new)"
    newdict = {}
    prevlen = 0
    for d in dicts:
        newdict.update(d)
        if for_func:
            if len(newdict) != prevlen + len(d):
                raise _coconut.TypeError("multiple values for the same keyword argument")
            prevlen = len(newdict)
    return newdict
_coconut_self_match_types = (bool, bytearray, bytes, dict, float, frozenset, int, list, set, str, tuple)
_coconut_MatchError, _coconut_count, _coconut_enumerate, _coconut_filter, _coconut_makedata, _coconut_map, _coconut_reiterable, _coconut_reversed, _coconut_starmap, _coconut_tee, _coconut_zip, TYPE_CHECKING, reduce, takewhile, dropwhile = MatchError, count, enumerate, filter, makedata, map, reiterable, reversed, starmap, tee, zip, False, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile

# Compiled Coconut: -----------------------------------------------------------

# TODO: interactivity

from itertools import product  #3 (line num in coconut source)
import words as wordle_words  #4 (line num in coconut source)
from lib_rbon import flip  #5 (line num in coconut source)
from lib_rbon import uncurry  #5 (line num in coconut source)
from lib_rbon import split  #5 (line num in coconut source)
import time  #6 (line num in coconut source)

class Info(_coconut.collections.namedtuple("Info", ('greens', 'yellows', 'bads', 'unknown', 'words')), _coconut.object):  #8 (line num in coconut source)
    __slots__ = ()  #8 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #8 (line num in coconut source)
    def __eq__(self, other):  #8 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #8 (line num in coconut source)
    def __hash__(self):  #8 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #8 (line num in coconut source)
    __match_args__ = ('greens', 'yellows', 'bads', 'unknown', 'words')  #8 (line num in coconut source)
    def __new__(_coconut_cls, greens=[], yellows=[], bads=[], unknown=[], words=()):  #8 (line num in coconut source)
        return _coconut.tuple.__new__(_coconut_cls, (greens, yellows, bads, unknown, words))  #8 (line num in coconut source)


_coconut_call_set_names(Info)  #10 (line num in coconut source)
class State(_coconut.collections.namedtuple("State", ('words', 'greens', 'yellows', 'bads', 'unknown')), _coconut.object):  #10 (line num in coconut source)
    __slots__ = ()  #10 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #10 (line num in coconut source)
    def __eq__(self, other):  #10 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #10 (line num in coconut source)
    def __hash__(self):  #10 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #10 (line num in coconut source)
    __match_args__ = ('words', 'greens', 'yellows', 'bads', 'unknown')  #10 (line num in coconut source)
    def __new__(_coconut_cls, words=(), greens=[], yellows=[], bads=[], unknown=[]):  #10 (line num in coconut source)
        return _coconut.tuple.__new__(_coconut_cls, (words, greens, yellows, bads, unknown))  #10 (line num in coconut source)



_coconut_call_set_names(State)  #13 (line num in coconut source)
@_coconut_tco  #13 (line num in coconut source)
def parse(command):  #13 (line num in coconut source)
    pairs = (zip)(*(split)(" = ", command))  #14 (line num in coconut source)
    greens = []  #15 (line num in coconut source)
    yellows = []  #16 (line num in coconut source)
    bads = []  #17 (line num in coconut source)
    unknown = [0, 1, 2, 3, 4]  #18 (line num in coconut source)
    index = 0  #19 (line num in coconut source)
    for i in pairs:  #20 (line num in coconut source)
        if i[1] == 'g':  #21 (line num in coconut source)
            greens.append((i[0], index))  #22 (line num in coconut source)
            if index in unknown:  #23 (line num in coconut source)
                unknown.remove(index)  #24 (line num in coconut source)
        elif i[1] == 'y':  #25 (line num in coconut source)
            yellows.append((i[0], index))  #26 (line num in coconut source)
        elif i[1] == 'b':  #27 (line num in coconut source)
            bads.append((i[0]))  #28 (line num in coconut source)
        index += 1  #29 (line num in coconut source)
    return _coconut_tail_call(Info, greens, yellows, bads, unknown)  #30 (line num in coconut source)

@_coconut_tco  #32 (line num in coconut source)
def info_add(info1, info2):  #32 (line num in coconut source)
    greens = info1.greens + info2.greens  #33 (line num in coconut source)
    yellows = info1.yellows + info2.yellows  #34 (line num in coconut source)
    bads = info1.bads + info2.bads  #35 (line num in coconut source)
    unknown = info1.unknown + info2.unknown  #36 (line num in coconut source)
    return _coconut_tail_call(Info, greens, yellows, bads, unknown)  #37 (line num in coconut source)

def step(command):  #39 (line num in coconut source)

    info = (parse)(command)  #41 (line num in coconut source)

    greens = info.greens  #43 (line num in coconut source)
    yellows = info.yellows  #44 (line num in coconut source)
    bads = info.bads  #45 (line num in coconut source)
    unknown = info.unknown  #46 (line num in coconut source)

    (print)("filtering words...")  #48 (line num in coconut source)
    start_time = time.perf_counter()  #49 (line num in coconut source)
# possible_words = possible_words \
    possible_words = (list)((filter)(_coconut.functools.partial(check_word, greens, yellows, unknown), (fmap)(tuple, wordle_words.all_words)))  # this is also needed for test parity  #51 (line num in coconut source)
    end_time = time.perf_counter()  #55 (line num in coconut source)
    (print)("finished in: " + ((str)(end_time - start_time)))  #56 (line num in coconut source)
    print("total words: " + str(len(possible_words)) + '\n')  #57 (line num in coconut source)

    return (possible_words)  #59 (line num in coconut source)

@_coconut_tco  #61 (line num in coconut source)
def new_parse(command):  #61 (line num in coconut source)
    pairs = (zip)(*(split)(" = ", command))  #62 (line num in coconut source)
    greens = []  #63 (line num in coconut source)
    yellows = []  #64 (line num in coconut source)
    bads = []  #65 (line num in coconut source)
    unknown = [0, 1, 2, 3, 4]  #66 (line num in coconut source)
    index = 0  #67 (line num in coconut source)
    for i in pairs:  #68 (line num in coconut source)
        if i[1] == 'g':  #69 (line num in coconut source)
            greens.append((i[0], index))  #70 (line num in coconut source)
            if index in unknown:  #71 (line num in coconut source)
                unknown.remove(index)  #72 (line num in coconut source)
        elif i[1] == 'y':  #73 (line num in coconut source)
            yellows.append((i[0], index))  #74 (line num in coconut source)
        elif i[1] == 'b':  #75 (line num in coconut source)
            bads.append((i[0]))  #76 (line num in coconut source)
        index += 1  #77 (line num in coconut source)
    return _coconut_tail_call(State, (), greens, yellows, bads, unknown)  #78 (line num in coconut source)

@_coconut_tco  #80 (line num in coconut source)
def add_state(state1, state2):  #80 (line num in coconut source)
    words = state1.words + state2.words  #81 (line num in coconut source)
    greens = state1.greens + state2.greens  #82 (line num in coconut source)
    yellows = state1.yellows + state2.yellows  #83 (line num in coconut source)
    bads = state1.bads + state2.bads  #84 (line num in coconut source)
    unknown = state1.unknown + state2.unknown  #85 (line num in coconut source)
    return _coconut_tail_call(State, words, greens, yellows, bads, unknown)  #86 (line num in coconut source)

@_coconut_tco  #88 (line num in coconut source)
def new_step(command, state=State(), cheat_level=1):  #88 (line num in coconut source)

    new_state = (new_parse)(command)  #90 (line num in coconut source)
    state = add_state(state, new_state)  #91 (line num in coconut source)

    if len(state.words) == 0:  #93 (line num in coconut source)
        _coconut_case_match_to_0 = cheat_level  #94 (line num in coconut source)
        _coconut_case_match_check_0 = False  #94 (line num in coconut source)
        if _coconut_case_match_to_0 == 0:  #94 (line num in coconut source)
            _coconut_case_match_check_0 = True  #94 (line num in coconut source)
        if _coconut_case_match_check_0:  #94 (line num in coconut source)
            (print)("generating words sans bad letters...")  #96 (line num in coconut source)
            start_time = time.perf_counter()  #97 (line num in coconut source)
            words = generate_words(state.bads)  #98 (line num in coconut source)
            end_time = time.perf_counter()  #99 (line num in coconut source)
            (print)("finished in: " + ((str)(end_time - start_time)))  #100 (line num in coconut source)
            (print)('total words: ' + ((str)((len)(words))) + '\n')  #101 (line num in coconut source)
        if not _coconut_case_match_check_0:  #102 (line num in coconut source)
            if _coconut_case_match_to_0 == 1:  #102 (line num in coconut source)
                _coconut_case_match_check_0 = True  #102 (line num in coconut source)
            if _coconut_case_match_check_0:  #102 (line num in coconut source)
                words = wordle_words.all_words  #103 (line num in coconut source)
        if not _coconut_case_match_check_0:  #104 (line num in coconut source)
            if _coconut_case_match_to_0 == 2:  #104 (line num in coconut source)
                _coconut_case_match_check_0 = True  #104 (line num in coconut source)
            if _coconut_case_match_check_0:  #104 (line num in coconut source)
                words = wordle_words.possible_solutions  #105 (line num in coconut source)
    else:  #106 (line num in coconut source)
        words = state.words  #107 (line num in coconut source)

    (print)("filtering words...")  #109 (line num in coconut source)
    start_time = time.perf_counter()  #110 (line num in coconut source)
    words = filter_words(words, state.greens, state.yellows, state.unknown, state.bads)  #111 (line num in coconut source)
    end_time = time.perf_counter()  #112 (line num in coconut source)
    (print)("finished in: " + ((str)(end_time - start_time)))  #113 (line num in coconut source)
    print("total words: " + str(len(words)) + '\n')  #114 (line num in coconut source)

    return _coconut_tail_call(State, words, state.greens, state.yellows, state.bads, state.unknown)  #116 (line num in coconut source)

def generate_words(bads):  #118 (line num in coconut source)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  #119 (line num in coconut source)
    chars = (tuple)((filter)(lambda y: y not in bads, alphabet))  #120 (line num in coconut source)
    possible_words = (tuple)(product(chars, repeat=5))  #121 (line num in coconut source)
    return (possible_words)  #122 (line num in coconut source)

@_coconut_tco  #124 (line num in coconut source)
def filter_words(words, greens, yellows, unknown, bads):  #124 (line num in coconut source)
    return _coconut_tail_call((tuple), (filter)(_coconut.functools.partial(check_word, greens, yellows, unknown, bads), (fmap)(tuple, words)))  #125 (line num in coconut source)

def fits_green(word, green):  #130 (line num in coconut source)
    return (word[green[1]] == green[0])  #130 (line num in coconut source)

def fits_all_greens(greens, word):  #132 (line num in coconut source)
    for green in greens:  #133 (line num in coconut source)
        if word[green[1]] != green[0]:  #134 (line num in coconut source)
            return (False)  #135 (line num in coconut source)
    return (True)  #136 (line num in coconut source)

def fits_yellow(word, unknown, yellow):  #138 (line num in coconut source)
    if word[yellow[1]] != yellow[0]:  #139 (line num in coconut source)
        res = False  #140 (line num in coconut source)
        for u in unknown:  #141 (line num in coconut source)
            if word[u] == yellow[0]:  #142 (line num in coconut source)
                return (True)  #143 (line num in coconut source)
    return (False)  #144 (line num in coconut source)

def fits_all_yellows(yellows, unknown, word):  #146 (line num in coconut source)
    for yellow in yellows:  #147 (line num in coconut source)
        if not fits_yellow(word, unknown, yellow):  #148 (line num in coconut source)
            return (False)  #149 (line num in coconut source)
    return (True)  #150 (line num in coconut source)

def bad_letters_in_word(bads, word):  #152 (line num in coconut source)
    for bad in bads:  #153 (line num in coconut source)
        if bad in word:  #154 (line num in coconut source)
            return (True)  #155 (line num in coconut source)
    return (False)  #156 (line num in coconut source)

def check_word(greens, yellows, unknown, bads, word):  #158 (line num in coconut source)
    if not (bad_letters_in_word)(bads, word):  #159 (line num in coconut source)
        if (fits_all_greens)(greens, word):  #160 (line num in coconut source)
            if (fits_all_yellows)(yellows, unknown, word):  #161 (line num in coconut source)
# if ''.join(word) in words.all_words:
                return (True)  #163 (line num in coconut source)
    return (False)  #164 (line num in coconut source)

@_coconut_tco  #166 (line num in coconut source)
def count_vowels(word):  #166 (line num in coconut source)
    return _coconut_tail_call((len), (tuple)((filter)(lambda x: x in 'aeiouy', word)))  #166 (line num in coconut source)

def reveal_4_vowel_words(word):  #168 (line num in coconut source)
    if ((count_vowels)(word)) == 4:  #169 (line num in coconut source)
        if not (len(word) != len(set(word))):  # filter dupes  #170 (line num in coconut source)
            print(word)  #171 (line num in coconut source)

def reveal_5_vowel_words(word):  #173 (line num in coconut source)
    if ((count_vowels)(word)) == 5:  #174 (line num in coconut source)
        if not (len(word) != len(set(word))):  # filter dupes  #175 (line num in coconut source)
            print(word)  #176 (line num in coconut source)

@_coconut_tco  #178 (line num in coconut source)
def fancy_format(iterable):  #178 (line num in coconut source)
    return _coconut_tail_call('\n'.join, tuple(map(''.join, iterable)))  #178 (line num in coconut source)

def fancy_print(state, word_max=1000):  #180 (line num in coconut source)
    words = (fancy_format)(state.words)  #181 (line num in coconut source)
    if (len)(state.words) > word_max:  #182 (line num in coconut source)
        print("Too many words to print.")  #183 (line num in coconut source)
    else:  #184 (line num in coconut source)
        print(words)  #185 (line num in coconut source)
    print("Total words: " + str(len(state.words)))  #186 (line num in coconut source)
    print("Greens: " + ((str)(state.greens)))  #187 (line num in coconut source)
    print("Yellows: " + ((str)(state.yellows)))  #188 (line num in coconut source)
    print("Bads: " + ((str)(state.bads)))  #189 (line num in coconut source)


def main():  #192 (line num in coconut source)
    state = State()  #193 (line num in coconut source)
# thing.strip() |> print
    while True:  #195 (line num in coconut source)
        print()  #196 (line num in coconut source)
        print("{_coconut_format_0}Warning: No active frommets remain. Continue?{_coconut_format_1}".format(_coconut_format_0=(bcolors.GREEN), _coconut_format_1=(bcolors.ENDC)))  #197 (line num in coconut source)
        i = input("yes?: ")  #198 (line num in coconut source)
        state = (new_step)(*(i, state), cheat_level=0)  #199 (line num in coconut source)
        (fancy_print)(state)  #200 (line num in coconut source)

class bcolors(_coconut.object):  #202 (line num in coconut source)
    HEADER = '\033[95m'  #203 (line num in coconut source)
    OKBLUE = '\033[94m'  #204 (line num in coconut source)
    OKCYAN = '\033[96m'  #205 (line num in coconut source)
    GREEN = '\033[97;42m'  #206 (line num in coconut source)
# WARNING = '\033[30;31m'
    FAIL = '\033[91m'  #208 (line num in coconut source)
    ENDC = '\033[0m'  #209 (line num in coconut source)
    BOLD = '\033[1m'  #210 (line num in coconut source)
    UNDERLINE = '\033[4m'  #211 (line num in coconut source)

_coconut_call_set_names(bcolors)  #213 (line num in coconut source)
if __name__ == '__main__':  #213 (line num in coconut source)
# words.all_words |> fmap $ reveal_4_vowel_words
# "audio = ybgby" |> step #|> fancy_format \
# ("apdlp = ggbgy", State()) |*> new_step |> print #|> fancy_format \
# |> print
    main()  #218 (line num in coconut source)
