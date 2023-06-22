import json
import logging
import configparser
import csv
from locust import HttpUser, task , events
from tests.requests.check_flights import check_flight_request

logger = logging.getLogger()
config = configparser.ConfigParser()
config.read("tests/configs/api.properties")

class HitCheckFlightAPI(HttpUser):
    testdata=[]
    with open("tests/data/city.csv", mode="r", encoding="utf-8-sig") as f:
        dataObj = csv.DictReader(f)
        testdata = list(dataObj)
        
    @events.init_command_line_parser.add_listener
    def init_parser(parser):
        parser.add_argument("--env", type=str, default= "qa")
        
    
    @events.test_start.add_listener
    def _(environment, **kwargs):
        logger.info("Targeted Env : %s" % environment.parsed_options.env)
        environment.host = config.get("host","qa")
        logger.info("********** Beginning Locust Load Testing **********" )
        
    @events.test_stop.add_listener
    def on_test_stop(**kwargs):
        logger.info("********** Stopping Locust Load Testing **********" )
        
    @events.quitting.add_listener
    def _(environment, **kwargs):
        if environment.stats.total.fail_ratio > 0.02:
            logger.error("Test Failed due to Failure ratio > 2%")
            environment.process_exit_code = 1
        elif environment.stats.total.get_response_time_percentile(0.95) > 5000:
            logger.error("Test Failed due to 95th percentile response time >  5000 ms")
            environment.process_exit_code = 1
        else:
              environment.process_exit_code = 0
              
    @task()
    def check_flight_api(self):
        data = check_flight_request(self.testdata)
        request_data = json.dumps(data)
        # header = json.loads()
        # header.update({"auth":"Bearer token"})
        with self.client.post(
            config.get("blazedemo","checkFlight"),
            # headers=header,
            data=request_data,
        ) as response: 
            if response.status_code != 200:
                logger.error("Request Failed for Cities : " + data["departure"] +  data["destination"])