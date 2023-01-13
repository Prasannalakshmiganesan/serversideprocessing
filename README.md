# Design a Website for Server Side Processing

## AIM:
To design a website to perform mathematical calculations in server side.

## DESIGN STEPS:

### Step 1:

First clone the repository in open theia ide terminal.

### Step 2:

Write the program using html and css for the calculations to be displayed in the server side.

### Step 3:

make the allowed hosts '*' in setting.py in order to run our webserver.

### Step 4:

add codes to urls.py, views.py to run the code into the server.

### Step 5:

Now give python3 manage.py runserver 0:8000 to make the server run.

### Step 6:

Publish the website in the given URL.

## PROGRAM :
```

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>AREA OF RECTANGLE</title>
        <style>
        form {
  width: 500px;
  margin: 0 auto;
  background-color: #8ea4d4 ;
  border: 1px solid rgb(122, 179, 202);
  border-radius: 5px;
  padding: 20px;
}

label {
  display: block;
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

input[type="text"],
input[type="number"] {
  width: 100%;
  padding: 12px 20px;
  margin-bottom: 20px;
  box-sizing: border-box;
  border: 1px solid rgb(32, 31, 31);
  border-radius: 4px;
  resize: vertical;
}

input[type="submit"] {
  background-color: #4CAF50;
  color: rgba(22, 18, 18, 0.788);
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type="submit"]:hover {
  background-color: #e261d1;
}

.container {
  border-radius: 5px;
  background-color: #b25eeb;
  padding: 20px;
}

.area {
  margin-bottom: 20px;
  color: purple;
  font-size: 20px;
  font-weight: bold;
}
h1 {
  text-align: center;
  font-size: 24px;
  color: rgb(104, 207, 176);
}

</style>
    </head>
            <body>
                  <h1>AREA OF A RECTANGLE</h1>
                  <form method="POST" action='/area/'>
                      {%csrf_token%}
		<label for="length">Enter Length</label>
        <input type="text" name="length" id="length" value="{{ length }}"/> <br>			
        <label for="width">Enter Width</label>
        <input type="width" name="width" id="width" value="{{ width }}"/><br>
        <input type="submit" value="Calculate area"/></br>
        
        <label for="area">Area:</label>
        <input type="area" name="area" id="area" value="{{ area }}"/></br>
	</form>
            </body>
    
</html>

```

## OUTPUT:
![output1](https://user-images.githubusercontent.com/118610231/212326192-5c8aefd0-2446-46b0-9719-a525a6e785e4.png)


### HOMEPAGE :
![output2](https://user-images.githubusercontent.com/118610231/212326099-cbe03a0b-8221-4f41-9fda-47298702ca67.png)




## Result:
Thus the program to design and display a website to perform mathematical calculations in server side is done.

