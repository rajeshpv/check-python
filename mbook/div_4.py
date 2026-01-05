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

      box-shadow:
        2px 2px 0 rgba(162, 37, 37, 0.35),
        6px 6px 14px rgba(0, 0, 0, 0.45);
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
      out = error if error else  mo.ui.text(label="Result", value=result, disabled=True)
    out
    return


@app.cell
def _(mo):
    # mo.ui.array(
    #   # [mo.ui.text(label=f"asdfasf asf {fb}").callout(kind=fb)  for fb in ["neutral", "danger", "warn", "success", "info"]]
    #   [mo.md(f"asdfasf asf {fb}").callout(kind=fb)  for fb in ["neutral", "danger", "warn", "success", "info"]]
    # )
    from dateutil import parser
    from datetime import datetime, timezone

    def string_to_epoch(dt_string: str) -> int:
      dt_value = parser.parse(dt_string)
      # dt_value = dt_value.replace(tzinfo=timezone.utc)
      epoch = int(dt_value.timestamp())
      return epoch

    def epoch_to_iso8601(epoch: int) -> str:
        epoch = float(epoch)

        # detect milliseconds
        if epoch > 1e11:
            epoch /= 1000.0

        return datetime.fromtimestamp(epoch).isoformat().replace("+00:00", "Z")

    text_date = mo.ui.text(label=f"parse dt to epoch:", value="11/14/24 10:06")
    text_epoch = mo.ui.text(label=f"parse epoch to date:", value="1731596760")
    mo.hstack([text_date,text_epoch], justify="start")
    return epoch_to_iso8601, string_to_epoch, text_date, text_epoch


@app.cell
def _(epoch_to_iso8601, string_to_epoch, text_date, text_epoch):
    if text_date.value:
      # dt_value = parser.parse(text_date.value) 
      # dt = dt_value.replace(tzinfo=timezone.utc)
      # epoch = int(dt.timestamp())
      # print(dt_value, epoch)
      epoch = string_to_epoch(text_date.value)
      print(epoch)

    if text_epoch.value:
      dt_str = epoch_to_iso8601(int(text_epoch.value))
      print(dt_str)    
      # 11/15/24 2:32:08.340 11/17/24 20:41:26.017
      # 1731637920  1731876060

      # 11/14/2024 1731542400 15=1731628800
    # EST 1731560400 1731646800 this worked

    #   1731470168285   11/12/24 22:56:08.285
    # 1731483734293   11/13/24 2:42:14.293
    # 1731499358340   11/13/24 7:02:38.340
    # 1731516356377   11/13/24 11:45:56.377
    # 1731530144325   11/13/24 15:35:44.325
    # 1731543404257   11/13/24 19:16:44.257
    # 1731558680268   11/13/24 23:31:20.268
    # 1731573104313   11/14/24 3:31:44.313
    # 1731582950360   11/14/24 6:15:50.360
    # 1731596762419   11/14/24 10:06:02.419 2024
    return


@app.cell
def _(string_to_epoch):
    import re

    def parse_date(value):
      s = value.removeprefix("@")
      return  str(string_to_epoch(s))

    input_str = "soemthing -k @11/14/24 -j @11/15/24 end"
    K_REGEX = r"(-k\s+)(\S+)"
    J_REGEX = r"(-j\s+)(\S+)"

    def apply_date_regex(THE_REGEX, in_str) -> str:
      new_str = in_str

      m = re.search(THE_REGEX, in_str)
      if m and m.group(2).startswith("@"):
          new_str = re.sub(THE_REGEX, lambda m: m.group(1) + parse_date(m.group(2)), in_str)
      return new_str

    print(apply_date_regex(K_REGEX, input_str))
    print(apply_date_regex(J_REGEX, input_str))
    print(apply_date_regex(J_REGEX, apply_date_regex(K_REGEX, input_str)))


    return


if __name__ == "__main__":
    app.run()
