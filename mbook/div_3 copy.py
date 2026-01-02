import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from pylib import fns

    get_err_msg, set_err_msg = mo.state(None)
    return get_err_msg, mo, set_err_msg


@app.cell
def _(get_err_msg, mo, set_err_msg):
    # common functions
    from functools import wraps

    def common_exception_handler(exc, func, args, kwargs):
        _emsg = f"Error in function: {func.__name__} Exception: {exc}"
        print(_emsg)
        set_err_msg(_emsg)
        return None

    def handle_error(default=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    common_exception_handler(e, func, args, kwargs)
                    return default
            return wrapper
        return decorator

    has_err_msg = get_err_msg()
    if has_err_msg:
      out = mo.callout(has_err_msg, kind="danger")
      set_err_msg(None)
      mo.stop(has_err_msg, out)
    return (handle_error,)


@app.cell
def _(handle_error, set_err_msg):
    # logic functions
    @handle_error(default=0)
    def calc_wrap(a,b) -> float:
      return  a/b

    def calc_direct(a,b) -> float:
      _v = 0
      try:
        _v = a/b
      except Exception as e:
        _emsg = f"Error is: {e}"
        set_err_msg(_emsg)
        print(_emsg)

      return _v
    return (calc_wrap,)


@app.cell
def _(calc_wrap, mo):
    n1 = 10
    n2 = 2

    # _v = calc_direct(n1,n2)
    _v = calc_wrap(n1,n2)
    mo.ui.text(label=f"{n1}/{n2}", value=f"{_v}")
    return n1, n2


@app.cell
def _(mo, n1, n2):

    mo.ui.text(label=f"{n1}/{n2}=")
    return


if __name__ == "__main__":
    app.run()
