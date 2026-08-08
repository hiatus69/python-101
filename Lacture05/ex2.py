inventory = [
    ["Apple",50,0.75],
    ["banana",100,0.50],
    ["Orange",75,0.80]
]
item_name=""
quantity_sold=0
price=0
def update_inventory(inventory,item_name,quantity_sold):
    for item in inventory:
            item_name = item[0]
            quantity_sold = int(input(f"วันนี้ {item_name} ขายได้เท่าไหร่ : "))
            item[1] -= quantity_sold  
    return

def calculate_total_value(inventory):
      for item in inventory:
            print("ชื่อสินค้า: ",item[0]," จำนวนสินค้า: ",item[1]," ราคา: ",item[2],)

def find_most_expensive(inventory,price):
        for item in inventory:
                if item[2] > price:
                       price = item[2]
        for item in inventory:
               if price == item[2]:
                      print(f"สินค้าที่ราคาเยอะที่สุดคือ: {item[0]} ราคาอยู่ที่ {item[2]}")


def add_item(inventory,item_name,quantity_sold,price):

        choice=int(input("คุณอยากจะอัพเดทข้อมูลหรือเพิ่มข้อมูล \n พิม:1 เพื่อแก้ข้อมูล \n พิม:2 เพื่อเพิ่มข้อมูล\n::"))
        num = 1
        if choice == 1:
            for item in inventory:
                  print(num,item)
                  num = num + 1
            list_num = int(input("ใส่ลำดับเลขแถวข้อมูลที่ต้องการแก้ไข :"))
            list_num = list_num - 1
            list_slot = inventory[list_num]
            edit_list = int(input("ต้องการจะแก้ที่ชื่อ: 1\nจำนวน: 2\nราคา: 3\n :: "))
            if edit_list == 1:
                edit_data = input("ใส้ข้อมูลที่ต้องการแก้ :")
                list_slot[0] = edit_data
                print(inventory)
            elif edit_list == 2:
                edit_data = input("ใส้ข้อมูลที่ต้องการแก้ :")
                list_slot[1] = edit_data
                print(inventory)
            elif edit_list == 3:
                edit_data = input("ใส้ข้อมูลที่ต้องการแก้ :")
                list_slot[2] = edit_data
                print(inventory)
            else:
                  print("ไม่มีช่องข้อมูลดังกล่าว")
         
        elif choice == 2:
            item_name = input("ชื่อ: ")
            quantity_sold = int(input("จำนวนสินค้า: "))
            price = float(input("ราคา: "))
            return inventory.append([item_name,quantity_sold, price])
        
update_inventory(inventory,item_name,quantity_sold)
calculate_total_value(inventory)
find_most_expensive(inventory,price)
add_item(inventory,item_name,quantity_sold,price)
print(inventory)