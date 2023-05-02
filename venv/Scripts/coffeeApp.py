from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name' # replace with your own database configuration
db = SQLAlchemy(app)

class Matrix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matrix = db.Column(db.String(1000))

def espresso_counter(n, m):
    matrix = []
    for i in range(2 ** n):
        binary = bin(i)[2:].zfill(n)
        ones = binary.count("1")
        if ones == m:
            matrix.append(binary)
    return matrix

def swap_rows(matrix, row1, row2):
    if row1 < 0 or row1 >= len(matrix) or row2 < 0 or row2 >= len(matrix):
        raise ValueError("Invalid row indices.")
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
            matrix_str = "\n".join(matrix)
            matrix_entry = Matrix(matrix=matrix_str)
            db.session.add(matrix_entry)
            db.session.commit()
            return render_template("index.html", matrix=matrix)
        except (ValueError, IndexError):
            error_message = "Invalid input. Please enter integers for n, m, row1, and row2, and ensure that row1 and row2 are valid row indices for the matrix."
            return render_template("input.html", error_message=error_message)
    else:
        matrices = Matrix.query.all()
        return render_template("input.html", matrices=matrices)

if __name__ == "__main__":
    app.debug = True
    app.run()
