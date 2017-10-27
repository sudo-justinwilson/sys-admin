# REGEX
## Regular expressions

This is just to document the regular expressions that I have used, so I don't have to think them up again:

- To match any ip address (with a possible subnet mask):
`ip addr show  | egrep "([[:digit:]]{1,3}\.){3}[[:digit:]]{1,3}(/[[:digit:]]{1,2})?"`
