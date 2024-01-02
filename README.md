# Nervethon Language

## Language Overview

Nervethon, adapted from the Python programming language with hints of the C language, is a user-friendly software development platform that aims to improve the skills and knowledge of beginners in programming. Although our team targets the improvement of beginners, Nervethon can be utilized by users of different backgrounds.

The idea behind the name “Nervethon” came from the ever-famous anime called Sword Art Online, which uses NerveGear, a streamlined helmet with high-density microwave transceivers capable of accessing the user’s brain. The “Nerve” in Nervethon comes from NerveGear, and the “-thon” is inspired by the Python Language.

## General Rules

- The standard is to use English words in writing a program.
- The program must have a main function enclosed within a Link.Start and a Link.End.
- Nervethon is a case-sensitive language; "Link" and "link" are considered different.
- Reserved words must start with an uppercase letter followed by lowercase letters, unless a period (.) is present, in which case the first letter after the period is capitalized, and the rest are lowercase (e.g., Generate, Absorb, Sys.Call).
- All identifiers should start with lowercase letters and can be followed by lowercase letters, uppercase letters, underscores (_), or numbers. Identifiers starting with an uppercase letter or a number will be considered an error.
- Reserved words, spaces, and special characters (except underscores) cannot be used as identifiers.
- All global declarations must precede the main function.
- Variables and constants declared before the main function are considered global declarations.
- Variables and constants declared within the main function or user-defined function/s are considered local declarations.
- All function definitions can only be done after the main function, and all function calls can only be made inside the main function or a user-defined function.
- Any statement outside the main function that is not a global declaration, a comment, a user-defined function, or enclosed inside a user-defined function will be considered an error.
- Comments should be enclosed in a forward slash and an asterisk and must end with an asterisk and a forward slash (/* */). They can be single-line or multi-line.
- Running a program with an invalid character/symbol will result in an error (e.g., a?).
- To terminate a statement, simply press the enter key.
