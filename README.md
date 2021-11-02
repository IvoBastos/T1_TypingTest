# T1_TypingTest

Use the terminal to run Typing Test.

Typing Test has two modes for operation. You can choose the fixed number of inputs mode or the fixed time mode.

In the fixed number of inputs mode, you can choose how many inputs you want to introduce by using the command --max_value or -mv followed by an integer number:

    ./main.py -mv 5
            
In this case, the program will ask you for 5 inputs with no time limitation.

For the fixed time mode, you must activate the mode using the --use_time_mode or -utm command and use -mv to indicate the number of seconds you want the program to run:

    ./main.py -utm -mv 5

In this case, the program will run for 5 seconds with no inputs limitation.

Press the space bar at any time to stop the test.

If you need any help use the command --help or -h

    ./main.py -h

This program was developed by Group 6 in the context of the Robotic Systems Programming course.

November 2021