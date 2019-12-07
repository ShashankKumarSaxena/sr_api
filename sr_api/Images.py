import aiohttp
import json

async def _call_api(endpoint):
    async with aiohttp.ClientSession() as c:
        async with c.get(f'https://some-random-api.ml/{endpoint}') as r:
            return await r.json()
        
async def __get_api_img(img):
    base = await _call_api(f'img/{img}')
    return base['link']

class Image:

    @property
    def dog(self=None):
        return await _get_api_img('dog')

    @property
    def cat(self=None):
        return _get_api_img('cat')

    @property
    def bird(self=None):
        return _get_api_img('bird')

    @property
    def fox(self=None):
        return _get_api_img('fox')

    @property
    def koala(self=None):
        return _get_api_img('koala')

    @property
    def panda(self=None):
        return _get_api_img('panda')

    @property
    def redpanda(self=None):
        return _get_api_img('red_panda')
