# Experiment MBE SimpleClass
This is an experimental repo to learn model based engineering by doing.

The immediate (and probably intermediate) aim is to handwrite a python equivalent of the `SimpleClass.java`.

The eventual aim is to have a compiler (can be written in Java) to produce the same SimpleClass in Python by taking in the same intermediate semantic models which produce the `SimpleClass.java`

## What is Model Based Engineering

Model Based Engineering (MBE) is a concept I learn in the book How To Engineer Software by Steve Tockey. Henceforth, HTES book.

I have an "incorrect" definition of MBE I carry in my head all the time. And it's:

> A way to write (designer) code that writes (to-be-executed) code in a more automated fashion

It's incorrect because the designer code I refer to is not actually regular code such as Java, etc.
It's actually semantic models written in a modeling language or a kind of Domain Specific Language. Then, a model compiler will take in the semantic models and then spew out the desired generated code to be executed.

Also, note that the generated code is currently just Model classes in a MVC structure. At least this is the case for now.

In future, the generated code might expand to include other stuff such as the View and Controller classes in a MVC structure.

The generated code is most definitely regular code such as Java, etc.

## So what's so awesome about MBE

I refer to Chapter 20 of the HTES book page 634 where it says and I quote:

> An open model compiler puts the translation process entirely under your control:
> > *"If you don't like the code generated by an open model compiler, don't modify that code. Instead, modify the compiler to have it generate the code you do like."*

Therefore, MBE is about creating an open model compiler to help you (but I actually mean me) to write code that's

1. more effective,
2. more readable, and
3. safer

And as a result, the process of software development becomes:

1. faster,
2. more enjoyable, and
3. more considerate of others such as future maintainers and extenders of your codebase

In other words, you (and again, I really mean me) can have a worklife as an engineer that is more effective, more enjoyable, and more considerate of others.

## So what's the output for this project

The output is to have an open model compiler that spits out a Python model class. What language the compiler itself is written in matters a lot less.

The compiler itself being be a toy version is also less crucial at this early stage.

With that in mind, there are two directions to approach this:

1. going backwards starting with handwriting the expected output Python class
2. going forwards starting with an already working open model compiler that generates a Java class and modify it to do the same for a Python class


I am starting with the backwards approach. See [issue #2](https://github.com/simkimsia/experiment-mbe-simpleclass/issues/2).

The forwards approach is briefly described in [issue #1](https://github.com/simkimsia/experiment-mbe-simpleclass/issues/1). It's only in the planning stage. Nothing's set in stone for this.

It may be the case I do both simultaneously and meet somewhere in the middle.

Or I simply go all the way with the backwards approach.

So long as I get it to work, it matters not how I get it done eventually.

## Structure of the repo

I follow https://docs.pytest.org/en/stable/goodpractices.html#tests-as-part-of-application-code
in terms of setting up the folder structure for the Python code.

As for the canonical Java class and the intermediate semantic models, they are under the folder `canonical`

The canonical files are based on the v5.3 of the Model editor and Model compiler that Steve Tockey wrote as part of the resources for the HTES book.

In that sense, the Python classes I write are deeply dependent on the canonical files. If they change in important ways, then the Python classes will have to change as well.

## Works for

Python 3.7.7

## How to run tests

1. Create your own virtualenv running python 3.7.7 for this project and activate it
2. GO to root folder and then install the dependencies with `pip install -r requirements.txt`
3. Type `pytest`

It should look like this:

![it works](assets/works.png)

## Assumptions

1. Use `mypy` because python is not statically typed
2. As far as possible try to indicate the types in the class/instance variables, method arguments, and method returns