# To be detailed

Basically make sure you `pip -r requirements.txt install`

Tests should be included in `.travis.yml` or `.github/actions/` later on but you can also run them

`python3 -m pytest -rpP tests/test_Smile.py`

# Directories

Intended: (yellow ones means, please submit yours)

 - [![Generic badge](https://img.shields.io/badge/Adam-v3-yellow.svg)]() setup with a boiler, Floor, Koen, Plug, Tom and Lisa (i.e. the whole shebang) (`adam_full_option`)
 - [![Generic badge](https://img.shields.io/badge/Adam-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/adam_living_floor_plus_3_rooms) setup with a boiler, Floor, Lisa and 3x Toms
 - [![Generic badge](https://img.shields.io/badge/Adam-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/adam_multiple_devices_per_zone) setup with everything but Koen and Anna, multiple devices per zone
 - [![Generic badge](https://img.shields.io/badge/Adam-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/adam_zone_per_device) setup with everything but Koen and Anna, device per zone
 - [![Generic badge](https://img.shields.io/badge/Adam-v3-yellow.svg)]() setup without a boiler, but with Lisa and either a Plug or a Tom (`adam_without_boiler`) 

 - [![Generic badge](https://img.shields.io/badge/Adam_Anna-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/adam_plus_anna) a boiler, Adam, Anna and Tom

 - [![Generic badge](https://img.shields.io/badge/Anna-v4-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/anna_v4) setup with a boiler
 - [![Generic badge](https://img.shields.io/badge/Anna-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/anna_without_boiler) without boiler(i.e. attached to city heating)
 - [![Generic badge](https://img.shields.io/badge/Anna-v1-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/legacy_anna) setup with a boiler, but legacy firmware (1.8)

 - [![Generic badge](https://img.shields.io/badge/P1-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/p1v3) electricity only
 - [![Generic badge](https://img.shields.io/badge/P1-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/p1v3solarfake) electricity only - just the above with added data, please submit **yours**
 - [![Generic badge](https://img.shields.io/badge/P1-v3-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/p1v3_full_option) electricity, solar and gas 
 - [![Generic badge](https://img.shields.io/badge/P1-v3-yellow.svg)]() electricity and gas (`p1v3_gas_nosolar`)
 - [![Generic badge](https://img.shields.io/badge/P1-v2-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/smile_p1_v2) electricity and gas
 - [![Generic badge](https://img.shields.io/badge/P1-v2-green.svg)](https://github.com/plugwise/Plugwise-Smile/tree/docs/tests/smile_p1_v2_2) another electricity and gas

If you see a yellow item and feel your setup fits in, please **MAIL** one of the authors the output of the below links. Feel free to create a PR if you follow the below privacy hint:

They should al start with `<xml` and copied as plain text (i.e. not preformatted like Chrome and Safari do).
Either use wget/curl or use your 'developer view' from your browser to copy the source text
 
```
http://{ip_of_your_smile}/core/appliances
http://{ip_of_your_smile}/core/direct_objects
http://{ip_of_your_smile}/core/domain_objects
http://{ip_of_your_smile}/core/locations
http://{ip_of_your_smile}/core/modules
```

# Important

Don't commit test-data in `tests` that shouldn't be available to 'the internet'.
To prevent this we've included a pre-commit hook that checks and validates that no private information is there (but do double-check yourselves!)
See 'pre-commit.sh' for details

Excerpt:

 - [ ] modify `domain_objects` and `modules` and set all occurances of `mac-address` to `0123456789AB`
 - [ ] modify `domain_objects` and set `short_id` to `abcdefgh`
 - [ ] modify `domain_objects` and set `wifi_ip` to `127.0.0.1`
 - [ ] modify `domain_objects` and set `lan_ip` to `127.0.0.1`
 - [ ] modify `domain_objects` and set all `ip_addresses` to `127.0.0.1`
 - [ ] modify `domain_objects` and set `hostname` to `smile000000`
 - [ ] modify `domain_objects` and set `longitude` to `4.49`
 - [ ] modify `domain_objects` and set `latitude` to `52.21`
 - [ ] modify `domain_objects` and set `city` to `Sassenheim`
 - [ ] modify `domain_objects` and set `postal_code` to `2171`


