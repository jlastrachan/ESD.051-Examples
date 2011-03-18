# Examples of Supporting [Angel.com][angel] transaction pages, for [EDS.051][esd.051]
[angel]: http://www.angel.com       "Angel.com"
[esd.051]: https://stellar.mit.edu/S/course/ESD/sp11/ESD.051/index.html     "MIT ESD.051"

#### Created by [Anthony Morelli][nm]
[nm]: https://github.com/nearlymonolith

As explained in class, Angel is a wonderful platform for creating voice applications, but
trades of extensibility and flexibility in exchange for ease of use by a non-technical
user. Luckily, it also contains the ability to create transaction pages, which open
up the option to interface with any application, provided you can do so via a URL.

The examples provided include interfacing with Angel to retrieve variables, querying
external APIs to retrieve data, parsing XML to extract the data you're interested in,
and formatting the data so that Angel can understand your response.

### Helpful Documentation Provided by Angel

 - [AngelXML Samples][1]: A small collection of example pages that show go to play prompts, add
   keyword responses, add error strategies (no input, no match), and create a
   question page.

 - [Transaction Page AngelXML Examples][2]: A much more exhaustive collection of sample
   AngelXML pages that cover almost all of the functionality you would ever need to
   accomplish just about anything via transaction pages.

 - [Transaction Page AngelXML Schema][3]: A complete definition of the AngelXML schema.
   You don't need to understand this to make a useful page, and it is complete overkill
   unless you're really interested in how it works under the hood. It will be largely
   incomprehensible unless you've had extensive XML experience.

 - [AngelXML and PHP][4]: A simple example of using PHP with AngelXML, just in case you
   prefer that to python.

 - [Transaction Page Overview][5]: A quick refresher on transaction pages.

[1]: https://www.socialtext.net/ivrwiki/angelxml_samples
[2]: https://www.socialtext.net/ivrwiki/transaction_page_angelxml_examples
[3]: https://www.socialtext.net/ivrwiki/index.cgi?transaction_page_angelxml
[4]: https://www.socialtext.net/ivrwiki/angelxml_and_php
[5]: https://www.socialtext.net/ivrwiki/transaction_page_overview

### Example Files

All python files have comments and explanations in the file. These should suffice to
make the code readable and understand how to accomplish certain objectives, although
the explanations assume a good working knowledge of and familiarity with python.

 - `Transaction_pages_web.pdf`: The presentation from class, just for reference.

 - `weather.py`: The example from class (and the presentation). Includes retrieving
   variables from a transaction page, querying the Google weather API for information,
   parsing XML for data, and creating a TTS prompt for Angel to read

 - `planahead/9000_GetPreliminaryInfo.py`: 
