## Checkout and inti uv project
```bash
git clone https://github.com/rajeshpv/check-python.git
cd check-python
uv venv .venv
source .venv/bin/activate
uv sync
```

## Run marimo notebook
```bash
uv run marimo run mbook/div_1.py
uv run marimo run mbook/div_2.py
uv run marimo run mbook/div_3.py
```

## Question.1
* I need a common place where I could capture error from any function I annotate for
* And render a "callout" to display the error message and stop further execution.
* And I agree, if I stop, the execution, we need to rerun from start.
### Solution
* div_1.py shows basic way of handling error
* And div_3.py shows function-wrap as well as usign mo.state to capture error message and display it in a callout.
## Help needed
* If anyone has a better way to handle error, please share.
* And is above method correct? or fragile? :) 

## Question.2
* On Seperate note:, I wanted to render result in same cell liek num1 and num2 are rendered.
* Which I tried in div_2.py
* And I think, it is not possible at all, unless I use mo.state and on_change liek marimo.io docs show exampel of "todo tasks"