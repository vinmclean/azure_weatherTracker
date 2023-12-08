import json
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    if req_body and 'city' in req_body and 'temperature' in req_body:
        city = req_body['city']
        temperature = req_body['temperature']

        # Perform actions based on the received data
        if float(temperature) < 50.0:
            # Handle the case where the temperature is greater than 50°F
            logging.info('My app logs here.Temp < 50. Its cold, we are not going outside to play')
            return func.HttpResponse(f'Temperature in {city} is {temperature}°F. Action taken.', status_code=200)
        else:
            # Handle the case where the temperature is not greater than 50°F
            logging.info('My app logs here.Temp > 50. Let us all go outside and play.')
            return func.HttpResponse(f'Temperature in {city} is {temperature}°F. No action taken.', status_code=200)
    else:
        return func.HttpResponse("Invalid request body", status_code=400)
