from flask import Flask
from flask import render_template, request
import xlrd
app = Flask(__name__)


@app.route("/ntu")
def ntu():
    return render_template("ntu.html")


@app.route("/ntu/<departmentCode>")
def department(departmentCode):
    workbook = xlrd.open_workbook_xls("dpt_code.xls")
    worksheet = workbook[0]
    info = f"{departmentCode} 沒有這個科系"
    # TODO change info
    return render_template("department.html", info=info)


if __name__ == "__main__":
    app.run(debug=True)
