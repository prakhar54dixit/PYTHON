import time
def cache(func):
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args] 
        result=func(*args)
        cache_value.update({args: result})
        return result
    return wrapper  


@cache
def long_time_running(a,b):
    time.sleep(5)
    return a+b

print(long_time_running(2,3))
print(long_time_running(2,3))