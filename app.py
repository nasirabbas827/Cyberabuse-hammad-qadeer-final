from flask import Flask, request, render_template
import joblib
import string

# Initialize Flask app
app = Flask(__name__)

# Load the models and vectorizer
nb_model = joblib.load('models/naive_bayes_model.pkl')
svm_model = joblib.load('models/svm_model.pkl')
dt_model = joblib.load('models/decision_tree_model.pkl')
vectorizer_ngram = joblib.load('models/vectorizer_ngram.pkl')  # Updated to match your trained vectorizer

# Define a function for prediction
def predict_comment(comment):
    # Preprocess the comment
    comment = comment.lower()
    comment = ''.join([char for char in comment if char not in string.punctuation])

    # Vectorize the comment using the same vectorizer used during training
    comment_vectorized = vectorizer_ngram.transform([comment])

    # Predict with each model
    nb_pred = nb_model.predict(comment_vectorized)[0]
    svm_pred = svm_model.predict(comment_vectorized)[0]
    dt_pred = dt_model.predict(comment_vectorized)[0]

    return nb_pred, svm_pred, dt_pred

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    comment = ""
    if request.method == 'POST':
        comment = request.form['comment']
        nb_pred, svm_pred, dt_pred = predict_comment(comment)

        # Convert predictions to readable format
        result = {
            'Naive Bayes': 'Abusive' if nb_pred == 'A' else 'Non-Abusive',
            'SVM': 'Abusive' if svm_pred == 'A' else 'Non-Abusive',
            'Decision Tree': 'Abusive' if dt_pred == 'A' else 'Non-Abusive'
        }

    return render_template('index.html', result=result, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
