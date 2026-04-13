## @author First Last
from Item import Item

def main() :
    print("Test the default constructor and set methods:")
    item1 = Item()
    item1.setName("Computer")
    item1.setPrice(500)
    item1.setQuantity(10)
    print("Item: %s, $%.2f, %d\n" % \
        (item1.getName(), item1.getPrice(), item1.getQuantity()))
    
    print("Test a new item and invalid data:");
    item2 = Item("Basketball", -19.99, -10);
    print("Item: %s, $%.2f, %d" % \
        (item2.getName(), item2.getPrice(), item2.getQuantity()))
    item2.setPrice(-19.99)
    item2.setQuantity(-10)
    print("Item: %s, $%.2f, %d" % \
        (item2.getName(), item2.getPrice(), item2.getQuantity()))
    item2.setPrice(19.99)
    item2.setQuantity(10)
    print("Item: %s, $%.2f, %d\n" % \
        (item2.getName(), item2.getPrice(), item2.getQuantity()))
    
    print("Attempt to reduce the number of basketballs by -2");
    item2.reduce(-2)
    print("Item: %s, $%.2f, %d" % \
        (item2.getName(), item2.getPrice(), item2.getQuantity()))
    print("Attempt to reduce the number of basketballs by 2");
    item2.reduce(2)
    print("Item: %s, $%.2f, %d" % \
        (item2.getName(), item2.getPrice(), item2.getQuantity()))
    
main()
