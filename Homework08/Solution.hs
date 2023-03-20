-- This homework is around creating Haskell types that represent wines from over the world.

-- Question 1
-- Different wines are made from different grapes, there are around 10000 varieties over the world!
-- Create a type synonym called "Grape" for the different grape names as strings.
-- Additionally, use this type synonym for the grapes: "Sangiovese", "Cabernet-sauvignon", "Merlot" and "Garnacha".

type Grape = String

grape1 :: Grape
grape1 = "Sangiovese"

grape2 = "Cabernet-sauvignon" :: Grape
grape3 = "Merlot" :: Grape
grape4 = "Garnacha" :: Grape

-- Question 2
-- The most famous regions that export wine are located in France, Italy and Spain.
-- Each of these countries is divided up in smaller regions.
-- These smaller regions are known for a certain style, for example the Champagne region in France
-- Create a type synonym called "Region" for wine region given their country and region as a tuple of strings.
-- Additionally, use this type synonym for the regions: Bordeaux in France, Tuscany in Italy and Rioja in Spain.

type Region = (String, String)

region1 = ("Bordeaux", "France") :: Region
region2 = ("Tuscany", "Italy") :: Region
region3 = ("Rioja", "Spain") :: Region

-- Question 3
-- A wine is either one of three kinds, these are red, white or rose wine.
-- Besides its kind, each wine also has a given alcohol level.
-- Create a data type called "Kind" that represents these three kinds, with each capturing the level of alcohol.
-- Additionally, use this data type for the examples: red wine with 14.5% alcohol, white wine with 13% alcohol 
-- and Rose wine with 12% alcohol.

data Kind = Red Float | White Float | Rose Float deriving (Show)

wine1 = Red 14.5 :: Kind
wine2 = White 13 :: Kind
wine3 = Rose 12 :: Kind

-- Question 4
-- In the world of wines, bottles display all of the above information for the consumer on its label.
-- Create a record type called "Label" that captures the grapes that are in a wine, the region it's from,
-- and its kind. Notice that some wines are a blended combination of multiple grapes!
-- Additionally, create for each of the described wine below a label.

data Label = Label {
    grapes :: [Grape],
    region :: Region,
    kind :: Kind
} deriving (Show)


-- Larrosa Rose is a rose wine from the region Rioja. It is made from the Garnacha grape and 
-- has a alcohol level of 14%.

larrosaRose = Label {grapes = [grape4], region = region3, kind = Rose 14 }

-- Castiglioni is a red wine from the region of Tuscany. It is made from the grape Sangiovese and
-- has a alcohol level of 12.5%.

castiglioni = Label {grapes = [grape1], region = region2, kind = Red 12.5 }

-- Bordeaux is known for its red wine, these are mainly a blend between Cabernet-sauvignon and Merlot.
-- Create a Label for the wine "Le Petit Haut Lafitte" that has an alcohol percentage 13.5%.

lePetitHaitLafitte = Label {grapes = [grape2, grape3], region = region1, kind = Red 13.5 }

-- Question 5
-- Write a function `containsGrape` that takes a list of Labels and a Grape and returns a boolean.
-- The function should check if the there exists a wine in the Label that contains this Grape.

containsGrape :: [Label] -> Grape -> Bool
containsGrape labels grape = any (\Label{grapes=xs} -> grape `elem` xs) labels

-- This is a test list for the `containsGrape` function with an grape that is not in the list.
grapeList = [larrosaRose,castiglioni,lePetitHaitLafitte]
newGrape = "Pinot Noir"
