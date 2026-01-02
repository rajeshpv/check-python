import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from pylib import fns

    num1 = mo.ui.text(label="Number 1: ", value="10")
    num2 = mo.ui.text(label="Number 2: ", value="2")
    calc_btn = mo.ui.run_button(label="÷")

    mo.hstack([num1, num2, calc_btn],justify="start")
    return calc_btn, fns, mo, num1, num2


@app.cell
def _(calc_btn, fns, mo, num1, num2):
    result = ""

    if calc_btn.value:
        try:
            a = float(num1.value)
            b = float(num2.value)
            result = str(fns.divide(a,b))
        except Exception as e:
            result = f"Error: {e}"

    mo.ui.text(label="Result", value=result, disabled=True)
    return


if __name__ == "__main__":
    app.run()
