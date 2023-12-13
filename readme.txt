setup virtual env:  py -m venv venv 
activate: enter path to Scripts within venv > .\venv\Scripts\activate
turn off: deactivate
ensure pip is updated: py -m pip install --upgrade pip       
install flask to virt env: py -m pip install flask    
run server: python -m flask --app .\controller.py run
port: http://localhost:5000/


---- setup index.html ----
1. in py class import render_template
2. add template folder inside project render_template will look here for name of html
2. add index html page -- html, body, h1 so on
3. in controller replace return with render_template('index.html')