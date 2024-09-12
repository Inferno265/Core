Core Framework Documentation
Overview
Core is a Java framework designed to make game development easier for developers. It provides essential functions to initialize game assets and load game information into memory, allowing developers to focus on building game logic and design rather than boilerplate code.

Installation
To install the Core framework, simply add the Core package to your Java project and import the required library.

Step-by-Step Guide
Add Core Package: Ensure you have the Core framework package available in your project.
Import Core: In your Java code, add the following import statement:
java
Skopiuj kod
import javax.game.*;
Functions
1. init() -> boolean
Initializes the framework and checks for the presence of essential game files.

Description: This function performs the initial setup for your game, ensuring that all required assets are in place.
Return Value:
true: Initialization is successful, and the game can proceed.
false: Initialization failed due to the absence of the gameinfo.gi file.
Example:
```if (Core.init()) {
     ...
}
```

2. loadgiRAM(int x) -> void
Loads the gameinfo.gi file into the specified RAM slot.

Description: This function reads the gameinfo.gi file and loads its contents into a designated memory slot specified by the integer x. This allows for easy access and manipulation of game data during runtime.
Parameters:
x (int): The RAM slot where the gameinfo.gi contents will be stored.
Example:
```Core.loadgiRAM(0b0000);``` // Loads gameinfo.gi into RAM slot 1.
Usage Example
```
import javax.game.*;

public class Main {
    public static void main(String[] args) {
        if (Core.init()) {
            Core.loadgiRAM(0b0000);
            System.out.println("Gameinfo loaded into RAM slot 0b0000.");
        }
    }
}
```
