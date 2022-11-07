# Create a pivot table of the start (minimum) and end (maximum) timestamps associated with each case:
case_starts_ends = events.pivot_table(index='patient', aggfunc={'datetime': ['min', 'max']}) 
case_starts_ends = case_starts_ends.reset_index() 
case_starts_ends.columns = ['patient', 'caseend', 'casestart'] 
# Merge with the main event log data so that for each row we have the start and end times.
events = events.merge(case_starts_ends, on='patient') 
# Calculate the relative time by subtracting the process start time from the event timestamp
events['relativetime'] = events['datetime'] - events['casestart']
# Convert relative times to more friendly measures
## seconds
events['relativetime_s'] = events['relativetime'].dt.seconds + 86400*events['relativetime'].dt.days 
## days
events['relativedays'] = events['relativetime'].dt.days
