from typing import TypeVar

from flask import flash, redirect, render_template, url_for
from werkzeug.wrappers import Response

from app import app
from app.forms import ProbabilityForm
from app.probability import probability


_RC = TypeVar("_RC", bound=Response)


@app.route("/probability", methods=["GET", "POST"])
def probability_calculate() -> _RC:
    """
    Calculate probability for birthday
    """
    form = ProbabilityForm(year_days=365, peoples_count=8, days_range=7)
    if form.validate_on_submit():
        calculated = probability(
            form.year_days.data, form.peoples_count.data, form.days_range.data
        )
        flash(
            f"Probability for {form.year_days.data} days, {form.peoples_count.data} "
            f"peoples and {form.days_range.data} days range is {calculated}%"
        )
        return redirect(url_for("probability_calculate"))
    return render_template("probability.html", form=form)
