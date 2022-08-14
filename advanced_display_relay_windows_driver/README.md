# advanced_display_relay_driver
This application reads input values stored in advanced_display_relay and drives windows scripts to automate functions on advanced displays.

# Important notes
This will not work unless the adr kubernetes app is already setup and adr fields 1,2,&3 are populated

Default ADR Field 1
http://localhost/adr_fields/new?adr_field=adr_field_1&json_data=%7B%22nextDesktop%22%3A%22OFF%22%2C%22prevDesktop%22%3A%22OFF%22%7D

Default ADR Field 3
http://localhost/adr_fields/new?adr_field=adr_field_3&json_data=%7B%22desktop%20change%20mode%20without%20animation%22%3A%22OFF%22%2C%22desktop%20change%20mode%20with%20animation%22%3A%22ON%22%2C%22chrome%20tab%20change%20mode%22%3A%22OFF%22%2C%22arrow%20mode%22%3A%22OFF%22%7D

Make sure the windows desktop being used has 5 desktops already.