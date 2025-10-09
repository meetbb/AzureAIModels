"""
Given a list of tickets, find the itinerary in order using the given list.

Note: It may be assumed that the input list of tickets is not cyclic and there is one ticket from every city except the final destination.

Examples:

Input: "Chennai" -> "Bangalore"
            "Bombay" -> "Delhi"
             "Goa"    -> "Chennai"
             "Delhi"  -> "Goa"
Output: Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Bangalore

Input: "New York" -> "Chicago"
            "Denver" -> "San Francisco"
            "Chicago" -> "Denver"
            "San Francisco" -> "Los Angeles"
Output: New York -> Chicago, Chicago -> Denver, Denver -> San Francisco, San Francisco -> Los Angeles
"""
def findItinerary(arr):
    dataSet = {}
    
    for i in arr:
        print(f"i[0] value is: {i[0]}")
        print(f"i[1] value is: {i[1]}")
        dataSet[i[0]] = i[1]
        print(f"dataSet value in loop is: {dataSet}")
    
    print(f"dataSet value outside loop is: {dataSet}")
    reverseMap = {}
    for i in arr:
        reverseMap[i[1]] = i[0]
        
    print(f"reverseMap value outside loop is: {reverseMap}")
    # Find the starting point of itinerary
    start = ""
    
    for i in range(len(arr)):
        print(f"arr[i][0] value is: {arr[i][0]}")
        if arr[i][0] not in reverseMap:
            print(f"arr[i][0] value: {arr[i][0]} is not present in reverseMap")
            start = arr[i][0]
            break
    print(f"Start value outside loop is: {start}")
    ans = []
    
    # Once we have a starting point, we simple need to go next, next of next using given hash map
    while start in dataSet:
        ans.append([start, dataSet[start]])
        start = dataSet[start]
    
    return ans

if __name__ == "__main__":
    arr = [["Chennai", "Bangalore"], ["Bombay", "Delhi"], 
           ["Goa", "Chennai"], ["Delhi", "Goa"]]

    res = findItinerary(arr)
    for i in res:
        print(i[0], "->", i[1])