from requests_oauthlib import OAuth1Session

class ListResult:
    def __init__(self, client):
        self.client = client

    def __enter__(self):
        


class Client:
    def __init__(self, domain, client_key, client_secret):
        self.domain = domain
        self.session = OAuth1Session(client_key, client_secret=client_secret)

    def get_profile(self, profile, props=None):
        if props:
            return self._request("get", "profiles/%s" % profile, Properties=",".join(props))
        return self._request("get", "profiles/%s" % profile)

    def delete_profile(self, profile):
        return self._request("delete", "profiles/%s" % profile)

    def _request(self, method, path, **params):
        url = "https://%s/rest/%s" % (self.domain, path)
        print(url)
        params['alt'] = 'json'
        f = getattr(self.session, method)
        result = f(url, params=params)
        if result.status_code != 200:
            msg = "Request issue: response code %i returned" % result.status_code
            raise RuntimeError(msg)
        return result.json()

    def get_segment_profiles(self, segment):
        return self._request("get", "segments/%s/profiles" % segment)

    def segments(self):
        return self._request('get', 'segments', count=10)
