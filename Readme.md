# PyHund [r5]
Pyhund is an open source intelligence tool used to find and gather information on usernames on approximately **300 websites!** PyHund comes built in with suck features as the PyHund **Harvester**[^2] and **DeepLink**. [^3]

## Usage
PyHund has three core usage modes: **harvest**[^2],  **deeplink**[^3], and **scan**[^1]
1. **Harvest**[^2]
```PyHund -t target1 ... targetN -s scan --harvest %rule1 ... ruleN format```
  
    The arguments above consist of providing the target(s) to scan along with the scan name.
    The addition of the ***\-\-harvest*** flag switches the PyHund application from ***scan***[^1] to ***harvest***[^2] mode. After being set to ***harvest***[^2] mode the application will proceed to scrape data from the valid sites, only showing the user the site it is currently parsing, unless otherwise specified. 
2. **DeepLink**[^3]
  `PyHund -t target1 ... targetN -s scan --deep-link path`
    
    The arguments provided above include the default required arguments along with the added ***\-\-deep-link*** flag. The addition of this flag sets the PyHund application into ***Deeplink***[^3] mode. When in ***Deeplink***[^3] mode PyHund will use up more time finding as much data on a target as possible with some reinforced guessing and tracking technology to find the most accurate data along with data that may not be easily accessed. 
    The ***\-\-deep-link*** flag takes only one argument, that being the path to the *deeplink.conf* file. If included those configurations will be loaded into the **Deeplink**[^3] module to be factored into the search. If no file path is provided then the **Deeplink**[^3] module will run with default settings. 
  
    **Note** : If default configuration is used it will produce generally less accurate results than a tailored config
3. **Scan**[^1]
  `PyHund -t target1 ... targetN -s scan -arg val ... --rule ...`
    
    The arguments provided for a regular scan mode are the default, required arguments along with possible extraneous arguments and flags. 
    In this mode each site will be scanned in the given scan, and will then return wether or not the target exists on that site.

## Arguments & Flags
For each mode there are unique and standard arguments and flags. each argument and flag can be used to acquire more precise results for your scan.
### Required Arguments
  * Required arguments are arguments that must be provided for the program to run
  **-s** : Scan : sets the scan for all targets. Scans are located in *./lib/scans/*.
    **-t**  : Targets : sets the list of targets to scan for. This can be any number of targets.
 
 ### General Arguments
 * General arguments are arguments that can be provided to filter input / output
   **-f** : filter : used to add filters to sites being read in from scan
   * **http-ver=** : will only read in sites with the provided http-ver. 
     **Note**: Can only be 1 or 2
       
   * **verify-method=** : will only read in sites with provided verify methods.  
   **Note**: Can only be url / status / match. methods seperated by ***( , )*** with no spaces 
### Harvester Arguments
* Harvester arguments are arguments that alter the behavior of the harvester in the way it scrapes and returns data
**%scope** : scope : Will restrict parser to only look for data in certain tags in the html data.
**Note**: must be a valid html tag

### General Flags
* General flags are rules that get passed into PyHund to alter behavior. Most flags alter how data gets presented to the user
**-\-no-url** : disables presenting url to stdout, instead only prints the site name
**\-\-no-err** : disables bad output, will not show negative responses to scan
**\-\-log** : logs stdout to file title *scan.inf*

## Associated Tools
Included with PyHund are a series of tools used to aid in the development and maintinance of the tool, that can be used to bolster your own tool. 
These tools Include : **makescan**, **makesite**, and **sitemanager**
### makescan
* Makescan is a tool used to produce a custom scan from the known sites in *lib/manifest.json*

### makesite
* Makesite is a more advanced tool that allows for the addition of new sites to the manifest[^4] in an easy way. The tool requires the url to the site and a known user on the site. From there it will infer the **validation method**[^5], and **harvester tokens**[^6] along with the **validation string**[^7]. This tool also check if falsified headers are required to gain an accurate response.

### sitemanager
* Sitemanager is a tool used to investigate and maintain the manifest[^4]. It is capable of checking what sites are in the manifest[^4], what each site's data is and can attempt a connection with the current data to ensure it is still valid. 

[^1]:**Scan** is the default use method of PyHund. This mode is used to scan for the existence of a user at a given site
[^2]: **Harvester** is a html parser that scrapes important data from a found and validated website. Harvester will look for important information for you and return the scraped data in your choice of **raw**, **html**, **json**, **csv**, or **latex** format
[^3]: **Deeplink** is a smart web scraper that will target provided information to return the most accurate results for a given target. Deeplink will use emails, phone numbers, addresses, and keywords to filter results and target other locations where more info can be found on the provided target
[^4]: **Manifest** is the file stored in *lib* that contains the data of all sites used by PyHund, including validation methods[^5], harvester tokens[^6], and the site's url along with potential headers
[^5]: **Validation Method** is the term used to describe how the site is checked for authenticity. This is used to detect false positives and negatives to get more accurate results.
[^6]: **Harvester Tokens** are regex raw strings that are used to locate important data to be parsed by the PyHund Harvester[^2]
[^7]: **Validation String** is a string that can be used as a reference to check if a http response is valid. This string may contain text from the html document, a segment of the response url, or a number representing a valid status code
