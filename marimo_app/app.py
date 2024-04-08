import marimo

__generated_with = "0.3.9"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md("# My app")
    return


@app.cell
def __(mo):
    n = mo.ui.number(0, 100, label="A number")
    n
    return n,


@app.cell
def __(n):
    result = n.value * 2
    result
    return result,


if __name__ == "__main__":
    app.run()
