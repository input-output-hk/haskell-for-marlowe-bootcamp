-- Question 1
-- Add the type signatures for the functions below and then remove the comments and try to compile.
-- (Use the types presented in the lecture.)

f1 :: Float -> Float -> Float -> Float
f1 x y z = x ** (y/z)

f2 :: Double -> Double -> Double -> Double
f2 x y z = sqrt (x/y - z)

f3 :: Bool -> Bool -> [Bool]
f3 x y = [x == True] ++ [y]

f4 :: String -> String -> String -> Bool
f4 x y z = x == (y ++ z)


-- Question 2
-- Are really all variables in Haskell immutable? Try googling for the answer.

{-Although the functional programming paradigm emphasises the virtues of immutable variables, sometimes you need mutable variables nonetheless. 
You can either simulate mutable variables using the state monad provided for instance by Control.Monad.Trans.State in the transformers package 
or you can use really mutable variables as provided by Data.IORef or Data.STRef or Control.Concurrent.STM.TVar from the stm package.
In either case you need a monad in order to cope with mutability, while staying purely functional.  -}

-- Question 3
-- Why should we define type signatures of functions? How can they help you? How can they help others?

{- Signatures cast the data types for the function output and it's associated inputs.
    This helps me by allowing me to restrict the data types of the input and output of my functions. For instance, I may want to restrict a function to useing Int instead of Integer for computational efficiency.
    This helps others by allowing them to read my code and understand what data types are assocaited with my functions -}

-- Question 4
-- Why should you define type signatures for variables? How can they help you?

{- I would define type signatures for variables to assign the data type to the variable.
    Since variables can be changed it is important to assign the data type to limit what data the variable can carry.
    It is important that data types of variables match the signature of a function, also important when appending/prepending variables to lists or Tuples -}

-- Question 5
-- Are there any functions in Haskell that let you transform one type to the other? Try googling for the answer.

{- convert f x y = fromIntegral (f (fromIntegral x) (fromIntegral y))

This is pretty straightforward. However, if I were to do it, I'd take advantage of the on function from Data.Function, which converts the inputs of functions that take two arguments before applying it.
    So, in your example, it would look like this:

convert f x y = fromIntegral ((f `on` fromIntegral) x y)

I, personally, would go one step further and make this function point-free, but because on f fromIntegral expects two arguments, you can't just use (.), so I usually define an operator for this:

(.:) = (.) . (.)

You can figure out why this works on your own if you'd like, but now I can define convert as this:

convert f = fromIntegral .: (f `on` fromIntegral)

I feel that this is a lot more readable, but I am biased because I have been coding Haskell like this for a while now.

Also, if you look at the inferred type of this variable, you'd see that it's much more general than what you wanted:

 convert :: (Integral a, Integral a1, Num b, Num b1) = (b1 -> b1 -> a) -> a1 -> a1 -> b -}


-- Question 6
-- Can you also define in Haskell list of lists? Did we showed any example of that? How would you access the inner
-- most elements?

{- Lists can be concatinated in Haskell, but as far as I am aware a list cannot be an element of a list. I get an error when I try to insert a list as an element of a new list.
    No examples were shown of defining lists of lists.
    To access the inner elements of a list I would use the function "!!" along with the element number (starting from 0) I want to access -}