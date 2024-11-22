from bottle import run, route, post, request
import html

@route('/')
def index():
    page = '''
            <h1>Hello</h1>

            <form action="process" method="post" id="form">
                Name: <input type="text" name="name" id="name" required><br><br>
                Age: <input type="number" name="age" id="age" required><br><br>
                Email: <input type="email" name="email" id="email" required><br><br>
                <input type="submit" value="Submit" onclick="validate(event)">
            </form>

            <script>
                function validate(event) {
                    event.preventDefault();

                    const name = document.getElementById("name");
                    const age = document.getElementById("age");
                    const email = document.getElementById("email");

                let message = "";

                if (!name.validity.valid) {
                    message += "Name is not valid\\n";
                }

                if (!age.validity.valid) {
                    message += "Age is not valid\\n";
                }

                if (!email.validity.valid) {
                    message += "Email is not valid\\n";
                }

                if (message) {
                    alert(message);
                } else {
                    document.getElementById("form").submit();                }
            }
            </script>
            '''
    return page

@post('/process')
def process():
    name = request.forms.get('name')
    age = request.forms.get('age')
    email = request.forms.get('email')
    
    #name = html.escape(name)

    page = f'''
            <h1>Name: {name}</h1>
            <h1>Age: {age}</h1>
            <h1>Email: {email}</h1>
            '''
    return page

run(host='0.0.0.0', port='8080')
