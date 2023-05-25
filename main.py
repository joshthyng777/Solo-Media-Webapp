from website import create_app



app = create_app()


# trying to define the api route for axios on the front end but am not sure how just yet
# Was thinking of creating a different file for it called routes.py
@app.route('/api/data', methods=['GET'])
def get_data():
         # Handle the GET request and return the response
        data = {
            'message': 'Hello from the backend!',
            'data': [1, 2, 3, 4, 5]
        }
        return jsonify(data)

@app.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    return {'csrf_token': csrf_token}

# Other routes and endpoints in your Flask application


if __name__ == '__main__':
    app.run(debug=True)

    
