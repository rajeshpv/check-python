import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    num1 = mo.ui.text(label="Number 1: ", value="10")
    num2 = mo.ui.text(label="Number 2: ", value="2")
    calc = mo.ui.run_button(label="Calc")
    # result = mo.ui.text(value=vresult, label="Result",    disabled=True) # use this line for method-C
    result = mo.ui.text(value="", label="Result",    disabled=True) # use this line for method-A and B

    mo.hstack([num1, num2, calc, result],justify="start")

    return calc, mo, num1, num2


@app.cell
def _(num1, num2):
    def do_calc() -> str:
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            _vresult = str(n1 / n2)
            # print(_vresult)
        except Exception:
            _vresult = "Invalid input"
        return _vresult
    return (do_calc,)


@app.cell
def _():
    ## This worked - method-A
    # vresult = ""

    # if calc.value:
    #     vresult = do_calc()

    # mo.ui.text(value=vresult, label="Result",    disabled=True)

    return


@app.cell
def _(calc, do_calc, mo):
    # This also worked worked - method-B
    vresult = do_calc() if calc.value else ""

    mo.ui.text(value=vresult, label="Result",    disabled=True)

    return


@app.cell
def _():
    # this DOE NOT work- method-C
    # vresult = do_calc() if calc.value else ""

    return


if __name__ == "__main__":
    app.run()
