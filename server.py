from flask import Flask
app = Flask(__name__)
 
@app.route("/", methods=["GET"])
def root():
   return "<h1>welcome to ITIL exam</h1>"
 
@app.route("/modules", methods=["GET"])
def root1():
   return "<h1>COSA <br> NDC <br> PKI <br> Security Concept <br> ITIM Devops     <br> Complience Audit </h1>"
 
@app.route("/me", methods=["GET"])
def root2():
   return "<h1>PRN: 230344223017 <br>Name: Diksha Sahu <br>Phone number: +91 7    389865615 </h1>"
 
app.run(host="0.0.0.0",port=4000, debug=True)
      

