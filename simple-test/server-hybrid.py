from flask import Flask, request
from opentelemetry import trace, metrics

tracer = trace.get_tracer("simplecalc.tracer")
meter = metrics.get_meter("simplecalc.meter")
output_counter = meter.create_counter("simplecalc.output", description="The number of times an output has been calculated")

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<html><body><h1>Simple Instrumented Calculator</h1><p><a href='/calc'>Start calculator</a></p></body></html>" 
    
@app.route("/calc", methods=["POST","GET"])
def calculator_page():
    number = 0
    to_add = 0
    new_value = 0
    with tracer.start_as_current_span("calc") as calcspan:
        if request.method == "POST":
            calcspan.set_attribute("calc.initial_value", request.form['start_value'])
            calcspan.set_attribute("calc.add_value", request.form['add_value'])
            number = int(request.form['start_value'])
            to_add = int(request.form['add_value'])
            new_value = number + to_add
            calcspan.set_attribute("calc.output", new_value)
            output_counter.add(1, {"calc.output": new_value})
    return f"<html><body><h1>Simple Instrumented Calculator</h1><form action='/calc' method='post'><input type='text' name='start_value' value='{new_value}' readonly /><br/><h4>+</h4><br/><input type='text' name='add_value'/><br/><input type='submit' value='Add Number'/></form></body></html>"
