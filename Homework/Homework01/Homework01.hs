
-- Question 1
-- Write a multiline comment below.
{- This is a multiline comment.
Yes, it is! -}

-- Question 2
-- Define a function that takes a value and multiplies it by 3.
multiplyBy3 x = x * 3

-- Question 3
-- Define a function that calculates the area of a circle.
areaOfACircle r = pi * r^2

-- Question 4
-- Define a function that calculates the volume of a cylinder by composing the previous function together with the height of the cylinder.
volumeOfACylinder r h = areaOfACircle r * h

-- Question 5
-- Define a function that checks if the volume of a cylinder is greater than or equal to 42.
checkVolume r h = volumeOfACircle r h  >= 42
