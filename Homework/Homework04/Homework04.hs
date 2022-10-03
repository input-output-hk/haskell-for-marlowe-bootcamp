import Distribution.Simple.Utils (xargs)
-- Question 1
-- Lets say you have the nested values defined bellow. How would you get the value of
-- 4 by using only pattern matching in a function?

nested :: [([Int], [Int])]
nested = [([1,2],[3,4]), ([5,6],[7,8])]

firstElement = nested !! 0

fourthElement :: (x, y) -> y
fourthElement (_,y) = y

three :: [([Int], [Int])] -> Int
three [(_,[_,d]), _] = d
three _ = 0

-- Question 2
-- Write a function that takes a list of elements of any type and, if the list has 3 or more elements, it
-- removes them. Else, it does nothing. Do it two times, one with multiple function definitions and one with
-- case expressions.

removeElements :: [a] -> [a]
removeElements newList
    | [x,y] = [x,y]
    | [x,y,z] = []
    | [x,y,z,a] = [a]

-- Question 3
-- Create a function that takes a 3-element tuple (all of type Integer) and adds them together

addThreeIntegers :: (Int, Int, Int) -> Int
addThreeIntegers (x, y, z) = x + y + z


-- Question 4
-- Implement a function that returns True if a list is empty and False otherwise.

findEmptyList :: [a] -> Bool
findEmptyList [] = True
findEmptyList _ = False

-- Question 5
-- Write the implementation of the tail function using pattern matching. But, instead of failing if
-- the list is empty, return an empty list.

tailFunction :: [a] -> [a]
tailFunction (x:xs) = xs
tailFunction [] = []

-- Question 6
-- write a case expression wrapped in a function that takes an Int and adds one if it's even. Otherwise does nothing. 
-- (Use the `even` function to check if the number is even.)

makeOdd :: Int -> Int
makeOdd x = case even x of
    True -> x + 1
    False -> x