# Overview
This is an interpreter written in python for the Plankalkül language, originally created by Konrad Zuse. I found that there was only a compiler written, and it required you to ude the 2D matrix originally designed by Zuse. This interpreter allows you to use the updated "Plankalkül 2000", or linearized Plankalkül, developed by Raúl Rojas, Cüneyt Göktekin, Gerald Friedland, Mike Krüger, Olaf Langmack, and Denis Kuniß.

## Running The Interpreter
Because this is a python program, and because there is no filetype for Plankalkül, just use a plain .txt document, and specify the document name in the command line call, like so:
> python3 interpreter.py code.txt

## Language Usage
The 1990 document doesn't specify how programs are called, so for my interpreter I've decided that programs will operate like functions, and need to be called outside of their definition. Simply call the program by the name of its Randauszug outside of the function definition to call it. Due to this, I have devised my own simple input method, where the only variable values that will be requested from the user are those in the actual function call. Additionally, for convenience, the bit limit will be provided with the request.
