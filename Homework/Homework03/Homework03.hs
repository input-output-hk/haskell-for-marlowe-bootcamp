import Text.XHtml.Transitional (maxlength)
import Distribution.Simple.Utils (xargs)
-- Question 1
-- Write a function that checks if the monthly consumption of an electrical device is bigger, equal, or smaller than the maximum allowed and
-- returns a message accordingly. 
-- The function has to take the hourly consumption of an electrical device, the hours of daily use, and the maximum monthly consumption allowed.
-- (Monthly usage = consumption (kW) * hours of daily use (h) * 30 days).

checkConsumption :: Float -> Float -> Float -> String
checkConsumption use hrs maxCon
         | consumption < maxCon = "Usage within limits."
        | consumption == maxCon = "Usage at limit."
        | otherwise = "Usage exceeds limits."
    where
        consumption = use * hrs * 30

-- Question 2
-- Prelude:
-- We use the function `show :: a -> String` to transform any type into a String.
-- So `show 3` will produce `"3"` and `show (3 > 2)` will produce `"True"`.

-- In the previous function, return the excess/savings of consumption as part of the message.

checkConsumption2 :: Float -> Float -> Float -> String
checkConsumption2 use hrs maxCon
        | consumption < maxCon = "Usage within limits with " ++ show remainder ++ " kW remaining."
        | consumption == maxCon = "Usage at limit " ++ show remainder ++ " kW remaining."
        | otherwise = "Usage exceeds limits " ++ show remainder ++ " kW remaining."
    where
        consumption = use * hrs * 30
        remainder = maxCon - consumption


-- Question 3
-- Write a function that showcases the advantages of using let expressions to split a big expression into smaller ones.
-- Then, share it with other students in Canvas.

showCaseLet  :: Float -> Float
showCaseLet  x = 
    let funk1 x = x + 3
        funk2 x = -x + 9
    in if x <=3 then funk1 x else funk2 x

-- Question 4
-- Write a function that takes in two numbers and returns their quotient such that it is not greater than 1.
-- Return the number as a string, and in case the divisor is 0, return a message why the division is not
-- possible. To implement this function using both guards and if-then-else statements.  

returnQuotient :: Float -> Float -> String
returnQuotient x y
    | x > y = if x /= 0 then "Route 1a: " ++ show(x/y) else "Route 1b: x is larger but equal to zero"
    | x < y = if y /= 0 then "Route 2a: " ++ show(y/x) else "Route 2b: y is larger but equal to zero"
    | otherwise = if x /=0 then "Route 3a: 1" else "Route 3b: x and y are both zero"

-- Back of the book answer
guardsAndIf :: Double -> Double -> String
guardsAndIf a b
  | a > b = if a /= 0 then show(a/b) else "a is larger but 0"
  | a < b = if b /= 0 then show(b/a) else "b is larger but 0"
  | otherwise = if a /= 0 then "1" else "a and b are both 0"

-- Question 5
-- Write a function that takes in two numbers and calculates the sum of squares for the product and quotient
-- of those numbers. Write the function such that you use a where block inside a let expression and a
-- let expression inside a where block. 

--I have a question regarding question #5. It asks to calculates the sum of squares for the product and quotient of 2 numbers. Just wondering what the equation for this, given x and y as inputs, is: (x + y)^2 + (x / y)^2?

funky :: Float -> Float -> Float
funky x y = let sqrtProd = sqrt xTimesY where xTimesY = x * y
                            in sqrtProd + sqrtQuot
                            where sqrtQuot = let xDivY = x / y in sqrt xDivY 
