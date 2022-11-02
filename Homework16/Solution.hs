
-- Question 1
-- Take the book code exple from the lesson and write a function that asks the user to
-- input an index (1, 2 or 3) and returns the title of the book by using the <$> operator.
-- The code you need is defined below. If it can't get the title write a message.

import qualified Data.Map as Map
import Data.Maybe (fromJust, isJust)

data Book = Book {
    price :: Int , 
    yearPublished :: Int ,
    title :: String
} deriving Show

book1 = Book {
    price = 15 ,
    yearPublished = 1997 ,
    title = "Harry Potter and the Philosopher's Stone"
}

book2 = Book {
    price = 17 ,
    yearPublished = 1998 ,
    title = "Harry Potter and the Chamber of Secrets"
}

book3 = Book {
    price = 19 ,
    yearPublished = 1999 ,
    title = "Harry Potter and the Prisoner of Azkaban"
}

books :: Map.Map Int Book
books = Map.fromList $ zip [1..3] [book1, book2, book3]

getTitle :: IO ()
getTitle = do
    putStrLn "Input an index:"
    ind <- read <$> getLine
    let book = Map.lookup ind books
    let myTitle = title <$> book
    if isJust myTitle then
        putStrLn $ "The title is:\n" ++ fromJust myTitle
    else putStrLn $ "Could not find the book with index: " ++ show ind

-- Question 2
-- For the Wrapper example make an instance of Functor for the Wrapper type. Then write 
-- a function that asks the user to input a number (can be also decimal), creates a Wraper 
-- type from it with (<$) and prints the result of applying add1 to it. 

data Wrapper a = Empty | Wrapper a deriving Show

add1 :: Num a => a -> a
add1 n = n + 1

fmapWrapper :: (a -> b) -> Wrapper a -> Wrapper b
fmapWrapper f Empty = Empty
fmapWrapper f (Wrapper n) = Wrapper (f n)

instance Functor Wrapper where
    fmap = fmapWrapper

createWrapper :: IO ()
createWrapper = do
    putStrLn "Input a number:"
    n <- (read <$> getLine) :: IO Double
    print $ add1 <$> (<$) n (Wrapper 0)

-- Question 3
-- Implement a linked list data type (a list that is build similar as Haskell lists are - 
-- with consing) and then define an Functor instance for this List data type. Then create
-- a list that has this type and apply the add1 function from the previous question to it.

data List a = Null | Cons a (List a) deriving Show 

instance Functor List where
    fmap f Null = Null
    fmap f (Cons x leftover) = Cons (f x) (fmap f leftover)

myList :: List Int
myList = Cons 1 (Cons 2 (Cons 3 Null))

add1ToListAndPrint :: IO ()
add1ToListAndPrint = do
    print $ add1 <$> myList
