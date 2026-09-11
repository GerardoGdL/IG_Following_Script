# IG_Following_Script

## What Does This Program Do?
This repository will compare your Instagram followers and following to find who does not follow you back.

## How Does It Work?
The system reads your following/followers lists from Instagram's official JSON files, turning them into sets. Their difference is then taken, resulting in a new set including all accounts which do not follow you back. This set is then printed with one account per line for legibility

## How To Get Your JSON Files
To get your JSON files, you must log into Instagram (Preferably on the device you will be running this script on) --> Settings --> Accounts Center --> Your Information And Permissions --> Export Your Information --> Create Export --> Select Desired Account --> Export To Device --> Customize Information (Only Select 'Followers and Following' under 'Connections' And Save) --> Date Range (All Time) --> Format (JSON) --> Start Export

Once you receive your export, extract all the files into the 'data/raw' directory