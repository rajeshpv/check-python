import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from pylib import fns

    get_err_msg, set_err_msg = mo.state(None)
    return fns, mo, set_err_msg


@app.cell
def _(mo, set_err_msg):
    # common functions
    from functools import wraps
    from typing import Any, Callable, Tuple

    def capture_exception(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Tuple[Any | None, Exception | None]:
            try:
                return func(*args, **kwargs), None
            except Exception as e:
                return None, mo.callout(str(e), kind="danger")
        return wrapper

    def common_exception_handler(exc, func, args, kwargs):
        _emsg = f"Error in function: {func.__name__} Exception: {exc}"
        # print(_emsg)
        set_err_msg(_emsg)
        return None

    def handle_error(default=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # set_err_msg(None)
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    common_exception_handler(e, func, args, kwargs)
                    return default
            return wrapper
        return decorator

    return (capture_exception,)


@app.cell
def _(capture_exception, fns, num1, num2):
    # logic functions
    @capture_exception
    def calc_wrap() -> str:
      a = float(num1.value)
      b = float(num2.value)  
      return  str(fns.divide(a,b))
    return (calc_wrap,)


@app.cell
def _(mo):
    num1 = mo.ui.text(label="Number 1: ", value="")
    num2 = mo.ui.text(label="Number 2: ", value="")
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


if __name__ == "__main__":
    app.run()
