from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField

from wtforms.validators import (
    InputRequired,
    AnyOf,
    NumberRange,
)

colors = ["red", "green", "orange", "blue"]


class LuckyNumForm(FlaskForm):
    """Form to validate get-lucky-num api call"""

    name = StringField(
        "Name", validators=[InputRequired(message=("This field is required"))]
    )
    year = IntegerField(
        "Birth Year",
        validators=[
            InputRequired(message=("This field is required")),
            NumberRange(
                min=1920,
                max=2000,
                message=("You must enter a year between 1920 and 2000"),
            ),
        ],
    )
    email = StringField(
        "Email", validators=[InputRequired(message=("This field is required"))]
    )
    color = StringField(
        "Color",
        validators=[
            InputRequired(message=("This field is required")),
            AnyOf(
                values=colors,
                message=(f"Must be one of: {", ".join(colors)}"),
            ),
        ],
    )
