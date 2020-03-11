"""Plugwise Home Assistant module."""

import time
import pytest
import pytest_asyncio
import pytest_aiohttp

import asyncio
import aiohttp
import os

from lxml import etree

from Plugwise_Smile.Smile import Smile

# Prepare aiohttp app routes
# taking smile_type (i.e. directory name under tests/{smile_app}/
# as inclusion point
async def setup_app():
    global smile_type
    if not smile_type:
        return False
    app = aiohttp.web.Application()
    app.router.add_get('/core/appliances',smile_appliances)
    app.router.add_get('/core/direct_objects',smile_direct_objects)
    app.router.add_get('/core/domain_objects',smile_domain_objects)
    app.router.add_get('/core/locations',smile_locations)
    app.router.add_get('/core/modules',smile_modules)
    return app

# Wrapper for appliances uri
async def smile_appliances(request):
    global smile_type
    f=open('tests/{}/core.appliances.xml'.format(smile_type),'r')
    data=f.read()
    f.close()
    return aiohttp.web.Response(text=data)

async def smile_direct_objects(request):
    global smile_type
    f=open('tests/{}/core.direct_objects.xml'.format(smile_type),'r')
    data=f.read()
    f.close()
    return aiohttp.web.Response(text=data)

async def smile_domain_objects(request):
    global smile_type
    f=open('tests/{}/core.domain_objects.xml'.format(smile_type),'r')
    data=f.read()
    f.close()
    return aiohttp.web.Response(text=data)

async def smile_locations(request):
    global smile_type
    f=open('tests/{}/core.locations.xml'.format(smile_type),'r')
    data=f.read()
    f.close()
    return aiohttp.web.Response(text=data)

async def smile_modules(request):
    global smile_type
    f=open('tests/{}/core.modules.xml'.format(smile_type),'r')
    data=f.read()
    f.close()
    return aiohttp.web.Response(text=data)

# Test if at least modules functions before going further
# note that this only tests the modules-app for functionality
# if this fails, none of the actual tests against the Smile library
# will function correctly
async def test_mock(aiohttp_client, loop):
    global smile_type
    smile_type = 'anna_without_boiler'
    app = aiohttp.web.Application()
    app.router.add_get('/core/modules',smile_modules)
    client = await aiohttp_client(app)
    resp = await client.get('/core/modules')
    assert resp.status == 200
    text = await resp.text()
    assert 'xml' in text

# Generic connect
@pytest.mark.asyncio
async def connect():
    global smile_type
    if not smile_type:
        return False
    port =  aiohttp.test_utils.unused_port()

    app = await setup_app()

    server = aiohttp.test_utils.TestServer(app,port=port,scheme='http',host='127.0.0.1')
    await server.start_server()

    client = aiohttp.test_utils.TestClient(server)
    websession = client.session

    url = '{}://{}:{}/core/modules'.format(server.scheme,server.host,server.port)
    resp = await websession.get(url)
    assert resp.status == 200
    text = await resp.text()
    assert 'xml' in text
    assert '<vendor_name>Plugwise</vendor_name>' in text

    smile = Smile( host=server.host, password='abcdefgh', port=server.port, websession=websession)
    assert smile._timeout == 20
    assert smile._domain_objects == None

    """Connect to the smile"""
    connection = await smile.connect()
    assert connection == True
    return server,smile,client


# GEneric list_devices
@pytest.mark.asyncio
async def list_devices(server,smile):
    device_list={}
    devices = smile.get_devices()
    for dev in devices:
        if dev['name'] == 'Controlled Device':
            ctrl_id = dev['id']
        else:
            device_list[dev['id']]={'name': dev['name'], 'ctrl': ctrl_id}
    #print(device_list)
    return device_list


# Generic disconnect
@pytest.mark.asyncio
async def disconnect(server,client):
    if not server:
        return False
    await server.close()
    await client.session.close()

# Actual test for directory 'Anna' without a boiler
@pytest.mark.asyncio
async def test_connect_anna_without_boiler():
    global smile_type
    smile_type = 'anna_without_boiler'
    server,smile,client = await connect()
    device_list = await list_devices(server,smile)
    #print(device_list)
    for dev_id,details in device_list.items():
        data = smile.get_device_data(dev_id, details['ctrl'])
        assert data['type'] == 'thermostat'
        assert data['setpoint_temp'] == 16.0
        assert data['current_temp'] == 20.62
        assert data['selected_schedule'] == 'Normal'
        assert data['boiler_state'] == None
        assert data['battery'] == None
    await disconnect(server,client)

# Actual test for directory 'Adam'
# living room floor radiator valve and separate zone thermostat
# an three rooms with conventional radiators
@pytest.mark.asyncio
async def test_connect_adam():
    global smile_type
    smile_type = 'adam_living_floor_plus_3_rooms'
    server,smile,client = await connect()
    device_list = await list_devices(server,smile)
    print(device_list)
    for dev_id,details in device_list.items():
        data = smile.get_device_data(dev_id, details['ctrl'])
        print(data)
    await disconnect(server,client)
