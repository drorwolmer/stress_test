from app import app
import api

# =======================================================================
# Direct running for flask dev server
# =======================================================================
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.debug = True
    app.config['TESTING'] = True
    app.testing = True

    app.run(debug=True, host='0.0.0.0', port=1234, threaded=True)
