# 0x12. JavaScript - Warm up

## Resources
Read or watch:

- Writing JavaScript Code
- Variables
- Data Types
- Operators
- Operator Precedence
- Controlling Program Flow
- Functions
- Objects and Arrays
- Intrinsic Objects
- Module patterns
- var, let and const
- JavaScript Tutorial
- Modern JS

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between var, const and let
- What are all the data types available in JavaScript
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use while and for loops
- How to use break and continue statements
- What is a function and how do you use functions
- What does a function that does not use any return statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Requirements

- [Writing JavaScript Code](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
- [Variables](https://intranet.alxswe.com/rltoken/zgOWmcpVLZFEmFlmuwayyg)
- [Data Types](https://intranet.alxswe.com/rltoken/VPd6JWaLrwOBzjAeXNAEqg)
- [Operators](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
- [Operator Precedence](https://intranet.alxswe.com/rltoken/PHtcJJk30gBNmlFQ9R4RVg)
- [Controlling Program Flow](https://intranet.alxswe.com/rltoken/tsreKcNh_KmTmLPHsfvJRw)
- [Functions](https://intranet.alxswe.com/rltoken/e3EfHIxICdIncGBwwIDbXQ)
- [Objects and Arrays](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
- [Intrinsic Objects](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
- [Module patterns](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
- [var, let and const](https://intranet.alxswe.com/rltoken/gJi61GeJTRX0g-M0Rx-0Iw)
- [JavaScript Tutorial](https://intranet.alxswe.com/rltoken/Y8hkOcy5jO22lQGyF6_NiA)
- [Modern JS](https://intranet.alxswe.com/rltoken/NZawtiBjWUpiojnrtVywNw)

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc

##### Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.

## Tasks
### 0. First constant, first print
Write a script that prints `“JavaScript is amazing”`:

- You must create a constant variable called myVar with the value `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 1. 3 languages
Write a script that prints 3 lines:

- The first line: `“C is fun”`
- The second line: `“Python is cool”`
- The third line: `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 2. Arguments
Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print `“No argument”`
- If only one argument is passed to the script, print `“Argument found”`
- Otherwise, print `“Arguments found”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- Reference: `process.argv`

`NB:`
The script first uses the `slice()` method to create a new array args that contains only the command-line arguments (i.e., it excludes the first two elements of process.argv). It then checks the length of this array to determine how many arguments were passed.

If args has `length 0`, it means no arguments were passed, so the script prints `"No argument"` using `console.log()`. If args has `length 1`, it means one argument was passed, so the script prints `"Argument found"`. Otherwise, it prints `"Arguments found"`.

### 3. Value of my argument
Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print `“No argument”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`
## solution
This script takes in a command line argument and outputs it. If no argument is passed, it outputs `"No argument"`. Here are some examples:

`vagrant@ubuntu-focal:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js `
`No argument`
`vagrant@ubuntu-focal:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js School`
`School`
`vagrant@ubuntu-focal:~/alx-higher_level_programming/0x12-javascript-warm_up$`

### 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: `“ is ”`

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 5. An Integer
Write a script that prints `My number`: <first argument converted in integer> if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

### 6.  
