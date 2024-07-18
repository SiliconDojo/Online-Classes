header = "Hello World!!!"

column1 = "This is a really cool site!"

column2 = "We hope you think this site is really cool too!"

column3 = "Please tell us how cool you think we are!"

footer = "You can contact us at bob@reallycoolsite.com"

style = '''
            <style>
                div {
                    display: flex;
                    justify-content: center;
                }
                div.header {
                    background-color: orange;
                    font-size: 100px;
                    text-align: center;
                    display:block;
                }
                div.column {
                    height: auto;
                    width: 200px;
                    display: inline-block;
                }
                div.footer {
                    background-color: orange;
                    font-size: 25px;
                    text-align: center;
                    display:block;
                }
            </style>            
        '''

with open('site.html', 'w') as file:
    file.write(f''' 
                    {style}
                    <div class="header">{header}</div>
                    <div>
                        <div class="column">{column1}</div>
                        <div class="column">{column2}</div>
                        <div class="column">{column2}</div>
                    </div>
                    <div class="footer">{footer}</div>
                ''')