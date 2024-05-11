from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()


@app.post("/")
async def handle_request(request: Request, track_order=None, order_status=None, order_id=None):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context : ongoing-tracking":
        track_order(parameters)

        def track_order(parameters: dict):
            order_id = parameters['order_id']
            order_status = db_helper.get_order_status(order_id)

        if order_status:
            fulfillment_text = f"the order status for order id:{order_id}is : {order_status}"
        else:
            fulfillment_text = f"No order status for order id:{order_id}"

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

