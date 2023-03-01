"""
    @author: Spycsh
"""

# Here you can create the test suite, call the unit test
# generate the test report, and also send the result to email
import unittest
from TestRunner import HTMLTestRunner
from TestRunner import SMTP
from test import TestDemo, TestDemo2
from flask import Flask,render_template, request, url_for, redirect, session

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')

# if __name__ == "__main__":
#   app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestDemo("test_success"))
    suit.addTest(TestDemo("test_skip"))
    suit.addTest(TestDemo("test_fail"))
    suit.addTest(TestDemo("test_error"))
    suit.addTest(TestDemo2("test_insert_sort"))
    suit.addTest(TestDemo2("test_insert_sort_wrong"))

    report = "./result.html"
    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Unit Test report',
            description='unit test'
        )
        runner.run(suit)
    app.run(debug=True, host='0.0.0.0', port=5000)
    # use gmail to provide email sending service
    # smtp = SMTP(user="sender@gmail.com", password="", host="smtp.gmail.com")
    # fill in the receiver email here
    # smtp.sender(to="sihanc@kth.se", attachments=report)