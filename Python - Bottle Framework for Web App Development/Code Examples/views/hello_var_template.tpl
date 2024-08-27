<h1>Hello {{ name }}</h1>

%if name == 'bob':
    <h1>{{ name }} is awesome!!!</h1>
%else:
    <h1>{{ name }} is not as cool as Bob!</h1>
%end