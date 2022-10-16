
-- Question 1
-- Write a multiline comment below.
{-
  This is my multi-line comment! I'm looking forward to learning Haskell and growing as a developer.
-}

-- Question 2
-- Define a function that takes a value and multiplies it by 3.
multiplyBy3 x = x * 3

-- Question 3
-- Define a function that calculates the area of a circle.
areaOfCircle radius = pi * radius ^ 2

-- Question 4
-- Define a function that calculates the volume of a cylinder by composing the previous function together with the height of the cylinder. 
volumeOfCylinder radius height = areaOfCircle radius * height 

-- Question 5
-- Define a function that takes the height and radius of a cylinder and checks if the volume is greater than or equal to 42.
cylinderVolumeAtLeast42 radius height = (volumeOfCylinder radius height) >= 42 

