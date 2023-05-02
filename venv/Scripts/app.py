from flask import Flask, render_template, request

app = Flask(__name__)

def espresso_counter(n, m):
    matrix = []
    for i in range(2 ** n):
        binary = bin(i)[2:].zfill(n)
        ones = binary.count("1")
        if ones == m:
            matrix.append(binary)
    return matrix

def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        try:
            n = int(request.form["n"])
            m = int(request.form["m"])
            matrix = espresso_counter(n, m)
            row1 = int(request.form["row1"])
            row2 = int(request.form["row2"])
            swap_rows(matrix, row1, row2)
            return render_template("index.html", matrix=matrix)
        except (ValueError, IndexError):
            error_message = "Invalid input. Please enter integers for n, m, row1, and row2, and ensure that row1 and row2 are valid row indices for the matrix."
            return render_template("input.html", error_message=error_message)
    else:
        return render_template("input.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
