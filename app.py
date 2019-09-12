from flask import Flask
from flask import request, jsonify
app=Flask(__name__)
#country data
country_data = {
"afghanistan":"Kabul",
"albania":"Tirana",
"andorra":"Andorra La Vella",
"angola":"Luanda",
"antigua and Barbuda":"St. John’s",
"argentina":"Buenos Aires",
"armenia":"Yerevan",
"australia":"Canberra",
"austria":"Vienna",
"azerbaijan":"Baku",
"bahamas":"Nassau",
"bahrain":"Manama",
"bangladesh":"Dhaka",
"barbados":"Bridgetown",
"belarus":"Minsk",
"belgium":"Brussels",
"belize":"Belmopan",
"benin":"Porto Novo, Cotonou",
"bhutan":"Thimphu",
"bolivia":"La Paz and Sucre",
"bosnia and Herzegovina":"Sarajevo",
"botswana":"Gaborone",
"brazil":"Brasí Lia",
"brunei":"Bandar Seri Begawan",
"bulgaria":"Sofia",
"burkina Faso":"Ouagadougou",
"burundi":"Bujumbura",
"cambodia":"Phnom Penh",
"cameroon":"Yaounde",
"canada":"Ottawa",
"cape verde":"Praia",
"cayman islands":"george Town",
"central african Republic":"Bangui",
"chad":"N’djamena",
"chile":"Santiago",
"china":"Beijing",
"colombia":"Bogota",
"comoros":"Moroni",
"costa rica":"San Jose",
"co te d’ivoire":"Yamoussoukro",
"croatia":"Zagreb",
"cuba":"Havana",
"cyprus":"Nicosia",
"czech republic":"Prague",
"democratic Republic of the Congo":"Kinshasa",
"denmark":"Copenhagen",
"djibouti":"Djibouti",
"dominica":"Roseau",
"dominican republic":"Santo Domingo",
"east timor":"Dili",
"ecuador":"Quito",
"egypt":"Cairo",
"el salvador":"San Salvador",
"equatorial guinea":"Malabo",
"eritrea":"Asmara",
"estonia":"Tallinn",
"ethiopia":"Addis Ababa",
"fiji":"Suva",
"finland":"Helsinki",
"france":"Paris",
"french guiana":"Cayenne",
"gabon":"Libreville",
"georgia":"Tbilisi",
"germany":"Berlin",
"ghana":"Accra",
"greece":"Athens",
"grenada":"St George’s",
"guatemala":"Guatemala",
"guinea":"Conakry",
"guinea":"Bissau",
"guyana":"Georgetown",
"haiti":"Port-au-Prince",
"honduras":"Tegucigalpa",
"hungary":"Budapest",
"iceland":"Reykjavik",
"india":"New Delhi",
"indonesia":"Jakarta",
"iran":"Tehran",
"iraq":"Baghdad",
"israel":"Jerusalem",
"italy":"Rome",
"jamaica":"Kingston, Jamaica",
"japan":"Tokyo",
"jordan":"Amman",
"kazakhstan":"Astana",
"kenya":"Nairobi",
"kiribati":"South Tarawa",
"kuwait":"Kuwait",
"Kyrgyzstan":"Bishkek",
"laos":"Vientianelatvia,Riga",
"lebanon":"Beirut",
"lesotho":"Maseru",
"liberia":"Monrovia",
"libya":"Tripoli",
"liechtenstein":"Vaduz",
"lithuania":"Vilnius",
"luxembourg":"Luxembourg City",
"madagascar":"Antananarivo",
"malawi":"Lilongwe",
"malaysia":"Kuala Lumpur",
"maldives":"Male",
"mali":"Bamako",
"malta":"Valletta",
"marshall islands":"Majuro",
"mauritania":"Nouakchott",
"mauritius":"Port Louis",
"mexico":"Mexico City",
"micronesia":"Palikir",
"moldova":"Chisinau",
"monaco":"Monaco",
"mongolia":"Ulaanbaatar",
"montenegro":"Podgorica",
"morocco":"Rabat",
"mozambique":"Maputo",
"myanmar":"Naypyidaw",
"namibia":"Windhoek",
"nauru":"Yaren",
"nepal":"Kathmandu",
"netherlands":"Amsterdam",
"new zealand":"Wellington",
"nicaragua":"Managua",
"niger":"Niamey",
"nigeria":"Abuja",
"north Korea":"Pyongyang",
"norway":"Oslo",
"oman":"Muscat",
"pakistan":"Islamabad",
"palau":"Koror",
"palestine":"Jerusalem",
"panama":"Panama City",
"papua new guinea":"Port Moresby",
"paraguay":"Asuncion",
"peru":"Lima",
"philippines":"Manila",
"poland,WarsawPortugal":"Lisbon",
"puerto rico":"San Juan",
"qatar":"Doha",
"republic of ireland":"Dublin",
"republic of macedonia":"Skopje",
"republic of the congo":"Brazzaville",
"romania":"Bucharest",
"russia":"Moscow",
"rwanda":"Kigali",
"saint kitts and nevis":"Basseterre",
"saint lucia":"Castries",
"saint vincent and the grenadines":"Kingstown",
"samoa":"Apia",
"san marino":"San Marino",
"sa o tome and prí ncipe":"Sa O Tome",
"saudi arabia":"Riyadh",
"senegal":"Dakar",
"serbia":"Belgrade",
"seychelles":"Victoria",
"sierra leone":"Freetown",
"singapore":"Singapore",
"slovakia":"Bratislava",
"slovenia":"Ljubljana",
"solomon islands":"Honiara",
"somalia":"Mogadishu",
"south africa":"Pretoria",
"south korea":"Seoul",
"south sudan":"Juba",
"spain":"Madrid",
"sri lanka":"Colombo",
"sudan":"Khartoum",
"suriname":"Paramaribo",
"swaziland":"Mbabane",
"sweden":"Stockholm",
"switzerland":"Bern",
"syria":"Damascus",
"taiwan":"Taipei",
"taiwan":"Taipei",
"tajikistan":"Dushanbe",
"tanzania":"Dar Es Salaam, Dodoma",
"thailand":"Bangkok",
"the gambia":"Banjul",
"togo":"Lome",
"tonga":"Nuku’alofa",
"trinidad and tobago":"Port of Spaintunisia ,Tunis",
"turkey":"Ankara",
"turkey":"Ankara",
"turkmenistan":"Asgabat",
"turks and caicos":"Cockburn Town",
"tuvalu":"Funafuti",
"uganda":"Kampala",
"ukraine":"Kyiv or Kiev",
"united arab emirates":"Abu dhabi",
"united kingdom":"London",
"united states":"Washington DC",
"uruguay":"Montevideo",
"uzbekistan":"Tashkent",
"vanuatu":"Port Vila",
"vatican city":"Vatican City",
"venezuela":"Caracas",
"vietnam":"Hanoi",
"western sahara":"la’youn",
"yemen":"Sana’a",
"zambia":"Lusaka",
"zimbabwe":"Harare"
}

@app.route('/', methods=['get'])
def home():#only for check my api is working or not
    #key=request.args.get()
    return "Hellow World"
@app.route('/data', methods=['get'])#provide the route of data
def store_data():#store data in json
    return jsonify(country_data)
@app.route('/capital', methods=['get'])
def capital():
    country1=request.args.get("country")#take argument by key in url
    country=country1.lower().strip()#convert all string in lowercase  and
    " ".join(country.split())#remove all whitespace
    if  country in country_data.keys() :#if country in our country data
         return "<h2>Capital of "+country.upper()+":{}</h2>".format(country_data[country])#return output
    elif len(country)==0:
        return "<h2> Country is Null"
    elif country.isdigit()==True:
       return "<h2>invalid input</h2>"
    #elif key.isalnum()==true:
    #    return "<h2> invalid input Country</h2>"
    else:
        return "<h3>Country is not present Country data</h3>"






if __name__ == '__main__':
    app.run("127.0.0.1","5000",debug=True)
