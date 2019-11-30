# Text-to-Brainfuck
Python script to translate plain text to Brainfuck code to output messages to the user.

The script inputs a string and outputs a Brainfuck code that can be used as a module in a larger Brainfuck program. The code only uses a single memory cell to output the message and also resets it to 0 after printing the message for future use.

Usage:

Run the script using:

```python3 change.py```

Then enter the message you want to translate when prompted.

The output will be printed on the console.

Alternate Usage:

Run the script using:

```python3 change.py outputFileName```

Then enter the message you want to translate when prompted.

The output will be saved to ```outputs/outputFileName```
