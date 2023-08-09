reference -> https://www.youtube.com/@CodeAesthetic

## Naming Things in Code:
  1) avoid using variables with single letters unless for mathematical use...
  2) **NEVER ABBREVIATE** your variable names...
  3) put units in your variable names... eg: delayseconds
  4) no need to add a type to your type... eg: starting interfaces with an I
  5) don't name a class "Base" or "Abstract"... if you feel the need to use this change the name of the base class
  6) Don't name code "Utils" give them their own classes...

#

## Comments:
  * they tell you about the internal workings of the code... 
  * If your code is complex enough that it needs a comment, you should instead try and simplify or refactor the code...
  * comments can be outdated if the code is being updated regularly...
  * **Instead,** try to make high-quality Documentation... it describes the high-level architecture and public APIs of a system, and it describes how to use the code...

#

## Abstraction making codes worse:
  it is true that code repetition is bad and abstraction is good but there is a hidden tradeoff namely **"COUPLING"**...
  * _Not Worth_ ->
    - Sharing member variables across two classes
    - Not valuable for abstraction user
  * _Worth_ ->
    - Many implementations with complex construction
    - Deferred execution from creation

## Road to never nesting:
  Never add more than 3 inner blocks to a piece of code...
  steps to reduce inner nesting:
    **Always make a function do only one thing**
   * _Extraction_ -> pulling out part of function into its own function...
   * _Inversion_ -> flipping conditions and switching to an early condition... write the wrong condition first

## Dependency Injection:
  when you have a piece of code that uses another piece of code and instead of using that code 
  directly it's passed in instead. (_When you pass something in to be used we call it injection i.e. we pass in the dependent code within the code that uses it..._)
  
