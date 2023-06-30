from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email, length


# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField(
        "First name",
        validators=[InputRequired(), length(2, 64, "Please input a valid name")],
    )
    surname = StringField(
        "Surname",
        validators=[InputRequired(), length(1, 64, "Please input a valid surname")],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            email(),
            length(4, 128, "Please input a valid email"),
        ],
    )
    address = StringField(
        "Address",
        validators=[InputRequired(), length(3, 50, "Please input a valid address")],
    )
    state = StringField(
        "State/Territory", validators=[InputRequired(), length(2, 3, "Invalid state")]
    )
    postcode = StringField(
        "Postcode",
        validators=[InputRequired(), length(3, 4, "Invalid Postcode")],
    )
    submit = SubmitField("Finish Order")
