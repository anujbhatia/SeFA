import sys, os
import typing as t

script_path = os.path.realpath(__file__)
script_folder = os.path.dirname(script_path)
top_folder = os.path.dirname(script_folder)
sys.path.insert(1, os.path.join(top_folder, "models"))
from org import Organization

ticker_org_info: t.Dict[str, Organization] = {
    "adbe": Organization(
        name="Adobe Incorporation",
        address="345 Park Avenue San Jose, CA",
        country_name="2 - United States",
        zip_code="95110",
        nature="Listed",
    ),
    "aapl": Organization(
        name="Apple Inc.",
        address="One Apple Park Way; Cupertino, CA",
        country_name="2 - United States",
        zip_code="95014",
        nature="Listed",
    ),
    "brk.b": Organization(
        name="Berkshire Hathway Inc",
        address="3555 Farnam St Omaha, NE",
        country_name="2 - United States",
        zip_code="68131",
        nature="Listed",
    ),
    "googl": Organization(
        name="Google Inc.",
        address="1600 Amphitheatre Pkwy. Mountain View, CA",
        country_name="2 - United States",
        zip_code="94043",
        nature="Listed",
    ),
    "intc": Organization(
        name="Intel Inc.",
        address="2200 Mission College Blvd, Santa Clara, CA",
        country_name="2 - United States",
        zip_code="95054",
        nature="Listed",
    ),
    "mdlz": Organization(
        name="Mondelz International Inc.",
        address="905 West Fulton Market, Suite 200 Chicago, IL",
        country_name="2 - United States",
        zip_code="60607",
        nature="Listed",
    ),
    "meta": Organization(
        name="Meta Platforms Inc.",
        address="1601 Willow Road Menlo Park, CA",
        country_name="2 - United States",
        zip_code="94025",
        nature="Listed",
    ),
    "msft": Organization(
        name="Microsoft Inc.",
        address="One Microsoft Way, Redmond, WA",
        country_name="2 - United States",
        zip_code="98052",
        nature="Listed",
    ),
    "acls": Organization(
        name="Axcelis Technologies, Inc.",
        address="108 CHERRY HILL DRIVE, BEVERLY, Massachusetts",
        country_name="2 - United States",
        zip_code="01915",
        nature="Listed",
    ),
    "crm": Organization(
        name="Salesforce, Inc.",
        address="415 MISSION STREET,3RD FLOOR, SALESFORCE TOWER, SAN FRANCISCO, California",
        country_name="2 - United States",
        zip_code="94105",
        nature="Listed",
    ),
    "csco": Organization(
        name="Cisco Systems, Inc.",
        address="170 WEST TASMAN DRIVE, SAN JOSE, California",
        country_name="2 - United States",
        zip_code="95134-1706",
        nature="Listed",
    ),
    "fslr": Organization(
        name="First Solar, Inc.",
        address="350 WEST WASHINGTON STREET,SUITE 600, TEMPE, Arizona",
        country_name="2 - United States",
        zip_code="85281",
        nature="Listed",
    ),
    "on": Organization(
        name="ON Semiconductor Corporation",
        address="5005 EAST MCDOWELL ROAD, PHOENIX, Arizona",
        country_name="2 - United States",
        zip_code="85008",
        nature="Listed",
    ),
    "vrtx": Organization(
        name="Vertex Pharmaceuticals Incorporated",
        address="50 NORTHERN AVENUE, BOSTON, Massachusetts",
        country_name="2 - United States",
        zip_code="02210",
        nature="Listed",
    ),
    "amzn": Organization(
        name="Amazon.com, Inc.",
        address="410 TERRY AVENUE NORTH, SEATTLE, Washington",
        country_name="2 - United States",
        zip_code="98109",
        nature="Listed",
    ),
}

ticker_currency_info: t.Dict[str, str] = {
    "adbe": "USD",
    "aapl": "USD",
    "brk.b": "USD",
    "googl": "USD",
    "intc": "USD",
    "mdlz": "USD",
    "meta": "USD",
    "msft": "USD",
    "acls": "USD",
    "crm": "USD",
    "csco": "USD",
    "fslr": "USD",
    "on": "USD",
    "vrtx": "USD",
    "amzn": "USD",
}
