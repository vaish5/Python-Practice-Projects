from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', [DataRequired(), Length(min=5)])
    cafe_location_url = URLField('Cafe Location on Google Maps (URL)',
                                 [DataRequired(), URL()])
    cafe_opening_time = StringField('Opening Time e.g. 8AM',
                                    [DataRequired()])
    cafe_closing_time = StringField('Closing Time e.g. 5:30PM',
                                    [DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                [DataRequired()],
                                choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),
                                         ('☕️☕️☕️', '☕️☕️☕️'),
                                         ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                         ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')],
                                render_kw={'style': 'width: 20ch'},)
    wifi_strength_rating = SelectField('Wifi Strength Rating',
                                [DataRequired()],
                                choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'),
                                         ('💪💪💪', '💪️💪️💪'),
                                         ('💪💪💪️💪️', '💪💪💪💪️'),
                                         ('💪💪💪💪💪️', '💪💪💪💪💪')],
                                render_kw={'style': 'width: 20ch'}, )
    power_socket_availability = SelectField('Power Socket Availability',
                                       [DataRequired()],
                                       choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'),
                                                ('🔌🔌🔌', '🔌🔌🔌'),
                                                ('🔌🔌🔌🔌️', '🔌🔌🔌🔌️'),
                                                ('🔌🔌🔌🔌🔌️', '🔌🔌🔌🔌🔌')],
                                       render_kw={'style': 'width: 20ch'}, )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([form.cafe.data, form.cafe_location_url.data,
                               form.cafe_opening_time.data,
                               form.cafe_closing_time.data,
                               form.coffee_rating.data,
                               form.wifi_strength_rating.data,
                               form.power_socket_availability.data])
            return redirect(url_for("cafes"))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            for items in list_of_rows:
                cafes_data_length = len(items)

    return render_template('cafes.html', cafes=list_of_rows,
                           cafes_length=cafes_data_length,
                           )


if __name__ == '__main__':
    app.run(debug=True)
