import logging

from datadog import initialize, api
from datetime import datetime, timezone
from oauthlib.oauth2 import BackendApplicationClient
from pprint import pprint
from requests_oauthlib import OAuth2Session

def main():
  logging.basicConfig(level=logging.DEBUG)

  log_formatter = logging.Formatter('%(levelname)s: %(message)s')
  log_out = logging.StreamHandler(sys.stdout)
  log_out.setFormatter(log_formatter)
  log.addHandler(log_out)
  log.setLevel(logging.DEBUG if args.verbose == 1 else logging.INFO)

  now = datetime.now(timezone.utc).replace(second=0, microsecond=0, minute=0)
  log.info("Logging hello world!")
