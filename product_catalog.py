from product_data import products
for i in products:
    print(i)

customer_preferences = []
preference = "" 
while preference != "N":
    preference = input("Input a preference: ") 
    if preference != "N":
        customer_preferences.append(preference)

customer_tags = set(customer_preferences)
print("Customer preferences:", customer_tags)

converted_products = []
for product in products:
    converted_product = {'name': product['name'],'tags': set(product['tags'])}
    converted_products.append(converted_product)

def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))

def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        if match_count > 0:
            matches.append({'name': product['name'],'matches': match_count})
    return sorted(matches, key=lambda x: x['matches'], reverse=True)

recommendations = recommend_products(converted_products, customer_tags)
print("Recommended Products:")
for i in recommendations:
    print(f"Product: {i['name']}, Matches: {i['matches']}")


    '''
The core operations that were used in this script were sets, lists, sorting, intersections, while/for loops, and functions. Sets were 
used to get rid of duplicates in customer preferences and to allow efficient tag comparisons. Sets also allow for the use of the "all or nothing" lookup 
method, which tries to find an exact match to the input provided. The intersection method was used to compare product and customer tags to find matches. The for loops were used 
to iterate through all the products for tag conversion and recommendation generation, which allowed searching through the entire list of products, while the while 
loop was used to allow the user to continue adding preferences until the letter "N" was inputted. The sorting method was used to order recommendations by matching 
the count in descending order from the most relevant products to the least relevant. List append methods were used to build the "customer_preferences" 
list and the recommendation output list to collect data. These operations were used because of their efficiency and usability. Sets allow for faster matching compared 
to lists. Sorting ensures that the best matches are presented first. For loop methods make sure all data is iterated to find the correct result. 

Something that I would change if there were 1000 products would be to add a method so that I don't have to iterate through over 1000 products. Another would 
be to add a database for better organization and management. Lastly, multi-threading/processing would be added for multitasking.     
    '''
