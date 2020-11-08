from flask import Flask, request,render_template

app=Flask(__name__)

@app.route("/")

def introduce():
    from .data.about import bot  #controller
    return render_template('index.html',data=bot,question={'key':'name','text':"May i know your name?"})


@app.route("/message",methods=['POST'])

def user_message():
    if request.method == 'POST':
        from  .intents import handle
        return handle(request.form)
    else:
        return "INVALID"


if __name__=='__main__':
    app.run(threaded=True,port=5000)