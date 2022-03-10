from application import app 

application_host = "cook-book-app_application:latest"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
