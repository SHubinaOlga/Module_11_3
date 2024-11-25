from pprint import pprint

def introspection_info(obj):
    _type = type(obj).__name__
    _attr = dir(obj)
    _method = [method for method in _attr if callable(getattr(obj, method))]
    _module = obj.__class__.__module__
    info = {'type': _type, 'attributes': _attr,
            'methods': _method, 'module': _module}
    return info

_num = introspection_info(42)
pprint(_num)

_str = introspection_info('строка')
pprint(_str)

_list = introspection_info([5, 3.4, 'строка',40])
pprint(_list)
