from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange


class ProbabilityForm(FlaskForm):
    """
    Form for calculate probability
    """

    year_days = IntegerField(
        "Days count", validators=[NumberRange(min=0, max=365)]
    )
    peoples_count = IntegerField(
        "Peoples count", validators=[NumberRange(min=0)]
    )
    days_range = IntegerField(
        "Days range", validators=[NumberRange(min=0, max=365)]
    )
    submit = SubmitField("Submit")
