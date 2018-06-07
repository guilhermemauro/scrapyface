from w3lib.http import basic_auth_header
from logging import getLogger

logger = getLogger(__name__)

class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        if spider.proxy != None:
            request.meta['proxy'] = 'https://' + spider.proxy
            logger.info('Proxy utilized: {}'.format(spider.proxy))
        else:
            logger.info('No custom proxy utilized.')
