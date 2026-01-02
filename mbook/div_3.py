import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from pylib import fns

    get_err_msg, set_err_msg = mo.state(None)
    return fns, get_err_msg, mo, set_err_msg


@app.cell
def _(get_err_msg, mo, set_err_msg):
    # common functions
    from functools import wraps

    def common_exception_handler(exc, func, args, kwargs):
        _emsg = f"Error in function: {func.__name__} Exception: {exc}"
        # print(_emsg)
        set_err_msg(_emsg)
        return None

    def handle_error(default=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                set_err_msg(None)
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    common_exception_handler(e, func, args, kwargs)
                    return default
            return wrapper
        return decorator

    # display error msg and stop further execution
    has_err_msg = get_err_msg()
    if has_err_msg:
      out = mo.callout(has_err_msg, kind="danger")
      set_err_msg(None)
      mo.stop(has_err_msg, out)
    return (handle_error,)


@app.cell
def _(fns, handle_error, mo):
    num1 = mo.ui.text(label="Number 1: ", value="10")
    num2 = mo.ui.text(label="Number 2: ", value="2")
    calc_btn = mo.ui.run_button(label="÷")

    # logic functions
    @handle_error(default="0")
    def calc_wrap() -> float:
      a = float(num1.value)
      b = float(num2.value)  
      return  str(fns.divide(a,b))

    mo.hstack([num1, num2, calc_btn],justify="start")  
    return calc_btn, calc_wrap


@app.cell
def _(calc_btn, calc_wrap, mo):
    result = calc_wrap() if calc_btn.value else ""

    mo.ui.text(label="Result", value=result, disabled=True).style({"width":"800px"})
    return


if __name__ == "__main__":
    app.run()
