
-- Question 1
-- Add the type signatures for the functions below and then remove the comments and try to compile.
-- (Use the types presented in the lecture.)

f1 :: Double -> Double -> Double -> Double
f1 x y z = x ** (y/z)

f2 :: Double -> Double -> Double -> Double
f2 x y z = sqrt (x/y - z)

f3 :: Char -> Double -> String -> String
f3 x y z = x:((show y) ++ z)

f4 :: Double -> Double -> Bool -> [Bool]
f4 x y z = [x > y] ++ [z]

f5 :: String -> String -> String -> Bool
f5 x y z = x == (y ++ z)

-- Question 2
-- Are really all variables in Haskell immutable? Try googling for the answer.
--   There are some Monad type that allow to deal with mutable variable within a context by keeping
--   at the same time a functional style.


-- Question 3
-- Why should we define type signatures of functions? How can they help you? How can they help others?
--   Even tough is not modantory, we should always add functions signatures in order to make the code more
--   readable and so more maintanable also from other devs.

-- Question 4
-- Why should you define type signatures for variables? How can they help you?



-- Question 5
-- Are there any functions in Haskell that let you transform one type to the other? Try googling for the answer.
--  Yes, for example the show show function allow to transform/cast any type to a [char]


-- Question 6

-- How would you write the prod function from our lesson so that it works for Int and Double? Does the code compile?
--   We can use the Num type class constraint on the function signature.
--   Num a => a -> a -> a
--   The num class contain the implementtion of the inline fucntion * that can be applied to
--   any value representing a number.


-- Question 7
-- Can you also define in Haskell list of lists? Did we showed any example of that? How would you access the inner
-- most elements?
-- Yes, for example a list of string [String] is equel to [[Char]]. We can access by !! indexFirstList !! indexSecondList
