
import cgi
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from r2l2_commands import R2L2Commands
#from dummy_commands import R2L2Commands

commands = R2L2Commands()

class RequestHandler(BaseHTTPRequestHandler):
    def input_form_html(self):
        return(
            '<h1>R2L2</h1>' +
            '<pre>' + commands.help() + '</pre>' +
            '<form method="post"><tt>' +
            'Enter command: <input name="command">' +
            '<input type="Submit"></tt></form>')

    def send_html_content(self, *content):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("\n".join(content))

    def do_GET(self):
        self.send_html_content(self.input_form_html())

    def do_POST(self):
        # we have to do this manually here ourselves..? wtf python
        post_data = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
            environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']})

        if 'command' in post_data:
            user_input = post_data['command'].value
            self.log_message("R2L2 user input: %s", user_input)

            command_response = commands.do_command(user_input)
            self.log_message("R2L2 response: %s", command_response)

            self.send_html_content(self.input_form_html(), '<tt>' + command_response + '</tt>')

        else:
            self.send_html_content(self.input_form_html())

try:
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever();
finally:
    commands.cleanup()
