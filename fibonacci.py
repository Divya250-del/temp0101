

from flask import *
app=Flask(__name__)


@app.route('/hdfl/<n>')
def hello(n):
    num=list(n)
    
     
    arr = list(map(int, num))
    evens=[]
    odds=[]
    for i in arr:
        if(i%2==0):
            evens.append(i)
        else:
            odds.append(i)

    result={
        "number":arr,
        "is_success": True,
        "user_id": "divya_jain_0832IT191012",
        "odd": odds,
        "even": evens


    }
    return result

if __name__== "__main__":
    app.run(debug=True)
