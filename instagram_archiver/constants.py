from typing import Final, Mapping

__all__ = ('SHARED_HEADERS', 'USER_AGENT')

USER_AGENT: Final[str] = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/112.0.0.0 Safari/537.36')
# Do not set the x-ig-d header as this will cause API calls to return 404
SHARED_HEADERS: Final[Mapping[str, str]] = {
    'accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,'
               'image/avif,image/webp,image/apng,*/*;q=0.8,'
               'application/signed-exchange;v=b3;q=0.9'),
    'accept-language':
    'en,en-GB;q=0.9,en-US;q=0.8',
    'authority':
    'www.instagram.com',
    'cache-control':
    'no-cache',
    'dnt':
    '1',
    'pragma':
    'no-cache',
    'referer':
    'https://www.instagram.com',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    USER_AGENT,
    'viewport-width':
    '2560',
    'x-ig-app-id':
    '936619743392459'
}
LOG_SCHEMA = '''
CREATE TABLE log (
    url TEXT PRIMARY KEY NOT NULL,
    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
);
'''
# Value taken from Instagram's JS under BootloaderConfig
RETRY_ABORT_NUM: Final[int] = 2
