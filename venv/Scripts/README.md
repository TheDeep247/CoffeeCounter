# CoffeeCounter
This is a Flask web application that defines a few functions and routes to create an "Espresso Counter" application.

The espresso_counter(n, m) function generates a matrix containing all binary strings of length n that have m ones. The swap_rows(matrix, row1, row2) function takes in a matrix and two row indices and swaps the two rows in the matrix.

The @app.route("/", methods=["GET", "POST"]) decorator defines the main route for the application. If the HTTP method is a POST request, the application tries to retrieve the input values from the submitted form, converts the values to integers, calls espresso_counter(n, m) to generate a matrix, swaps the rows specified by the user, and renders the template index.html with the generated matrix. If an error occurs, the application renders the template input.html with an error message.

If the HTTP method is a GET request, the application simply renders the template input.html with the form for the user to enter their inputs.

Finally, the if __name__ == "__main__" block runs the application in debug mode.