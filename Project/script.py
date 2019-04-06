from data import types, restaurant_data
from welcome import print_welcome
from linkedlist import LinkedList
from node import Node

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_types_linked_list = LinkedList()

for food_type in types:
    food_types_linked_list.insert_beginning(food_type)

#Write code to insert restaurant data into a data structure here. The data is in data.py
options_linked_main = LinkedList()
options_linked_ger = LinkedList("german")
options_linked_jap = LinkedList("japanese")
options_linked_veg = LinkedList("vegetarian") 
options_linked_fr = LinkedList("french")
options_linked_afr = LinkedList("african")
options_linked_amr = LinkedList("american")
options_linked_bar = LinkedList("barbecue")
options_linked_cz = LinkedList("czech")
options_linked_ch = LinkedList("chinese")
options_linked_th = LinkedList("thai")
options_linked_mex = LinkedList("mexican")
options_linked_ind = LinkedList("indian")
options_linked_caf = LinkedList("cafe")
options_linked_piz = LinkedList("pizza")
options_linked_it = LinkedList("italian")

options_list = [options_linked_ger, options_linked_jap, options_linked_veg, options_linked_fr, options_linked_afr, options_linked_amr, options_linked_bar, options_linked_cz, options_linked_ch, options_linked_th, options_linked_mex, options_linked_ind, options_linked_caf, options_linked_piz, options_linked_it]

for item in options_list:
  options_linked_main.insert_beginning(item)   
  
current_node_2 = options_linked_main.get_head_node()
current_node_10 = current_node_2.get_value().get_head_node()

while current_node_2.get_next_node():
  for restaurant in restaurant_data:
    if current_node_2.get_value().get_head_node().get_value() == restaurant[0]:
      new_node = Node(restaurant)
      current_node_10.set_next_node(new_node) 
      current_node_10 = current_node_10.get_next_node()
  if current_node_2.get_next_node().get_value() != None:
    current_node_2 = current_node_2.get_next_node()
    current_node_10 = current_node_2.get_value().get_head_node()
  else:
    break
        
#Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    
    #Inserting all the possible options in the new linked list
    current_node = food_types_linked_list.get_head_node()
    new_food_types_linked_list = LinkedList()
    while current_node.get_next_node():
      if current_node.get_value()[0: len(user_input)] == user_input:
        new_food_types_linked_list.insert_beginning(current_node.get_value())
      current_node = current_node.get_next_node()
    
    #Printing the values in the new linked list for the possible user choices
    if (new_food_types_linked_list.get_head_node()).get_next_node():
      options_1 = []
      current_node_1 = new_food_types_linked_list.get_head_node()
      while current_node_1.get_next_node():
        if current_node_1.get_value() != None:
          options_1.append(current_node_1.get_value())     
        current_node_1 = current_node_1.get_next_node()
      print("With those beginning letters, your choices are: " + str(options_1) + ".") 
      food_types_linked_list = new_food_types_linked_list
      
      #If there is only 1 item in the linked list
      if len(options_1) == 1:
        user_input_2 = str(input(" This is your only option. Would you like to look at " + options_1[0] + " restaurants? Enter \"y\" for yes and \"n\" for no \n")).lower()
        
        #Code for displaying all the options starts here
        if user_input_2 == "y":
          print("The ", options_1[0].capitalize(), " restaurants in SoHo are..... \n")
          #Iterate through main linked list    
          current_node_3 = options_linked_main.get_head_node()
          while current_node_3.get_next_node():
            if current_node_3.get_value().get_head_node().get_value() == options_1[0]:  
              #Iterate through sub linked list 
              current_node_4 = current_node_3.get_value().get_head_node().get_next_node()
              while current_node_4:   
                print("Name: ", current_node_4.get_value()[1])
                print("Price: ", current_node_4.get_value()[2], "/5")
                print("Rating: ", current_node_4.get_value()[3], "/5")
                print("Address: ", current_node_4.get_value()[4])
                print("---------------------------\n")
                current_node_4 = current_node_4.get_next_node()
              break
            current_node_3 = current_node_3.get_next_node()	 
          user_input_again = str(input("Do you want to look at other restaurants? Enter \"y\" for yes and \"n\" for no \n")).lower()
          if user_input_again == "n":
            break
          else:
            food_types_linked_list = LinkedList()
            for food_type in types:
              food_types_linked_list.insert_beginning(food_type)
        else:  
          food_types_linked_list = LinkedList()
          for food_type in types:
            food_types_linked_list.insert_beginning(food_type)
    else:
      print("For the input you entered, there are no matching food types. Please try again") 