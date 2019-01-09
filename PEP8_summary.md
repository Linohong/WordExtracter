# PEP8 summary

### Code Lay-out

* **Indentation**

  * Functions

  ```python
  # Function Calls 
  foo = long_function_name(var_one, var_two,
                           var_three, var_four)
  
  # Function Definition
  '''
  	* arugments on first line forbidden
  	* Further indentation required so as to distinguish from the contents
  '''
  def long_function_name(
          var_one, var_two, var_three,
          var_four) : 
      print(var_one)
  ```

  * conditional statements 

    ```python
    # 2 choices out of 3
    
    # Add a comment
    if (this_is_one_thing and
        that_is_another_thing) : 
        # Since both conditions are true, we can frobnicate
        do_something()
        
    # Add some extra indentation on the conditional continuation line.
    if (this_is_one_thing 
            and that_is_another_thing) :
        do_something()
    ```

  * Closing brace/bracket/parenthesis

    ```python
    # 2 choices
    
    # lined up under the first character of the line
    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )
    
    # line up under the first non-whitespace character of the last line of list
    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]
    
    result = some_function_that_takes_arguments(
    	'a', 'b', 'c',
        'd', 'e', 'f',
        )
    ```

* **No TABS !!** 

* **Maximum Line length : 79 characters**

  * docstrings or comments should be limited to 72 characters.
  * preferred way of wrapping long lines is by using Python's implied line continuation ( ' \ ' )

* **break before binary operations** 

  ```
  income = (gross_wages
            + taxable_interest
            + (dividends - qualified_dividends)
            - ira_deduction
            - student_loan_interest)
  ```

* **Blank Lines**

  * surrond top-level function, class definitions with two blank lines.
  * method defs in class are surrounded by a single blank line.
  * Extra blank lines may be used (sparingly) to separate groups of related functions.
  * blank lines in functions : sparingly used, to indicate logical sections

* **Source File Encoding : USE UTF-8**

* **Imports** 
  * import be on separte lines

    ```python
    import os
    import sys
    
    # This should not be done
    import sys, os
    
    # This is okay
    from subprocess import Popen, PIPE
    ```

  * imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

  * import should be grouped in the following order : 

    * 1. Standard library imports.
      2. Related third party imports
      3. Local application/library specific imports 

    * between groups above, put a blank line. 

    * Absolute imports are recommended

      ```python
      import mypkg.sibling
      from mypkg import sibling
      from mypkg.sibling import example
      
      # explicit relative imports are acceptable when absolute imports would be verbose.
      from . import sibling
      from .sibling import example
      ```

* Dunder Names should be placed after the module docstring but before any import statements 



### White Spaces

* **Pet Peeves** (불쾌함, 화남, 불쾌한 원인, 불만거리)

  * Immediately inside parentheses, brackets or braces

  ```python
  # Yes 
  spam(ham[1], {eggs: 2})
  # No
  spam( ham[ 1 ], { eggs: 2 })
  ```

  * Between a trailing comma and a following close parenthesis.

    ```python
    # Yes
    foo = (0,)
    # No
    bar = (0, )
    ```

  * Immediately before a comma, semicolon, or colon : 

    ```python
    # Yes
    if x == 4: print x, y; x, y = y, x
    # No
    if x == 4 : print x , y ; x , y = y , x
    ```

  * Slice : equal amounts on either side

    ```python
    # Yes 
    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    # No
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[1 : : 9]
    
    #Yes
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[lower + offset : upper + offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ```

  * Immediately before the open parenthesis that starte the argument list of a function call : \
    Immediately before the open parenthesis that starts an indexing or slicing : 

    ```
    # Former
    Yes : spam(1)
    No : spam (1)
    
    # Latter
    Yes : dct['key'] = lst[index]
    No : dct['key'] = lst [index]
    ```

* **Other Recommendations**
  * Surround these binary operators with a single space 

    * =, +=, -=, ==, <=, <, >, !=, <>, in, not in, is, is not, and, or, not

  * Don't use spaces around the = sign when used to indicate a keyword argument or a default param.

    ```python
    # Yes
    def complex(real, image=0.0) :
        return magic(r=real, i=imag)
        
    # No
    def complex(real, imag = 0.0) : 
        return magic(r = real, i = imag) 
    ```

  * spaces around -> arrow, normal rules for colons

    ```python
    # yes 
    def munge(input: AnyStr): ...
    def munge() -> AnyStr: ...
    
    # No
    def munge(input:AnyStr): ...
    def munge()->PosInt: ...
    ```

  * Compound statements are generally discouraged.
    if/for/while statements with single line okay

    ```python
    '''
    	formal
    '''
    # yes 
    if foo == 'blah' : 
        do_blah_thing()
    do_one()
    do_two()
    do_three()
    
    # no
    if foo == 'blah' : do_blah_thing()
    do_one(); do_two(); do_three()
    
    '''
    	latter
    '''
    # yes
    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay() 
        
    # No
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()
    ```


### Trailing Commas

* **Used when expected to be extended over time**

  ```python
  # Yes
  FILES = [
      'setup.cfg',
      'tox.ini', 
  ]
  
  initialize(FILES,
  	error=True,
  )
  ```



### Comments

> * Make a priority of keeping the comments UP-TO-DATE when the code changes ! 
> * Comments should be complete sentences ! 
>   * first word should be capitalized
>   * Block comments generally with multiple paragraphs built out of complete sentences.
> * Use two spaces after a sentence-ending period in multi-sentence comments, except after the final sentence.
> * in English : follow Strunk and White.



* **Block Comments**

  * generally apply to some (or all) code that follows them
  * indented to the same level as the code.
  * Each line of a block comment starts with a # and a single space 
  * Paragraphs inside a block comment are separated by a line containing a single #.

* **Inline Comments**

  * Use it sparingly

  * should be separted by at least two spaces from the statement.

    ```python
    x = x + 1    # Compensate for border, sometimes useful
    
    x = x + 1    # Increment x, distracting for it is too obvious
    ```



* **Documentation Strings (= docstrings)**

  * Wrtie docstrings for all public modules, functions, classes, and methods. 

    ```python
    """Return a foobang
    
    Optional plotz says to frobnicate the bizbaz first.
    """
    ```

  * Writing docstring becomes the '_ _ doc _ _' special attribute of that object.

  * One-line Docstrings

    ```python
    def kos_root():
    	"""Return the pathname of the KOS root directory."""
    	global _kos_root
    	if _kos_root: return _kos_root
    ```

    * docstring as a phrase ending in a period.
    * It prescribes(규정,지시하다) the function or method's effect as a command ("Do this", "Return that")
    * Not as a description; e.g., don't write "Returns the pathname ...". 

  * Multi-line Docstrings

    * summary -> blank -> more elaborate description.
    * indented the same as the quotes at its first line. (""" <- 얘랑 똑같은 라인에 indent 시킬것)
    * Docstring for a **module**
      * list the classes, 
      * exceptions
      * functions and any other objects
    * Docstring for a **function**
      * summarize its behavior
      * document its arguments
      * return values
      * side effects
      * exceptions raised
      * restrictions on when it can be called
      * Optional arguments should be indicated 
    * Docstring for a **class**
      * summarize its behavior
      * list the public methods
      * list the instance variables
      * interface should be listed separately
      * constructor should be documented in the docstring for its _ _ init _ _ method.

    ```python
    def complex(real=0.0, imag=0.0):
    	"""Form a complex number.
    	
    	Keyword arguments:
    	real -- the real part (default 0.0)
    	imag -- the imaginary part (default 0.0)
    	"""
    	if imag == 0.0 and real == 0.0:
    		return complex_zero
    		
    ```



### Naming Conventions

* **Class Names**

  * CapWords convention (CamelCase)

* **Type Variable Names**

  * CapWords convention preferring short names (T, AnyStr, Num)

    ```python
    from typing import TypeVar
    
    VT_co = TypeVar('VT_co', covariant=True)
    KT_contra = TypeVar('KT_contra', contravariant=True)
    ```

* **Exception Names**

  * exceptions are classes, so CapWords.
  * use the suffix "Error" if the exception actually is an error.

* **Function and Variable Names**

  * function name : should be lowercase, with words separated by underscores

    ```python
    def calc_func(): 
    ```

  * variable name : should follow the same convention as the function names
  * mixedCase allowed only in contexts where that's already the prvailing style.
  * global variable names convention as the function names convention.

* **Function and Method Arguments**

  * always use 'self' for the first argument to instance methods.
  * always use 'cls' for the first argument to class methods.

* **Method Names and Instance Variables**

  * use the function naming rules: lowercase with words separated by underscores
  * one leading underscore only for non-public methods and instance variables
* **Constants**

  * capital letters : MAX_OVERFLOW, TOTAL

* **Google Python Style Guide**

  > module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name



### _Under_Scores__

* **_single_leading_underscore**
  * declaring private variables, functions, methods, and classes in module
  * Anything with this convention are ignored in `from module import *`
  * not truly private, weak internal use indicator

```python
_internal_name = 'one_nodule' # private variable
_internal_version = '1.0' # private variable

class _Base: # private class
    _hidden_factor = 2 # private variable
    def __init__(self, price):
        self._price = price
    def _double_price(self): # private method
        return self._price * self._hidden_factor
    def get_double_price(self):
        return self._double_price()
```



* **single_trailing_underscore_**

  * used for avoiding conflict with Python keywords or built-ins.

  ```python
  Tkinter.Toplevel(master, class_='ClassName') # Avoid conflict with 'class' keyword
  list_ = List.objects.get(1) # Avoid conflict with 'list' built-in type
  ```


* **__double_leading_underscore**

  * not a convention, a syntax
  * useful if you write a class that is expected to be extended many times.
  * double underscore will mangle the attribute names of a class to avoid conflicts of attribute names between classes.
  * prohibits accessing with "ClassName.__method"

  ```python
  >>> class Foo(object):
  ...     def __init__(self):
  ...         self.__baz = 42
  ...     def foo(self):
  ...         print self.__baz
  ...     
  >>> class Bar(Foo):
  ...     def __init__(self):
  ...         super(Bar, self).__init__()
  ...         self.__baz = 21
  ...     def bar(self):
  ...         print self.__baz
  ...
  >>> x = Bar()
  >>> x.foo()
  42
  >>> x.bar()
  21
  >>> print x.__dict__
  {'_Bar__baz': 21, '_Foo__baz': 42}
  ```



* **__ double_leading_and_trailing_underscore __**
  * used for "magic method" : __ init__ , __ len __
  * __ file __ : indicates the location of Python file
  * __ eq __ : executed when a == b expression is excuted 
  * user customized cases : modifying __ init __ , you might almost do not use it.