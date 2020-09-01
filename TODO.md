# TODO

* ~~Devicetype Mapping~~
* ~~Add ZwayDevice as intermediate class between cc lib Device and current device classes~~
* Devicetypes (manufacturer-manufacturerProductType-manufacturerProductId)
    - ~~2-5-373: urn:infai:ses:device-type:9ae1f9eb-ebd6-4fb5-ae1f-a03d40c500ed~~
    * ~~373-1-18: urn:infai:ses:device-type:1c200f02-67ac-42e1-8c6c-748bdc091764~~  
    * ~~2-5-4: urn:infai:ses:device-type:662d9c9f-949d-4577-9485-9cb7255f547f~~
    * ~~134-4-80: urn:infai:ses:device-type:6c05a263-7318-47bf-a4af-a0d13cc95008~~
    * ~~373-2-14: urn:infai:ses:device-type:d4219e84-d14b-42be-9cd8-1afe4fd2afe5~~
    * ~~134-2-100: urn:infai:ses:device-type:39d1e71a-a5d2-4471-b251-466f60c7d398~~
    * ~~600-3-4237: urn:infai:ses:device-type:bec7e624-9a65-4a50-ab3d-d3fd8ce4bfe1~~
    * ~~265-8225-8449: urn:infai:ses:device-type:3cc09a10-1feb-4f8b-9390-8d08bf3ba22d~~
    * ~~271-1538-4097: urn:infai:ses:device-type:51aa4611-d2d2-4516-8555-4bd3f620b3bb~~
    * 271-2049-4097: urn:infai:ses:device-type:1f6ba259-2fc3-4537-93e4-2c97b6521c09
    * 271-3841-4096: urn:infai:ses:device-type:218f1705-fd74-4570-a8f0-dddd28e25cbb
    * ~~600-3-4226: urn:infai:ses:device-type:052d6e99-32f4-483f-967e-16341127ff89~~
    * ~~1027-3-2: urn:infai:ses:device-type:af2a302f-51c7-4344-a8fc-894cfaebb1bd~~ 
    * 881-2-7: urn:infai:ses:device-type:305e2378-0ad1-48b4-89ab-84ee9cab94a7
    * 271-6913-4096: urn:infai:ses:device-type:7f1d4ee3-a456-431d-a4af-16b560650e98
    * 271-6657-4096: urn:infai:ses:device-type:37f59ac2-5606-411c-afa2-60e150b3db06
    * 351-2305-12546: urn:infai:ses:device-type:cce425e5-3a76-4dbf-976f-3ad077bd61d2
* Code improvements
    * Error handling
        * key in dict
        * http error catching (i. e. connection refused)
        * indicate return value types
        * indicate function argument types
* Event handling
* Device provisioning (currently, creating a device will always be attempted)
* Regular checking for changed devices (new devices, status changes)
