# python-dev-intern-task-8-rule-based-chatbot
Python Developer Internship Task 8 (Rule Based Chatbot)

## Rule-Based Chatbot? ##

A rule-based chatbot uses a set of predefined rules to respond to user input. These rules are often based on keyword matching or simple pattern recognition.

Advantages of Rule-Based Chatbots

    Predictability: Responses are consistent and controlled.
    Simplicity: Easier to implement and maintain compared to AI-based chatbots.
    Cost-Effective: Does not require extensive computational resources or large datasets for training.

Disadvantages of Rule-Based Chatbots

    Limited Understanding: Can only handle scenarios it is explicitly programmed for.
    Lack of Flexibility: Unable to learn from interactions and improve over time.
    Scripted Responses: May feel less natural compared to AI-driven chatbots.

Other category is Self-learning chatbot

For GUI
pip install tkinter - not required

1. scrolledtext is used for a multi-line text widget with a built-in scrollbar.
2. grid() method: This method is used to place widgets in specific rows and columns within the window or frame.

    row, column: Specifies the row and column for the widget.
    columnspan: Allows a widget to span multiple columns.
    padx, pady: Adds padding around the widget.
    sticky="nsew": Makes the widget expand to fill the available space in its grid cell (North, South, East, West).

3. root.grid_rowconfigure(0, weight=1) and root.grid_columnconfigure(0, weight=1): These lines are crucial for making the layout responsive. They tell Tkinter to allocate extra space to row 0 (where the chat history is) and column 0 (where the entry field is) when the window is resized.