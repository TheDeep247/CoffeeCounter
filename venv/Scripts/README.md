# CoffeeCounter
This Flask application defines a route ("/") with a GET method that renders the "input.html" template, and a POST method that calls the "espresso_counter" and "swap_rows" functions based on user input from a form in the "input.html" template, and then renders the "index.html" template with the updated matrix.

The "espresso_counter" function generates all possible binary numbers of length "n" and counts the number of ones in each binary number. It returns a list of binary numbers that have "m" ones.

The "swap_rows" function takes a matrix (list of binary numbers) and two row indices to swap in place.

The GET method in the "/" route renders the "input.html" template, which contains a form with inputs for "n", "m", "row1", and "row2", as well as a submit button. When the form is submitted, the POST method in the "/" route is called. This method extracts the values of "n", "m", "row1", and "row2" from the form, calls the "espresso_counter" function to generate the matrix, calls the "swap_rows" function to swap the specified rows, and then renders the "index.html" template with the updated matrix.