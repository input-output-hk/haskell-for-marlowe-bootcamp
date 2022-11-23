-- Question 1
-- Write a function that checks if the monthly consumption of an electrical device is bigger, equal, or smaller than the maximum allowed and
-- returns a message accordingly. 
-- The function has to take the hourly consumption of an electrical device, the hours of daily use, and the maximum monthly consumption allowed.
-- (Monthly usage = consumption (kW) * hours of daily use (h) * 30 days).

checkConsumption consumption time maxC
    | monthlyC > maxC = "Penguins are disappointed in you!"  
    | monthlyC == maxC = "Don't push it!"
    | otherwise = "You're good!"
    where
        monthlyC = consumption * time * 30

-- Question 2
-- Prelude:
-- We use the function `show :: a -> String` to transform any type into a String.
-- So `show 3` will produce `"3"` and `show (3 > 2)` will produce `"True"`.

-- In the previous function, return the excess/savings of consumption as part of the message.

checkConsumption consumption time maxC
    | monthlyC > maxC = "Penguins are disappointed in you. You're wasting: " ++ show (monthlyC - maxC) ++ "kWh per month!"
    | monthlyC == maxC = "Don't push it!"
    | otherwise = "You're saving: " ++ show (maxC - monthlyC) ++ "kWh per month! Good job!!"
    where
        monthlyC = consumption * time * 30

-- Question 3
-- Write a function that showcases the advantages of using let expressions to split a big expression into smaller ones.
-- Then, share it with other students in Canvas.


-- Question 4
-- Write a function that takes in two numbers and returns their quotient such that it is not greater than 1.
-- Return the number as a string, and in case the divisor is 0, return a message why the division is not
-- possible. To implement this function using both guards and if-then-else statements.  

guardsAndIf :: Double -> Double -> String
guardsAndIf a b
  | a < 0 && b < 0 = if (a < b) then show (b / a) else show (a / b)
  | a > b = if a /= 0 then show (a/b) else "a is larger but 0"
  | a < b = if b /= 0 then show (b/a) else "b is larger but 0"
  | otherwise = if a /= 0 then "1" else "a and b are both 0"


-- Question 5
-- Write a function that takes in two numbers and calculates the sum of square roots for the product and quotient
-- of those numbers. Write the function such that you use a where block inside a let expression and a
-- let expression inside a where block. 

invertedConstructions :: Double -> Double -> Double
invertedConstructions a b = let sqrtProd = sqrt abProd where abProd = a * b
                            in sqrtProd + sqrtQuot
                            where sqrtQuot = let abQuot = a / b in sqrt abQuot

