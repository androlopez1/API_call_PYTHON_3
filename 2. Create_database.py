import xml.etree.ElementTree as ET
import sqlite3

### THIS FUNCTION READS XML FILE AND STORE CATEGORY TREE IN DATABASE

def create_database ():
    conn = sqlite3.connect('categories_tree.db')
    c = conn.cursor()
    conn.commit
    c.executescript('drop table if exists categories;')
    conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS categories(CategoryID INT, CategoryNAME TEXT, CategoryLEVEL INT,CategoryParent INT, BestOffer BOOLEAN)')
    conn.commit
    tree = ET.parse('categories_tree.xml',  ET.XMLParser(encoding = 'ISO-8859-1'))#NOTE: ENCODING ISO-8859-1 WERE NECESSARY TO READ CORRECTLY THE XML FILE.
    root = tree.getroot()
    for text in root[4].findall('{urn:ebay:apis:eBLBaseComponents}Category'):    
        try:  
            category_id = text.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text
            category_name = text.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
            category_level = text.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text
            category_parent = text.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text
            best_offer = text.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled').text
            c.execute("INSERT INTO categories (CategoryID, CategoryNAME, CategoryLEVEL,CategoryParent, BestOffer) VALUES(?, ?, ?, ?, ?)", (category_id, category_name, category_level,category_parent, best_offer)) 
        except AttributeError:
            pass       
    conn.commit()            
    c.close()
    conn.close()
    print ('Database succesfully created!')

create_database()
