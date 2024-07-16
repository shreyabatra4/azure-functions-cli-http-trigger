import azure.functions as func
import logging
import time

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")
def main(req):
    user = req.params.get("user")
    return f"Hello, {user}!"

# @app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="%ServiceBusQueueName%",
#                                connection="ServiceBusConnection") 
# def servicebus_queue_trigger(azservicebus: func.ServiceBusMessage):
#     logging.info('Python ServiceBus Queue trigger start processing a message: %s',
#                 azservicebus.get_body().decode('utf-8'))
#     time.sleep(30)
#     logging.info('Python ServiceBus Queue trigger end processing a message')