from flask import Flask, request,jsonify
app = Flask(__name__) 

@app.route('/hello_world', methods=['GET']) 
def sayHelloword(): 
    data = { 
    1: "Hello World" 
        } 
    return jsonify(data)
@app.route('/users', methods=['GET']) 
def returnUserinfo():
    id=request.args.get("id")
    
    pass
users={
        1: {
          "name":"Alex",
          "age":25   
        },

        2: {
          "name":"Max",
          "age":28   
        },
        
        3: {
          "name":"Egor",
          "age":15   
        },


    }

if __name__ == "__main__": 
    app.run(debug=True)
