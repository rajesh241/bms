"""Call Manager File"""
import argparse
import requests
import os
import django
import pandas as pd
from commons import logger_fetch
from defines import DJANGO_SETTINGS
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS)
django.setup()
from django.conf import settings
from baseapp.models import PhoneCall

account_sid = settings.EXOTEL_SID
token = settings.EXOTEL_TOKEN
exotel_no = '02071178599' 
def args_fetch():
    '''
    Paser for the argument list that returns the args list
    '''

    parser = argparse.ArgumentParser(description=('This is blank script',
                                                  'you can copy this base script '))
    parser.add_argument('-l', '--log-level', help='Log level defining verbosity', required=False)
    parser.add_argument('-t', '--test', help='Test Loop',
                        required=False, action='store_const', const=1)
    parser.add_argument('-e', '--execute', help='Test Loop',
                        required=False, action='store_const', const=1)
    parser.add_argument('-ti1', '--testInput1', help='Test Input 1', required=False)
    parser.add_argument('-ti2', '--testInput2', help='Test Input 2', required=False)
    args = vars(parser.parse_args())
    return args

def exotel_call_status(logger, callsid):
  url = f"https://{account_sid}:{token}@twilix.exotel.in/v1/Accounts/{account_sid}/Calls/{callsid}.json"
  res = requests.get(url)
  return res.json()

def exotel_place_call(logger, phone, app_name, callid, exotel_no=None):
    calltype = "trans"
    url = 'http://my.exotel.in/exoml/start/' + app_name
    exotel_no = '02071178599' 
    data={
        'From': phone,
        'To': exotel_no,
        'CallerId': exotel_no,
        'Url': url,
        #'TimeLimit': timelimit,
        #'TimeOut': timeout,
        'CallType': calltype,
        'CustomField': callid
    #    'StatusCallback': callback_url
    }
    res = requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=account_sid),
        auth=(account_sid, token), data=data)
    logger.info(res.status_code)
    logger.info(res.json())
    return res.json()


def main():
    """Main Module of this program"""
    args = args_fetch()
    logger = logger_fetch(args.get('log_level'))
    if args['test']:
        logger.info("Testing")
        phone = '9845065241'
        app_name = '294685'
        PhoneCall.objects.create(phone=phone, exotel_app_no=app_name)
    logger.info("...END PROCESSING")
    if args['execute']:
        # Get Call Status
        exotel_status = ["completed", "busy", "no-answer", "failed"]
        objs = PhoneCall.objects.filter(in_progress = True)
        for obj in objs:
            sid = obj.sid
            res = exotel_call_status(logger, sid)
            res_dict = res["Call"]
            vendor_status = res_dict["Status"]
            if vendor_status in exotel_status:
                obj.vendor_status = vendor_status
                obj.retry = obj.retry + 1
                obj.in_progress = False
                obj.extra_fields = res_dict
                if vendor_status == "completed":
                    obj.status = "completed"
                    obj.is_complete = True
                else:
                    if obj.retry == 10:
                        obj.status = "maxRetryFail"
                        obj.is_complete = True
                obj.save()
            logger.info(res)
        #Place Calls
        objs = PhoneCall.objects.filter(is_complete=False, in_progress=False)
        for obj in objs:
            data = exotel_place_call(logger, obj.phone, obj.exotel_app_no,
                                     obj.id)
            try:
                sid = data["Call"]["Sid"]
            except:
                sid = None
            if sid is None:
                obj.is_complete = True
                obj.status = "DND"
                obj.save()
            else:
                obj.in_progress = True
                obj.sid = sid
                obj.save()

if __name__ == '__main__':
    main()
