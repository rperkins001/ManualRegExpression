# ManualRegExpression

2) given as input a list of strings, with each string only containing alphabetical characters, 
describe an algorithm that generates a regular expression which match all words.
 
For example, given:
 
[burger, cheeseburger, coke, cost], one such expression could be:
 
(.*burger)|(co.*)
 
There is no unique answer here, since there are infinite expressions that would work, 
so the discussion is about strategies that lead to set of strings as long as possible 
(i.e. "Burger" vs just "urg")
