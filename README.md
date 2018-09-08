Set of scripts to export flights from TripIt and import them into Flightdiary. Quick and dirty.
## Installation
* python 2.7

https://www.python.org/download/releases/2.7/
* python libraries:
```
pip install -r requierements.txt
```
* Install jq

https://stedolan.github.io/jq/download/
## TripIt setup

* Register an application at  https://www.tripit.com/developer
* Get API Key and Secret
* Save them to a file named `creds.json`

```json
{
    "CLIENT_KEY": "*** API Key ***",
    "CLIENT_SECRET": "*** API Secret ***"
}
```

## Flightdiary setup

Just put username and password in `creds.json`

```json
    "FD_USER": "*** USER ***",
    "FD_PASSWORD": "*** PASSWORD ***"
```
https://my.flightradar24.com/
## Getting access token
* Run `get_token.py`
* A link gonna open in the browser to grant the app access to your account 
* **You will land at a "Page Not Found", that's normal**
* Copy the URL, which looks like `http://www.foo.com/?oauth_token=` back into the terminal
* The `creds.json` data gonna get updated with the access token data


## Syncing

Run `sync.py`, it will add missing flight (as identified by date and flight number) that are in TripIt to Flightdiary.
Additionally, you can run using the argument "-i <tripit json filename>" (e.g. `sync.py -i tripit.json`) to import the file generated when running `tripit.py > tripit.json`

## Dumping all TripIt information

Run `tripit.py`, it will output a JSON of all your past trips.

You can then run `./jq.sh < tripit.json > tripit.txt` to get a textual list of flights. (You need to install jq.)

## Dumping Flightdiary flights

Run `flightdiary.py`, it will output a textual list of all your flights.

You can compare this list with the one on TripIt (for example before running the sync) like this:

```
./flightdiary.py | sort | diff -u - tripit.txt
```

Any lines starting with `+` are the ones that `sync.py` will add (unless it's just the airports codes that are wrong).
