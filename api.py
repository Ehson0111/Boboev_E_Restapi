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
   users={
        1: {
          "name":"Alex_",
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
   user_id = int(id)
   user = users.get(user_id)
   return jsonify(user)
        
  
if __name__ == "__main__": 
    app.run(debug=True)
