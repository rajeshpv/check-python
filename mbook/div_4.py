import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full", app_title="Div 4 Test")


@app.cell
def _():
    import marimo as mo
    from pylib import fns
    return fns, mo


@app.cell
def _(mo):
    # common functions
    from functools import wraps
    from typing import Any, Callable, Tuple

    def red_box(text: str, title: str = "Exception"):
        return mo.md(f"""
    <div style="
      width: 100%;text-align:left;
      border: 1px solid #ef4444;
      color: #ef4444;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 13px;
      line-height: 1.2;
      margin: 4px 0;
    ">
      <b>{title}:</b> {text}
    </div>
    """)

    def _build_callout(msg:str, kind="danger"):
        return red_box(msg)

    def capture_error(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Tuple[Any | None, Exception | None]:
            try:
                return func(*args, **kwargs), None
            except Exception as e:
                return None, _build_callout(str(e))
        return wrapper
    return (capture_error,)


@app.cell
def _(capture_error, fns, num1, num2):
    # logic functions
    @capture_error
    def calc_wrap() -> str:
      a = float(num1.value)
      b = float(num2.value)  
      return  str(fns.divide(a,b))
    return (calc_wrap,)


@app.cell
def _(mo):
    num1 = mo.ui.text(label="Number 1: ", value="10")
    num2 = mo.ui.text(label="Number 2: ", value="2")
    calc_btn = mo.ui.run_button(label="÷")

    mo.hstack([num1, num2, calc_btn],justify="start")  
    return calc_btn, num1, num2


@app.cell
def _(calc_btn, calc_wrap, mo):
    out = None
    if calc_btn.value:
      result, error = calc_wrap()
      out = error if error else  mo.ui.text(label="Result", value=result, disabled=True).style({"width":"800px"})
    out
    return


@app.cell
def _(mo):
    mo.ui.text(label="tesxt")
    return


if __name__ == "__main__":
    app.run()
