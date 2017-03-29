#BASH COMMANDS

## To get the top ten instances of a string from a log:
    # for ua in `cat access_log | cut -f10 -d' ' | sort | uniq`; do echo "$ua   `grep -c $ua access_log`"; done | sort -k2 -n  -r | head -11 | tail -10
    # presuming the keywords are in column 10
