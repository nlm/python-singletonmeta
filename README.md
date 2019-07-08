# SingletonMeta

A python module for easily creating singletons

## SingletonMeta

A metaclass to restricts the instantiation of a class to one "single" instance.

```
>> from singletonmeta import SingletonMeta
>>
>> class MyClass(metaclass=SingletonMeta):
..   pass
..
>> print(id(Myclass()) == id(MyClass()))
True
```

## ThreadSafeSingletonMeta

A metaclass to restricts the instantiation of a class to one "single" instance,
thread-safe version (using lock).
