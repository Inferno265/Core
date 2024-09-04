# Core

A programming lanugage for Sentinel Corporation

## Installation

Download file core.exe and put it into C:\Core

Then add C:\Core into the env variables and restart

## Usage

type: ```core yourfile.co``` (if you have created a file) into the cmd

## Documentation

### .var

#### Properties:
.name -> assign name to variable
.value -> assign value to variable

#### Syntax:

```.var(.name("x").value(10))```

### .msg

#### .msg!
##### Properties of msg!:

argv*std::string -> print out string

##### Syntax of msg!:
```.msg("Hello World!")```
##### Properties:
argv -> print out variable

##### Syntax:

```.msg(x)```
