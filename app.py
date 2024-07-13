from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize an empty list to store rental data
rental_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        car_brand = request.form.get('carBrand')
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')
        customer_name = request.form.get('customerName')
        customer_id = request.form.get('customerId')

        # Create a dictionary for the submitted data
        rental_entry = {
            'Car Brand': car_brand,
            'Start Date': start_date,
            'End Date': end_date,
            'Customer Name': customer_name,
            'Customer ID': customer_id
        }

        # Append the dictionary to the rental_data list
        rental_data.append(rental_entry)

    return render_template('index.html', rental_data=rental_data)

if __name__ == '__main__':
    app.run(debug=True)