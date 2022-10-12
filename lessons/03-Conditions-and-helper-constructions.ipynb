{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "# Conditions and helper constructions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "## Outline\n",
        "\n",
        "* If-then-else expressions.\n",
        "\n",
        "* Guards\n",
        "\n",
        "* `let` expressions\n",
        "\n",
        "* `where`\n",
        "\n",
        "* Should I use `let` or `where`?\n",
        "\n",
        "* Things to keep in mind"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "## If-then-else expressions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "Often in your code, you have to make a choice. There are several ways to express conditions. In Haskell, we most commonly use **if-then-else** expressions:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "source": [
        "```haskell\n",
        "if <Condition> \n",
        "  then <Expesssion1>\n",
        "  else <Expesssion2>\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "Where `Condition` is a logical expression that yields `True` or `False`, `Expression1` is the expression used if `Condition` is `True`, and `Expression2` is the expression used if `Condition` is `False`. The function `checkLocalHost` below checks whether the argument is localhost or not and reports it to the user."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "\"It's localhost!\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "checkLocalhost :: String -> String\n",
        "checkLocalhost ip =\n",
        "    -- True or False?\n",
        "    if ip == \"127.0.0.1\"\n",
        "        -- When the condition is True the answer is\n",
        "        then \"It's localhost!\"\n",
        "        -- Otherwise the condition is False and the answer is\n",
        "        else \"No, it's not localhost.\"\n",
        "\n",
        "checkLocalhost \"127.0.0.1\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "The `checkLocalhost` function is applied to a single argument of type `String` and returns another value of type `String`. The argument is a string `ip` containing the IP address, and the function checks if the string is equal to `\"127.0.0.1\"`. If the check is successful the function returns `\"It's localhost!\"`, otherwise it returns `\"No, it's not localhost.\"` "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "<div class=\"alert alert-block alert-info\">\n",
        "    While in imperative programming languages, the <code>else</code> is not mandatory, in Haskell, it is! That's because, in Haskell, every function has to return a value. So, we are obligated to provide a result of the same type for both the <code>then</code> and <code>else</code> cases. \n",
        "</div>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "## Guards"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "Now, imagine that we want to do a more complex check. Like checking if this year's birthday has some special meaning. We could use nested if-else statements like this:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<style>/* Styles used for the Hoogle display in the pager */\n",
              ".hoogle-doc {\n",
              "display: block;\n",
              "padding-bottom: 1.3em;\n",
              "padding-left: 0.4em;\n",
              "}\n",
              ".hoogle-code {\n",
              "display: block;\n",
              "font-family: monospace;\n",
              "white-space: pre;\n",
              "}\n",
              ".hoogle-text {\n",
              "display: block;\n",
              "}\n",
              ".hoogle-name {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-head {\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-sub {\n",
              "display: block;\n",
              "margin-left: 0.4em;\n",
              "}\n",
              ".hoogle-package {\n",
              "font-weight: bold;\n",
              "font-style: italic;\n",
              "}\n",
              ".hoogle-module {\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-class {\n",
              "font-weight: bold;\n",
              "}\n",
              ".get-type {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "font-family: monospace;\n",
              "display: block;\n",
              "white-space: pre-wrap;\n",
              "}\n",
              ".show-type {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "font-family: monospace;\n",
              "margin-left: 1em;\n",
              "}\n",
              ".mono {\n",
              "font-family: monospace;\n",
              "display: block;\n",
              "}\n",
              ".err-msg {\n",
              "color: red;\n",
              "font-style: italic;\n",
              "font-family: monospace;\n",
              "white-space: pre;\n",
              "display: block;\n",
              "}\n",
              "#unshowable {\n",
              "color: red;\n",
              "font-weight: bold;\n",
              "}\n",
              ".err-msg.in.collapse {\n",
              "padding-top: 0.7em;\n",
              "}\n",
              ".highlight-code {\n",
              "white-space: pre;\n",
              "font-family: monospace;\n",
              "}\n",
              ".suggestion-warning { \n",
              "font-weight: bold;\n",
              "color: rgb(200, 130, 0);\n",
              "}\n",
              ".suggestion-error { \n",
              "font-weight: bold;\n",
              "color: red;\n",
              "}\n",
              ".suggestion-name {\n",
              "font-weight: bold;\n",
              "}\n",
              "</style><div class=\"suggestion-name\" style=\"clear:both;\">Use guards</div><div class=\"suggestion-row\" style=\"float: left;\"><div class=\"suggestion-warning\">Found:</div><div class=\"highlight-code\" id=\"haskell\">specialBirthday age\n",
              "  = if age == 1 then\n",
              "        \"First birthday!\"\n",
              "    else\n",
              "        if age == 18 then\n",
              "            \"You're an adult!\"\n",
              "        else\n",
              "            if age == 60 then\n",
              "                \"Finally, I can stop caring about new lingo!\"\n",
              "            else\n",
              "                \"Nothing special\"</div></div><div class=\"suggestion-row\" style=\"float: left;\"><div class=\"suggestion-warning\">Why Not:</div><div class=\"highlight-code\" id=\"haskell\">specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | otherwise = \"Nothing special\"</div></div>"
            ],
            "text/plain": [
              "Line 2: Use guards\n",
              "Found:\n",
              "specialBirthday age\n",
              "  = if age == 1 then\n",
              "        \"First birthday!\"\n",
              "    else\n",
              "        if age == 18 then\n",
              "            \"You're an adult!\"\n",
              "        else\n",
              "            if age == 60 then\n",
              "                \"Finally, I can stop caring about new lingo!\"\n",
              "            else\n",
              "                \"Nothing special\"\n",
              "Why not:\n",
              "specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | otherwise = \"Nothing special\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "specialBirthday :: Int -> [Char]\n",
        "specialBirthday age =\n",
        "  if age == 1\n",
        "    then \"First birthday!\"\n",
        "    else\n",
        "      if age == 18\n",
        "        then \"You're an adult!\"\n",
        "        else\n",
        "          if age == 60\n",
        "            then \"Finally, I can stop caring about new lingo!\"\n",
        "            else \"Nothing special\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "That's just a mess! Too complicated to both read and write. Luckily, we have guards!\n",
        "\n",
        "Guards work similarly to if-else statements, but you can have multiple conditions:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "```haskell\n",
        "func arg\n",
        "  | <Condition1> = <Result1>\n",
        "  | <Condition2> = <Result2>\n",
        "  | <Condition3> = <Result3> \n",
        "  ...\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "We use the symbol `|` to indicate the beginning of each guard."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "source": [
        "<div class=\"alert alert-block alert-info\">\n",
        "    Notice that there's no <code>=</code> sign after <code>func</code> arguments! That's a common pitfall when writing guards. Don't add that <code>=</code>!\n",
        "</div>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "With guards, we can write the `specialBirthday` function like this:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<style>/* Styles used for the Hoogle display in the pager */\n",
              ".hoogle-doc {\n",
              "display: block;\n",
              "padding-bottom: 1.3em;\n",
              "padding-left: 0.4em;\n",
              "}\n",
              ".hoogle-code {\n",
              "display: block;\n",
              "font-family: monospace;\n",
              "white-space: pre;\n",
              "}\n",
              ".hoogle-text {\n",
              "display: block;\n",
              "}\n",
              ".hoogle-name {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-head {\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-sub {\n",
              "display: block;\n",
              "margin-left: 0.4em;\n",
              "}\n",
              ".hoogle-package {\n",
              "font-weight: bold;\n",
              "font-style: italic;\n",
              "}\n",
              ".hoogle-module {\n",
              "font-weight: bold;\n",
              "}\n",
              ".hoogle-class {\n",
              "font-weight: bold;\n",
              "}\n",
              ".get-type {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "font-family: monospace;\n",
              "display: block;\n",
              "white-space: pre-wrap;\n",
              "}\n",
              ".show-type {\n",
              "color: green;\n",
              "font-weight: bold;\n",
              "font-family: monospace;\n",
              "margin-left: 1em;\n",
              "}\n",
              ".mono {\n",
              "font-family: monospace;\n",
              "display: block;\n",
              "}\n",
              ".err-msg {\n",
              "color: red;\n",
              "font-style: italic;\n",
              "font-family: monospace;\n",
              "white-space: pre;\n",
              "display: block;\n",
              "}\n",
              "#unshowable {\n",
              "color: red;\n",
              "font-weight: bold;\n",
              "}\n",
              ".err-msg.in.collapse {\n",
              "padding-top: 0.7em;\n",
              "}\n",
              ".highlight-code {\n",
              "white-space: pre;\n",
              "font-family: monospace;\n",
              "}\n",
              ".suggestion-warning { \n",
              "font-weight: bold;\n",
              "color: rgb(200, 130, 0);\n",
              "}\n",
              ".suggestion-error { \n",
              "font-weight: bold;\n",
              "color: red;\n",
              "}\n",
              ".suggestion-name {\n",
              "font-weight: bold;\n",
              "}\n",
              "</style><div class=\"suggestion-name\" style=\"clear:both;\">Use otherwise</div><div class=\"suggestion-row\" style=\"float: left;\"><div class=\"suggestion-warning\">Found:</div><div class=\"highlight-code\" id=\"haskell\">specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | True = \"Nothing special\"</div></div><div class=\"suggestion-row\" style=\"float: left;\"><div class=\"suggestion-warning\">Why Not:</div><div class=\"highlight-code\" id=\"haskell\">specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | otherwise = \"Nothing special\"</div></div>"
            ],
            "text/plain": [
              "Line 2: Use otherwise\n",
              "Found:\n",
              "specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | True = \"Nothing special\"\n",
              "Why not:\n",
              "specialBirthday age\n",
              "  | age == 1 = \"First birthday!\"\n",
              "  | age == 18 = \"You're an adult!\"\n",
              "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
              "  | otherwise = \"Nothing special\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "specialBirthday :: Int -> [Char]\n",
        "specialBirthday age\n",
        "  | age == 1 = \"First birthday!\"\n",
        "  | age == 18 = \"You're an adult!\"\n",
        "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
        "  | True = \"Nothing special\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "That last `True` is there to be a catch-all condition. A condition that always evaluates to `True` because it's literally `True`.\n",
        "\n",
        "This pattern of adding a last `True` in the last guard is so common that Haskell comes with a variable called `otherwise` that it's equal to `True` (`otherwise = True`) to make for an even more readable guard:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "\"Finally, I can stop caring about new lingo!\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "specialBirthday :: Int -> [Char]\n",
        "specialBirthday age\n",
        "  | age == 1 = \"First birthday!\"\n",
        "  | age == 18 = \"You're an adult!\"\n",
        "  | age == 60 = \"Finally, I can stop caring about new lingo!\"\n",
        "  | otherwise = \"Nothing special\"\n",
        "\n",
        "specialBirthday 60"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "Now you can easily understand what this expression does with a quick glance!\n",
        "\n",
        "OK, that's it about conditional evaluations. Now let's see how we can take our function-syntax game up a notch with `let` and `where`!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "## `let` and `where`"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "We use `let` and `where` to store the results of intermediate computations and bind local variables."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        " Let's start with `let`!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "### `let` expressions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "`let` can bind expressions to local variables in the following way:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "source": [
        "```haskell\n",
        "func arg =\n",
        "    let <BIND_1> \n",
        "        <BIND_2> \n",
        "    in  <EXPR that uses BIND_1 and/or BIND_2>\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "Where `<BIND_X>` are local bindings accessible throughout the entire `let` expression."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "Now, let's create a function that takes two temperatures—one in Celsius and one in Fahrenheit—and returns the hotter one but in Kelvin. Those are quite a few conversions, aren't they?\n",
        "\n",
        "To go from Fahrenheit to Celsius, we have to first subtract 32 and then multiply by 5/9, like this:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        " $tC = (tF - 32) * 5/9$"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "To go from Celsius to Kelvin, we just need to add 273.16 like this:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "source": [
        "$tK = tC + 273.16$"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "So, if we want to create **a single function** that does all that, we can create something like this:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "313.16"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "hotterInKelvin :: Double -> Double -> Double\n",
        "hotterInKelvin c f = if c > (f - 32) * 5 / 9 then c + 273.16 else ((f - 32) * 5 / 9) + 273.16\n",
        "\n",
        "hotterInKelvin 40 100"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "It works, but that's textbook I-have-no-idea-what-I-wanted-to-do-with-that-two-weeks-ago code.\n",
        "\n",
        "A better approach is using `let` bindings for the intermediate expressions and writing the expression that pulls everything together at the `in` part:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "313.16"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "hotterInKelvin' :: Double -> Double -> Double\n",
        "hotterInKelvin' c f =\n",
        "  let fToC t = (t - 32) * 5 / 9\n",
        "      cToK t = t + 273.16\n",
        "      fToK t = cToK (fToC t)\n",
        "   in if c > fToC f then cToK c else fToK f\n",
        "\n",
        "hotterInKelvin' 40 100"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "Now our code is way more readable and doesn't have all that repeated expressions!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "But wait, there's more! We can also use the `where` construction!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "### `where`"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "We can use `where` to bind values to variables in the following way:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "source": [
        "```haskell\n",
        "func arg = <EXP that uses BIND_1 and/or BIND_2>\n",
        "    where <BIND_1>\n",
        "          <BIND_2>\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "skip"
        }
      },
      "source": [
        "So, the same `hotterInKelvin` function as before can be expressed with `where` like this:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "Where `<BIND_X>` are bindings accessible throughout the entire function body."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "313.16"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "hotterInKelvin'' :: Double -> Double -> Double\n",
        "hotterInKelvin'' c f = if c > fToC f then cToK c else fToK f\n",
        "  where\n",
        "    fToC t = (t - 32) * 5 / 9\n",
        "    cToK t = t + 273.16\n",
        "    fToK t = cToK (fToC t)\n",
        "\n",
        "hotterInKelvin'' 40 100"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "Ok, they both seem to do the same thing. So, why bother having both? Couldn't we just choose to use one of them?\n",
        "\n",
        "Well, there are plenty of cases where they are interchangeable. In those cases, you can choose whichever you like the most. But they also have their limitations and strengths."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "### Should I use `let` or  `where`?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "`let` expressions are convenient whenever we want to split complex expressions into smaller building blocks that you combine into a final expression."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "For example, imagine you wish to calculate the volume of a house. We could simplify the problem like this:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "A house is a cube with a pyramid on top (the roof). So, to find its volume, we need to calculate the volume of the cube and the volume of the pyramid and add them together:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "30.0"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "houseV side roofH = let cubeV = side ^ 3\n",
        "                        pyramidV = (side ^ 2) * roofH / 3\n",
        "                    in  cubeV + pyramidV\n",
        "                    \n",
        "houseV 3 1"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "We create the `cubeV` and `pyramidV` building blocks inside the `let` block, and then we use them inside the `in` expression.\n",
        "\n",
        "Besides the clarity of the syntax, another advantage is that if the final expression later becomes more complicated (for example, we add a chimney to the house), we just need to add another binding and use it in the final expression!:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "30.25"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "houseV side roofH = let cubeV = side ^ 3\n",
        "                        pyramidV = (side ^ 2) * roofH / 3\n",
        "                        chimneyV = (0.5 ^ 2) * roofH\n",
        "                    in  cubeV + pyramidV + chimneyV\n",
        "                    \n",
        "houseV 3 1"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "On the other hand, `where` expressions are convenient whenever we want to scope bindings over several guarded equations."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "Because we can't access `let` bindings across all guards, but with `where` bindings, we can!!\n",
        "For example:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 51,
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        },
        "vscode": {
          "languageId": "python"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "\"What in the world is that huge thing?!\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "analyzeCylinder :: Float -> Float -> String\n",
        "analyzeCylinder diameter height\n",
        "       | volume < 10 = \"The cylinder is a glass.\"\n",
        "       | volume < 100 = \"The cylinder is a bucket.\"\n",
        "       | volume < 1000 = \"The cylinder is a tank.\"\n",
        "       | otherwise = \"What in the world is that huge thing?!\"\n",
        "    where\n",
        "        volume = pi * diameter^2 * height / 4\n",
        "\n",
        "analyzeCylinder 15 6"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "As you can see, we defined the `volume` binding inside the `where` block, and then we accessed it on every guarded expression!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "And finally, the main difference between the two is that `where` bindings are declarations bounded to a surrounding syntactic construct. Meaning, they can only be used in specific places (like inside a function body). But `let` introduces an expression, so it can be used wherever an expression can be used. For example:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 55,
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        },
        "vscode": {
          "languageId": "python"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "86400"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/plain": [
              "6000"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "-- Seconds in a day\n",
        "24 * (let seconds = 60 in seconds * 60) \n",
        "\n",
        "-- The volume of a rectangular prism (we can separate expressions by semicolons to have them in the same line)\n",
        "let s1 = 10; s2 = 20; s3 = 30; in s1*s2*s3 "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "In all the cases where you could use one or the other, pick the one that feels right for the situation or your style. It takes some practice to appropriately choose which one to use, and there's also the programmer's preference. So don't worry too much about it. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "### Things to keep in mind"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "Expressions defined with `where` are not accessible outside that function body."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 56,
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "outputs": [
        {
          "ename": "",
          "evalue": "",
          "output_type": "error",
          "traceback": [
            "<interactive>:1:1: error:\n    • Variable not in scope: fToC :: t0 -> t\n    • Perhaps you meant ‘fToK’ (line 1)"
          ]
        }
      ],
      "source": [
        "fToK t = 273.16 + fToC t\n",
        "    where fToC t = (t - 32) * 5 / 9\n",
        "    \n",
        "fToC 60"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "Expression introduced in a `let` expression exist only within that `let` expression."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "For example, this function takes your name and last name and returns your initials:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 59,
      "metadata": {
        "slideshow": {
          "slide_type": "fragment"
        }
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "\"R.F.\""
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "initials :: String -> String -> String\n",
        "initials name lastName = if name == \"\" || lastName == \"\"\n",
        "                         then \"How was your name again?\"\n",
        "                         else let x = head name\n",
        "                                  y = head lastName\n",
        "                              in [x] ++ \".\" ++ [y] ++ \".\"\n",
        "\n",
        "initials \"Richard\" \"Feynman\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "notes"
        }
      },
      "source": [
        "The expressions `x` and `y` are only available inside that `let` expression. If you tried to use them inside `if` or `then`, they would be outside the scope, and it would not compile."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "slideshow": {
          "slide_type": "slide"
        }
      },
      "source": [
        "## Summary\n",
        "\n",
        "In this lesson, we've discussed:\n",
        "\n",
        "* If-then-else statements, and why you always have to define the else case.\n",
        "\n",
        "* How to use guards to avoid nested if-else statements.\n",
        "\n",
        "* How to use `let` and `where` to store the results of intermediate computations, bind local variables, allow for cleaner code, and avoid repeating yourself."
      ]
    }
  ],
  "metadata": {
    "celltoolbar": "Slideshow",
    "kernelspec": {
      "display_name": "Haskell",
      "language": "haskell",
      "name": "haskell"
    },
    "language_info": {
      "codemirror_mode": "ihaskell",
      "file_extension": ".hs",
      "mimetype": "text/x-haskell",
      "name": "haskell",
      "pygments_lexer": "Haskell",
      "version": "8.10.7"
    },
    "rise": {
      "enable_chalkboard": true,
      "header": "<img style=\"position: relative; left: 1230px; width: 200px; top: 10px;\" src=\"https://raw.githubusercontent.com/rober-m/haskell-bootcamp/main/images/input-output.svg\"/>"
    },
    "vscode": {
      "interpreter": {
        "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
