# Passing configuration in a "package"

## Objective:

You want to load a configuration file ([`test.json`](./test.json)) into a run of an application.
Minimzing the passing of parameters, objects, etc. is desired.

## Solution

Define a [`Config`](./config.py) class (following the [borg design pattern](http://code.activestate.com/recipes/66531-singleton-we-dont-need-no-stinkin-singleton-the-bo/)).
In the CLI part of your application, instantiate an instance of `Config` and set its `env` attribute as per [`test.json`](./test.json).
Next, in the actual logic which [`app.py`](./app.py) calls, and is implemented in [`mod.py`](./mod.py), instansitate another instance of `Config`.
This second instance will have the same shared state, and in turn will hold the same configuration in it `env` attribute.

## Testing

Let us run some tests, which also give better feeling to how this solution actually works.
Check out `test3` and `test4` in [`test_config1.py`](./test_config1.py); the two instances have different IDs but their underlying `__dict__` is the same.

## Open problem and limitations

An issue arises with `test2` of [`test_config2.py`](./test_config2.py).
Although in this second test case `foo` and `bar` are swapped, the `Config` objects which are instantiated have the same value for `env` as the one defined in `test_config1.py`.
It seems like, somehow, the shared state which is created during the run of `test_config1.py`, is not removed / garbage collected /etc., and is still there when running the second test case.

The problem with the tests, suggests further problems with this solution in case of distributed setting, multi-thread/processes, etc.
